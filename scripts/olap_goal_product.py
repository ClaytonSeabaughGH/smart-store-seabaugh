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

# Local imports
PROJECT_ROOT = pathlib.Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

    from utils.logger import logger