
import pandas as pd
from pathlib import Path

# 1. Locate and load the dataset
project_root = Path(__file__).resolve().parent.parent
input_file = project_root / "data" / "raw" / "repositories.csv"

df = pd.read_csv(input_file)

# Calculate days since the last repository update
df["updated_at"] = pd.to_datetime(
    df["updated_at"],
    utc=True,
    errors="coerce"
)

collection_time = pd.Timestamp.now(tz="UTC")

df["days_since_update"] = (
    (collection_time - df["updated_at"]).dt.total_seconds()
    / 86400
).round(1)

print("\n=== 10 REPOSITORIES LEAST RECENTLY UPDATED ===")

least_recently_updated = df.nlargest(10, "days_since_update")

print(
    least_recently_updated[
        ["name", "updated_at", "days_since_update", "stars"]
    ].to_string(index=False)
)

# Categorize repositories by update recency
def classify_update_recency(days):
    if pd.isna(days):
        return "Unknown"
    elif days <= 30:
        return "Updated within 30 days"
    elif days <= 90:
        return "Updated 31-90 days ago"
    elif days <= 180:
        return "Updated 91-180 days ago"
    else:
        return "Not updated for over 180 days"


df["update_recency"] = df["days_since_update"].apply(
    classify_update_recency
)

print("\n=== UPDATE RECENCY DISTRIBUTION ===")
print(df["update_recency"].value_counts(dropna=False))

print("\n=== UPDATE RECENCY SUMMARY ===")
print(
    df["days_since_update"].describe().round(2)
)

print(
    "\nOldest update age (days):",
    round(df["days_since_update"].max(), 2)
)

print(
    "Most recent update age (days):",
    round(df["days_since_update"].min(), 2)
)


# Calculate engagement-related metrics
df["fork_to_star_ratio"] = (
    df["forks"] / df["stars"] * 100
)

print("\n=== TOP 5 REPOSITORIES BY FORK-TO-STAR RATIO ===")

top_fork_ratio = df.nlargest(5, "fork_to_star_ratio")

print(
    top_fork_ratio[
        ["name", "stars", "forks", "fork_to_star_ratio"]
    ].to_string(index=False)
)

# 2. Calculate key metrics
print("=== KEY METRICS ===")
print("Number of repositories:", len(df))
print("Average stars:", round(df["stars"].mean(), 2))
print("Median stars:", round(df["stars"].median(), 2))
print("Average forks:", round(df["forks"].mean(), 2))
print("Median forks:", round(df["forks"].median(), 2))
print("Average open issues:", round(df["open_issues"].mean(), 2))
print("Median open issues:", round(df["open_issues"].median(), 2))

# 3. Show the top 5 repositories by stars
print("\n=== TOP 5 REPOSITORIES BY STARS ===")
top_stars = df.nlargest(5, "stars")
print(top_stars[["name", "stars", "forks", "open_issues"]].to_string(index=False))

# 4. Show the top 5 repositories by forks
print("\n=== TOP 5 REPOSITORIES BY FORKS ===")
top_forks = df.nlargest(5, "forks")
print(top_forks[["name", "stars", "forks", "open_issues"]].to_string(index=False))

# 5. Show repositories with the most open issues
print("\n=== TOP 5 REPOSITORIES BY OPEN ISSUES ===")
top_issues = df.nlargest(5, "open_issues")
print(top_issues[["name", "stars", "forks", "open_issues"]].to_string(index=False))

import matplotlib.pyplot as plt

# 6. Visualize the top 10 repositories by stars
chart_data = df.nlargest(10, "stars").sort_values("stars")

plt.figure(figsize=(12, 7))

plt.barh(chart_data["name"], chart_data["stars"])

plt.title("Top 10 Python Repositories by GitHub Stars")
plt.xlabel("Number of Stars")
plt.ylabel("Repository")

plt.tight_layout()

# Save the chart
output_file = project_root / "docs" / "top_repositories_by_stars.png"
plt.savefig(output_file, dpi=300, bbox_inches="tight")

print("\nChart saved to:", output_file)

plt.show()
