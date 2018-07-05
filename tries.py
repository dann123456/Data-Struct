class node():
	def __init__(self):
		self.child = [None]*26
		self.flag = False

class trie():
	def __init__(self):
		self.root = node()
	
	def gethash(self, key):
		return ord(key)-ord("a")

	def add(self, key):
		nex = self.root
		for char in list(key):
			index = self.gethash(char)
			#if index is none, create new node inside current node
			if nex.child[index] == None:
				nex.child[index] = node()
			#if there is then a node, the focus move on to that node
			nex = nex.child[index]
		nex.flag = True

	def search(self, key):
		nex = self.root
		for char in list(key):
			index = self.gethash(char)
			#if index is none, no node found
			if nex.child[index] == None:
				return False
			#if there is then a node, the focus move on to that node
			nex = nex.child[index]
		return nex != None and nex.flag

def main():
 
    # Input keys (use only 'a' through 'z' and lower case)
    keys = ["the","a","there","anaswe","any",
            "by","their"]
    output = ["Not present in trie",
              "Present in tire"]
 
    # Trie object
    t = trie()
 
    # Construct trie
    for key in keys:
        t.add(key)
 
    # Search for different keys
    print("{} ---- {}".format("the",output[t.search("the")]))
    print("{} ---- {}".format("these",output[t.search("these")]))
    print("{} ---- {}".format("their",output[t.search("their")]))
    print("{} ---- {}".format("thaw",output[t.search("thaw")]))
 
if __name__ == '__main__':
    main()