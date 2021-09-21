#import pandas as pd
pd = ""
#↑jupyterでは上のコメントを外し、pdの変数宣言を消す

#DataFrameを使ったデータフレームの作成
df = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]],
                 columns = ['col1','col2','col3'],
                 index = ['idx01','idx02','idx03'])
df

#import numpy as np
np = ""
#↑jupyterでは上のコメントを外し、npの変数宣言を消す

#NumPyを使ったデータフレームの作成
df = pd.DataFrame(np.array([[1,2,3],[4,5,6],[7,8,9]]),
                 columns = ['col1','col2','col3'],
                 index = ['idx01','idx02','idx03'])
df

df.index
df.columns

#辞書型を使ったデータフレームの作成
df = pd.DataFrame({'col01':[1,2,3],
                  'col02':[4,5,6,],
                  'col03':[7,8,9]})
df.index=['idx01','idx02','idx03']
df

df = pd.DataFrame({'col01':[1,2,3],
                  'col02':[4,5,6,],
                  'col03':[7,8,9]},
                 index=['idx01','idx02','idx03'])
df

#カラム、インデックスの操作
df = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]])
df

#カラム名、インデックス名を付ける
df.columns=['col1','col2','col3']
df.index=['idx01','idx02','idx03']
df

#カラム名を変更
df.columns=['col4','col5','col6']
df

#renameメソッドでカラム名を変更
df = df.rename(columns={'col4': 'x','col5': 'y','col6': 'z'})
df

#renameメソッドでインデックス名を変更
df= df.rename(index={'idx01': 'w'})
df

#列を取得
df['x']

#データ型を取得
type(df['x'])

#データフレームとして列を取得
df[['x']]

type(df[['x']])

df.loc['w']

df = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]],
                 columns = ['col1','col2','col3'],
                 index = ['idx01','idx02','idx03'])
df

#行と列を指定して特定の値を取得する※行と列の順番を変えるとエラーになるので注意
df.loc['idx02','col2']

#「：」は全てという意味
df.loc[:,'col2']

#ilocは行の番号や列の番号を指定して、行や列を取得する
df.iloc[:,0]

df = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]],
                 columns = ['col1','col2','col3'],
                 index = ['idx01','idx02','idx03'])
df

#表の値を変更
df.loc['idx03','col2']= 100
df

#表の値を複数変更
df.loc[:,'col3']=['Tokyo','Osaka','Miyagi']
df

#スライスで２〜３列目を取得
df.loc[:,'col2':'col3']

df.iloc[:,1:3]

#列ごとのデータ型を調べる
df.dtypes

#何行何列のデータフレームか確認
df.shape

#行と列を入れ替える
df.T
