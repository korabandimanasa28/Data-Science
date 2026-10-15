import pandas as pd
p = pd.Period('2026-04', freq='M')
print("Original Period:")
print(p)

print("\nAfter adding 2:")
print(p + 2)
print("\nAfter adding 4:")
print(p + 4)

print("\nAfter subtracting 1:")
print(p - 1)
print("\nAfter subtracting 2:")
print(p - 2)
periods = pd.period_range(
    start='2026-04',
    periods=5,
    freq='M'
)
print("\nRange of Periods:")
print(periods)