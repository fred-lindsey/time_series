import pandas as pd
import acquire
import os
import requests

def prepare_stores():
    df = acquire.get_combined_df()
    # set the DTG column
    df.sale_date = df.sale_date.strftime('%d-%m-%Y')
    df.sale_date = pd.to_datetime(df.sale_date)
    # set the DTG columns as index, and sort by index
    df = df.set_index('sale_date').sort_index()
    # print check statements for df shape, and item sales dates
    print("The number of unique days is", df.index.nunique())
    n_days = df.index.max() - df.index.min() + pd.Timedelta('1d')
    print("Number of days between first and last day is ", n_days)
    df['month'] = df.index.strftime('%b')
    df['weekday'] = df.index.strftime('%a')
    df['sales_total'] = df.sale_amount * df.item_price
    df = df.drop(columns=['store_id', 'item'])
    return df