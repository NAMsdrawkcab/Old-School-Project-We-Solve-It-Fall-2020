#People in Line Simulator
import random #imports the random module to help simulate random lines

#this function welcomes the user
def Welcome(): #defines Welcome helper function
    print("Welcome to my COVID-19 Line Simulator!") #greets the user

#this function receives the number of 6-foot positions in a line
def Positions(): #defines Positions helper function
    while True: #creates while loop that lasts until broken
        p = int(input("Please enter the number of 6-foot positions: ")) #prompts user to enter the number of positions
        print("You entered", p) #displays value that user entered
        if p<3 or p>99: #checks if value is not between 3 and 99
            print("Please enter a number between 3 and 99!") #informs user that value is invalid, prompting question again to enter new value
        else: #value is between 3 and 99
            break #breaks loop
    return p #returns value to be used by another function

#this function receives the number of people in line
def People(n): #defines People helper function
    while True: #creates while loop that lasts until broken
        h = int(input("Please enter the number of people: ")) #prompts user to enter the number of people
        print("You entered", h) #displays value that user entered
        if h<1 or h>98: #checks is value is not between 1 and 98
            print("Please enter a number between 1 and 98!") #informs user that value is invalid, prompting question again to enter new value
        elif h>=n: #checks if value is greater than the number of positions
            print("The number of people must be less than the number of 6-foot positions!") #inforoms user that value is invalid, prompting question again to enter new value
        else: #values fulfills all conditions; less than positions while between 1 and 98
            break #breaks loop
    return h #returns value to be used by another function

#this function creates a list that will be used in the last helper function
def Line(x, y): #defines Line helper function
    counter = y #sets internal value for later use in the function
    line = [] #creates list named 'line'
    possible = ["P", "E"] #list contain two possible outcomes for each position; "P" for person, "E" for empty
    while True: #creates while loop that lasts until broken
        for i in range(x): #creates for loop based on value x
            line.append(random.choice(possible)) #chooses random object from 'possible' and places it in 'line'; ensures lines are unique
            if line[i]=="P": #checks if functions places object "P" in list
                y -= 1 #counter that decreases by 1 everytime "P" is added to list
                if y<0: #checks if counter is negative
                    line[i] = "E" #replaces future instances of "P" with "E"
        if y>0: #checks if counter is greater then zero; checks if all people have been placed in line
            line = [] #if not all people are placed in line, resets the list to create new line
            y = counter #uses the internal value from earlier to reset counter
        elif y<1: #checks if all people have been placed in line
            break #breaks loop
    return line #returns value to be used by another function

#this function produces the final result
def Final(lst): #defines Final helper function
    print("Line:") #displays text to label final result
    for s in range(len(lst)): #creates loop based on how long list is
        if lst[s]=="E": #checks if position is empty
            if s==len(lst)-1 and lst[s-1]=="P": #checks final position and if previous position is occupied
                lst[s] = 1 #1 person is adjacent
            elif s==len(lst)-1 and lst[s-1]!="P": #checks final position and if previous position is unoccupied
                lst[s] = 0 #no one is adjacent
            elif s==0 and lst[s+1]=="P": #checks first position and if previous position is occupied
                lst[s] = 1 #1 person is adjacent
            elif s==0 and lst[s+1]!="P": #checks first position and if previous position is unoccupied
                lst[s] = 0 #no one is adjacent
            elif lst[s-1]!="P" and lst[s+1]!="P": #checks if adjacent positions are unoccupied
                lst[s] = 0 #no one is adjacent
            elif lst[s-1]=="P" and lst[s+1]!="P": #checks if person is behind while no one is ahead
                lst[s] = 1 #1 person is adjacent
            elif lst[s-1]!="P" and lst[s+1]=="P": #checks if person is ahead while no one is behind
                lst[s] = 1 #1 person is adjacent
            elif lst[s-1]=="P" and lst[s+1]=="P": #checks if adjacent positions are occupied
                lst[s] = 2 #2 people are adjacent
        print(lst[s], end = " ") #displays line

#performs main function of program calling helper functions
def main(): #defines main function
    Welcome() #calls Welcome function
    number = Positions() #calls Positions function, assigning it to variable 'number'
    ready = Line(number, People(number)) #calls Line function while simultaneously calling for People function; both functions use value from Positions
    Final(ready) #calls Final function, giving the user a simulated line

main() #calls main function
