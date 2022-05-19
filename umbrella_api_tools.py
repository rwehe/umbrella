import os
from dotenv import load_dotenv
from umbrella_destination_lists import getDestinationLists

load_dotenv()
organizationId = os.environ.get("organizationId")
management_key = os.environ.get("management_key")
management_secret = os.environ.get("management_secret")

def runScriptAgain():
    run_again = input('\n\nWould You Like To use another tool? [Y/N]: ').lower()
    if run_again not in (['yes','ye','y']):
        exit()
    else:
        True

def mainScriptLoop():
    print('''
***********************************************************************************************
*                                                                                             *
*                      Cisco Umbrella API Tools (Written for Python 3.10+)                    *
*                                                                                             *
***********************************************************************************************
*                                                                                             *
* USER INPUT NEEDED:                                                                          *
*                                                                                             *
*  1. Print destination lists                                                                 *
***********************************************************************************************
''')
    userchoice = input('Please Select Tool or Q to quit: ')
    return userchoice

if __name__ == "__main__":
    while True:
        invalid_entry = False
        userchoice = mainScriptLoop()
        if userchoice == '1':
            getDestinationLists(organizationId, management_key, management_secret)
        elif userchoice == '2':
            print('Functionality not yet avaliable')
        elif userchoice == 'q'.lower():
            exit()
        else:
            print('INVALID ENTRY... ')
            invalid_entry = True
        if not invalid_entry:
            runScriptAgain()
