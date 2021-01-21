# Function used to analyze and parse individual characters of the string and show state in the DFA
def dfa_analysis_algorithm(string):
    # Variable used to track the state of the character in the DFA
    state = 0
    # Set of lower-case Roman letters
    gamma = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','y','z']
    # Set of period
    delta = '.'
    # Set of the @ symbol
    phi = '@'
    # Variable serves to automatically reject characters and strings that go in the trap state
    reject = 0
    
    # Checks each character individually
    for ch in string:
        # Initial State and if character in gamma -> Go to State 1
        if ch in gamma and state == 0:
            state = 1
            qState = str(state)
            print(ch+' q'+qState)
        # State 1 and if character in gamma -> Loop back to State 1
        elif ch in gamma and state == 1:
            state = 1
            qState = str(state)
            print(ch+' q'+qState)
        # State 1 and if character is a period -> Go back to the Initial State
        elif ch == delta and state == 1:
            state = 0
            qState = str(state)
            print(ch+' q'+qState)
        # State 1 and if character is the @ symbol -> Go to State 2
        elif ch == phi and state == 1:
            state = 2
            qState = str(state)
            print(ch+' q'+qState)
        # State 2 and if character in gamma -> Go to State 3
        elif ch in gamma and state == 2:
            state = 3
            qState = str(state)
            print(ch+' q'+qState)
        # State 3 and if charater in gamma -> Loop back to State 3
        elif ch in gamma and state == 3:
            state = 3
            qState = str(state)
            print(ch+' q'+qState)
        # State 3 and if character is a period -> Go to State 4
        elif ch in delta and state == 3:
            state = 4
            qState = str(state)
            print(ch+' q'+qState)
        # State 4 and if character is a 'c' -> Go to State 5
        elif ch == gamma[2] and state == 4:
            state = 5
            qState = str(state)
            print(ch+' q'+qState)
        # State 4 and if character in gamma but not a 'c' -> Go to State 3
        elif ch in gamma and state == 4 and ch != gamma[2]:
            state = 3
            qState = str(state)
            print(ch+' q'+qState)
        # State 5 and character is a 'o' -> Go to State 6
        elif ch == gamma[14] and state == 5:
            state = 6
            qState = str(state)
            print(ch+' q'+qState)
        # State 5 and character is a period -> Go to State 4
        elif ch in delta and state == 5:
            state = 4
            qState = str(state)
            print(ch+' q'+qState)
        # State 5 and character in gamma but not a 'o' -> Go to State 3
        elif ch in gamma and state == 5 and ch != gamma[14]:
            state = 3
            qState = str(state)
            print(ch+' q'+qState)
        # State 6 and character is a period -> Go to State 4
        elif ch in delta and state == 6:
            state = 4
            qState = str(state)
            print(ch+' q'+qState)
        # State 6 and character in gamma but not a 'm' -> Go to State 3
        elif ch in gamma and state == 6 and ch != gamma[12]:
            state = 3
            qState = str(state)
            print(ch+' q'+qState)
        # State 6 and character is an 'm' -> Go to State 7
        elif ch == gamma[12] and state == 6:
            state = 7
            qState = str(state)
            print(ch+' q'+qState)
        # State 7 and character is a period -> Go to State 4
        elif ch in delta and state == 7:
            state = 4
            qState = str(state)
            print(ch+' q'+qState)
        # State 7 and character in gamma -> Go to State 3
        elif ch in gamma and state == 7:
            state = 3
            qState = str(state)
            print(ch+' q'+qState)
        # ALL EDGES NOT SPECIFIED GO TO A TRAP STATE
        else:
            print(ch+' q8 TRAP STATE')
            reject = 1
    
    # If any character goes to trap state, string rejected
    if reject == 1:
        print("STRING REJECTED")
    # If the string finishes in the final state 7, string accepted
    elif state == 7:
        print("STRING ACCEPTED")
    # Else string rejected
    else:
        print("STRING REJECTED")
        
        
while(True):
    # Read user input ("y" or "n")
    yes_or_no = input("Do you want to enter a string: ")
    
    # input("yes") 
    if (yes_or_no == "y"):
        # Read user input (string over language L)
        dfa_string = input("Enter a string: ")
        # DFA Analysis Function to return the state of the string, character by character
        dfa_analysis_algorithm(dfa_string)
    # input("no") -> Terminate loop and program
    elif(yes_or_no == "n"):
        break
    else:
        # Incase of invalid input
        print("Invalid input! Try again")
        continue
    
