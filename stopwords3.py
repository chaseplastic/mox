#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 11:32:02 2017

@author: davkenda1
"""

import unicodecsv
import pandas as pd

#stop_words = set(stopwords.words('english'))
stop = ["am", "his", "the", "to", "they", "i", "your", "so", "it", "it's", "a", "is", "and", "of", "for", "in", "that", "we", "was", "are", "be", "at", "he", "my", "but", "this", "it", "on", "if", "im"]

df = pd.read_csv("~/Desktop/vw_R_PostLikes.csv", 'wb', usecols=['Comment'], na_values=[" "], encoding="latin1")

df["Comment"].str.replace('[^\w\s]','')

df["Comment"].fillna('', inplace=True)

df['Comment'] = df['Comment'].str.lower().str.split()

df['Comment'] = df['Comment'].apply(lambda x: [item for item in x if item not in stop])

print(df.head())

#Comment = df['Comment']

df["Comment"] = df['Comment'].apply(lambda x: ' '.join(x))
    
#Comment.str.cat(sep=' ')

#" ".join(Comment)

df['Comment'] = df['Comment'].map(lambda x: x.encode('unicode-escape').decode('utf-8'))  # this is amazing. Solves ascii encoding problem!

with open('****Posts.csv', 'w') as f:
    df.to_csv(f, header=True, encoding='utf-8', index=False)