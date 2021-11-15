#%%
import pandas as pd
# from pandas_profiling import ProfileReport
import matplotlib.pyplot as plt
import seaborn as sns
#%%
file = 'data\heart.csv'
df = pd.read_csv(file)
df
#%%
fig, axs = plt.subplots(len(df.columns), figsize=(5, 20))
for n, col in enumerate(df.columns):
    # print(col)
    a = df[col].hist(ax=axs[n])
    a.set_title(col)

fig.tight_layout()
#%%
plt.figure(figsize=(8,8))
sns.displot(df['Age'], color="red", label="Age", kde= True)
plt.legend()
plt.savefig("images\CVD_by_Age.png")
#%%
plt.figure(figsize=(8,8))
sns.displot(df['Cholesterol'], color="blue", label="Cholesterol")
plt.legend()
plt.savefig("images\C2.png")
#%%
df.Cholesterol.plot(kind = "hist", bins = 20, figsize = (8,5))
plt.legend()
plt.savefig("images\cholesterol.png")
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
