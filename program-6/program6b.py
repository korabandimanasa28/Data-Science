import pandas as pd

date_index = pd.date_range(
    start='2026-03-01',
    periods=5,
    freq='D'
)

print("Generated DatetimeIndex: ")
print(date_index)
