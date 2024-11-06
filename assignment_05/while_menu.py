# This will initialize the menu_option as an empty string to start the loop
menu_option = ''

# Loop until the user enters 'q'
while menu_option != 'q':
    # Ths will display the menu
    print('MENU:', 'a: elf friend', 'b: dwarf companion', 'c: dragon egg', 'q: quit', sep="\n")
    
    # Prompt the user for input and store it in menu_option
    menu_option = input("Enter a letter for more info on your selection: ")

    # Check the user input and respond accordingly
    if menu_option == 'a':
        print('You selected an elf friend. They are wise and good with marksmanship.')
    elif menu_option == 'b':
        print('You selected a dwarf companion. They are fun and good with great craftsmanship')
    elif menu_option == 'c': 
        print('You selected dragon egg. They are rare and can hatch into a loyal but ferocious beast')
    elif menu_option == 'q':
        print("Exiting the menu.")
    else:
        print("Invalid option, please choose a, b, c, or q.")

