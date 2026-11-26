import pandas as pd

def load(name):
    return pd.read_csv(f"../data_clean/{name}.csv")

branches = load("branches")
ledger = load("stock_ledger")
inv = load("inventory_master")
so = load("sales_orders_header")

# 1. Capacity: text ("45230 sqft") to number
branches["capacity_sqft"] = (branches["warehouse_capacity"]
    .str.replace(",", "").str.extract(r"(\d+)")[0].astype(int))

# 2. Throughput 2024 (units IN and OUT)
ledger["movement_date"] = pd.to_datetime(ledger["movement_date"])
y = ledger[ledger["movement_date"].dt.year == 2024]
flow = y.pivot_table(index="branch_id", columns="movement_type",
                     values="quantity", aggfunc="sum", fill_value=0)
flow = flow[["IN", "OUT"]].rename(columns={"IN": "in_2024", "OUT": "out_2024"}).reset_index()

# 3. Current stock per branch
stock = inv.groupby("branch_id")["current_stock"].sum().reset_index()

# 4. Delivered sales 2024 per branch
so["order_date"] = pd.to_datetime(so["order_date"])
s = so[(so["order_status"] == "Delivered") & (so["order_date"].dt.year == 2024)]
sales = s.groupby("branch_id")["total_order_value"].sum().rename("sales_2024").reset_index()

# 5. Join everything
report = (branches[["branch_id", "city", "warehouse_type", "capacity_sqft",
                    "total_employees", "avg_monthly_revenue", "monthly_operational_cost"]]
          .merge(flow, on="branch_id", how="left")
          .merge(stock, on="branch_id", how="left")
          .merge(sales, on="branch_id", how="left"))

# 6. New measures
report["throughput_2024"] = report["in_2024"] + report["out_2024"]
report["units_per_sqft"] = report["current_stock"] / report["capacity_sqft"]
report["throughput_per_employee"] = report["throughput_2024"] / report["total_employees"]
report["out_to_in_pct"] = report["out_2024"] / report["in_2024"] * 100
report["cost_to_revenue_pct"] = report["monthly_operational_cost"] / report["avg_monthly_revenue"] * 100
report["sales_per_month_2024"] = report["sales_2024"] / 12

report = report.round(2).sort_values("throughput_2024", ascending=False)
report.to_csv("warehouse_performance.csv", index=False)

for cols in [["capacity_sqft", "current_stock", "units_per_sqft"],
             ["in_2024", "out_2024", "throughput_2024", "out_to_in_pct"],
             ["total_employees", "throughput_per_employee", "cost_to_revenue_pct"],
             ["avg_monthly_revenue", "sales_per_month_2024"]]:
    print()
    print(report[["branch_id"] + cols].to_string(index=False))

# 7. Workload per employee (2024)
moves = y.groupby("branch_id")["quantity"].agg(movements="count", avg_qty="mean").reset_index()
moves = moves.merge(branches[["branch_id", "total_employees"]], on="branch_id")
moves["movements_per_employee"] = moves["movements"] / moves["total_employees"]
print("\nWorkload:")
print(moves.round(2).to_string(index=False))

# 8. Buying vs selling by branch and year
ledger["year"] = ledger["movement_date"].dt.year
yearly = ledger.pivot_table(index=["branch_id", "year"], columns="movement_type",
                            values="quantity", aggfunc="sum", fill_value=0)
yearly["in_per_out"] = yearly["IN"] / yearly["OUT"]
print("\nIN vs OUT by year:")
print(yearly.round(1))

# 9. Revenue check (2019 to 2024)
d = so[(so["order_status"] == "Delivered") & (so["order_date"].dt.year <= 2024)]
real = d.groupby("branch_id")["total_order_value"].sum() / 72
check = branches.set_index("branch_id")[["avg_monthly_revenue"]].join(real.rename("orders_monthly"))
check["times_higher"] = check["orders_monthly"] / check["avg_monthly_revenue"]
print("\nRevenue check:")
print(check.round(1))
