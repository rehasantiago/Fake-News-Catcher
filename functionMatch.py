import nltk
import re
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import wordnet, stopwords



class Generator:
    def __init__(self, para):
        self.para=para
           
    def keywordGenerator(self):
        words=[]
        matches=re.findall(r'[a-zA-Z0-9\']+',self.para)
        for match in matches:
            words.append(match.lower())

        sw=stopwords.words('english')
        i=0
        sw=stopwords.words('english')
        while i<len(words):
            j=0    
            while j<len(sw):
                try:
                    if words[i]==sw[j]:
                        words.pop(i)
                        i=i-1                
                except:
                    break
                j=j+1
            i=i+1    
        cleanWords=words
        return cleanWords

    def synonymGenerator(self, cleanWords):
        wordSynonyms=[]
        for matchedWords in cleanWords: 
            for syn in wordnet.synsets(matchedWords):
                for lemma in syn.lemmas():
                    wordSynonyms.append(lemma.name().lower())
        
        wordSynonyms.sort()
        wordSynonyms2=[]

        for d in wordSynonyms:
            if d not in wordSynonyms2:
                wordSynonyms2.append(d)

        return wordSynonyms2

    def matchingSimilarity(keyWords1, keyWords2, synonymWords1, synonymWords2):
        #keywords get 80% matching, synonyms get 20% matching
        kwcount1=len(keyWords1)
        kwcount2=len(keyWords2)
        syncount1=len(synonymWords1)
        syncount2=len(synonymWords2)

        kwmatchcount=0
        synmatchcount=0

        for i in range(0, kwcount1):
            for j in range(0, kwcount2):
                if(keyWords1[i]==keyWords2[j]):
                    kwmatchcount=kwmatchcount+1
        for i in range(0, syncount1):
            for j in range(0, syncount2):
                if(synonymWords1[i]==synonymWords2[j]):
                    synmatchcount=synmatchcount+1

        similaritykw=((kwmatchcount*2)/(kwcount1+kwcount2))*100/100
        similaritysyn=((synmatchcount*2)/(syncount1+syncount2))*50/100
        totalsimilarity=similaritykw+similaritysyn
        return totalsimilarity*100
        

#channel=[]
def runApp(channel,para1):
    finalresult=[]
    gen_ref=Generator(para1)
    keyWords_ref=gen_ref.keywordGenerator()    
    synonym_ref=gen_ref.synonymGenerator(keyWords_ref)

    i=0
    while i<len(channel):
        gen_1=Generator(channel[i])
        keyWords1=gen_1.keywordGenerator()    
        synonym1=gen_1.synonymGenerator(keyWords1)
        finalresult.append(Generator.matchingSimilarity(keyWords_ref, keyWords1, synonym_ref, synonym1))
        i=i+1
    return finalresult
    #print(finalresult)