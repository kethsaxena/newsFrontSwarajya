import pandas as pd
import json 

projPath=r"D:\python\newsFrontSwarajya\data"
file = projPath+r"\news.csv"
outfile="out.json"
data = pd.read_csv(file)

compressed = data.loc[:,['Paper_Name','headline',"links"]]

outData=dict.fromkeys(compressed['Paper_Name'].unique(),[])
row_iterator = compressed.itertuples()




for key in outData.keys():
    set =compressed[compressed.Paper_Name==key]
    outData[key]=set.loc[:,["headline","links"]].to_dict("records") 
    # print("-----------")
    # print("-----------")

#     if key==row.Paper_Name:
#         l.append({"headline":row.headline,"links":row.links})
#     print(l)
# l=[]


#print(outData)
#outData['Indian_Express']=[{"headline":1,"link":2},{"headline":2,"link":3}]
            
        



file=projPath+"\\"+outfile
out_file = open(file, "w") 
json.dump(outData,out_file,indent=4)
out_file.close() 