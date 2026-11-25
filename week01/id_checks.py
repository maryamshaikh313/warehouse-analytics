import pandas as pd

def load(name):
    return pd.read_csv(f"../data/{name}.csv", low_memory=False)

keys = {
    "invoices": "invoice_id",
    "payments": "payment_id",
    "sales_orders_header": "so_id",
    "purchase_orders_header": "po_id",
    "stock_ledger": "movement_id"
}

for table, key in keys.items():
    df = load(table)
    dup = df[df[key].duplicated(keep=False)].sort_values(key)
    print(f"\n{table}: {df[key].duplicated().sum()} duplicate {key}")
    print(dup.head(4).to_string(index=False))
