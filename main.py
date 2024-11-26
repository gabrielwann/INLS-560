import sys


while True:
    
    
    file_variable = input ('''
    What file would you like to serach for?:
    a) prince_mj_songlist.csv
    b) retired_soccer_players.csv
    x) to exit
    ''')
    
    # process user input
    if file_variable == 'x':
        sys.exit() 
    elif file_variable =='a':
        file_variable = 'prince_mj_songlist.csv'
    elif file_variable == 'b':
        file_variable = 'retired_soccer_players.csv'
    else:
        print("Invalid option. Please select a, b, or x. It's not that hard.")
        continue
    
    # etner a serach term this // is a global variable
    search_variable = input(f'Enter the search term for {file_variable} file: ')
    search_variable = search_variable.title() # Make it so that the user can enter lower-case term.
    
    
    # go to 02_serach_for_term
    def find(file_variable, search_variable): 
        with open(file_variable, 'r') as file:
            content = file.read()
        # Now the file is in the memory buffer as content
        
        
        #Next check to see if the search_variable is in the content buffer:
        if search_variable in content:
            
            
            print(f'Your search term {search_variable} exists in the file {file_variable} file!')
            see_entries = input ('Would you like to see the entries (y or n)')
            
        # if y then run this code to output all entries:
            if see_entries.lower() == 'y':
                print(f'Here are all of the entries with the term {search_variable}:')
                with open(file_variable, 'r') as file:
                    for line in file:
                        if search_variable in line: 
                            print(line.strip())
            # if N lowercase (user does not want to) then run this code:
            elif see_entries.lower() =='n':
                print ('Goodbye')
                sys.exit()
            
            else:
                print('Invalid option. Please enter y or n.')
            
        else:  print(f'{search_variable} does not exist in {file_variable}')
    

    find(file_variable, search_variable)