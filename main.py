import list

def displayMenu():
  choice = int(input('1. Add name \n2. Display list \n3. Quit \n'))
  while choice > 3 or choice < 1:
    choice = int(input('Invalid choice - please re-enter: '))
  else:
    if choice == 1:
      name = input('Enter the name to be added to the list: ')
      pos = int(input('Enter the position in the list to insert the name (1-10): '))
      list.list.insert(pos,name)
      displayMenu()
    elif choice == 2:
      print(list.list)
      displayMenu()
    elif choice == 3:
      print('Program terminating')
      quit()


input('Welcome to the list program!\nPress enter to continue... ')
displayMenu()
