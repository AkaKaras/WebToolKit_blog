# -*- coding: UTF-8 -*-
import json
import glob
import numpy as np

#file_name = "poet.tang.4000"
count_poet = 0
#open files and store the files in a list
tang_poet_files = glob.glob("C:/Users/chun_/Documents/programing_learning/chinese-poetry/json/poet.tang.*.json")
#tang_poet_files = ["C:/Users/chun_/Documents/programing_learning/chinese-poetry/json/%s.json"%(file_name)]


#loop each json file
for file in tang_poet_files:

    print(file)

    #open the file
    with open(file,'r',encoding="utf-8") as j:
        #load the file into json format
        data = json.loads(j.read())

    for d in data:
        try:
            paragraphs = d['paragraphs']
            hasQuestion = True in ["？" in p for p in paragraphs]
            #print(d['title'])
            endQuestion = True in ['？' in p[-1] for p in paragraphs]

            li = [len(p) for p in paragraphs]
            std = np.std(li)
            most_freq = np.bincount(li).argmax()

            new_para = []
            if std > 1 and ((hasQuestion and not endQuestion) != False):
                count_poet += 1
                print(d['title'])
                for p in paragraphs:
                    if "？" in p and len(p) > most_freq:
                        print(p)
                        sentences = p.split("？")
                        if len(sentences) == 2:
                            sentence = sentences[0]+"？"
                            new_para.append(sentence)
                            new_para.append(sentences[1])
                        else:
                            new_para.append(p)
                            print(d['title'],p)
                    else:
                        new_para.append(p)
                d['paragraphs'] = new_para
        except:
            print(d['title'])
        
    j.close()

    with open(file,'w',encoding='utf-8') as nf:
        json.dump(data,nf,ensure_ascii=False,indent=4)
    
    nf.close()

print("fix ", count_poet,"poets")
   

