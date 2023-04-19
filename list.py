#Given the list fruits = ["apple", "banana", "cherry"] 
#How do you add mango to the list?

fruits = ["apple", "banana", "cherry"]
fruits.append("mango")
fruits.insert(1,"pineaple")
fruits.extend(["pawpaw","kiwi"])
fruits.pop()
#How do you add these two fruits at once pawpaw, kiwi?

#How do you sort the list?
fruits.sort()

#How do you remove everything from the list?
fruits.remove("banana")
#how do you reverse the list
fruits.reverse()
fruits.sort(reverse=True)
fruits.sort()
fruits.sort(reverse=True)

#remove duplicate from the folowing numbers=[1,2,3,4,1,2,4,5,7,6,6]
#from the list
numbers=[1,2,3,4,1,2,4,5,7,6,6]
x=list(set(numbers))
print(x)
#Find the index of the 1st matching element
fruit = ['pear', 'orange', 'apple', 'grapefruit', 'apple', 'pear']
y=fruit.index('apple')
print(y)

 #How to concatenate two lists

one = ['a', 'b', 'c']
two = [1, 2, 3]
concatenate=one+two

 #Filter even values out of a list with list comprehension
list=[1,2,3,4,5,6,7,8,9,10]
a=[i for i in list if i % 2 !=0]
print(a)


#Get the first element from each nested list in a list
li=[[1,2,3],[4,5,6],[7,8,9]]
b=[i[0] for i in li]
print(b)

# create a list of prime numbers
prime_numbers = [2, 3, 5, 7]

# remove the element at index 2
removed_element = prime_numbers.pop(2)

print('Removed Element:', removed_element)
print('Updated List:', prime_numbers)

