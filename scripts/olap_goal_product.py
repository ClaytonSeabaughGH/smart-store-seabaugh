"""
OLAP Goal Script
File: scripts/olap_goal_product.py

Goal: Analyze sales data from each product over time to find out which product sold the most in each region every week. 

Action: This can help inform decision about supplying more products in particular regions or possibly changing pricing to raise or lower demand. 

Process: 
Divde sales amount by unit price of each product in each transaction to find the amount of each item sold.
Group these transactions by week.
Group these transactions by region. 

"""

# Library Imports
import pandas as pd
import matplotlib.pyplot as plt
import pathlib
import sys
import sqlite3

# Local imports
PROJECT_ROOT = pathlib.Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

    from utils.logger import logger



conn = sqlite3.connect('data/dw/smart_sales.db')

def get_sales_data():
    query = """
        SELECT
            s.sale_id,
            s.sale_date,
            s.quantity,
            s.sale_amount,
            p.product_name,
            p.category,
            p.unit_price,
            c.region
        FROM sale s
        JOIN product p ON s.product_id = p.product_id
        Join customer c ON s.customer_id = c.customer_id
        WHERE s.sale_date IS NOT NULL
    """
    return pd.read_sql(query, conn)

def process_sales_data(df):
    # Convert sale_date to datetime
    df['sale_date'] = pd.to_datetime(df['sale_date'])

    # Create a column for the week 
    df['week'] = df['sale_date'].dt.strftime('%Y-%U') # Year-Week format

    # Group by region, week, and product_name to calculate total quantity sold per product per week
    weekly_sales = df.groupby(['region', 'week', 'product_name'])['quantity'].sum().reset_index()

    # Find the product with the maximum quantity sold per region per week
    top_products = weekly_sales.loc[weekly_sales.groupby(['region', 'week'])['quantity'].idmax()]

    return top_products

def olap_cube(df):
    # Pivot table to emulate OLAP cube behavior
    olap_cube = pd.pivot_table(df, values='quantity', index=['region', 'week'], columns='product_name', aggfunc='sum', fill_value=0 )
    return olap_cube

def save_to_csv(dataframe, filename='top_selling_products_per_week.csv'):
    # Save results to CSV file
    dataframe.to_csv(filename, index=True)






