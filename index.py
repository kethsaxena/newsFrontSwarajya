import pandas as pd


projPath=r"D:\python\newsFrontSwarajya\data"
file = projPath+r"\news.csv"
outfile="out.json"
data = pd.read_csv(file)
headline = data.loc[:0,'headline']
link = data.loc[:0,'links']

data.to_json(projPath+outfile,orient="records")