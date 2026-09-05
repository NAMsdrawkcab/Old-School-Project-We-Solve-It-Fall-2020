#Final Project - Nam Luu, Kristen Odum, Joshua Thomas

#below is a series of dictionaries that will be reference later in the program
countries = {1: 'Mexico', 2: 'China', 3: 'India', 4: 'Vietnam'} #list of countries
status = {1: 'single', 2: 'married'} #potential marital status
houses = {1: 'a normal house', 2: 'an apartment', 3: 'a townhouse', 4: 'a condo'} #hosuing choices
currency = {1: 'Mexican peso', 2: 'Chinese yuan', 3: 'Indian rupee', 4: 'Vietnamese dong'} #types of currency
exchange = {1: 0.05, 2: 0.15, 3: 0.014, 4: 0.000043} #USD equivalent to 1 of selected currency

#these lists will be placed into a text file
normal = ['210000 7 5039_Sand_Hill_Dr', '139900 6 4639_Randall_Dr', '129900 6 1706_East_Mazor_Dr', '124900 6 1004_East_Crockett_Dr','119000 5 6435_Benson_Dr'] #data for normal houses
apartments = ['1540 4 8400_Veterans_Pky',  '1250 5 8500_Franciscan_Woods_Dr', '1217 4 1400_Boxwood_Blvd', '900 4 6029_Flat_Rock_Rd', '865 5 3390_North_Lumpkin_Rd'] #data for apartments
townhouses = ['99980 7 732_Broadway', '75000 7 8115_Dream_Boat_Dr'] #data for townhouses
condos = ['320000 7 1201_Front_Ave_404', '96000 4 1201_Front_Ave_521', '39800 2 1201_Front_Ave_219'] #data for condos

#the following will create a text file that will contain data for the avaiable houses
refer = open('housedata.txt', 'w') #opens file for writing
for i in range(len(normal)): 
  refer.write(normal[i] + '\n')
for i in range(len(apartments)):
  refer.write(apartments[i] +'\n')
for i in range(len(townhouses)):
  refer.write(townhouses[i] + '\n')
for i in range(len(condos)):
  refer.write(condos[i] + '\n')
refer.close() #closes file

#this function welcomes the user and gives a brief overview of the program
def Welcome(): #defines Welcome function
  print("Welcome to HomeFinder! Created by Kristen Odum, Nam Luu, and Joshua Thomas") #welcomes user
  print("This program will help you find a good home in Columbus, GA after you migrate.") #overview
  print("Answers will be number-based, and to confirm your answer, press Y for Yes or N for No. If nothing shows at the end, that means there was no house that matched your criteria.") #instruction

#this function asks the user for the country they come from, and records that value for later use
def askCountry(): #defines askCountry function
  while True: #sets while loop to repeat question
    country = int(input("Which country are you migrating from? 1 = Mexico, 2 = China, 3 = India, 4 = Vietnam: ")) #asks for country
    if country>0 and country<5: #checks if value is part of list
      confirm = str(input("You have chosen {}. Is this correct? Y/N: ".format(countries.get(country)))) #asks confirmation
      if confirm=="Y" or confirm=="y": #user confirms
        print("You are from {}!".format(countries.get(country))) #results
        break #breaks loop
      elif confirm=="N" or confirm=="n": #user says no
        continue #loops back to original question
      else: #invlaid input
        print("ERROR! Please type Y or N") #error message
    else: #invlaid input
      print("ERROR! Please select an option from the menu!") #error message
  return country #returns country selected

#this function asks the user for the size of their family, recording that value for later use
def askFamily():
  while True: #sets while loop to repeat question
    marital = int(input("Are you single or married? 1 = single, 2 = married: ")) #asks if user is married
    if marital>0 and marital<3: #checks if value is part of list
      confirm = str(input("You are {}. Is this correct? Y/N: ".format(status.get(marital)))) #asks confirmation
      if confirm=="Y" or confirm=="y": #user confirms
        size = str(input("Do you have children living with you? Y/N: ")) #asks user if they have children
        if size=="Y" or size=="y": #user says yes
          kids = int(input("How many kids do you have? ")) #asks user for number of children
          if kids>0: #validates input
            confirm2 = str(input("You have {} kids. Is this correct? Y/N: ".format(kids))) #asks confirmation
            if confirm2=="Y" or confirm2=="y": #user confirms
              family = marital + kids #family size is parents plus kids
              print("You are {} and have {} kids! Your family size is {}!".format(status.get(marital), kids, family)) #results
              break #breaks loop
            elif confirm2=="N" or confirm2=="n": #user says no
              continue #loops back to original question
            else: #invlaid input
              print("ERROR! Please type Y or N") #error message
          else: #invlaid input
            print("ERROR! Please enter a number greater than 0!") #error message
        elif size=="N" or size=="n": #user says no
          family = marital #family is just parents
          print("You are {} and have no kids! Your family size is {}!".format(status.get(marital), family)) #results
          break #breaks loop
        else: #invlaid input
          print("ERROR! Please type Y or N") #error message
      elif confirm=="N" or confirm=="n": #user says no
        continue #loops back to original question
      else: #invlaid input
        print("ERROR! Please type Y or N") #error message
    else: #invlaid input
      print("ERROR! Please select an option from the menu!") #error message
  return family #returns family size

