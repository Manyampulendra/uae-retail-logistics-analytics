import sqlite3
import os

BASE_DIR = os.path.join(os.path.dirname(__file__), "..")
DB_PATH = os.path.join(BASE_DIR, "data", "uae_retail.db")


def main():

    conn = sqlite3.connect(DB_PATH)

    tables = [
        "customers",
        "suppliers",
        "products",
        "warehouses",
        "orders",
        "order_items",
        "deliveries"
    ]

    print("Database verification")
    print("-" * 40)

    for table in tables:

        result = conn.execute(
            f"SELECT COUNT(*) FROM {table}"
        ).fetchone()

        print(f"{table:<15} {result[0]:,} rows")

    print("\nForeign-key verification")
    print("-" * 40)

    result = conn.execute(
        "PRAGMA foreign_key_check"
    ).fetchall()

    if len(result) == 0:
        print("Foreign-key check: PASS")
    else:
        print("Foreign-key check: FAILED")
        for row in result:
            print(row)

    conn.close()


if __name__ == "__main__":
    main()