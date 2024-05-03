#####42
import random
sayi = random.randint(1, 10)
print(sayi)

#0.000 - 0.9999
random_float = random.random()
print(random_float)

#0.0 - 4.999
random5 = random_float * 5
print(random5)
print(type(random5))

x = str(random5)
t = x.count("0")
print(t)

love_score = random.randint(1, 100)
print(f"your love score is {love_score} ")