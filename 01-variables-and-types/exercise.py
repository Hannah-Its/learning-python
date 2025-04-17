name = input("What's your name? ")
age = input("How old are you? ")
fav_number = input("What's your favorite number? ")

print(f"Hi {name}! You're {age} years old and your favorite number is {fav_number}.")

fav_number_float = float(fav_number)
print(f"The float version of your favorite number is: {fav_number_float}")
print(f"The type is: {type(fav_number_float)}")
