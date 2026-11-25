import pandas as pd

def load(name, dates=None):
    return pd.read_csv(f"../data_clean/{name}.csv", parse_dates=dates)

so = load("sales_orders_header", ["order_date"])
lines = load("sales_orders_lines")
po = load("purchase_orders_header", ["expected_delivery_date", "received_date"])
products = load("products")

delivered = so[so["order_status"] == "Delivered"]
received = po[po["po_status"] == "Received"]

print("Total sales:", delivered["total_order_value"].sum())
print("Average order value:", round(delivered["total_order_value"].mean(), 2))
print("\nOrder status %:")
print((so["order_status"].value_counts(normalize=True) * 100).round(2))

cancel_rate = (po["po_status"] == "Cancelled").mean() * 100
on_time = (received["received_date"] <= received["expected_delivery_date"]).mean() * 100
print("\nPO cancellation rate %:", round(cancel_rate, 2))
print("On-time delivery rate %:", round(on_time, 2))

sold = lines[lines["so_id"].isin(delivered["so_id"])]
top = sold.groupby("product_id")["line_total"].sum().nlargest(5).reset_index()
top = top.merge(products[["product_id", "product_name"]], on="product_id")
print("\nTop 5 products:")
print(top.to_string(index=False))

print("\nYearly sales:")
print(delivered.groupby(delivered["order_date"].dt.year)["total_order_value"].sum())
