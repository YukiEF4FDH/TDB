from asyncio.windows_events import NULL
from cmath import nan
from contextlib import nullcontext
from email.policy import default
# from nis import match
from pickle import FALSE, TRUE
import pandas as pd
from flask import Flask, jsonify
from flask_cors import CORS

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

# # 定义一个Ref class 用于在app.py与ref_validation.py之间通信
# class Reference:
#     sentence = NULL
#     sentence_before = NULL

# ------------------------------Csv Files Loading------------------------------
#    Load all of the csv files under "\CSVFiles"
#    and turn them into instances of class:CsvDf.
#    Create a csv_df_list for the results.
#    csv_df_list[i] -> An instance of class:CsvDf of the csv file.

import csv_df as cd

csv_dfs = cd.CsvDfs()  # The list of class:CsvDf

# Load *all* of the csv files under "\CSVFiles"
def load_csv_files():
    cd.load_csv_files(csv_dfs)

load_csv_files()

# ----------------------Csv Data (df) -> Json -> Front-end----------------------
# To get the particular csv data at the front-end in Json:
# path = "http://127.0.0.1:5000/CSV/sheet1"
# path = "http://127.0.0.1:5000/CSV/sheet2A"
# ...
# path = "http://127.0.0.1:5000/CSV/<string:sheetId>"
# Where the sheetId refers to the csv file name.

@app.route('/CSV/<string:sheetId>', methods=['GET'])
def chart(sheetId):
    for csv_df in csv_dfs.csv_df_list:
        if csv_df.id == sheetId:
            json_of_df = csv_df.jsonify()
            return json_of_df



SEC1_TEXT0_MD = [
    {
        'CONTENT': 'Sec1-Text0-MD: This <ref>is</ref> the updated *text* content !!!',
    },
]
	
@app.route('/sec1-text0-md', methods=['GET']) # Test for markdown text to html
def sec1_text0_md():
	return jsonify(SEC1_TEXT0_MD);

SEC2_TEXT0_MD = [
    {
        'CONTENT': 'Sec2-Text0-MD: This <ref>is</ref> the updated *text* content !!!',
    },
]
	
@app.route('/sec2-text0-md', methods=['GET']) # Test for markdown text to html
def sec2_text0_md():
	return jsonify(SEC2_TEXT0_MD);

df = pd.read_csv (r'F1A_Data.csv',header=0)#, index_col=0)
total = df.sum(axis=1)
df['total'] = total
f1a = df.to_json (orient='records',force_ascii=False)
index1 = df.loc[:,"month"].values.tolist()
col1 = set(df.columns.values[1:].tolist())
print(index1)
print(col1)
	
@app.route('/f1a-json', methods=['GET']) # Test for Json loading
def f1a_json():
	return jsonify(f1a);

df2 = pd.read_csv (r'F2A_Data.csv',header=0)
f2a = df2.to_json (orient='records',force_ascii=False)
index2 =  df2.loc[:,"name"].values.tolist()
col2 = set(df2.columns.values[1:].tolist())
print(df2)
print(index2)
print(col2)
df2ColName = '業界'

@app.route('/data-2-1', methods=['GET']) # Test for Json loading
def f2a_json():
    return jsonify(f2a);

df22 = pd.read_csv (r'F2A_Data2.csv',header=0)
f2a2 = df22.to_json (orient='records',force_ascii=False)
index22 =  df22.loc[:,"name"].values.tolist()
col22 = set(df22.columns.values[1:].tolist())
print(index22)
print(col22)

@app.route('/data-2-2', methods=['GET']) # Test for Json loading
def f2a2_json():
    return jsonify(f2a2);

df3 = pd.read_csv (r'F3A_Data.csv',header=0)
f3a = df3.to_json (orient='records',force_ascii=False)
index3 =  df3.loc[:,"name"].values.tolist()
col3 = {''}

@app.route('/f3a-json', methods=['GET']) # Test for Json loading
def f3a_json():
    return jsonify(f3a);
    
import re

def Warning():
    print("warning!")

