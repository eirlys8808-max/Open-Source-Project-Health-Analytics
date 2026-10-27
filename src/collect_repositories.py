
import requests
import pandas as pd
from pathlib import Path

# 1. Define the GitHub API endpoint
url = "https://api.github.com/search/repositories"

# 2. Define search parameters
params = {
    "q": "language:Python stars:>1000",
    "sort": "stars",
    "order": "desc",
    "per_page": 100,
}

# 3. Request data from GitHub API
response = requests.get(url, params=params, timeout=30)
response.raise_for_status()

result = response.json()
repositories = result["items"]

# 4. Select fields for analysis
rows = []

for repo in repositories:
    rows.append({
        "name": repo["full_name"],
        "stars": repo["stargazers_count"],
        "forks": repo["forks_count"],
        "language": repo["language"],
        "open_issues": repo["open_issues_count"],
        "updated_at": repo["updated_at"],
    })

# 5. Convert records into a DataFrame
df = pd.DataFrame(rows)

# 6. Create the output directory
project_root = Path(__file__).resolve().parent.parent
output_dir = project_root / "data" / "raw"
output_dir.mkdir(parents=True, exist_ok=True)

# 7. Save the dataset as CSV
output_file = output_dir / "repositories.csv"
df.to_csv(output_file, index=False, encoding="utf-8-sig")

print("Repositories collected:", len(df))
print("CSV saved to:", output_file)
print("\nPreview:")
print(df.head())
