print("Welcome to the Elite 101 Chatbot!")
name = input("Please enter your name: ")
print("Nice to meet you " + name + "! ")
age = input("How old are you? ") 
print("Welcome " + name + "! Oh, to be " + age + " again... How may I help you today?")
print("")
print("Please choose from the following options: ")
print("1. Placeholder")
print("2. Placeholder")
print("3. Placeholder")
print("4. Exit")
choice = int(input("Please enter the number of your choice: "))
if choice == 4: 
  print("Goodbye " + name + "! Have a great day!")
elif choice == 1:
  print("Placeholder number 1")
elif choice == 2:
  print("Placeholder number 2")
elif choice == 3:
  print("Placeholder number 3")
else:
  print("Invalid choice. Please try again.")