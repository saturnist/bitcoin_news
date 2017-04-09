import pandas as pd
from datetime import datetime

from coindesk import btc_interval

def bpi_df(start, end):
    """
    shows a dataframe of price on a interval of dates 
    :param start: string in year, month, day e.g. 20170419
    :param end: string in year, mont, day e.g. 20170420
    :return: dataframe with date and USD column
    """
    btc = btc_interval(start, end)
    btc = btc['bpi']
    df = pd.DataFrame(list(btc.items()), columns=['Date', 'USD'])
    return df


def percent_change(df):
    """
    
    :param df: dataframe from bpi_df
    :return: amount of percent change in each day following previous day
    """
    return df['USD'].pct_change()


def merger(df, df2):
    """
    
    :param df: data frame from bpi_df
    :param df2: percent change df
    :return: merged df
    """
    merge_df = df.merge(df2.to_frame(), left_index=True, right_index=True)
    merge_df.columns = ['Date', 'USD', 'percent_change']
    return merge_df


def high_percents(merge_df):
    """
    
    :param merge_df: merged df
    :return: shows dates with greater than 9% change
    """
    date_inc = merge_df[merge_df['percent_change'] > 0.09]
    return date_inc['Date']


def low_percents(merge_df):
    """
    
    :param merge_df: merged df
    :return: shows dates with less than 9% change
    """
    date_dec = merge_df[merge_df['percent_change'] < -0.09]
    return date_dec['Date']


def timestamp_convert(df):
    """
    
    :param df: merged df
    :return: converts the dates from above into usable timestamps for nyt api
    """
    times = {'high': [], 'low': []}

    for high in high_percents(df):
        times['high'].append(int(datetime.strptime(high, '%Y-%m-%d').timestamp()))

    for low in low_percents(df):
        times['low'].append(int(datetime.strptime(low, '%Y-%m-%d').timestamp()))

    return times