refRegExs = [
            # 1.「今後マイナスの影響がある」が11.1%、...
            # ...『小売』が10.3%で最も高かった。
            # 3.「新しい生活様式」がすでに定着している企業は10.0%<br>
            '(.*?)([(「(.+?)」)(『(.+?)』)])[がは]([0-9]+?)((\.[0-9]+?)*)(%*).*', 
            # ...『マイナスの影響がある』(「既にマイナスの影響がある」と「今後マイナスの影響がある」の合計)と見込む企業は83.7%となった。
            # ...『プラスの影響がある』(「既にプラスの影響がある」と「今後プラスの影響がある」の合計)と見込む企業は4.6%となり、...。
            '(.*?)『(.+?)』(.*?)[がは]([0-9]+?)((\.[0-9]+?)*)(%*).*',

            # 次いで、『金融』(9.1%)、『製造』(5.8%)が続く。
            '(.*?)『(.+?)』\(([0-9]+?)((\.[0-9]+?)*)(%*)\).*',

            # 0720
            # (...(「row|col」...(尽可能少的字符)<ref ...>val%</ref>))+...
            r'(.*?)((([(「(.+?)」)(『(.+?)』)])(.*?)<ref (.*?)>(([0-9]+?)((\.[0-9]+?)*))(%*)</ref>)+)(.*)', 
            
            ]
df = df.astype('str')
df2 = df2.astype('str')
df3 = df3.astype('str')
import numpy as np

# def RecommendIndexColumnPairs(idx,col):
    
defaultTimeStamp = '11月'

def MatchInTable(refSentence): # 对于每个「」：在set中找到 对应的col或者row 
    global index1
    valRe = r'<ref (.*?)>([0-9]+(\.[0-9]+)?)%?</ref>'
    mathcedVals = re.findall(valRe, refSentence) # 找到带ref的句子中的每一个val
    nameRe = r'「.+?」|『.+?』'  # 抽出句子中的「」(本来想找离val最近的 但是无所谓了
    matchedNames_ = set(re.findall(nameRe, refSentence))
    matchedNames = set()
    for name in matchedNames_:
        matchedNames.add(name[1:len(name)-1])
    for matchedVal in mathcedVals: #对于每一个val：
        refId = matchedVal[0] 
        val = matchedVal[1] 
        boolDf = df.eq(val) 
        x,y = np.where(boolDf)
        indexes = (boolDf.index[x]).tolist() # 找出该表格中所有和这个val相等的index和col对
        indexes = [index1[i] for i in indexes]
        columns = (boolDf.columns[y]).tolist() # 这两者应该长度一致
        for i in range(len(indexes)):
            index = indexes[i]
            column = columns[i]
            if (index in matchedNames) and (column in matchedNames):
                print ("Are you looking for ("+index+", "+column+") where val = "+str(val)+" ?")
            elif (index in matchedNames) or (column in matchedNames):
                print ("Are you looking for ("+index+", "+column+") where val = "+str(val)+" ?")

def MatchInTable2(refSentence): # 对于每个「」：在set中找到 对应的col或者row 
    valRe = r'<ref (.*?)>([0-9]+(\.[0-9]+)?)%?</ref>'
    mathcedVals = re.findall(valRe, refSentence) # 找到带ref的句子中的每一个val
    nameRe = r'「.+?」|『.+?』'  # 抽出句子中的「」(本来想找离val最近的 但是无所谓了
    matchedNames_ = set(re.findall(nameRe, refSentence))
    matchedNames = set()
    for name in matchedNames_:
        matchedNames.add(name[1:len(name)-1])
    for matchedVal in mathcedVals: #对于每一个val：
        refId = matchedVal[0] 
        val = matchedVal[1] 
        boolDf = df2.eq(val) 
        x,y = np.where(boolDf)
        indexes = (boolDf.index[x]).tolist() # 找出该表格中所有和这个val相等的index和col对
        indexes = [index2[i] for i in indexes]
        columns = (boolDf.columns[y]).tolist() # 这两者应该长度一致
        for i in range(len(indexes)):
            index = indexes[i]
            column = columns[i]
            if (index in matchedNames) and (column in matchedNames):
                print ("Are you looking for ("+index+", "+column+") where val = "+str(val)+" ?")
            elif (index in matchedNames) or (column in matchedNames):
                print ("Are you looking for ("+index+", "+column+") where val = "+str(val)+" ?")

