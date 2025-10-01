import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    logs['Group'] = (logs['num'] !=logs['num'].shift()).cumsum()
    logs['Group'] = logs['Group'].fillna(0).astype(int)
    logs['count']= logs.groupby('Group')['num'].transform('count')
    return pd.DataFrame({'ConsecutiveNums' : logs[logs['count'] >=3]['num'].drop_duplicates()})
