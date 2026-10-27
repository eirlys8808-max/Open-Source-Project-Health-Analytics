
import pandas as pd
from pathlib import Path

# 1. Locate the project and CSV file
project_root = Path(__file__).resolve().parent.parent
input_file = project_root / "data" / "raw" / "repositories.csv"

# 2. Load the CSV
df = pd.read_csv(input_file)

# 3. Check the dataset size
print("=== DATASET OVERVIEW ===")
print("Rows:", len(df))
print("Columns:", len(df.columns))
print("Column names:", df.columns.tolist())

# 4. Check data types
print("\n=== DATA TYPES ===")
print(df.dtypes)

# 5. Check missing values
print("\n=== MISSING VALUES ===")
print(df.isnull().sum())

# 6. Check duplicate repositories
print("\n=== DUPLICATE CHECK ===")
print("Duplicate repository names:", df["name"].duplicated().sum())

# 7. Check basic statistics
print("\n=== NUMERIC SUMMARY ===")
print(df[["stars", "forks", "open_issues"]].describe())

# 8. Validate dates
print("\n=== DATE VALIDATION ===")

df["updated_at"] = pd.to_datetime(
    df["updated_at"],
    utc=True,
    errors="coerce"
)

print("Invalid dates:", df["updated_at"].isna().sum())
print("Latest update:", df["updated_at"].max())
print("Oldest update:", df["updated_at"].min())

# 9. Check impossible negative values
print("\n=== VALUE VALIDATION ===")

numeric_columns = ["stars", "forks", "open_issues"]

for column in numeric_columns:
    negative_count = (df[column] < 0).sum()
    print(f"Negative values in {column}: {negative_count}")
