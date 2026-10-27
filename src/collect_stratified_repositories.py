
import requests
import pandas as pd
from pathlib import Path
import time

# 1. Define project paths
project_root = Path(__file__).resolve().parent.parent
output_dir = project_root / "data" / "raw"
output_dir.mkdir(parents=True, exist_ok=True)

# 2. Define star groups
star_groups = {
    "high": "stars:>=100000",
    "medium": "stars:10000..99999",
    "lower": "stars:1000..9999",
}

# 3. Collect repositories from each group
all_rows = []

for group_name, star_filter in star_groups.items():
    print(f"\nCollecting group: {group_name}")

    params = {
        "q": f"language:Python {star_filter}",
        "sort": "stars",
        "order": "desc",
        "per_page": 100,
    }

    url = "https://api.github.com/search/repositories"
    response = requests.get(url, params=params, timeout=30)
    response.raise_for_status()

    items = response.json()["items"]
    print("Repositories collected:", len(items))

    for repo in items:
        all_rows.append({
            "name": repo["full_name"],
            "stars": repo["stargazers_count"],
            "forks": repo["forks_count"],
            "language": repo["language"],
            "open_issues": repo["open_issues_count"],
            "updated_at": repo["updated_at"],
            "star_group": group_name,
        })

    # Brief pause between requests
    time.sleep(2)

# 4. Create a DataFrame and remove duplicate repositories
df = pd.DataFrame(all_rows)
df = df.drop_duplicates(subset="name")

# 5. Save to a separate CSV file
output_file = output_dir / "repositories_by_star_group.csv"
df.to_csv(output_file, index=False, encoding="utf-8-sig")

# 6. Print a summary
print("\n=== COLLECTION SUMMARY ===")
print("Total unique repositories:", len(df))
print("\nRepositories by group:")
print(df["star_group"].value_counts())
print("\nSaved to:", output_file)
