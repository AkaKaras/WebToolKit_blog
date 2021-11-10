# -*- coding: UTF-8 -*-
import json
import glob
import numpy as np




def readAll():
    count_poet = 0

    #loop each json file
    for file_num in range(0,58):

        file_num = file_num*1000

        file_name = "C:/Users/chun_/Documents/programing_learning/chinese-poetry/json/poet.tang.%s.json"%(file_num)
        print("```")
        print("poet.tang.%s"%(file_num))

        #open the file
        with open(file_name,'r',encoding="utf-8") as j:
            #load the file into json format
            data = json.loads(j.read())

        for d in data:
            paragraphs = d['paragraphs']
            #hasQuestion = True in ["？" in p for p in paragraphs]
            #endQuestion = True in ['？' in p[-1] for p in paragraphs]

            li = [len(p) for p in paragraphs]
            
            std = np.std(li)
            diff_std =  3 if len(li) <= 2 else np.std(np.diff(li))
            #mean = np.mean(li)

            
            #if std > 1: #find 曲
            #if std > 1 and (hasQuestion):
            if std > 3.3 and diff_std > 1 and ('曲' not in d['title'] and '歌' not in d['title']):
                count_poet += 1
                print(d['title'],d['author'])
    

        print("```")   

        input("")  

            
        j.close()

    print("total ",count_poet,"poets needed to be fixed")

def readFile(file_num):
    count_poet = 0
    file_num = file_num*1000

    file_name = "C:/Users/chun_/Documents/programing_learning/chinese-poetry/json/poet.tang.%s.json"%(file_num)
    print("```")
    print("poet.tang.%s"%(file_num))

    #open the file
    with open(file_name,'r',encoding="utf-8") as j:
        #load the file into json format
        data = json.loads(j.read())

    for d in data:
        paragraphs = d['paragraphs']
        #hasQuestion = True in ["？" in p for p in paragraphs]
        #endQuestion = True in ['？' in p[-1] for p in paragraphs]

        li = [len(p) for p in paragraphs]
        
        std = np.std(li)
        diff_std =  3 if len(li) <= 2 else np.std(np.diff(li))
        #mean = np.mean(li)

        
        #if std > 1: #find 曲
        #if std > 1 and (hasQuestion):
        if std > 3.3 and diff_std > 1 and ('曲' not in d['title'] and '歌' not in d['title']):
            count_poet += 1
            print(d['title'],d['author'])


    print("```")   

    input("")  

        
    j.close()

def readFile(file_num,condition):
    count_poet = 0
    file_num = file_num*1000

    file_name = "C:/Users/chun_/Documents/programing_learning/chinese-poetry/json/poet.tang.%s.json"%(file_num)
    print("```")
    print("poet.tang.%s"%(file_num))

    #open the file
    with open(file_name,'r',encoding="utf-8") as j:
        #load the file into json format
        data = json.loads(j.read())

    for d in data:
        paragraphs = d['paragraphs']
        #hasQuestion = True in ["？" in p for p in paragraphs]
        #endQuestion = True in ['？' in p[-1] for p in paragraphs]

        li = [len(p) for p in paragraphs]
        
        std = np.std(li)
        #diff_std =  3 if len(li) <= 2 else np.std(np.diff(li))
        #mean = np.mean(li)

        
        #if std > 1: #find 曲
        #if std > 1 and (hasQuestion):
        if std > 0 and condition:
            count_poet += 1
            print(d['title'],d['author'])


    print("```")   

    input("")  

        
    j.close()

readFile(57,True)