#this function asks the user what house they want, recording it for later use
def askHouse():
  while True: #sets while loop to repeat question
    home = int(input("What kind of house do you want? 1 = normal house, 2 = apartment, 3 = townhouse, 4 = condo: ")) #asks what house user wants
    if home>0 and home<5: #checks if value is part of list
      confirm = str(input("You have chosen {}. Is this correct? Y/N: ".format(houses.get(home)))) #asks confirmation
      if confirm=="Y" or confirm=="y": #user confirms
        print("You want to live in {}!".format(houses.get(home))) #results
        break #breaks loop
      elif confirm=="N" or confirm=="n": #user says no
        continue #loops back to original question
      else: #invlaid input
        print("ERROR! Please type Y or N") #error message
    else: #invlaid input
      print("ERROR! Please select an option from the menu!") #error message
  return home #returns home selection

#this function asks the user how many rooms they want, narrowing down choices
def askRooms(): #defines askRooms function
  while True: #sets while loop to repeat question
    bath = int(input("How many bathrooms would you like? ")) #asks how many bathrooms user wants
    if bath>0: #validates input
      confirm = str(input("You have entered {}. Is this correct? Y/N: ".format(bath))) #asks confirmation
      if confirm=="Y" or confirm=="y": #user confirms
        break #breaks loop
      elif confirm=="N" or confirm=="n": #user says no
        continue #loops back to original question
      else: #invlaid input
        print("ERROR! Please type Y or N") #error message
    else: #invlaid input
      print("ERROR! Please select an option from the menu!") #error message
  while True: #sets while loop to repeat question
    bed = int(input("How many bedrooms would you like? ")) #asks how many bedrooms user wants
    if bed>0: #validates input
      confirm = str(input("You have entered {}. Is this correct? Y/N: ".format(bed))) #asks confirmation
      if confirm=="Y" or confirm=="y": #user confirms
        break #breaks loop
      elif confirm=="N" or confirm=="n": #user says no
        continue #loops back to original question
      else: #invlaid input
        print("ERROR! Please type Y or N") #error message
    else: #invlaid input
      print("ERROR! Please select an option from the menu!") #error message
  room = bath + bed #adds bathrooms and bedrooms together for total amount
  print("You want {} bathrooms and {} bedrooms. Not counting other rooms, you want a total of {} rooms!".format(bath, bed, room)) #results
  return room #returns total number of rooms

#this function asks the user how much money they have, which will be converted to USD based on their country of origin
def cashRange(x): #defines cashRange function
  print("You have chosen {}, meaning that your native currency is the {}.".format(countries.get(x), currency.get(x))) #tells user currency of country selected
  while True: #sets while loop to repeat question
    money = float(input("How much money do you have? ")) #asks user for money amount
    if money>0: #validates input
      confirm = str(input("You have entered {} {}. Is this correct? Y/N: ".format(money, currency.get(x)))) #asks confirmation
      if confirm=="Y" or confirm=="y": #user confirms
        convert = round(money * exchange.get(x), 2) #converts money to
        print("Your money has been converted to {} US dollars!".format(convert)) #results
        break #breaks loop
      elif confirm=="N" or confirm=="n": #user says no
        continue #loops back to original question
      else: #invlaid input
        print("ERROR! Please type Y or N") #error message
    else: #invlaid input
      print("ERROR! Please enter the amount of money you have!") #error message
  return convert #returns converted money

#this function will give the user the final results
def result(a, b, c, d, e): #defines result function
  print("Overview: You are from {} with a family of {}. You want to move into {} with {} rooms. Your money has been converted to {} US dollars.".format(countries.get(a), b, houses.get(c), d, e)) #gives overview of all user's answers
  final = open('housedata.txt', 'r') #opens file for reading
  if c==1: #if user chose normal house
    line_to_read = [0, 1, 2, 3, 4]
    for posi, line in enumerate(final):
      if posi in line_to_read:
        value = line.split()
        if int(value[0])<e and int(value[1])>d:
          print("For ${}, you can live at {} with {} rooms!".format(value[0], value[2], value[1])) #results
          break #breaks loop
        else:
          continue
  elif c==2: #if user chose apartment
    line_to_read = [5, 6, 7, 8, 9]
    for posi, line in enumerate(final):
      if posi in line_to_read:
        value = line.split()
        if int(value[0])<e and int(value[1])>d:
          print("For ${} per month, you can live at {} with {} rooms!".format(value[0], value[2], value[1])) #results
          break #breaks loop
        else:
          continue
  elif c==3: #if user chose townhouse
    line_to_read = [10, 11]
    for posi, line in enumerate(final):
      if posi in line_to_read:
        value = line.split()
        if int(value[0])<e and int(value[1])>d:
          print("For ${} as a down payment, you can live at {} with {} rooms!".format(value[0], value[2], value[1])) #results
          break #breaks loop
        else:
          continue
  elif c==4: #if user chose condo
    line_to_read = [12, 13, 14]
    for posi, line in enumerate(final):
      if posi in line_to_read:
        value = line.split()
        if int(value[0])<e and int(value[1])>d:
          print("For ${} as a down payment, you can live at {} with {} rooms!".format(value[0], value[2], value[1])) #results
          break #breaks loop
        else:
          continue 
  final.close() #closes file

#this is the main function of the program; calls all previous helper functions
def main(): #defines main function
  Welcome() #calls Welcome
  ready = askCountry() #calls askCountry; assigns to variable 'ready'
  result(ready, askFamily(), askHouse(), askRooms(), cashRange(ready)) #calls result while calling askFamily, askHouse, askRooms, cashRange
  print("Thank you for using our program! Have a nice day!") #thanks the user for usage before closing

main() #calls main function
