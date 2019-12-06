#!/usr/bin/python

import pandas as pd

rf = pd.read_csv('imdb_source.csv')

print rf.head()

print rf.describe()