def MatchInTable22(refSentence): # 对于每个「」：在set中找到 对应的col或者row 
    valRe = r'<ref (.*?)>([0-9]+(\.[0-9]+)?)%?</ref>'
    mathcedVals = re.findall(valRe, refSentence) # 找到带ref的句子中的每一个val
    nameRe = r'「.+?」|『.+?』'  # 抽出句子中的「」(本来想找离val最近的 但是无所谓了
    matchedNames_ = set(re.findall(nameRe, refSentence))
    matchedNames = set()
    for name in matchedNames_:
        matchedNames.add(name[1:len(name)-1])
    for matchedVal in mathcedVals: #对于每一个val：
        refId = matchedVal[0] 
        val = matchedVal[1] 
        boolDf = df22.eq(val) 
        x,y = np.where(boolDf)
        indexes = (boolDf.index[x]).tolist() # 找出该表格中所有和这个val相等的index和col对
        indexes = [index22[i] for i in indexes]
        columns = (boolDf.columns[y]).tolist() # 这两者应该长度一致
        for i in range(len(indexes)):
            index = indexes[i]
            column = columns[i]
            if (index in matchedNames) and (column in matchedNames):
                print ("Are you looking for ("+index+", "+column+") where val = "+str(val)+" ?")
            elif (index in matchedNames) or (column in matchedNames):
                print ("Are you looking for ("+index+", "+column+") where val = "+str(val)+" ?")


def MatchInTable3(refSentence): # 对于每个「」：在set中找到 对应的col或者row 
    valRe = r'<ref (.*?)>([0-9]+(\.[0-9]+)?)%?</ref>'
    mathcedVals = re.findall(valRe, refSentence) # 找到带ref的句子中的每一个val
    nameRe = r'「.+?」|『.+?』'  # 抽出句子中的「」(本来想找离val最近的 但是无所谓了
    matchedNames_ = set(re.findall(nameRe, refSentence))
    matchedNames = set()
    for name in matchedNames_:
        matchedNames.add(name[1:len(name)-1])
    for matchedVal in mathcedVals: #对于每一个val：
        refId = matchedVal[0] 
        val = matchedVal[1] 
        boolDf = df3.eq(val) 
        x,y = np.where(boolDf)
        indexes = (boolDf.index[x]).tolist() # 找出该表格中所有和这个val相等的index和col对
        indexes = [index3[i] for i in indexes]
        columns = (boolDf.columns[y]).tolist() # 这两者应该长度一致
        for i in range(len(indexes)):
            index = indexes[i]
            column = columns[i]
            if (index in matchedNames) and (column in matchedNames):
                print ("Are you looking for ("+index+", "+column+") where val = "+str(val)+" ?")
            elif (index in matchedNames) or (column in matchedNames):
                print ("Are you looking for ("+index+", "+column+") where val = "+str(val)+" ?")
            else:
                for name in matchedNames:
                    print(name)
                    print(index)
                    if name in index:
                        print ("Are you looking for ("+index+", "+column+") where val = "+str(val)+" ?")


def CheckRef(sentence): 
    if "ref" in sentence:
        MatchInTable(sentence)
    else:
        Warning()
    # flag = FALSE
    # for refRE in refRegExs:
    #     matchResults = re.match(refRE, sentence)
    #     if matchResults:
    #         print(matchResults[2]) # -> MatchInTable()
    #         print('\n')
    #         flag = TRUE
    # if flag==FALSE:
    #     Warning()
 
# import test as te
# te.ThisIsAFunc(5)

def CheckRef2(sentence): 
    if "ref" in sentence:
        MatchInTable2(sentence)
        MatchInTable22(sentence)
    else:
        Warning()

def CheckRef3(sentence): 
    if "ref" in sentence:
        MatchInTable3(sentence)
    else:
        Warning()


