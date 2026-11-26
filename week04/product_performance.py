import pandas as pd

def load(name):
    return pd.read_csv(f"../data_clean/{name}.csv")

so = load("sales_orders_header")
lines = load("sales_orders_lines")
products = load("products")

delivered_ids = so.loc[so["order_status"] == "Delivered", "so_id"]
sold = lines[lines["so_id"].isin(delivered_ids)]

perf = sold.groupby("product_id").agg(
    units_sold=("quantity", "sum"),
    sales=("line_total", "sum"),
    orders=("so_id", "nunique")
).reset_index()

perf = products[["product_id", "product_name", "category"]].merge(perf, on="product_id", how="left")
perf = perf.fillna({"units_sold": 0, "sales": 0, "orders": 0})
perf = perf.sort_values("sales", ascending=False)

# ABC classification (sales value)
perf["sales_share_pct"] = perf["sales"] / perf["sales"].sum() * 100
share_before = perf["sales_share_pct"].cumsum() - perf["sales_share_pct"]
perf["abc_class"] = pd.cut(share_before, bins=[-1, 80, 95, 101], labels=["A", "B", "C"])

# Fast / Medium / Slow movers (units sold)
perf["movement"] = pd.qcut(perf["units_sold"].rank(method="first"), 3, labels=["Slow", "Medium", "Fast"])

perf.to_csv("product_performance.csv", index=False)

print(perf[["product_id", "product_name", "units_sold", "sales", "abc_class", "movement"]].to_string(index=False))
print("\nABC summary:")
print(perf.groupby("abc_class", observed=False)["sales_share_pct"].agg(["count", "sum"]).round(2))
