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

def cumulative(row):
   totals_above = df['total_price'][0:row.name+1]
   return totals_above.sum()

df['cumulative'] = df['total_price'].cumsum()

# Create a line plot of cumulative revenue vs. order_id
df.plot(x="cumulative", y="order_id", kind="line", title="Cumulative Revenue vs. Order_ID", legend = False)

# Format line chart
plt.xlabel('Cumulative Revenue ($)')
plt.ylabel('Order_ID')
current_values = plt.gca().get_xticks() # Format y values to be more readable
plt.gca().set_xticklabels(['{:,.0f}'.format(y) for y in current_values])

# Plot line chart
plt.show()

# Task 3: Interactive Visualizations with Plotly
import plotly.express as px
import plotly.data as pldata
df = pldata.wind(return_type='pandas')

print("First 10 lines of the DataFrame")
print(df.head(10))

print("Last 10 lines of the DataFrame")
print(df.tail(10))

# Clean Data

# Clean strength column
df['strength'] = df['strength'].str.replace('[+-]', '', regex=True)

# Convert strength column to a float
df['strength'] = df['strength'].astype(float)

print("First 10 lines of the DataFrame")
print(df.head(10))

print("Last 10 lines of the DataFrame")
print(df.tail(10))

print("Confirm correct data types for the DataFrame")
print(df.dtypes)

# Create interactive scatter plot of strength vs. frequency, with colors based on direction
import plotly.express as px
import plotly.data as pldata

df = pldata.wind(return_type='pandas') # Returns a DataFrame.  plotly.data has a number of sample datasets included.
fig = px.scatter(df, x='strength', y='frequency', color='direction',
                 title="Wind Data, Strength vs. Frequency", hover_data=["frequency"])
fig.write_html("wind.html", auto_open=True)
