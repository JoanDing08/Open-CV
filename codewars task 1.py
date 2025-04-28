#Write a function that accepts an array of 10 integers (between 0 and 9) 
#that returns a string of those numbers in the form of a phone number.

def create_phone_number():
  digits=[]
  for i in range(10):
    digits.append(input())
  print(f"({"".join(digits[0:3])}) {"".join(digits[3:6])}-{"".join(digits[6:])}")

create_phone_number()
