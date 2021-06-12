def main():
  mainFunction = input("Hi and welcome to the software! What can I do for you?\n")

  if mainFunction.upper() == "EXIT":
    exit()
  elif mainFunction.upper() == "CHICKEN":
    print("Wassup")  



#Get name and max
name = input("What is your name? \n")
age = int(input(f"Hello {name}, what is your age? \n"))

if age < 13:
  print("Sorry you are not old enough to use Software")
  exit = input("Please press any key to exit")
  exit()
else:
  main()