def AIncreasedXComparedWithB(sentence,sentenceBefore):
    global col1
    global index1
    clRE = r'(.*?)([0-9]+月)より<claim .*?>(([0-9]+)((\.[0-9]+)*))(.*?)</claim>増加.*'
    RowOrColNameRE = r'「.+?」|『.+?』'
    matchResults = re.match(clRE, sentence)
    if matchResults:
        rowB = matchResults[2]
        X = matchResults[3]
        rowA = defaultTimeStamp
        if matchResults[1] != None and matchResults[1] != '':
            # print(matchResults[1])
            colNames = set(re.findall(RowOrColNameRE, str(matchResults[1])))
            print(colNames)
        elif sentenceBefore != None and sentenceBefore != '':
            colNames = set(re.findall(RowOrColNameRE, sentenceBefore))
            print(colNames)
        else:
            colNames = ''
        if colNames:
            for colName in colNames:
                colName = colName[1:len(colName)-1]
                if colName in col1:
                    print(colName)
                    val1 = df.at[index1.index(rowA),colName]
                    val2 = df.at[index1.index(rowB),colName]
                    print(rowA+' '+colName+' '+val1)
                    print(rowB+' '+colName+' '+val2)
    else:
        return
import decimal
from decimal import Decimal
def APlusBEqualToX(sentence): # 「」と「」の合計
    global col1
    global index1
    clRE = r'.*?(『.+?』)（(「.+?」と「.+?」)の合計）.*?[がは]<claim .*?>([0-9]+(\.[0-9]+)*)(.*?)</claim>.*'
    matchResults = re.match(clRE, sentence)
    if matchResults:
        C = matchResults[1]
        AB = matchResults[2]
        X = matchResults[3]
        RowOrColNameRE = r'「.+?」|『.+?』'
        AB = re.findall(RowOrColNameRE, AB)
        C = re.findall(RowOrColNameRE, C)
        if AB:
            A = AB[0]
            A = A[1:len(A)-1]
            B = AB[1]
            B = B[1:len(B)-1]
            if A in col1 and B in col1:
                valA = float(df.at[index1.index(defaultTimeStamp),A])
                valB = float(df.at[index1.index(defaultTimeStamp),B])
                X = Decimal(float(X)).quantize(Decimal("0.01"), rounding = "ROUND_HALF_UP")
                valAB = Decimal(valA+valB).quantize(Decimal("0.01"), rounding = "ROUND_HALF_UP")
                if valAB==X:
                    print(str(valA)+'+'+str(valB)+'='+str(X))
            else:
                # 将AB加入到df的备份里 让后面的计算也可以用 这边的计算全部用备份更新过的df做 前面的绘图用旧的df做 需要更新的时候再用新的
                df[A] = nan
                df[B] = nan
                print(df)
        if C:
            C = C[0]
            C = C[1:len(C)-1]
            if C in col1:
                valC = float(df.at[index1.index(defaultTimeStamp),C])
                valC = Decimal(float(valC)).quantize(Decimal("0.01"), rounding = "ROUND_HALF_UP")
                X = Decimal(float(X)).quantize(Decimal("0.01"), rounding = "ROUND_HALF_UP")
                if valC==X:
                        print(str(valC)+'='+str(X))
            else:
                # df. astype({A: float}, errors='raise')
                # df. astype({B: float}, errors='raise')
                df[A] = pd.to_numeric(df[A])
                df[B] = pd.to_numeric(df[B])
                df[C] = df.loc[:,[A,B]].sum(axis=1)
                print(df)
        index1 = df.loc[:,"month"].values.tolist()
        col1 = set(df.columns.values[1:].tolist())
    else:
        Warning()
import math
# 『マイナスの影響がある』...<claim claim_id=\'claim-1-4\'>3カ月ぶりに増加</claim>に転じた
def TurnedToIncreaseInXMonths(sentence,sentenceBefore):
    global index1
    clRE = r'.*?<claim .*?>([0-9]+?)カ月ぶりに増加.*'
    matchResults = re.match(clRE, sentence)
    rowNames = list()
    if matchResults:
        X = int(matchResults[1])
        defaultTimeStampDigit = int(defaultTimeStamp[0:defaultTimeStamp.find('月')])
        X0 = defaultTimeStampDigit - X - 1
        ColNameRE = r'『.+?』'
        colNames = re.findall(ColNameRE, sentence)
        if colNames:
            print(colNames)
        else:
            colNames = re.findall(ColNameRE, sentenceBefore)
            print(colNames)
        for i in range (X0, defaultTimeStampDigit+1):
            rowNames.append(str(i)+'月')
        for col in colNames:
            col = col[1:len(col)-1]
            if col in col1:
                for i in range(0, len(rowNames)-1):
                    row = rowNames[i]
                    row1 = rowNames[i+1]
                    if not math.isnan(df.at[index1.index(row),col]) and not math.isnan(df.at[index1.index(row1),col]):
                        if i==0 or i==(len(rowNames)-2):
                            print((row1+','+col+': '+str(df.at[index1.index(row1),col]))+'-'+(row+','+col+': '+str(df.at[index1.index(row),col]))+'>0')
                        else:
                            print((row+','+col+': '+str(df.at[index1.index(row),col]))+'-'+(row1+','+col+': '+str(df.at[index1.index(row1),col]))+'>0')

