#!　/usr/bin/env python
from ast import Return
import speech_recognition as sr
import MeCab
import glob

breakLaw = [
    [['助動詞', '基本形'], ["名詞-一般", ""]],
    [['助動詞', '基本形'], ["名詞-代名詞-一般", ""]],
    [['助動詞', '基本形'], ["名詞-非自立-副詞可能", ""]],
    [['助動詞', '基本形'], ["名詞-副詞可能", ""]],
    [['助動詞', '基本形'], ["名詞-形容動詞語幹", ""]],
    [['助動詞', '基本形'], ["名詞-固有名詞-人名-名", ""]],
    [['助動詞', '基本形'], ["名詞-固有名詞-地域-一般", ""]],
    [['助動詞', '基本形'], ["形容詞-自立", "基本形"]],
    [['助動詞', '基本形'], ["連体詞", ""]] ,
    [['助動詞', '基本形'], ["副詞-一般", ""]] ,
    [['助動詞', '基本形'], ["接続詞", ""]] ,
    [['動詞-自立', '基本形'], ["連体詞", ""]],
    [['動詞-非自立', '基本形'], ["名詞", ""]],
    [['形容詞-自立', '基本形'], ["接続詞", ""]],
    [['形容詞-自立', '基本形'], ["名詞-固有名詞-一般", ""]] 
]

def main():
    audioFile = GetInputFileName() 
    
    r = sr.Recognizer()
    with sr.AudioFile(audioFile) as source:
        audio = r.record(source)
    
    v = r.recognize_google(audio, language='ja')
    neo_wakati = MeCab.Tagger('-Ochasen -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd') #追加辞書を適用
    
    neo_wakati = neo_wakati.parse(v).strip()
    #print(neo_wakati)
    
    word = neo_wakati.split('\n')
    line =[]
    index = 0
    prevWordContents =''
    
    for item in word:
        wordContents= item.split('\t')
        if 3 < len(wordContents):
            if index == 0 and line == []:
                    line.append(wordContents[0])
            else:
                if IsSentenceBreak(prevWordContents,wordContents) == True:
                    line[index]+="。"
                    index+=1
                    line.append(wordContents[0])
                else:
                    line[index]+=wordContents[0]
        prevWordContents = wordContents
    line[index]+="。"
    
    writeFile =audioFile[0:len(audioFile)-4]+'.txt'
    f = open(writeFile, 'w')
    for item in line:
        f.write(item+'\n')
    print(writeFile+' に出力しました')


def GetInputFileName():
    try:
        #ディレクトリ内ファイル列挙
        files = glob.glob('./*')
        j = 1
        wavFileList = []
        for file in files :
            if file.endswith('.wav') :
                print(j,':',file[2:]) 
                j+=1
                wavFileList.append(file[2:])
        if len(wavFileList) == 0 :
            print('wavファイルが同ディレクトリに存在しません')
            return '', 
        #入力受け取り
        print('入力するwavファイルに対応する数字を入力してください:',end='')
        i = input()
        num = int(i)
        return wavFileList[num-1]
    except Exception as e:
        print(e)
        exit(1)

def IsSentenceBreak(prevWordContents,wordContents):
    isBreak =False
    for law in breakLaw :
        if prevWordContents[3] != law[0][0]:
            continue
        if prevWordContents[5] != law[0][1]:
            continue
        if law[1][0] =='':
            if wordContents[3] != law[1][0]:
                continue
        else:
            if wordContents[3] != law[1][0]:
                continue
            if wordContents[5] != law[1][1]:
                continue
        isBreak =True
        break
    return isBreak

if __name__ == "__main__":
    main()