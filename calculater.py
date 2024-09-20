def Addition(x,y):
  return x + y

def Subtratction(x,y):
  return x - y

def Multiplication(x,y):
  return x * y

def Division(x,y):
  if y == 0:
    return "Division by zero error!"
  else :
      return x / y

def Modulus(x,y):
  return y % x

def Square(x,y):
  return x ** y

def msg():
  return ("I hope you enjoy this .")

def eror():
  return ("Invalid input please give the correct input .")


while True:
  print ("\nDo you want to perform any calculation ")
  option = input ("Yes / no : ")
  option = option.lower()

  if option == "yes":
      print ("Welcome to World of Calculation ")
      print ("Select operation:")
      print ("1. Addittion")
      print ("2. Subtraction")
      print ("3. Multiplication")
      print ("4. Division")
      print ("5. Modulus")
      print ("6. Square")
      print ("7. Exit")

      choice = input("Please select( 1 / 2 / 3 / 4 / 5 / 6 / 7 ) : ")
      if choice in ('1' , '2' , '3' , '4' , '5' , '6'):

          num1 = int(input("Enter first number: "))
          num2 = int(input("Enter second number: "))

          if choice == '1':
            print (num1 , "+" , num2 , "=" , Addition( num1 , num2))

          elif choice == '2':
            print (num1 , "-" , num2 , "=" , Subtratction( num1 , num2))

          elif choice == '3':
            print (num1 , "*" , num2 , "=" , Multiplication( num1 , num2))

          elif choice == '4':
            print (num1 , "/" , num2 , "=" , Division( num1 , num2))
        
          elif choice == '5':
            print(num1 , "%" , num2 , "=" , Modulus(num1 , num2))

          elif choice == '6':
            print (num1 , "**" , num2 , "=" ,Square(num1 , num2))

      elif choice == '7':
        print (msg())
        break

      else:
        print (eror()) 
  else :
    print (msg())
    break
