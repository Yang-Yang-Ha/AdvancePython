import numpy as np
import pandas as pd

import sys_logging

df = pd.DataFrame()


def header(msg):
    sys_logging.info('-' * 50)
    sys_logging.info(f'[{msg}]')


def load_hard_coded_data():
    # 1. load hard-coded data into a dataframe
    header(f'1. Load hard-coded data into df')
    global df
    df = pd.DataFrame(
        [['Jan', 58, 42, 74, 22, 2.95],
         ['Feb', 61, 45, 78, 26, 3.02],
         ['Mar', 65, 48, 84, 25, 2.34],
         ['Apr', 67, 50, 92, 28, 1.02],
         ['May', 71, 53, 98, 35, 0.48],
         ['Jun', 75, 56, 107, 41, 0.11],
         ['Jul', 77, 58, 105, 44, 0],
         ['Aug', 77, 59, 102, 43, 0.03],
         ['Sep', 77, 57, 103, 40, 0.17],
         ['Oct', 73, 54, 96, 34, 0.81],
         ['Nov', 64, 48, 84, 30, 1.7],
         ['Dec', 58, 42, 73, 21, 2.56]],
        index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
        columns=['month', 'avg_high', 'avg_low', 'record_high', 'record_low', 'avg_precipitation']
    )
    sys_logging.info(df)


def data_slice():
    header(f'7.1 slicing -- df.avg_low')  # single column
    sys_logging.info(df.avg_low)
    header(f"7.2 slicing -- df['avg_low']")  # single column
    sys_logging.info(df['avg_low'])
    header(f'7.3 slicing --df[2:4]')  # multiple rows
    sys_logging.info(df[2:4])
    header(f"7.4 slicing -- df[['avg_low', 'avg_high]]")
    sys_logging.info(df[['avg_low', 'avg_high']])
    header(f"7.5 slicing -- df.loc[:, ['avg_low', 'avg_high']]")
    sys_logging.info(df.loc[:, ['avg_low', 'avg_high']])  # df.doc[from_row:to_row,['column1', 'column2']]
    header(f"7.6 slicing -- df.loc[9, ['avg_low', 'avg_high']]")
    sys_logging.info(df.loc[9, ['avg_low', 'avg_high']])
    header(f"7.7 slicing -- df.iloc[3:5,[0,3]]")
    sys_logging.info(df.iloc[3:5, [0, 3]])


def data_attributes():
    header(f'4.1 df.dtypes')
    sys_logging.info(df.dtypes)
    header(f'4.2 df.index')
    sys_logging.info(df.index)
    header(f'4.3 df.columns')
    sys_logging.info(df.columns)
    header(f'4.4 df.values')
    sys_logging.info(df.values)
    header(f'5. df.describe')
    sys_logging.info(df.describe())
    sys_logging.info(df.describe()['avg_high'].max())
    header(f'6. df.sort values record high, ascending = False)')
    sys_logging.info(df.sort_values('record_high', ascending=False))


def load_file_data():
    header(f'2. load file data')
    global df
    df = pd.read_csv('colors.csv')
    sys_logging.info(df)

    header(f'3.1 df.head()')
    sys_logging.info(df.head())
    header(f'3.2 df.tail(3)')
    sys_logging.info(df.tail(3))


def data_assignment():
    header(f"9.1 df.loc[9, ['avg_precipitation']] = 101.3")
    df.loc[9, ['avg_precipitation']] = 101.3
    sys_logging.info(df.iloc[9:11])
    header(f"9.2 df.loc[9, ['avg_precipitation']] = np.nan")
    df.loc[9, ['avg_precipitation']] = np.nan
    sys_logging.info(df.iloc[9:11])
    header(f"9.3 df.loc[:,['avg_low']] = np.array([5]*len(df))")
    df.loc[:, 'avg_low'] = np.array([5] * len(df))
    sys_logging.info(df.head())
    header(f"9.4 df['avg_day'] = (df.avg_low + df.avg_high)/2")
    df['avg_day'] = (df.avg_low + df.avg_high) / 2
    sys_logging.info(df.head())


def data_filtering():
    header(f'8.1 df[df.avg_precipitation>1.0]')
    sys_logging.info(df[df.avg_precipitation > 1.0])
    header(f"8.2 df[df['month'].isin['Jun', 'Jul', 'Aug']]")
    sys_logging.info(df[df['month'].isin(['Jun', 'Jul', 'Aug'])])


def rename_columns():
    header("10.1 df.rename(columns = {'avg_precipitation': 'avg_rain'}, inplace = True)")
    df.rename(columns={'avg_precipitation': 'avg_rain'}, inplace=True)
    sys_logging.info(df.head())
    header("10.2 df.columns = ['month', 'av_hi', 'av_lo', 'rec_hi', 'rec_lo', 'av_rain']")
    df.columns = ['month', 'av_hi', 'av_lo', 'rec_hi', 'rec_lo', 'av_rain']
    sys_logging.info(df.head())


if __name__ == '__main__':
    load_hard_coded_data()
    # load_file_data()
    # data_slice()
    # data_filtering()
    # data_assignment()
    # rename_columns()
    sys_logging.info(type([5]*5))
