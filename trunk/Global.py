import os, sys, cPickle

for fname in os.listdir("."): #first, create the binaries/verify presence
        if fname[-4:]==".dat":
            if not os.path.exists(fname[:-3]+"bin"):
                source=open(fname)
                dest=open(fname[:-3]+"bin","wb")
                ls = [line.strip() for line in source]
                cPickle.dump(ls,dest,protocol=2)
                print "Wrote %s"%(fname[:-3]+"bin",)
                source.close()
                dest.close()
tmp=open("noun.bin","rb")  #now load the binaries
nouns=cPickle.load(tmp)
tmp=open("adjective.bin","rb")
adjs=cPickle.load(tmp)
tmp=open("verb.bin","rb")
verbs=cPickle.load(tmp)
tmp=open("adverb.bin","rb")
advs=cPickle.load(tmp)

class POS:
	noun, verb, adj, adv, null = range(5)
	def getPOSFromFiles(word):#shouldn't be needed outside of this code
		ret = set()
		if word in nouns:
			ret.add(POS.noun)
		if word in verbs:
			ret.add(POS.verb)
		if word in adjs:
			ret.add(POS.adj)
		if word in advs:
			ret.add(POS.adv)
		if len(ret) == 0:
			ret.add(POS.null)
		return ret

###########build our map of words -> set of POS
if not os.path.exists("posmap.bin"):
	POSMap = {}
	for word in nouns:
		POSMap[word] =  POS.getPOSFromFiles(word)
	for word in adjs:
		POSMap[word] = POS.getPOSFromFiles(word)
	for word in verbs:
		POSMap[word] = getPOSFromFiles(word)
	for word in advs:
		POSMap[word] = getPOSFromFiles(word)
	dest=open("posmap.bin","wb")
	cPickle.dump(POSMap,dest,protocol=2)
	dest.close()
else:
	source=open("posmap.bin","rw")
	POSMap=cPickle.load(source)
	source.close()
#####dict is built
def getPOS(word):
    try:
        return POSMap[word]
    except KeyError:
        pass
    if word[-1]=="s":
        try:
            return POSMap[word[:-1]]
        except KeyError:
            pass
    return set([POS.null])
