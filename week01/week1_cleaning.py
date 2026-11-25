import pandas as pd
from pathlib import Path

raw = Path("../data")
clean = Path("../data_clean")
clean.mkdir(exist_ok=True)

data = {f.stem: pd.read_csv(f, low_memory=False) for f in raw.glob("*.csv")}

# 1. Dates ko date type mein badlein
for name, df in data.items():
    date_cols = [c for c in df.columns if c.endswith("_date") or c == "customer_since"]
    for col in date_cols:
        before = df[col].isna().sum()
        df[col] = pd.to_datetime(df[col], errors="coerce")
        failed = df[col].isna().sum() - before
        print(f"{name}.{col}: {failed} dates convert nahi huin")

inv = data["invoices"]
pay = data["payments"]

# 2. Har row ki apni unique key
inv.insert(0, "invoice_key", range(1, len(inv) + 1))
pay.insert(0, "payment_key", range(1, len(pay) + 1))

# 3. Confusing invoice IDs par flag
dup_ids = inv.loc[inv["invoice_id"].duplicated(keep=False), "invoice_id"]
inv["ambiguous_id"] = inv["invoice_id"].isin(dup_ids)
pay["ambiguous_invoice"] = pay["invoice_id"].isin(dup_ids)

print("Ambiguous invoices:", inv["ambiguous_id"].sum())
print("Ambiguous payments:", pay["ambiguous_invoice"].sum())
print("Duplicate so_id in invoices:", inv["so_id"].duplicated().sum())

# 4. Saaf data alag folder mein save karein
for name, df in data.items():
    df.to_csv(clean / f"{name}.csv", index=False)

print("Done!")