def trenddetector(list_of_index, array_of_data, order=1):
    result = np.polyfit(list_of_index, list(array_of_data), order)
    slope = result[-2]
    return float(slope)

def SlightlyIncreasingSinceX(sentence, sentenceBefore):
    global index1
    clRE = r'.*?<claim .*?>([0-9]+?)月以降微増傾向.*'
    matchResults = re.match(clRE, sentence)
    colNames = list()
    ColNameRE = r'「.+?」|『.+?』'
    colNames = set(re.findall(ColNameRE, sentence))
    if not colNames and sentenceBefore != None and sentenceBefore != '':
        colNames = set(re.findall(ColNameRE, sentenceBefore))
    elif not colNames:
        colNames = ''
    rowNames = list()
    if matchResults:
        X = int(matchResults[1]) # 2
        defaultTimeStampDigit = int(defaultTimeStamp[0:defaultTimeStamp.find('月')]) # 11
        for i in range (X, defaultTimeStampDigit+1):
            rowNames.append(str(i)+'月')
    dataList = list()
    list_of_index = list()
    i=1
    for col in colNames:
        containsNan = bool(False)
        col = col[1:len(col)-1]
        for row in rowNames:
            val = float(df.at[index1.index(row),col])
            if not containsNan and math.isnan(val):
                containsNan = bool(True)
            elif not containsNan:
               dataList.append(val) 
               list_of_index.append(i)
               i+=1
        containsNan = bool(False)
    print(dataList)
    print(list_of_index)
    if len(dataList)>0 and len(list_of_index)>0:
        result = np.polyfit(np.array(list_of_index), np.array(dataList), 1)
        slope = result[-2]
        print("slope="+str(float(slope)))
        if float(slope)>0:
            print("Increasing.")

# 2.『マイナスの影響』は5カ月ぶりに全業界で<claim claim_id=\'claim-2-1\'>8割</claim>超
def AExceededXPercentInBInYMonths(sentence, sentenceBefore):
    clRE = r'.*?『(.+?)』は[0-9]+?カ月ぶりに(.*?)で<claim .*?>([0-9]+?)割</claim>超.*'
    matchResults = re.match(clRE, sentence)
    if matchResults:
        threshold = float(matchResults[3])*10.0
        flag = bool(True)
        A = matchResults[1]
        B = matchResults[2]
        if df2ColName in str(B) and str(B)[0] == '全':
            col = str(A)
            if col in col22:
                for row in index22:
                    val = float(df22.at[index22.index(row),col])
                    if val < threshold:
                        flag = bool(False)
                        break
        if flag:
            print("Validated.")

# 2.『マイナスの影響』は5カ月ぶりに全業界で<claim claim_id=\'claim-2-1\'>8割</claim>超、『プラスの影響』は「小売」が<claim claim_id=\'claim-2-2\'>トップ</claim>
def AIsTheHighestInB(sentence, sentenceBefore):
    clRE = r'「(.+?)」が<claim .*?>トップ</claim>.*'
    # matchResults = re.match(clRE, sentence)
    matchResults = re.search(clRE, sentence)
    if matchResults:
        kakkoItem = matchResults.group(1)
        leftKakkoIndex = matchResults.start()
        nearbyKakkoItemR = ExtractNearestKakkoItemReversely(sentence,leftKakkoIndex)
        print(nearbyKakkoItemR+" "+kakkoItem)
        print(col2)
        print(index2)

        col = nearbyKakkoItemR
        row = kakkoItem

        if col in col2:
            if row in index2:
                highestVal = float(df2.at[index2.index(row),col])
                print(str(row)+" "+str(col)+str(highestVal))
                flag = bool(True)
                for r in index2:
                    val = float(df2.at[index2.index(r),col])
                    if val > highestVal:
                        flag = bool(False)
                        break
                if flag:
                    print("Validated.")

