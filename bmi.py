#this is a short python program to calculate the bmi of a person
#home-work of dgplug
""""Update required:-----

    1. this is for adults male, make for adults female and for the children even
    2. Add. a BMI chart
    3. Make a GUI version of it
    
"""

print ("ok")

def check(bmi):
  if bmi<16:
    print("severe thinness")
  elif bmi>=16 and bmi<17:
    print("moderate thinness")
  elif bmi>=17 and bmi<18.5:
    print("mild thinness")
  elif bmi>=18.5 and bmi<25:
    print("normal")
  elif bmi>=25 and bmi<30:
    print("overweight")
  elif bmi>=30 and bmi<35:
    print("obese class-1")
  elif bmi>=35 and bmi<40:
    print("obese class-2")
  elif bmi>=40:
    print("obese class-3")


#print ("we want to calculate your BMI Press 1. to continue")
ch=int(input("we want to calculate your BMI Press 1. to continue ----- enter your choice====>"))

if ch==1:
  
  print ("pressd 1")
  weight=float(input("Enter your weight in kg"))
  height=float(input("enter your height in metres"))
  bmi=weight/(height*height)
  
  
  ch2=int(input("to check your condition that you belong to which category press 1====>"))
  if ch2==1:
    print("bmi(kg/m^2)=",bmi)
    check(bmi)
