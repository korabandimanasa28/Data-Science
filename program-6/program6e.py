import pandas as pd
dates = pd.to_datetime([
    '2025-05-10',
    '2025-06-15',
    '2025-07-20',
    '2025-08-25'
])
sales = pd.Series(
    [1200, 1700, 2100, 2600],
    index=dates
)
print("Original Series:")
print(sales)
period_series = sales.to_period('M')
print("\nSeries converted to Monthly Periods:")
print(period_series)
df = pd.DataFrame(
    {
        'Sales': [1200, 1700, 2100, 2600],
        'Profit': [250, 350, 450, 600]
    },
    index=dates
)
print("\nOriginal DataFrame:")
print(df)
period_df = df.to_period('M')
print("\nDataFrame converted to Monthly Periods:")
print(period_df)