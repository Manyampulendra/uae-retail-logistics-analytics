import sqlite3
import os
import pandas as pd

BASE_DIR = os.path.join(os.path.dirname(__file__), "..")
DB_PATH = os.path.join(BASE_DIR, "data", "uae_retail.db")

conn = sqlite3.connect(DB_PATH)

query = """
SELECT
    p.product_name,
    p.category,
    SUM(oi.quantity) AS units_sold,
    ROUND(SUM(oi.line_total_aed), 2) AS revenue_aed
FROM order_items oi
JOIN products p
    ON p.product_id = oi.product_id
GROUP BY p.product_id
ORDER BY revenue_aed DESC
LIMIT 10;
"""

result = pd.read_sql_query(query, conn)

print(result.to_string(index=False))

conn.close()