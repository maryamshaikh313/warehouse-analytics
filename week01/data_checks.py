import pandas as pd

def load(name):
    return pd.read_csv(f"../data/{name}.csv", low_memory=False)

po = load("purchase_orders_header")
inv = load("inventory_master")
ledger = load("stock_ledger")
pay = load("payments")

# 1. Missing values kahan hain?
print(po.isna().sum())
print(po.groupby("po_status")["received_date"].apply(lambda s: s.isna().sum()))

# 2. Stock ka farq
print((inv["current_stock"] > inv["max_stock"]).sum(), "of", len(inv))
print(ledger.groupby(["movement_type", "reference_type"])["quantity"].agg(["count", "sum", "min", "max"]))
p = ledger[(ledger["product_id"] == "P001") & (ledger["branch_id"] == "DEL001")]
print(p.sort_values("movement_date").tail(10).to_string())
print(inv[(inv["product_id"] == "P001") & (inv["branch_id"] == "DEL001")].to_string())

# 3. Ek invoice par kitni payments?
print(pay.groupby("invoice_id").size().value_counts())
print("Duplicate payment_id:", pay["payment_id"].duplicated().sum())
