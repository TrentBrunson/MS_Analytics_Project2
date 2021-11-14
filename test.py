#%%
import pandas as pd
from pandas_profiling import ProfileReport
#%%
file = 'data\heart.csv'
df = pd.read_csv(file)
df
# %%
(df == 0).sum(axis=1)
#%%
df.isin([0]).sum(axis=1)
#%%
df.describe()
#%%
cleanedDF = df.RestingBP.mask(df.RestingBP == 0, 132)

# df.loc[(df.RestingBP == 0), 'RestingBP']=132
cleanedDF
#%%
cleanedDF.describe()
#%%
df
#%%
df.RestingBP.mask(df.RestingBP == 0, 132, inplace=True)
df
#%%
print(df.describe())
# %%
# This library captures most of the EDA done above
# https://pandas-profiling.github.io/pandas-profiling/docs/master/index.html
profile = ProfileReport(df, title="Cardiovascular Disease Data Profiling Report", explorative=True)

profile.to_notebook_iframe()
# %%
profile.to_file("index.html")

# %%
