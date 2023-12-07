import random

print(random.random())
print(random.uniform(10,20))
print(random.randint(10,99))
print(random.randrange(0,100,5))

number=[1,2,3,4,5,6]

print(random.choice(number))

coin=["H","T"]

print(random.choice(coin))


print(number)
random.shuffle(number)
print(number)

print(random.sample(number,3))
