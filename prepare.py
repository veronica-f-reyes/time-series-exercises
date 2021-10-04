# Data Prep with Time Series Exercises

# Using your store items data from acquire.py, create functions to prepare and plot data

import acquire
import pandas as pd

#Acquire store data from acquire.py function
#============================================

df = acquire.combine_sales_stores_items_data()

# Function to convert date column to datetime format.
#====================================================

def convert_col_to_date():

    df.sale_date = pd.to_datetime(df.sale_date)

    return 


# Function to plot the distribution of sale_amount and item_price.
#=================================================================

def plot_dists():

    df.sale_amount.hist()
    df.item_price.hist()
    return


# Function to set the index to be the datetime variable.
#=======================================================

def set_datevar_to_index():

    df = df.set_index('sale_date').sort_index()
    return


# Function to add a 'month' and 'day of week' column to your dataframe.
#======================================================================

def add_month_dayofweek_col():

    df['month'] = df.index.month
    df['day_of_week'] = df.index.day_of_week
    return



# Function to add a column to your dataframe, sales_total, which is a derived from sale_amount (total items) and item_price.
#===========================================================================================================================

def add_sales_total_col():

    df['sales_total'] = df.sale_amount * df.item_price
    return