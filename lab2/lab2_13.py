x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
a = 33
b = 200

if b > a:
  pass #do nothing
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")