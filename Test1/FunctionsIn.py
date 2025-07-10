import pandas as pd

data = {
    'Name' : ['Alice','Giri','Guru','Sheriff'],
    'AWS' : [75,100,95,100],
    'Azure':[100,85,89,90]
}

df  = pd.DataFrame(data)

print(df)

print(df[['AWS','Azure']].apply(lambda x : x.mean()))