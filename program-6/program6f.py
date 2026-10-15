import pandas as pd
import numpy as np
rng = pd.date_range('2025-05-01', periods=6, freq='D')
ts = pd.Series(
    np.random.randn(len(rng)),
    index=rng
)
print("Time Series:")
print(ts)
ts_utc = ts.tz_localize('UTC')
ts_ind = ts_utc.tz_convert('Asia/Kolkata')
print("\nTime Series in India Time:")
print(ts_ind)
p = pd.Period('2025Q2')
print("\nNext Quarter:")
print(p + 1)
print("\nQuarter Converted to Month:")
print(p.asfreq('M', 'end'))
ts = pd.Series(
    np.random.randn(90),
    index=pd.date_range(
        '2025-05-01',
        periods=90,
        freq='D'
    )
)
ts_monthly = ts.resample('ME').mean()
print("\nMonthly Mean:")
print(ts_monthly)