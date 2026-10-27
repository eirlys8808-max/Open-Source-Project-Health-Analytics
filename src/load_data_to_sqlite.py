
import sqlite3
from pathlib import Path

import pandas as pd

# Locate the project root and input CSV
PROJECT_ROOT = Path(__file__).resolve().parent.parent
CSV_PATH = PROJECT_ROOT / "data" / "processed" / "repositories_powerbi.csv"
DB_PATH = PROJECT_ROOT / "data" / "processed" / "repositories.db"

def main():
    if not CSV_PATH.exists():
        raise FileNotFoundError(f"Dataset not found: {CSV_PATH}")

    df = pd.read_csv(CSV_PATH)

    with sqlite3.connect(DB_PATH) as connection:
        df.to_sql(
            "repositories_powerbi",
            connection,
            if_exists="replace",
            index=False,
        )

        row_count = connection.execute(
            "SELECT COUNT(*) FROM repositories_powerbi"
        ).fetchone()[0]

    print(f"Database created: {DB_PATH}")
    print(f"Rows loaded: {row_count}")
    print(f"Columns loaded: {len(df.columns)}")

if __name__ == "__main__":
    main()
