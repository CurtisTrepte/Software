def main():
  mainFunction = input("Hi and welcome to the software! What can I do for you?\n")

  if mainFunction.upper() == "EXIT":
    exit()
  elif mainFunction.upper() == "WEBSITE":
    print("curtist.webhostapp.com")
  elif mainFunction.upper() == ""  



#Get name and max
name = input("What is your name? \n")
age = int(input("What is your age? \n"))

if age < 13:
  exit()
else:
  main()