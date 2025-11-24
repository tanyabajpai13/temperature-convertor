#Temperature conversion tool
def celsius_to_fahrenheit(c):
  return(c* 9/5) + 32 
def celsius_to_kelvin(c):
  return c + 273.15
def fahrenheit_to_celsius(f):
  return (f-32) * 5/9
def fahrenheit_to_kelvin(f):
  return (f-32) * 5/9 + 273.15
def kelvin_to_celsius(k):
  return k- 273.15 
def kelvin_to_fahrenheit(k):
  return (k- 273.15) * 9/5 + 32

print("Temperature Conversion Tool")
print("1. celsius to fahrenheit")
print("2. celsius to kelvin")
print("3. fahrenheit to celsius")
print("4. fahrenheit to kelvin")
print("5. kelvin to celsius")
print("6. kelvin to fahrenheit")

choice = int(input(" enter your choice (1-6):"))

if choice in range(1,7):
  value = float(input("enter the temperature value to convert:"))
  if choice == 1:
    print(f"{value} c = {celsius_to_fahrenheit(value)} f")
  elif choice == 2:
    print(f"{value} c = {celsius_to_kelvin(value)} k")
  elif choice == 3:
    print(f"{value} f = {fahrenheit_to_celsius(value)} c")
  elif choice == 4:
    print(f"{value} f = {fahrenheit_to_kelvin(value)} k")
  elif choice == 5:
    print(f"{value} k = {kelvin_to_celsius(value)} c")
  elif choice == 6:
    print(f"{value} k = {kelvin_to_fahrenheit(value)}f")
else:
  print("invalid choice! please enter a number from 1 to 6")