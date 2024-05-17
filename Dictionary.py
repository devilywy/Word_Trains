import requests
from bs4 import BeautifulSoup
from random_word import RandomWords
#word=input("Please enter a word: ")
url="https://randomwordgenerator.com/json/words_ws.json" 
'''
url="https://api.dictionaryapi.dev/api/v2/entries/en/{0}".format(word)
'''
response=requests.get(url)
if(response.status_code==200):
   ''' 
   soup=BeautifulSoup(response.content,'html.parser')
   print(soup.prettify())
   print(response.content)
   '''
   dictionary=response.json()["data"]
   Listofwords=[]
   for data in dictionary:
      Listofwords.append(data["word"]["value"])

   print(Listofwords)
   randomword=response.json()["data"][100]["word"]["value"]
   print("First level question: {0} ".format(randomword))
   lastletter=randomword[-1]
   print("The last letter of {0} is {1}".format(randomword, lastletter))

   for word in Listofwords:
      if(lastletter.lower()== word[0].lower()):
         print(word)