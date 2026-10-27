
import sqlite3
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DB_PATH = PROJECT_ROOT / "data" / "processed" / "repositories.db"
SQL_PATH = PROJECT_ROOT / "sql" / "01_repository_health_analysis.sql"


def main():
    if not DB_PATH.exists():
        raise FileNotFoundError(f"Database not found: {DB_PATH}")

    if not SQL_PATH.exists():
        raise FileNotFoundError(f"SQL file not found: {SQL_PATH}")

    sql_text = SQL_PATH.read_text(encoding="utf-8")
    queries = [
        statement.strip()
        for statement in sql_text.split(";")
        if statement.strip()
    ]

    with sqlite3.connect(DB_PATH) as connection:
        for number, query in enumerate(queries, start=1):
            print(f"\n{'=' * 70}")
            print(f"QUERY {number}")
            print("=" * 70)

            cursor = connection.execute(query)
            rows = cursor.fetchall()

            if cursor.description:
                columns = [column[0] for column in cursor.description]
                print(" | ".join(columns))

                for row in rows:
                    print(" | ".join(str(value) for value in row))

                print(f"\nRows returned: {len(rows)}")
            else:
                print("Query executed successfully.")

    print(f"\nValidated {len(queries)} SQL queries.")


if __name__ == "__main__":
    main()