def ExtractNearestKakkoItemReversely(str,index):
    i = str.rfind(r"』", 0, index)
    item = ''
    i-=1
    while i>0 and str[i]!='「' and str[i]!='『':
        item = str[i]+item
        i-=1
    return item

def GetRelatedRowForDf(itemX, itemY):
    return ''

def GetRelatedColForDf(itemX, itemY):
    return ''


clRegExs = [
            # ...10月より<claim claim_id=\'claim-1-1\'>2.5ポイント</claim>増加<br>
            # 10月より0.5ポイント増加し、...
            # ...10月より2.5ポイント増加しており、...
            # '.*?[0-9]+月より[0-9]+(\.[0-9]+)?ポイント増加.*', # cal 1
            r'(.*?)([0-9]+月)より<claim .*?>(([0-9]+)((\.[0-9]+)*))(.*?)</claim>増加.*',
            # ...『マイナスの影響がある』(「既にマイナスの影響がある」と「今後マイナスの影響がある」の合計)と見込む企業は83.7%となった。
            # ...『プラスの影響がある』(「既にプラスの影響がある」と「今後プラスの影響がある」の合計)と見込む企業は4.6%となり、...。
            r'(.*?)『(.+?)』（「(.+?)」と「(.+?)」の合計）(.*?)[がは]([0-9]+)((\.[0-9]+)*)(%*).*',
            # ...3カ月ぶりに増加に転じた。
            r'(.*?)([0-9]+?)カ月ぶりに増加.*',
            # ...2月以降微増傾向を示している。
            r'(.*?)([0-9]+?)月以降微増傾向.*',

            # 2.『マイナスの影響』は5カ月ぶりに全業界で8割超
            r'(.*?)『(.+?)』は([0-9]+?)カ月ぶりに(.*?)で([0-9]+?)割超.*',
            # ...『プラスの影響』は「小売」がトップ<br>
            r'(.*?)『(.+?)』は「(.+?)」がトップ.*',
            # ...9業界中6業界（運輸・倉庫、金融、製造、不動産、小売、サービス）で10月を下回った。
            # ...9業界中6業界(小売、金融、製造、サービス、不動産、運輸・倉庫)では10月を上回り
            '(.*?)([0-9]+?)(.+?)中([0-9]+?)(.+?)（.+?）で(は*)([0-9]+?)月を[(下回)(上回)].*',
            # ...『製造』『サービス』では3カ月連続で減少しており
            '(.*?)((『(.+?)』)+?)では([0-9]+?)カ月連続で減少.*',
            # ...6月以降5カ月ぶりに全業界で8割を超えるなど...
            '(.*?)([0-9]+?)月以降([0-9]+?)カ月ぶりに(.*?)で([0-9]+?)割を超.*',
            # ...『小売』が10.3%で最も高かった。
            '(.*?)『(.+?)』が([0-9]+?)((\.[0-9]+?)*)(%*)で最も高.*',
            # 次いで、『金融』(9.1%)、『製造』(5.8%)が続く。
            '(.*?)次いで、(『(.+?)』\(([0-9]+?)((\.[0-9]+?)*)(%*)\))(、*)((『(.+?)』\(([0-9]+?)((\.[0-9]+?)*)(%*)\))*)が続く.*',
            # ...『卸売』『建設』のように10月を下回る業界...
            '(.*?)(『(.+?)』)+?のように([0-9]+?)月を[(下回)(上回)].*',
            # ...依然として大半の企業がマイナスの影響を認識しており...
            # ...依然として大半の企業が業績にマイナスの影響を受けている。
            '(.*?)大半の(.+?)が.*'
            ]
def CheckClaim(sentence):
    # 「column」が rowより val 増加
    # 计算方法 计算结果 ← 必要
    # 参考excel的计算来 function
    flag = FALSE
    for clRE in clRegExs:
        # print(clRE)
        matchResults = re.match(clRE, sentence)
        if matchResults:
            # print(matchResults.groups())
            flag = TRUE
    if flag==FALSE:
        Warning()

#

