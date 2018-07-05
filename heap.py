class maxheap():
	def __init__(self, l):
		self.heap = [0]
		for i in l:
			self.heap.append(i)
			self.floatup(len(self.heap)-1)
	
	def push(self, d):
		self.heap.append(d)
		if len(self.heap) > 2:
			self.floatup(len(self.heap)-1)
			return True
		else:
			return False
	
	def peek(self):
		if len(self.heap) >= 2:
			return self.heap[1]
		else:
			return False
	
	def pop(self):
		if len(self.heap) > 2:
			self.swap(1, len(self.heap)-1)
			max = self.heap.pop()
			self.bubbledown(1)
			return max
		if len(self.heap) == 2:
			return self.heap.pop()
		else:
			return False

	def swap(self, x, z):
		self.heap[x], self.heap[z] = self.heap[z], self.heap[x]		
	
	def floatup(self, x):
		parent = x//2
		if self.heap[x] > self.heap[parent] and parent!=0:
			self.swap(x, parent)
			return self.floatup(parent)
	
	def bubbledown(self, x):
		right = x*2+1
		left = x*2
		top = x
		if len(self.heap) > right:	
			if self.heap[top] < self.heap[right]:
				self.swap(top, right)
				return self.bubbledown(right)
			if self.heap[top] < self.heap[left]:
				self.swap(top, left)
				return self.bubbledown(left)

m = maxheap([95, 3, 21])
m.push(10)
print(str(m.heap[0:len(m.heap)]))
print(str(m.pop()))
print(str(m.heap[0:len(m.heap)]))
