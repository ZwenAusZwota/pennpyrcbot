#!/usr/bin/python

import re, categorizer, random, epi, sys, Global
from semantics import *

def main(sentence):
    alt = getAlt(sentence.predicate.core.val)
#    print getResponse(sentence,alt)
    return getResponse(sentence,alt)
    

#creates a response for the input sentence
def getResponse(sentence,alt):
    p = getProb(sentence.type)
    if p <= 30:
        return getComment(sentence,alt)
    elif p <= 60:
        #this one asks questions
        return getSuggestion(sentence)
    elif p <= 90:
        return getQuestion(sentence,alt)
    else: 
        return getLost(sentence,alt)

#returns a list of common other things to talk about
#[action, agent, descriptor]
def getAlt(core):
    catFile = open("cat.dat", "r")
    ret = ["@action", "@agent", "@des"]
    
    word = Global.lookup(core)

    for line in catFile:
        lineList = line.split(" ")
        if word.cat == lineList[0]:
            acList = lineList[2].split(":")
            ret[0] = acList[random.randint(1,len(acList)-1)]
            agList = lineList[3].split(":")
            ret[1] = agList[random.randint(1,len(agList)-1)]
            deList = lineList[4].split(":")
            ret[2] = deList[random.randint(1,len(deList)-1)]
            return ret
    return None

def getProb(type):
    if type == "statement":
        return random.randint(0,91)
    elif type == "question":
        return random.randint(0,60)

def getQuestion(sentence,alt):
    i = random.randint(0,12)

    if i == 0: 
        return "I know you like " + sentence.predicate.core.val + ", but what else can you " + sentence.action.core.val + "?"
    elif i == 1:
        return "Can't you say something else about the " + sentence.predicate.core.val + "?"
    elif i == 2:
        return "What type of " + sentence.predicate.core.val + " do you like?"
    elif i == 3:
        return "What else is related to the " + sentence.predicate.core.val + "?"
    elif i == 4:
        return "Where is this conversation going if we keep talking about " + sentence.predicate.core.val + "?"
    elif i == 5:
        return "How is the " + sentence.predicate.core.val + " relevant at all?"
    elif i == 6:
        return "Can't it " + sentence.action.core.val + " something else?"
    elif i == 7:
        return "Oh Wow, how do you " + sentence.action.core.val + " " + sentence.predicate.core.val + "?"
    elif i == 8:
        return "Have you ever tried to " + alt[0] + " " + alt[1] + "? You might like that better."
    elif i == 9:
        return "I knew that already, how do you like to " + sentence.action.core.val + " your " + sentence.predicate.core.val + "?"
    elif i == 10:
        return "Is the " + sentence.predicate.core.val + " also " + alt[2] + "?"
    elif i == 11:
        return "That's too specific. What else do you like to " + sentence.action.core.val + "?"
    elif i == 12:
        return "I never knew that. Really?"

def getComment(sentence,alt):
    i = random.randint(0,5)

    if i == 0:
        return "I really don't understand why you like to " + sentence.action.core.val + " " + sentence.predicate.core.val + " so much."
    elif i == 1:
        return "I really don't know what to say about that."
    elif i == 2:
        return "I don't " + sentence.action.core.val + " " + sentence.predicate.core.val + " very often."
    elif i == 3:
        return "I prefer to " + alt[0] + " " + alt[1] + "."
    elif i == 4:
        return "Tell me more."
    elif i == 5:
        return "You're losing my attention. We've been through who " + sentence.action.core.val + "s " + sentence.predicate.core.val + "."
    elif i == 6:
        pass


def getSuggestion(sentence):
    i = random.randint(0,3)

    if i == 0:
        return "oh, I found a cool recipe for " + sentence.predicate.core.val + ". Look at this! " + epi.getFoodLink(sentence.predicate.core.val)
    elif i == 1:
        return "Check out this dish I made with " + sentence.predicate.core.val + " the other day. " + epi.getFoodLink(sentence.predicate.core.val)
    elif i == 2:
        return "I usually use this recipe with my " + sentence.predicate.core.val + ". " + epi.getFoodLink(sentence.predicate.core.val) + ". You should try it some time."
    elif i == 3:
        return "I like " + sentence.predicate.core.val + " too. This is my favorite recipe to go with it! " + epi.getFoodLink(sentence.predicate.core.val)

def getLost(sentence,alt):
    return "Anyway, I gotta go, cya."


if __name__ == "__main__":
    exit(main())