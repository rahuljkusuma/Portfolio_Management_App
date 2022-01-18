from pandas import Series, DataFrame
import pandas as pd

data = {'names':["Alembic","RVNL","RIL","NOCIL","RVNL","Dmart","RVNL","Alembic","MSTC","Alembic"],
		'qty':[1,13,5,10,22,2,27,2,11,1],
		'bp':[105.9,21.5,1000,213,19.75,3275,29,132.7,182.2,103.75],
		}


df = pd.DataFrame(data=data)


for i in range(0,len(df['qty'])):
    df.loc[i,'Total'] = df.loc[i,'qty']*df.loc[i,'bp']
    
print(df)


# I am looking for average buying price for each stock.

# Formula for average buying price is (sum of total)/(sum of quantity)

# For example for Alembic average buying price is (105.9+265.4+103.75)/(1+2+1)=118.76