import pandas as pd 
import matplotlib.pyplot as plt
import sqlite3 

# Task 1: Plotting with Pandas
try:
    with sqlite3.connect("../db/lesson.db") as conn:
        sql_statement = """SELECT last_name, SUM(price * quantity) AS revenue 
                            FROM employees e 
                            JOIN orders o 
                                ON e.employee_id = o.employee_id 
                            JOIN line_items l 
                                ON o.order_id = l.order_id 
                            JOIN products p 
                                ON l.product_id = p.product_id 
                            GROUP BY e.employee_id;"""
        employee_results = pd.read_sql_query(sql_statement, conn)
except Exception as e:
    print(f"Exception caught: {e}")

# Create bar chart
employee_results.plot(x="last_name", y="revenue", kind="bar", color="skyblue", title="Revenue by Employee", legend = False)

# Format bar chart
plt.xlabel('Employee Last Name')
plt.ylabel('Revenue ($)')
current_values = plt.gca().get_yticks() # Format x values to be more readable
plt.gca().set_yticklabels(['{:,.0f}'.format(x) for x in current_values])

# Plot bar chart
plt.show()