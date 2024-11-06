# Initialize menu_option as an empty string to start the loop
menu_option = ''

# Loop until the user enters 'q'
while menu_option != 'q':
    # Display the menu using an f-string without sep="\n"
    print(f'''
    Shop information FAQs:
    a: elf friend
    b: dwarf companion
    c: dragon egg
    q: quit
    ''')

    # Prompt the user for input and store it in menu_option
    menu_option = input("Enter a letter for more info on your selection: ")

    # Check the user input and respond accordingly
    if menu_option == 'a':
        print('You selected an elf friend. They are wise and good with marksmanship.')
        # Ask an additional question
        training = input("Would you like training in archery with your elf friend? (y or n): ")
        if training == 'y':
            print("Great! Your elf friend will train you in archery.")
        else:
            print("No problem! You can enjoy their companionship without training.")
    elif menu_option == 'b':
        print('You selected a dwarf companion. They are fun and good with great craftsmanship.')
        # Ask an additional question
        crafting = input("Would you like to learn crafting skills with your dwarf companion? (y or n): ")
        if crafting == 'y':
            print("Excellent! Your dwarf companion will teach you crafting skills.")
        else:
            print("Alright! You can enjoy their company without learning crafting.")
    elif menu_option == 'c':
        print('You selected a dragon egg. They are rare and can hatch into a loyal but ferocious beast.')
        # Ask an additional question
        hatching = input("Do you want to incubate the dragon egg to hatch? (y or n): ")
        if hatching == 'y':
            print("Exciting! You’re on your way to raising a dragon.")
        else:
            print("Understood. The dragon egg will remain safely unhatched.")
    elif menu_option == 'q':
        print("Exiting the menu.")
    else:
        print("Invalid option, please choose a, b, c, or q.")


