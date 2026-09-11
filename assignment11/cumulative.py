import pandas as pd 
import matplotlib.pyplot as plt
import sqlite3 

# Task 2: A Line Plot with Pandas
try:
    with sqlite3.connect("../db/lesson.db") as conn:
        sql_statement = """
            SELECT o.order_id, SUM(l.quantity * p.price) AS total_price 
            FROM orders AS o
            JOIN line_items AS l
                ON o.order_id = l.order_id
            JOIN products AS p 
                ON l.product_id = p.product_id
            GROUP BY o.order_id
            ORDER BY o.order_id;
        """
        df = pd.read_sql_query(sql_statement, conn)
except Exception as e:
    print(f"Exception caught: {e}")

df['cumulative'] = df['total_price'].cumsum()

# Create a line plot of cumulative revenue vs. order_id
df.plot(x="order_id", y="cumulative", kind="line", title="cumulative revenue vs. order_id", legend = False)

# Format line chart
plt.xlabel('order_id')
plt.ylabel('cumulative revenue ($)')

# Plot line chart
plt.show()