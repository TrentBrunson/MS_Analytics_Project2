#%%
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from pandas_profiling import ProfileReport
#%%
file = 'data\heart.csv'
df = pd.read_csv(file)
df
# %%
# This library captures most of the EDA done above
# https://pandas-profiling.github.io/pandas-profiling/docs/master/index.html
profile = ProfileReport(df, title="Pandas Profiling Report", explorative=True)

profile.to_notebook_iframe()
# %%
profile.to_file("CVD.html")
# %%
