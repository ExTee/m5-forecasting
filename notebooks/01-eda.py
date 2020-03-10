#%% [markdown]
# # EDA

#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pathlib

SELL_PRICES_PATH = pathlib.Path("../data/raw/sell_prices.csv")

#%%
df_prices = pd.read_csv(SELL_PRICES_PATH)

# Assign categories
df_prices = df_prices.assign(
    category = df_prices['item_id'].apply(lambda x : x.split('_')[0]),
    subcategory = df_prices['item_id'].apply(lambda x : x.split('_')[1]),
)

# %% [markdown] 
# # Inspect prices

print("\nNo N/A records")
print(df_prices.isna().any())


print("\nHow many stores?")
print(df_prices['store_id'].nunique())

print("\nHow many unique items?")
print(df_prices['item_id'].nunique())

print("\nWhat are the items categories?")
print(df_prices['category'].unique())

print("\nHow many items in each category?")
print(
    df_prices
    .groupby(['category'])
    .agg(
        subcategory_count = ('subcategory', 'nunique')
    ))

print("\nHow many unique items?")
df_prices.groupby(['category', 'subcategory']).agg(unique_items = ('item_id', 'nunique'))

# %%


# %%
pd.Series(df_prices['item_id'].unique()).apply(lambda x : x.split('_')[0]).unique()

# %%


# %%