# 假定的ref_id和claim_id的编码逻辑: section x 的 第 y 个 ref/cl : ref-x-y | claim-x-y
# 但其实这里应该需要和其他components的编码耦合
section1 = '1.「今後マイナスの影響がある」が<ref ref_id=\'ref-1-1\'>11.1%</ref>、10月より<claim claim_id=\'claim-1-1\'>2.5ポイント</claim>増加<br>'
section1+= '新型コロナウイルス感染症により自社の業績にどのような影響があるか尋ねたところ、『マイナスの影響がある』（「既にマイナスの影響がある」と「今後マイナスの影響がある」の合計）と見込む企業は<claim claim_id=\'claim-1-2\'>83.7%</claim>となった。'
section1+= '10月より<claim claim_id=\'claim-1-3\'>0.5ポイント</claim>増加し、<claim claim_id=\'claim-1-4\'>3カ月ぶりに増加</claim>に転じた。'
section1+= '特に「今後マイナスの影響がある」は、10月より<claim claim_id=\'claim-1-5\'>2.5ポイント</claim>増加しており、感染拡大の第3波の影響により、先行きを懸念する企業が増えたとみられる。<br>'
section1+= '他方、『プラスの影響がある』（「既にプラスの影響がある」と「今後プラスの影響がある」の合計）と見込む企業は<claim claim_id=\'claim-1-6\'>4.6%</claim>となり、<claim claim_id=\'claim-1-7\'>2月以降微増傾向</claim>を示している。'
sentencesSec1 = re.split('。|<br>',section1)    
# for i in range(len(sentencesSec1)):
#     sentenceSec1 = sentencesSec1[i]
#     if sentenceSec1 == None or sentenceSec1 == '':
#         continue
#     if i>0:
#         sentenceBefore = sentencesSec1[i-1]
#     else:
#         sentenceBefore = ''
#     print(sentenceSec1)
#     # CheckRef(sentenceSec1)
#     # CheckClaim(sentenceSec1)
#     # AIncreasedXComparedWithB(sentenceSec1,sentenceBefore)
#     APlusBEqualToX(sentenceSec1)
#     # TurnedToIncreaseInXMonths(sentenceSec1,sentenceBefore)
#     SlightlyIncreasingSinceX(sentenceSec1,sentenceBefore)


section2 = '2.『マイナスの影響』は5カ月ぶりに全業界で<claim claim_id=\'claim-2-1\'>8割</claim>超、『プラスの影響』は「小売」が<claim claim_id=\'claim-2-2\'>トップ</claim><br>' # 被错误标记为ref
section2+= '『マイナスの影響がある』割合を業界別にみると、9業界中6業界（運輸・倉庫、金融、製造、不動産、小売、サービス）で10月を<claim claim_id=\'claim-2-3\'>下回</claim>った。'
section2+= '特に、『製造』『サービス』では3カ月連続で<claim claim_id=\'claim-2-4\'>減少</claim>しており、マイナスの影響は僅かながらも緩和している。' # 被错误标记为ref
section2+= 'しかし、6月以降5カ月ぶりに全業界で<claim claim_id=\'claim-2-5\'>8割</claim>を超えるなど、依然として<claim claim_id=\'claim-2-6\'>大半</claim>の企業がマイナスの影響を認識しており、不透明な状況は続いている。'
section2+= '他方、『プラスの影響がある』では、『小売』が<ref ref_id=\'ref-2-1\'>10.3%</ref>で<claim claim_id=\'claim-2-7\'>最も高</claim>かった。'
section2+= '<claim claim_id=\'claim-2-8\'>次いで</claim>、『金融』(<ref ref_id=\'ref-2-2\'>9.1%</ref>)、『製造』(<ref ref_id=\'ref-2-3\'>5.8%</ref>)が続く。'
section2+= '9業界中6業界(小売、金融、製造、サービス、不動産、運輸・倉庫)では10月を<claim claim_id=\'claim-2-9\'>上回</claim>り、飲食料品を取り扱う業種が上位に並んだ。'
section2+= 'しかし、『卸売』『建設』のように10月を<claim claim_id=\'claim-2-10\'>下回</claim>る業界もあるなど、プラスの影響は一部の企業にとどまり、依然として<claim claim_id=\'claim-2-11\'>大半</claim>の企業が業績にマイナスの影響を受けている。'
sentencesSec2 = re.split('。|<br>',section2)
for i in range(len(sentencesSec2)):
    sentenceSec2 = sentencesSec2[i]
    if sentenceSec2 == None or sentenceSec2 == '':
        continue
    if i>0:
        sentenceBefore = sentencesSec2[i-1]
    else:
        sentenceBefore = ''
    print(sentenceSec2)
    # CheckRef2(sentenceSec2)
    # CheckClaim(sentenceSec2)
    AExceededXPercentInBInYMonths(sentenceSec2,sentenceBefore)
    AIsTheHighestInB(sentenceSec2,sentenceBefore)

