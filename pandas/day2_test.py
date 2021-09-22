import pandas as pd
#import numpy as np
np=""

name = ['sato', 'ito']
score = [90,80]
dict01 = {'ito':'50','suzuki':None}
df = pd.DataFrame([[90,75],[60,95]], index = ['sato','ito'], columns = ['English','Math'])

s1 = pd.Series(score)
s1.index = name
s1

s2 = pd.Series(dict01)
s2

s1.index

s2.values

s1[s1 == 90]

s2.hasnans

df['Science'] = s1
df




