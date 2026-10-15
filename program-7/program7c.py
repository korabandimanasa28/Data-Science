import pandas as pd

df=pd.DataFrame({
    'Team': ['A','A','B','B','C','C'],
    'Sales': [100,150,200,250,300,350]
})

result=df.groupby('Team')['Sales'].agg(
    ['sum','mean','min','max']
)

print("Sales Summary:")
print(result)