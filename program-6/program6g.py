import pandas as pd
import numpy as np

print("1. Create Time Series:")

rng = pd.date_range('2025-04-01', periods=5, freq='D')
ts = pd.Series([15, 25, 35, 45, 55], index=rng)
print(ts)

print("\n2. Time Zone Conversion:")

ts_utc = ts.tz_localize('UTC')
ts_ind = ts_utc.tz_convert('Asia/Kolkata')
print(ts_ind)

print("\n3. Period Arithmetic and Conversion:")

p = pd.Period('2025Q2')
print("Next Quarter:", p + 1)
print("Quarter End Month:", p.asfreq('M', 'end'))

print("\n4. Resampling:")

dates = pd.date_range('2025-01-01', periods=6, freq='D')
ts = pd.Series([10, 20, 30, 40, 50, 60], index=dates)

ts_monthly = ts.resample('ME').mean()
print("Monthly Average:")
print(ts_monthly)