# Where we actually generate the Pokemon name

import string
import time
import random
import unirest
import requests
import json
#import requests.packages.urllib3
#requests.packages.urllib3.disable_warnings()
from secrets import *

fileNames = []
fileNames.append("./wordLists/japaneseOnomatopoeias.txt")
fileNames.append("./wordLists/englishOnomatopoeias.txt")
fileNames.append("./wordLists/colors.txt")
fileNames.append("./wordLists/temperatureWords.txt")
fileNames.append("./wordLists/actionVerbs.txt")
fileNames.append("./wordLists/moods.txt")
fileNames.append("./wordLists/oceanAnimals.txt")
fileNames.append("./wordLists/oceanWords.txt")
fileNames.append("./wordLists/natureWords.txt")

NUM_OF_WORDLISTS = len(fileNames)

#takes a word, returns a list of its syllables; if request fails returns empty
def Syllabification( word ):
        print("About to syllabify:")
        print(word)

        url = "https://wordsapiv1.p.mashape.com/words/" + word + "/syllables"

        response = unirest.get( url,
                  headers = {"X-Mashape-Key": WORDS_KEY, "Accept": "application/json"}
                )

        requestCap = 10
        while( response.code != 200 and requestCap > 0  ):
                response = unirest.get( url,
                  headers = {"X-Mashape-Key": WORDS_KEY, "Accept": "application/json"}
                )
                print( response.code )
                requestCap -= 1


        if( response.code == 200 ):
                print(response.body)
                return response.body["syllables"]["list"]
        else:
                print("ERROR: empty list returned")
                return []


def Unsyllabification( wordArray ):
        word = ""
        for syllable in wordArray:
                word += syllable

        return word


#for when you have over 2 syllables. First is a bool
def ShortenWord( wordArray, first ):
        if( len( wordArray ) <= 2 ):
                return wordArray
        else:
                if first:
                        return ( wordArray[0] + wordArray[1] )
                else:
                        return ( wordArray[len(wordArray) - 2] + wordArray[len(wordArray) - 1] )


# HOW DO WE COMBINE THE TWO FUNCTIONS BELOW?

# This is after we have two properly shortened words
def CheckSpliceCompatibility( firstWord, secondWord ):
        # this is where we see if the last letter(s) of the first word and the first letter(s) of the last word fit together
        # letter pairs: th, qu, sh, ph, 

        # matching single letters get combined

        return bool


# Put the two already compatable parts together
def SpliceWords( firstWord, secondWord ):

        #firstWord = firstWord[:-1] # this takes a letter off the end
        secondWord = secondWord[1:] # this should take a letter off the front...?

        if( secondWord[0] == firstWord[len(firstWord) - 1] ):
                print("Matching splice letters. Merging...")
                secondWord = secondWord[1:]


        return ( firstWord + secondWord )#[1:] )



# this is the big one called by GetName. hi-level assumption is that they're from different files
# we pass the lists and not the words so that we can get a new word from the same list if one is not compatible
def MakeName( wordList1, wordList2, firstListNum, secondListNum ):
        firstWord = wordList1[random.randrange( 0, (len( wordList1 )) )]
        secondWord = wordList2[random.randrange( 0, (len( wordList2 )) )]

        if( firstListNum > 1 ):
                firstWordSyllables = Syllabification( firstWord )

                firstWordSyllablesShortened = ShortenWord( firstWordSyllables, True )


                '''for syllable in firstWordSyllables:
                        print( syllable )

                while( !CheckSpliceCompatibility( firstWord, secondWord ) )
                        secondWord = wordList2[random.randrange( 0, (len( wordList2 ) - 1) )]
                        ShortenWord( secondWord )'''

                firstWordUnsyllabified = Unsyllabification( firstWordSyllablesShortened )
        else:
                firstWordUnsyllabified = firstWord

        if( secondListNum > 1 ):
                secondWordSyllables = Syllabification( secondWord )
                secondWordSyllablesShortened = ShortenWord( secondWordSyllables, False )
                secondWordUnsyllabified = Unsyllabification( secondWordSyllablesShortened )
        else:
                secondWordUnsyllabified = secondWord

        print(firstWordUnsyllabified)
        print(secondWordUnsyllabified)

        name = SpliceWords( firstWordUnsyllabified, secondWordUnsyllabified )

        return name

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
        text = MakeName( wordList1, wordList2, firstListNum, secondListNum )
        text = text.title() # this should capitalize the word??? python????
        return text