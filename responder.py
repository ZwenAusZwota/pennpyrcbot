#!/usr/bin/python

"""
About:
This script takes apart the output of the harness program specified in a specific format as specified below. The following data structures are used:

theme(tMap): part -> word (ie. core -> radish)
agent(aMap): part -> word (ie. core -> boy)

It then takes the map and retreives common topics associated with that agent/theme.

Finally, through a probabilistic approach, it returns a response.

Input Format:
type:word theme:word@thm:word@det:word@des:word@cor agent:word@agt:word@det:word@des:word@cor
"""
import sys, re, categorizer, random

def main(args=None):
    #makes maps
    theme = {}
    agent = {}
    type = ""

    #to be adjusted to read from output of another class/script
    #sample input is currently rotten carrots
    file = open("input", 'r')
    for line in file:
        input = line

    #sectionList breakdown
    #type[]
    #theme[]
    #agent[]
        sectionList = input.split(" ")
        for group in sectionList:
            currentDict = {}
            groupList=group.split(":")
            if groupList[0] == "type":
                type = groupList[1]
            elif groupList[0] == "theme" or groupList[0] == "agent":
                for element in groupList[1:]:
                    pair = element.split("@")
                    currentDict[pair[1]] = pair[0]
            else:
                print "Input format not recognized"

            if groupList[0] == "theme":
                theme = currentDict
            elif groupList[0] == "agent":
                agent = currentDict
    #generate response
        print genResponse(type, theme, agent)

#generates response from word:POS using category
def genResponse(type, tMap, aMap):
    #type has yet to be used

    #find alternate common topic for each through rgen
    #reminder: commons is a list [action, agent, descriptor]
    commons = getCommons(tMap["thm"])

    #original eg.cut, carrot, salty
    original =  [tMap["des"],tMap["cor"], aMap["des"]]

    #choose type of sentence to construct
    choice = random.randint(20, 30)
    var = random.randint(0,4)
    if choice == 0:
        return goodbye()
    elif choice < 11:
        return generalize(commons,original,var)
    elif choice < 21:
        return comment(commons,original,var)
    elif choice < 31:
        return question(commons,original,var)
    elif choice < 41:
        return imperative(commons,original,var)
    else:
        return "\"There are 10 kinds of people in this world, those who understand binary, and those who don't\""

#returns a list of length 3 @action,@agent,@desc
def getCommons(theme):
    catFile = open("cat.dat", "r")
    ret = ["@action", "@agent", "@desc"]
    for line in catFile:
        lineList = line.split(" ")
        if theme == lineList[0]:
            acList = lineList[2].split(":")
            ret[0] = acList[random.randint(1,len(acList)-1)]
            agList = lineList[3].split(":")
            ret[1] = agList[random.randint(1,len(agList)-1)]
            deList = lineList[4].split(":")
            ret[2] = deList[random.randint(1,len(deList)-1)]
            return ret
    return None

def question(commons,original,var):
    if var == 0:
        print "Why " + original[1] + "?"
    elif var == 1:
        print "What's so good about " + original[1] + "?"
    elif var == 2:
        print "I know you like " + original[1] + ", but can you tell me more?"
    elif var == 3:
        print "Do you have something else to say about " + original[1] + "?"
    else:
        print "Ok...and?"

def comment(commons,original,var):
    
    if var == 0:
        print "I really don't understand why you like " + original[1] + "so much."
    elif var == 1:
        print "I knew that already, tell me more about " + original[1] + "."
    elif var == 2:
        print "I really don't know what to say about that."
    elif var == 3:
        print "I've never thought about that. Hmm..."
    else:
        print "I hold a very different point of view."

def imperative(commons,original,var):
    if var == 0:
        print "You should not think that way"
    elif var == 1:
        print "There is nothing worse than that"
    elif var == 2:
        print "Please don't..."
    elif var == 3:
        print "Tell me more."
    else:
        print "You're losing my attention. Be more interesting."

def generalize(commons,original,var):
    if var == 0:
        print ""
    elif var == 1:
        print "Why " + original[1] + "?"
    elif var == 2:
        pass
    elif var == 3:
        pass
    else:
        pass

def goodbye():
    print "Anyway, I gotta go, catch you later."
    #sign off here

if __name__=="__main__":
    exit(main())
