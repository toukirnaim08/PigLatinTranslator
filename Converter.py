import re
import os 

SpecialChar1 = '"-,'  
SpecialChar2 = "'!"     
Consonant = "abcdefghijklmnopqrstuvwxzABCDEFGHIJKLMNOPQRSTUVWXZ"
Vowle = "aeiouAEIOU"
Number="1234567890"

#main logics of Pig-Latin Converter
def WordConverter(text):
    convertedWord=""
    
    if text[0] in SpecialChar1 or text[0] in SpecialChar2 and len(text)==1:
        convertedWord = text
    elif text[0] in Vowle:
        convertedWord = text + "yay"
    elif text[0] in Consonant and len(text)==1:
        convertedWord = text + "ay"
    elif text[1] in Vowle:
        convertedWord = text[1:len(text)] + text[0] + "ay"
    elif text[1] == "y":
        convertedWord = text[1:len(text)] + text[0] + "ay"
    elif text[2] == "y":
        convertedWord = text[2:len(text)] + text[0:2] + "ay"
    elif text[2] in Consonant:
        convertedWord = text[2:len(text)] + text[0:2] + "ay"
    else:
        convertedWord = text
    return convertedWord

#logic for ""
def QuotationMarkOparation(text):
    
    modifiedText=""
    tempModifiedWord = ""
    position = text.find('"')
    tempQuotationMarkConvertedWord = ""
    if '"' in text:
        modifiedText = text.replace('"', '')
        
    if "!" in modifiedText:
        tempModifiedWord = ExclamationMarkOparation(modifiedText)
    elif "," in modifiedText:
        tempModifiedWord = CommaOparation(modifiedText)
    else:
        tempModifiedWord = WordConverter(modifiedText)
    if position == 0:
        tempQuotationMarkConvertedWord = '"' + tempModifiedWord
    else:
        tempQuotationMarkConvertedWord =  tempModifiedWord + '"'
        
    return tempQuotationMarkConvertedWord

#logic for "."
def FullStopOparation(text):
    
    modifiedText=""
    tempFullStopConvertedWord = ""
    if "." in text:
        modifiedText = text.replace('.', '')
    tempFullStopConvertedWord = WordConverter(modifiedText) + "."
        
    return tempFullStopConvertedWord

#logic for "!"
def ExclamationMarkOparation(text):
    
    modifiedText=""
    tempExclamationMarConvertedWord = ""
    if "!" in text:
        modifiedText = text.replace('!', '')
    tempExclamationMarConvertedWord = WordConverter(modifiedText) + "!"
        
    return tempExclamationMarConvertedWord

#logic for ","
def CommaOparation(text):
    
    modifiedText=""
    tempCommaConvertedWord = ""
    if "," in text:
        if text[0] in Number:
            modifiedText = text
            tempCommaConvertedWord = WordConverter(modifiedText)
        else:
            modifiedText = text.replace(',', '')
            tempCommaConvertedWord = WordConverter(modifiedText) + ","
    
        
    return tempCommaConvertedWord

#logic logc "-"
def DashOparation(text):
    splitedWord = text.split("-")
    tempDashConvertedWord = ""
    DashConvertedWord = ""
    
    for i in range(len(splitedWord)):
        tempDashConvertedWord = WordConverter(splitedWord[i])
        
        if i==0:
            DashConvertedWord = tempDashConvertedWord
        else:
            DashConvertedWord = DashConvertedWord + "-" + tempDashConvertedWord   
    return DashConvertedWord

#logic for ''
def InvitedCommaOparation(text):
    
    splitedWord = text.split("'")
    
    tempCommaConvertedWord = ""
    CommaConvertedWord = ""
    
    for i in range(len(splitedWord)):
        tempCommaConvertedWord = WordConverter(splitedWord[i])
        if i==0:
            CommaConvertedWord = tempCommaConvertedWord
        else:
            CommaConvertedWord = CommaConvertedWord + "'" + tempCommaConvertedWord  
            
    return CommaConvertedWord

#split sentence based on space
#interator
#apply main logic upon words
def Spliters(Fullstring):
    if(len(Fullstring)>1):
        startingSpace = re.search('\S', Fullstring).start()
    else:
        startingSpace = 1
    splitString = Fullstring.split(" ")
    tempConvertedString = ""
    convertedString = ""
    for i in range(startingSpace,len(splitString),1):
        if len(splitString[i])==0:
            tempConvertedString = splitString[i]
        elif "-" in splitString[i] and len(splitString[i])>1:
            tempConvertedString = DashOparation(splitString[i])
        elif '"' in splitString[i] and len(splitString[i])>1:
            tempConvertedString = QuotationMarkOparation(splitString[i])
        elif "'" in splitString[i] and len(splitString[i])>1:
            tempConvertedString = InvitedCommaOparation(splitString[i])
        elif "!" in splitString[i] and len(splitString[i])>1:
            tempConvertedString = ExclamationMarkOparation(splitString[i])
        elif "," in splitString[i] and len(splitString[i])>1:
            tempConvertedString = CommaOparation(splitString[i])
        elif "." in splitString[i] and len(splitString[i])>1:
            tempConvertedString = FullStopOparation(splitString[i])
        else:
            tempConvertedString = WordConverter(splitString[i])
        if i == startingSpace:
            convertedString = tempConvertedString
        else:
            convertedString = convertedString + " " + tempConvertedString
    return convertedString

#read football txt file
workingDirectory = os.getcwd()
fielPath =  workingDirectory + "/football.txt"   
textFile = open(fielPath,'r')
fullText = textFile.readline().lower()
print("Fulltext:")
print(fullText)
print("Converting to Pig-Latin.....")

#split full text based on fullstop
#insert splited texts into list
splitedTextList = fullText.split(".")
outPutList = []
for i in range(len(splitedTextList)):
    if len(splitedTextList[i]) > 0:
        strTemp = Spliters(splitedTextList[i])
        outPutList.append(strTemp.capitalize() + ". ")
        
print("Done Converting")
print("Saving to output directory.....")

#create output directory
file = open(workingDirectory + "/football_PigLatin.txt", "w") 
piglatinWords= ""
for i in range(len(outPutList)):
    piglatinWords = piglatinWords + outPutList[i-1]

#write converted string into football_PigLatin.txt
file.write(piglatinWords[2:len(piglatinWords)]) 
file.close()
print("File saved")