section3 = '3.「新しい生活様式」がすでに定着している企業は<ref ref_id=\'ref-3-1\'>10.0%</ref><br>'
section3+= '「新しい生活様式」に対応した企業活動が社会全体として定着するのはいつ頃と考えているかを尋ねたところ、'
section3+= '『2021年中の定着を見込む』企業は、<claim claim_id=\'claim-3-1\'>36.2%</claim>となり、<claim claim_id=\'claim-3-2\'>3社に1社</claim>が2021年中に「新しい生活様式」に対応した企業活動が定着すると見込んでいた。'
section3+= '他方、『2020年中の定着を見込む』企業は、<claim claim_id=\'claim-3-3\'>17.5%</claim>となった。'
section3+= 'そのうち、<ref ref_id=\'ref-3-2\'>10.0%</ref>の企業が「すでに定着している」と考えていた。'
section3+= 'とりわけ「電気通信」や「娯楽サービス」では、<claim claim_id=\'claim-3-4\'>3割</claim>超の企業で既に定着しているとしており、サービス業を中心にその割合が高い。'
section3+= '他方、「新しい生活様式に対応した企業活動は定着しない」とみている企業は<ref ref_id=\'ref-3-3\'>11.9%</ref>となった。'
sentencesSec3 = re.split('。|<br>',section3)
for sentenceSec3 in sentencesSec3:
    if sentenceSec3 == None or sentenceSec3 == '':
        continue
    print(sentenceSec3)
    # CheckRef3(sentenceSec3)
    # CheckClaim(sentenceSec2)

specifications = pd.read_json(r'specifications.json')
for i in specifications.index.values.tolist():
    for j in specifications.columns.values.tolist():
        sp = specifications.at[i,j]
        if sp!=None and sp['cellType']=='text-cell':
            md = specifications.at[i,j]['cellData']
            sentences = md.split("。")
            # for sentence in sentences:
            #     if '<ref>' in sentence:
            #         # do something
            #         matchRef = CheckRef(sentence)
            #         if matchRef:
            #             continue
            #         else:
            #             Warning()
            #     if '<claim>' in sentence:
            #         # do something
            #         matchCl = CheckClaim(sentence)
            #         if matchCl:
            #             continue
            #         else:
            #             Warning()   
            
specifications = specifications.to_json(orient='records',force_ascii=False)
@app.route('/specifications-json', methods=['GET']) # Test for Json loading
def specifications_json():
    return jsonify(specifications);
	
if __name__ == '__main__':
    app.run()



class Cell:
    pos = "A1"
    val = 0

    def __init__(self) -> None:
        pass

    def __init__(self, p, v):
        self.p = p
        self.val = v

    def SetCellVal(self, v):
        self.val = v
    
    def GetCellVal(self):
        return self.val
    
    def GetCellPos(self):
        return self.pos

class CellBlock:
    range=""

    def __init__(self) -> None:
        pass

class CellCollection:
    cellBlocks = NULL
    def __init__(self) -> None:
        pass

class Row:
    pos = "1"
    
    def __init__(self) -> None:
        pass

class RowBlock:
    def __init__(self) -> None:
        pass

class RowCollection:
    def __init__(self) -> None:
        pass

class Column:
    pos = "A"
    
    def __init__(self) -> None:
        pass

class ColumnBlock:
    def __init__(self) -> None:
        pass

class ColumnCollection:
    def __init__(self) -> None:
        pass

class RowHeader:
    def __init__(self) -> None:
        pass
        
        
class ColumnHeader:
    def __init__(self) -> None:
        pass

    

# 想定的计算：发生在以上的类之间
# 例如： 输入一个什么公式->得到计算结果 (解析公式)