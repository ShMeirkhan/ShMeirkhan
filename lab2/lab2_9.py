fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
# Output: ['apple', 'banana', 'mango']
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
# Output: ['banana', 'kiwi', 'mango', 'orange', 'pineapple']
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)
# Output: [100, 82, 65, 50, 23]
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:] # : is used to copy the list
print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
# Output: ['apple', 'banana', 'cherry']s