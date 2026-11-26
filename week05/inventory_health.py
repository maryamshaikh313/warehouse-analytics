import pandas as pd

def load(name):
    return pd.read_csv(f"../data_clean/{name}.csv")

inv = load("inventory_master")
ledger = load("stock_ledger")
products = load("products")
keys = ["product_id", "branch_id"]

ledger["movement_date"] = pd.to_datetime(ledger["movement_date"])
ledger = ledger.sort_values(keys + ["movement_date"], kind="stable")

# 1. Does current_stock match the last ledger balance?
last = ledger.groupby(keys)["running_balance"].last().rename("ledger_balance").reset_index()
report = inv.merge(last, on=keys, how="left")
report["balance_match"] = report["current_stock"] == report["ledger_balance"]
print("Balance matches:", report["balance_match"].sum(), "of", len(report))

# 2. Do adjustments add or remove stock?
ledger["change"] = ledger.groupby(keys)["running_balance"].diff()
adj = ledger[(ledger["movement_type"] == "ADJUSTMENT") & ledger["change"].notna()]
print("\nAdjustments that added stock:", (adj["change"] > 0).sum())
print("Adjustments that removed stock:", (adj["change"] < 0).sum())

# 3. Stock status
def status(row):
    if row["current_stock"] <= row["safety_stock"]:
        return "Critical"
    if row["current_stock"] <= row["reorder_level"]:
        return "Reorder"
    if row["current_stock"] > row["max_stock"]:
        return "Overstock"
    return "Healthy"

report["stock_status"] = report.apply(status, axis=1)
print("\nStock status:")
print(report["stock_status"].value_counts())

# 4. Turnover and days of stock (2024)
y = ledger[ledger["movement_date"].dt.year == 2024]
out_units = y[y["movement_type"] == "OUT"].groupby(keys)["quantity"].sum().rename("out_2024")
avg_stock = y.groupby(keys)["running_balance"].mean().rename("avg_stock_2024")
report = report.merge(pd.concat([out_units, avg_stock], axis=1).reset_index(), on=keys, how="left")
report["turnover_2024"] = report["out_2024"] / report["avg_stock_2024"]
report["days_of_stock"] = report["current_stock"] / (report["out_2024"] / 366)

# 5. Stock value at cost
report = report.merge(products[["product_id", "product_name", "unit_cost"]], on="product_id", how="left")
report["stock_value"] = report["current_stock"] * report["unit_cost"]

report.to_csv("inventory_health.csv", index=False)

print("\nTurnover 2024:")
print(report["turnover_2024"].describe().round(4))
print("\nDays of stock:")
print(report["days_of_stock"].describe().round(0))
print("\nTotal stock value:", report["stock_value"].sum())
print("\nStock value by branch:")
print(report.groupby("branch_id")["stock_value"].sum().sort_values(ascending=False))
print("\nTop 5 products by stock value:")
print(report.groupby("product_name")["stock_value"].sum().nlargest(5))



# 6. Ledger consistency check
step = ledger["change"].abs() == ledger["quantity"]
has_prev = ledger["change"].notna()
print("\nRows where balance change equals quantity %:", round(step[has_prev].mean() * 100, 2))

bad = report[~report["balance_match"]].copy()
bad["difference"] = bad["current_stock"] - bad["ledger_balance"]
print(bad[["product_id", "branch_id", "current_stock", "ledger_balance", "difference"]].to_string(index=False))







