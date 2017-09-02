# Where we actually generate the Pokemon name

import string
import time
import random
import requests
import json
#import requests.packages.urllib3
#requests.packages.urllib3.disable_warnings()
from secrets import *

fileNames = []
fileNames.append("./wordLists/colors.txt")
fileNames.append("./wordLists/japaneseOnomatopoeias.txt")
fileNames.append("./wordLists/englishOnomatopoeias.txt")
fileNames.append("./wordLists/temperatureWords.txt")

NUM_OF_WORDLISTS = len(fileNames)

#takes a word, returns a list of its syllables
def Syllabification(word):
        print(word)
        url = "https://wordsapiv1.p.mashape.com/words/" + word + "/syllables"
        headers = {"X-Mashape-Key": WORDS_KEY, "Accept": "application/json"}
        raw_response = requests.get(url, headers)
        print(raw_response.status_code)
        if (raw_response.status_code == 200):
                parsed_response = raw_response.json()
                return parsed_response["syllables"]["list"]
                #parsed_response.json() = json.parse(raw_response)
        else:
                return []

#for when you have over 2 syllables
def ShortenWord( word ):
        '''if( GetSyllableCount(word) <= 2 ):
                return word
        else SHAVE OFF SOME SYLLABLES hahaha
                return word'''


# HOW DO WE COMBINE THE TWO FUNCTIONS BELOW?

# This is after we have two properly shortened words
def CheckSpliceCompatibility( firstWord, secondWord ):
        # this is where we see if the last letter(s) of the first word and the first letter(s) of the last word fit together
        # letter pairs: th, qu, sh, ph, 

        # matching single letters get combined


        return bool


# Put the two already compatable parts together
def SpliceWords( firstWord, secondWord ):

        firstWord = firstWord[:-1] # this takes a letter off the end
        secondWord = secondWord[-1:] # this should take a letter off the front...?


        return ( firstWord + secondWord )



# this is the big one called by GetName. hi-level assumption is that they're from different files
# we pass the lists and not the words so that we can get a new word from the same list if one is not compatible
def MakeName( wordList1, wordList2 ):
        firstWord = wordList1[random.randrange( 0, (len( wordList1 )) )]
        secondWord = wordList2[random.randrange( 0, (len( wordList2 )) )]

        firstWordSyllables = Syllabification( firstWord )

        for syllable in firstWordSyllables:
                print( syllable )

        '''ShortenWord( firstWord )
        ShortenWord( secondWord )

        while( !CheckSpliceCompatibility( firstWord, secondWord ) )
                secondWord = wordList2[random.randrange( 0, (len( wordList2 ) - 1) )]
                ShortenWord( secondWord )

        SpliceWords( firstWord, secondWord )'''

        return ( firstWord + secondWord )

def GetName():

        # change this logic later to use a better read in file method haha
        # for now this makes 2 big string arrays of the 2 random lists
        firstListNum = random.randrange( 0, NUM_OF_WORDLISTS )
        f = open( fileNames[ firstListNum ], 'r' )
        wordList1 = f.read().splitlines()
        secondListNum = random.randrange( 0, NUM_OF_WORDLISTS )
        while( secondListNum == firstListNum ):
                secondListNum = random.randrange( 0, NUM_OF_WORDLISTS )

        f = open( fileNames[secondListNum ], 'r' )
        wordList2 = f.read().splitlines()



        # now that we have the lists we'll be using
        text = MakeName( wordList1, wordList2 )
        text = text.title() # this should capitalize the word??? python????
        return text