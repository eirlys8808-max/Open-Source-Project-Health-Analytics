
import pandas as pd
from pathlib import Path

# 1. Define project paths
project_root = Path(__file__).resolve().parent.parent

input_file = (
    project_root
    / "data"
    / "raw"
    / "repositories_by_star_group.csv"
)

output_dir = project_root / "data" / "processed"
output_dir.mkdir(parents=True, exist_ok=True)

# 2. Load raw data
df = pd.read_csv(input_file)

# 3. Convert dates to datetime
df["updated_at"] = pd.to_datetime(
    df["updated_at"],
    utc=True,
    errors="coerce"
)

# 4. Calculate analysis metrics
df["fork_to_star_ratio"] = (
    df["forks"] / df["stars"] * 100
).round(2)

collection_time = pd.Timestamp.now(tz="UTC")

df["days_since_update"] = (
    (collection_time - df["updated_at"])
    .dt.total_seconds() / 86400
).round(2)

# 5. Create a readable group label
group_labels = {
    "high": "High Popularity",
    "medium": "Medium Popularity",
    "lower": "Lower Popularity",
}

df["star_group_label"] = df["star_group"].map(group_labels)

# 6. Select and order columns for Power BI
columns = [
    "name",
    "language",
    "star_group",
    "star_group_label",
    "stars",
    "forks",
    "open_issues",
    "fork_to_star_ratio",
    "updated_at",
    "days_since_update",
]

df = df[columns]

# 7. Save the processed dataset
output_file = output_dir / "repositories_powerbi.csv"

df.to_csv(
    output_file,
    index=False,
    encoding="utf-8-sig"
)

# 8. Print a validation summary
print("=== POWER BI DATA PREPARATION ===")
print("Rows:", len(df))
print("Columns:", len(df.columns))
print("Missing values:", df.isnull().sum().sum())
print("Duplicate repositories:", df["name"].duplicated().sum())
print("\nRows by group:")
print(df["star_group_label"].value_counts())
print("\nSaved to:", output_file)

# 9. Additional checks for Power BI readiness
print("\n=== POWER BI READINESS CHECK ===")

print("Star group labels:")
print(df["star_group_label"].value_counts())

print("\nMetric summary:")
print(
    df[
        [
            "stars",
            "forks",
            "open_issues",
            "fork_to_star_ratio",
            "days_since_update",
        ]
    ].describe().round(2)
)

print("\nDate range:")
print("Oldest update:", df["updated_at"].min())
print("Newest update:", df["updated_at"].max())

print("\nNegative metric values:")
for column in [
    "stars",
    "forks",
    "open_issues",
    "fork_to_star_ratio",
    "days_since_update",
]:
    print(f"{column}: {(df[column] < 0).sum()}")
