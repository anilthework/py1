#####19

print(len("anil"))

print("hello")

#ilk karakteri bas
print("hello" [0])
print("12345" [0])

#yazılanları basar
print("hello" + " " + "world")

#sayıları toplar
print(2 + 2)

#string
print("hello" [0])
#integer
print(2+2)
#floating point number: 3.14
#boolean: True/False

#####20

x = 123
print(type(x))

k = "anil"
print(type(k))

y = str(456)
print(type(y))

#####21
two_digit_number = input("type a two digit number: ")
print(type(two_digit_number))
first_digit_number = two_digit_number[0]
second_digit_number = two_digit_number[1]
result = int(first_digit_number) + int(second_digit_number)
print(result)


anil = input("bana bi sayı ver hacı ")
ilk = anil[0]
iki = anil[1]
topla = int(ilk) + int(iki)
print("toplamı hacı bunun nereden baksan " + str(topla) + " olur, o da sana")


#####22

#çarpma bölme işlemi sonucu float'tır
print(type(6/3))

#toplama çıkarma işlem sonucu int
print(type(2+1))


# power, ** sonuç int
print(type(2**3))


print(str(10) + str(30))

print(float(10) + float(30))

print(float(10) + 30)

#bölme işlemi sonucu float olur
print(6/2)

print(type(2**2))

#pemdas öncelikli işler yapılır (parantez,exponents,multiplication,division,addition,substraction)
#parantez,üstel,çarpma,bölme,toplama,çıkarma


#####23
##vücut kitle endeksi uygulaması

height = input("enter height m: ")
weight = input("enter weight kg: ")

bmi = int(weight) / float(height) ** 2
print(int(bmi))


#####24

print(8/3)
print(round(8/3, 2))
print(round(2.44444, 2))
#int sonuc verir, 8/3=2
# // integer division
print(8//3)

result = 4/2
result /= 2
print(result)

score = 0
score += 1
print(score)

a = 1
b = 1.8
isWin = True
#f-string
print(f"your score is {a}, your b is {b} , you are winnig {isWin}")

#####25
#life in weeks

age = input("whats your current age: ")
age_as_int = int(age)
years_remaining = 90 - age_as_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12
message = f"you have {days_remaining} days, {weeks_remaining} weeks, {months_remaining} months"
print(message)

#####26
#tip calculator
print("welcome to tip calculator")
bill = float(input("what was the total bill? $"))
tip = int(input("tip persentage? "))
people = int(input("how many people to split the bill? "))
total_bill = round((bill + tip * bill / 100) / people, 2)
print(f"each people should pay: ${total_bill}")



def is_p(s):
    print(f"{s} == {s[::-1]}")
    return s == s[::-1]

a = "OTO"
b = "YATAK"

print(f"isPalindrome({a}) = {is_p(a)}")
print(f"isPalindrome({b}) = {is_p(b)}")