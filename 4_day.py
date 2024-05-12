#####42
import random
sayi = random.randint(1, 10)
print(sayi)

#0.000 - 0.9999
import random
random_float = random.random()
print(random_float)

#0.0 - 4.999
import random
random_float = random.random()
random5 = random_float * 5
print(random5)
print(type(random5))

x = str(random5)
print(x)
t = x.count("0")
print(t)

love_score = random.randint(1, 100)
print(f"your love score is {love_score} ")

import random
random_side = random.randint(0,1)

#####44

#data structure: list
fruits = ["apple", "orange", "banana"]
print(fruits[0])
print(fruits[-2])
fruits[2] = "muz"
print(fruits[2])
fruits.append("anill")
print(fruits)
fruits.extend(["yes", "no"])
print(fruits)

#data structures more for list
#https://docs.python.org/3/tutorial/datastructures.html


#####46

fruits = ["apple", "orange", "banana"]
print(len(fruits))
num_of_fruits = len(fruits)
print(fruits[num_of_fruits -1 ])
vegetables = ["tomato" , "pateto"]
foods = [fruits, vegetables]
print(foods)
print(foods[1])
print(foods[1][1])

#####47