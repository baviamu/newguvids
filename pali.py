class Stack:
def __init__(self):
self.deva = []
def is_empty(self):
return self.deva == []
def push(self, data):
self.deva.append(data)
def pop(self):
return self.deva.pop()
subi= Stack()
barathi = input(&#39; &#39;)
for char in barathi:
subi.push(char)
rev_text = &#39;&#39;
while not subi.is_empty():
rev_text = rev_text + subi.pop()
if barathi== rev_text:
print(&#39;YES&#39;)
else:
print(&#39;NO&#39;)
