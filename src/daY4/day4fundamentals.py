"""
a={"b":10}
print(a)
"""
"""
student={"name":"Preksha","age":22,"course":"MCA"}


print(student["name"])
student["age"]=22
student["city"]="managlore"
print(student)

"""
"""
marks={"maths":90,"science":85,"english":88}
print(marks.get("maths"))
print(marks.get("history",0))
for subject,score in marks.items():
    print(subject,score)
    marks.update({"Social":93})
    print(marks)



    """
"""

purchase={
    "A":200,
    "B":300,
    "C":400
}

for name, amount in purchase.items():
    print(f"{name} spent ₹{amount}")
    print("total customers:",len(purchase))
    print("total customers:",purchase.keys())
    print("total amount:",purchase.values())


n=int(input("enter the number of customers:"))
user_purchase={}

for i in range(n):
    name=input("enter customer name:")
    amount=float(input("enter purchase amount"))
    user_purchase[name]=amount

print("customer data:",user_purchase)


top_spender=max(purchase,key=purchase.get)
print("top spender:",top_spender)
min_spender=min(purchase,key=purchase.get)

print("min spender:",min_spender)
"""

"""
numbers={1,2,3,3,4,5}
print(numbers)
numbers.add(6)
print(numbers)
"""

a={1,2,3}
b={3,4,5}
print(a|b)
print(a&b)
print(3 in a)