import pandas as pd
import numpy as np

ds2014 = pd.read_csv("dataset/2014_Financial_Data.csv")
ds2015 = pd.read_csv("dataset/2015_Financial_Data.csv")
ds2016 = pd.read_csv("dataset/2016_Financial_Data.csv")
ds2017 = pd.read_csv("dataset/2017_Financial_Data.csv")
ds2018 = pd.read_csv("dataset/2018_Financial_Data.csv")

print(ds2014.shape, ds2015.shape, ds2016.shape, ds2017.shape, ds2018.shape)

ds2014.dropna(axis="columns")
ds2014.dropna(axis="rows")
ds2015.dropna(axis="columns")
ds2015.dropna(axis="rows")
ds2016.dropna(axis="columns")
ds2016.dropna(axis="rows")
ds2017.dropna(axis="columns")
ds2017.dropna(axis="rows")
ds2018.dropna(axis="columns")
ds2018.dropna(axis="rows")

print(ds2014.shape, ds2015.shape, ds2016.shape, ds2017.shape, ds2018.shape)
