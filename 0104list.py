item1 = "bread"
item2 = "pasta"
item3 = "fruits"
# print(item1, item2, item3)
# but list does better
items = ["bread", "pasta", "fruits", "veggies"]
# print(items)
# print(items[0])
for i in items:
    print(i)
# similar to strings
items[0] = "chips"
print(items)
print(items[-1])
items.append("banana")
print(items)
items.insert(1, "onion")
print(items)

l1 = ["grumpy", "rude"]
l2 = l1+items
print(l2)
# items = items+"you"
# print(items)
print(len(items))
if "banana" in items:
    print("banana")
print("veggies" in items)
# items = []
# prices = []
# name = input("Enter the name: ")
# while True:

#     if name == "q":
#         break
#     else:
#         price = int(input("Enter the price: "))
#         items.append(name)
#         prices.append(price)
# total = sum(prices)
# print(total)
