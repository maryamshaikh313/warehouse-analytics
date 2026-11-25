import pandas as pd
from pathlib import Path

docs = Path("../docs")
docs.mkdir(exist_ok=True)

rows = []

for file in sorted(Path("../data_clean").glob("*.csv")):
    df = pd.read_csv(file, low_memory=False)
    for col in df.columns:
        is_date = col.endswith("_date") or col == "customer_since"
        rows.append({
            "table": file.stem,
            "column": col,
            "data_type": "date" if is_date else str(df[col].dtype),
            "missing": df[col].isna().sum(),
            "unique_values": df[col].nunique(),
            "example": df[col].dropna().iloc[0],
            "description": ""
        })

dictionary = pd.DataFrame(rows)
dictionary.to_csv(docs / "data_dictionary.csv", index=False)
print(len(dictionary), "columns documented")
