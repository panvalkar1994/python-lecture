# string iterpolation using format method
name = "vaibhav"
country = "India"
age = 27
print("Hello {}".format(name))

# using positions
print("Name:{2}, Country:{0},age:{1}".format(country, age, name))

# using variables
print("The {q} {b} {f}".format(q='Quick', b='Brown', f='Fox'))

# float formating {value:width.precision f}
result = 22/7
print("The result is {r:1.3f}".format(r=result))

# another way to format
print(f"New result {result:1.2f}")
