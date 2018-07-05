class hashtable():
	def __init__(self):
		self.size = 6
		self.map = [None] * self.size
	
	def hash(self, key):
		keyhash = 0 
		for char in str(key):
			keyhash += ord(char)
		return keyhash % self.size

	def add(self, key, value):
		index = self.hash(key)
		key_value = [key, value]
		if self.map[index] is None:
			self.map[index] = list([key_value])
			return True
		else:
			for i in self.map[index]:
				if i[0] == key:
					i[1] = value
					return True
			self.map[index].append(key_value)
			return True
	
	def get(self, key):
		index = self.hash(key)
		if self.map[index] is None:
			return False
		for i in self.map[index]:
			if i[0] == key:
				return i[1]


	def delete(self, key):
		index = self.hash(key)
		if self.map[index] is None:
			return False
		print("l = ",len(self.map[index]))
		for i in range(len(self.map[index])):
			print(i)
			print("index", index)
			if self.map[index][i][0] == key:
				self.map[index].pop(i)
				return True 

	def print(self):
		print("---Phonebook---")
		for i in self.map:
			if i is not None:
				print(str(i))

h = hashtable()
h.add("bob", "567-8888")
h.add("ming", "293-6753")
h.add("ming", "333-8233")
h.add("ankit", "293-8625")
h.add("aditya", "852-6551")
h.add("alicia", "331-4424")
h.add("mike", "567-2188")
h.add("aditya", "777-8888")
print(h.map[1][2][0])
h.print()
h.delete("bob")
h.print()
print("ming:", h.get("ming"))