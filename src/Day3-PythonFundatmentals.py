"""
numbers=[10,20,30,40]
coordinates=(5,10)
print(numbers)
print(coordinates)
"""
"""
a=[100,200,300,400,500,600,700,800,900]

print(a[-3:-1])

print(a[1:4:1])

print(a[-2:-5:-1])
"""

lst = [5, 2, 9, 1, 7]
lst.sort()
print(lst)

lst = [5, 2, 9, 1, 7]
lst.sort(reverse=True)
print(lst)

lst = [1, 2, 3]

lst.append(4)        
lst.insert(1, 10)    
lst.extend([5, 6])   
lst.pop()            

print(lst)