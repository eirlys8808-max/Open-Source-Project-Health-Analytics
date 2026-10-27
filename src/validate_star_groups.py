
import pandas as pd
from pathlib import Path

# 1. Locate the dataset
project_root = Path(__file__).resolve().parent.parent
input_file = (
    project_root
    / "data"
    / "raw"
    / "repositories_by_star_group.csv"
)

# 2. Load the dataset
df = pd.read_csv(input_file)

print("=== DATASET OVERVIEW ===")
print("Rows:", len(df))
print("Columns:", len(df.columns))

# 3. Check missing values
print("\n=== MISSING VALUES ===")
print(df.isnull().sum())

# 4. Check duplicates
print("\n=== DUPLICATE CHECK ===")
print("Duplicate names:", df["name"].duplicated().sum())

# 5. Check actual star ranges
print("\n=== STAR RANGE BY GROUP ===")
print(
    df.groupby("star_group")["stars"]
    .agg(["count", "min", "max"])
)

# 6. Validate group assignments
print("\n=== GROUP VALIDATION ===")

valid_high = (
    (df["star_group"] == "high") &
    (df["stars"] >= 100000)
)

valid_medium = (
    (df["star_group"] == "medium") &
    (df["stars"].between(10000, 99999))
)

valid_lower = (
    (df["star_group"] == "lower") &
    (df["stars"].between(1000, 9999))
)

valid_rows = valid_high | valid_medium | valid_lower

print("Rows matching their assigned group:", valid_rows.sum())
print("Rows with incorrect group assignment:", (~valid_rows).sum())
