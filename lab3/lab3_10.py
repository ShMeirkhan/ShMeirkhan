def unique_elements(input_list):
    unique_list = []
    for element in input_list:
        if element not in unique_list:
            unique_list.append(element)
    return unique_list
s=[]
n=int(input())
for i in range(n):
    x=int(input())
    s.append(x)
print(unique_elements(s)) 