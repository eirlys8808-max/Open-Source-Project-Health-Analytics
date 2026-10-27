
import pandas as pd
from pathlib import Path

# 1. Locate and load the dataset
project_root = Path(__file__).resolve().parent.parent

input_file = (
    project_root
    / "data"
    / "raw"
    / "repositories_by_star_group.csv"
)

df = pd.read_csv(input_file)

# 2. Calculate engagement-related metrics
df["fork_to_star_ratio"] = (
    df["forks"] / df["stars"] * 100
)

# 3. Calculate repository update age
df["updated_at"] = pd.to_datetime(
    df["updated_at"],
    utc=True,
    errors="coerce"
)

collection_time = pd.Timestamp.now(tz="UTC")

df["days_since_update"] = (
    (collection_time - df["updated_at"])
    .dt.total_seconds() / 86400
)

# 4. Compare groups
group_summary = (
    df.groupby("star_group")
    .agg(
        repository_count=("name", "count"),
        avg_stars=("stars", "mean"),
        median_stars=("stars", "median"),
        avg_forks=("forks", "mean"),
        median_forks=("forks", "median"),
        avg_open_issues=("open_issues", "mean"),
        median_open_issues=("open_issues", "median"),
        avg_fork_to_star_ratio=("fork_to_star_ratio", "mean"),
        median_days_since_update=("days_since_update", "median"),
    )
    .round(2)
)

# 5. Display results in a logical order
group_order = ["high", "medium", "lower"]

group_summary = group_summary.reindex(group_order)

print("=== REPOSITORY GROUP COMPARISON ===")
print(group_summary.to_string())

# 6. Save the summary for future analysis
output_file = (
    project_root
    / "data"
    / "raw"
    / "star_group_summary.csv"
)

group_summary.to_csv(
    output_file,
    encoding="utf-8-sig"
)

print("\nSummary saved to:", output_file)
