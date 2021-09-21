import pandas as pd

df = pd.DataFrame({'col01':[1,2,3],'col02':[4,5,6],'col03':[7,8,9]},
                 index=['idx01','idx02','idx03'])
df

#カラムの値を取得
df.columns

#idx03をidx04に変更
df = df.rename(index={'idx03':'idx04'})
df

#col01列をシリーズで取得
df['col01']

#ilocを使って１列目を取得
df.iloc[:,0]

#locを使って１列目から２列目を取得
df.loc[:,'col01':'col02']

#データフレームの各列のデータ型を調べる
df.dtypes
