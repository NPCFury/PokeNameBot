# Where we actually generate the Pokemon name

import string


fileNames = []
fileNames.append("colors.txt")
fileNames.append("japaneseOnomatopoeias.txt")

NUM_OF_WORDLISTS = len(fileNames)


def GetSyllableCount():
        return numSyllables


#for when you have over 2 syllables
def ShortenWord( word ):
        if( GetSyllableCount(word) <= 2 )
        return word
        else SHAVE OFF SOME SYLLABLES hahaha
                return word


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
        firstWord = wordList1[randrange( 0, (len( wordList1 ) - 1) )]
        secondWord = wordList2[randrange( 0, (len( wordList2 ) - 1) )]

        ShortenWord( firstWord )
        ShortenWord( secondWord )

        while( !CheckSpliceCompatibility( firstWord, secondWord ) )
                secondWord = wordList2[randrange( 0, (len( wordList2 ) - 1) )]
                ShortenWord( secondWord )

        SpliceWords( firstWord, secondWord )
        return text

def GetName():

        # change this logic later to use a better read in file method haha
        # for now this makes 2 big string arrays of the 2 random lists
        firstListNum = randrange(1, NUM_OF_WORDLISTS)
        f = open( fileNames[firstListNum - 1], 'r' )
        wordList1 = f.readlines()

        secondListNum = randrange( 1, NUM_OF_WORDLISTS )
        while( secondListNum == firstListNum):
                secondListNum = randrange( 1, NUM_OF_WORDLISTS )

        f = open( fileNames[secondListNum - 1], 'r' )
        wordList2 = f.readlines()


        # now that we have the lists we'll be using
        text = MakeName( wordList1, wordList2 )
        string.title(text) # this should capitalize the word??? python????
        return text