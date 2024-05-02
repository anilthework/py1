#####30

number = int(input("give a number: "))
if number % 2 == 0:
    print("this is a even number")
else:
    print("this is an odd number")

#####31

print("welcome to rollercoaster")
height = int(input("what is your height in cm? "))
if height >= 120:
    print("you can ride rc")
    age = int(input("whats your age? "))
    if age < 12:
        print("please pay $5")
    elif age <= 18:
        print("please pay $7")
    else:
        print("please pay $12")
else:
    print("sorry you can not ride rc")

#####32

# BMI

h1 = float(input("enter your height in m: "))
w1 = float(input("enter your weight in kg: "))
bmi = round(w1 / h1 ** 2)
if bmi < 18.5:
    print(f"your bmi is {bmi}, you are underweight")
elif bmi < 25:
    print(f"your bmi is {bmi}, you are normal weight")
else:
    print(f"your bmi is {bmi}, you are fat..")


#####33

#leap year

year = int(input("which year do you want to check? "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("artık yıl")
        else:
            print("artık yıl değil")
    else:
        print("artık yıl değil")
else:
    print("artık yıl değil")

#####34
#rc için foto parası ekle

print("welcome to rollercoaster")
height = int(input("what is your height in cm? "))
if height >= 120:
    print("you can ride rc")
    age = int(input("whats your age? "))
    if age < 12:
        ode = 5
        print("child tickets are $5")
    elif age <= 18:
        ode = 7
        print("youth tickets are $7")
    else:
        ode = 12
        print("adult tickets are $12")
    wants_photo = input("do you want photo? Y or N ")
    if wants_photo == "Y":
        ode += 3
    print(f"son odeme tutarı ${ode}")
else:
    print("sorry you can not ride rc")


#####35

#Pizzacı
#small pizza $15
#medium pizza $20
#large pizza $25
#pepperoni for small pizza +$2
#pepperoni for medium or large pizza +$3
#extra cheese for any pizza +$1

print("welcome to pizzacı")
size = input("what size of pizza do you want? s,m,l ")
add_pepperoni = input("do you want pepperoni? y or n ")
extra_cheese = input("do you want extra cheese? y or n ")
bill = 0
if size == "s":
    bill += 15
elif size == "m":
    bill += 20
elif size == "l":
    bill += 25

if add_pepperoni == "y":
    if size == "s":
        bill += 2
    else:
        bill += 3

if extra_cheese == "y":
    bill += 1

print(f"your final bill ${bill} ")


#####36

#rc 45-55 yaşlarına beleş olsun

print("welcome to rollercoaster")
height = int(input("what is your height in cm? "))
if height >= 120:
    print("you can ride rc")
    age = int(input("whats your age? "))
    if age < 12:
        ode = 5
        print("child tickets are $5")
    elif age <= 18:
        ode = 7
        print("youth tickets are $7")
    elif age >= 45 and age <= 55:
        ode = 0
        print("sana beleşş")
    else:
        ode = 12
        print("adult tickets are $12")
    wants_photo = input("do you want photo? Y or N ")
    if wants_photo == "Y":
        ode += 3
    print(f"son odeme tutarı ${ode} ")
else:
    print("sorry you can not ride rc ")


#####37

#love calculator

print("welcome to love calculator")
name1 = input("whats your name? \n")
name2 = input("whats your name \n")

combined_string = name1 + name2
lower_case_string = combined_string.lower()
t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

true = t + r + u + e

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

love = l + o + v + e

love_score = int(str(true) + str(love))

if (love_score < 10) or (love_score >90):
    print(f"your love score is {love_score} , you go together coke and mentos ")
elif (love_score >= 40) and (love_score <=50):
    print(f"your score is {love_score}, you are alright together")
else:
    print(f"your score is {love_score}")

#kolay örnek
anil = input("whats ur name? \n")
lowerc = anil.lower()
print(lowerc)
x = lowerc.count("x")
print(x)

#####38

#treasure island

print("welcome to treasure island")
choice1 = input("choose right or left").lower()
if choice1 == "left":
    choice2 = input("wait or swim?").lower()
    if choice2 == "wait":
        choice3 = input("red yellow blue ?").lower()
        if choice3 == "red":
            print( "3.de gameover")
        elif choice3 == "yellow":
            print("you WIN!")
        elif choice3 == "blue":
            print("bu da gameover..")
        else:
            print("yanlis bisey sectin yine game ooover")
    else:
        print("yine gameover")
else:
    print("gameover")
