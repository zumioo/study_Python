import pandas as pd

#シリーズを作成
s1 = pd.Series([99,88,54,22,55])
s1

#変数に入れてからシリーズを作成する方法
data = [99,88,54,22,55]

s1 = pd.Series(data)
s1

#import numpy as np
np = ""
#↑jupyterでは逆で


#numpyで1~10まで２ずつ増やして値を格納
np.arange(1,10,2)

data2 = np.arange(1,10,2)

s2 = pd.Series(data2)
s2

#データ型を表示
s1.dtypes

#インデックスを表示
s1.index

s1.index= ['sato','suzuki','takahashi', 'tanaka', 'ito']
s1

s1.index

#配列を作成
dict01 = {'sato':90,'suzuki':78,'takahashi':65, 'tanaka':87, 'ito':72}

s3 = pd.Series(dict01)
s3

s1.values

s1['suzuki']

s1[1]

#インデックス名で値を取得
s1[['suzuki','tanaka']]

#インデックス番号で値を取得
s1[[1,3]]

s1 > 80

s1[s1 > 80]

#要素数を取得
s1.size

#要素数を取得
len(s1)

#index名を変更
s1.index.name = 'member'
s1.name = 'score'
s1

#四則演算
s1 + 2

s2.index = ['suzuki','takahashi','tanaka','ito','watanabe']

#シリーズ同士で足し算
s1 + s2

#Nan値があるか判定
s1.hasnans

s4 = pd.Series([22,None,43,21,55])
s4

s4.hasnans

#どの値が欠損しているか確認
pd.isnull(s4)

df = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]],
                 columns = ['col01','col02','col03'],
                 index = ['idx01','idx02','idx03'])
df


df['col01']

type(df['col01'])

s5 = pd.Series({'idx01':10,'idx02':11,'idx03':12})

df['col04'] = s5
df

#時系列データの作成
dates = pd.date_range('2000/01/01', periods = 5, freq = 'D')
dates

s1.index =dates 
s1
