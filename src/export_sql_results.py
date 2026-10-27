
import sqlite3
from pathlib import Path

import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DB_PATH = PROJECT_ROOT / "data" / "processed" / "repositories.db"
OUTPUT_DIR = PROJECT_ROOT / "data" / "processed" / "sql_results"

QUERIES = {
    "01_repository_counts.csv": """
        SELECT star_group_label,
               COUNT(*) AS repository_count
        FROM repositories_powerbi
        GROUP BY star_group_label
        ORDER BY repository_count DESC;
    """,
    "02_group_metrics.csv": """
        SELECT star_group_label,
               COUNT(*) AS repository_count,
               ROUND(AVG(stars), 2) AS average_stars,
               ROUND(AVG(forks), 2) AS average_forks,
               ROUND(AVG(open_issues), 2) AS average_open_issues
        FROM repositories_powerbi
        GROUP BY star_group_label
        ORDER BY average_stars DESC;
    """,
    "03_fork_to_star_ratio.csv": """
        SELECT star_group_label,
               ROUND(AVG(fork_to_star_ratio), 2)
                   AS average_fork_to_star_ratio_pct
        FROM repositories_powerbi
        GROUP BY star_group_label
        ORDER BY average_fork_to_star_ratio_pct DESC;
    """,
    "04_update_recency.csv": """
        SELECT star_group_label,
               ROUND(AVG(days_since_update), 2)
                   AS average_days_since_update
        FROM repositories_powerbi
        GROUP BY star_group_label
        ORDER BY average_days_since_update ASC;
    """,
    "05_top_open_issues.csv": """
        SELECT name, stars, forks, open_issues, star_group_label
        FROM repositories_powerbi
        ORDER BY open_issues DESC
        LIMIT 10;
    """,
}


def main():
    if not DB_PATH.exists():
        raise FileNotFoundError(f"Database not found: {DB_PATH}")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    with sqlite3.connect(DB_PATH) as connection:
        for filename, query in QUERIES.items():
            result = pd.read_sql_query(query, connection)
            output_path = OUTPUT_DIR / filename
            result.to_csv(output_path, index=False)
            print(f"Exported {filename}: {len(result)} rows")

    print(f"\nAll reports saved to: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
