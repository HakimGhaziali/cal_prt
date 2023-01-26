import pandas as pd
import numpy as np
import re



df = pd.read_json('result.json')
df = pd.DataFrame(df)
x = df['messages']
litext=[]
lidate=[]


for i in range(0,1000155):
    texti=x[i]['text']
   

    litext.append(texti)



litext = list(map(str, litext))

clean = [re.sub('\n','', file) for file in litext]
clean = [re.sub('-','', x) for x in clean]
clean = [re.sub('\?','', x) for x in clean]
clean = [re.sub(' ','', x) for x in clean]
clean = [re.sub('_','', x) for x in clean]
clean = [re.sub('\.','',x) for x in clean]
clean = [re.sub('\'','',x) for x in clean]
clean = [re.sub('\}','',x) for x in clean]
clean = [re.sub('\{','',x) for x in clean]
clean = [re.sub('\,','',x) for x in clean]


clean = [x.upper() for x in clean]
lust=['25630','28510','23121']


def myfun(lust , clean):

    for i in lust:



         new = [re.findall(i+'....\d',file) for file in clean]
         res = [ele for ele in new if ele != []]
         x = pd.DataFrame(res)
         y= x.iloc[0:,0].value_counts().to_frame()

         t = pd.DataFrame(y[:40]).reset_index().to_html()



         return t
   


