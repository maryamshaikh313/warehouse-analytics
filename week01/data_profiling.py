import pandas as pd
from pathlib import Path

summary = []

for file in Path("../data").glob("*.csv"):
    df = pd.read_csv(file, low_memory=False)
    summary.append({
        "table": file.stem,
        "rows": len(df),
        "columns": df.shape[1],
        "missing_values": df.isna().sum().sum(),
        "duplicate_rows": df.duplicated().sum()
    })
    print(f"\n{file.stem}")
    print(df.dtypes)
    print(df.head(5))

summary = pd.DataFrame(summary)
print(summary)
summary.to_csv("profiling_summary.csv", index=False)
