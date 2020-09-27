import pandas as pd


projPath=r"D:\python\newsFrontSwarajya\data"
file = projPath+r"\news.csv"
outfile="out.json"
data = pd.read_csv(file)

compressed = data.loc[:,['Paper_Name','headline',"links"]]

outData=dict.fromkeys(compressed['Paper_Name'].unique(),[])
#print(compressed.to_dict('list'))
# data.to_json(projPath+outfile,orient="records")

l=[]

for index, row in compressed.iterrows():
    if row["Paper_Name"] in outData:
        outData[row["Paper_Name"]].append({"headline":row['headline'],"links":row['links']})
    else:
        pass

        #l.append({"headline":row['headline'],"links":row['links']})

print(outData['The_HT'])

#print(l[1])
