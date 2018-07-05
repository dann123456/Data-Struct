class node():
	def __init__(self, d, n=None):
		self.data = d
		self.next = n
	def getnext(self):
		return self.next
	def setnext(self, n):
		self.next = n
	def getdata(self):
		return self.data
	def setdata(self, d):
		self.data = d

class linked():
	def __init__(self, r=None):
		self.root = r
		self.size = 0
	def getsize(self):
		return self.size
	def add(self, d):
		self.root = node(d, self.root)
		self.size += 1
	def remove(self, d):
		this = self.root
		behind = None
		while this is not None:
			if this.getdata() == d :
				if behind is not None:
					behind.setnext(this.getnext())
				else: 
					self.root = this.getnext()
				self.size -=1
				return True
			behind = this
			this = this.getnext()
		return False
	def find(self, d):
		this = self.root
		while this is not None:
			if this.getdata() == d:
				return d
			elif this.getnext() is None:
				return False
			this = this.getnext()

def main():
	m = linked()
	m.add(5)
	m.add(9)
	m.add(3)
	m.add(8)
	m.add(9)
	print("size=", str(m.getsize()))
	m.remove(8)
	print("size=", str(m.getsize()))
	print("remove 15", m.remove(15))
	print("size=", str(m.getsize()))
	print("find 25", m.find(25))

main()