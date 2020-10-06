from loginPage import loginPage
from mainDirectory import mainMethods

user_info = loginPage.login()
run = True
while run:
    print("What feature would you like to use?\n(Enter a number)")
    feature = int(input("Track spending (1)\nTrack work hours (2)\nTrack savings (3)"))
    if feature == 1:
        mainMethods.trackSpend(user_info)
    elif feature == 2:
        mainMethods.trackWork(user_info)
    elif feature == 3:
        mainMethods.trackSave(user_info)
    else:
        print('No features match given input, please try again')
    exit_loop = True
    while exit_loop:
        cont = input("Would you like to continue using budgetAssistant? (y/n)")
        if cont == 'y':
            exit_loop = False
        elif cont == 'n':
            run = False
            user_info['Username'].terminateProgram("User selection to end program")
        else:
            print("Input not recognized, please try again")
