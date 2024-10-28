# Constants for 
MIN_RHINO_EGGS = 4
MIN_YEARS_TOP_AWARD = 3

years_sales = int(input('Enter the amount of rhino eggs you have laid'))
years_top_sales = int(input('Enter how many years you have been salesperson of the year: '))

if years_sales >= MIN_RHINO_EGGS and years_top_sales >= MIN_YEARS_TOP_AWARD:
    print('Congratulations! You are eligible for the Sales Manager Position')
else: 
    print(f'''
Haha! you do not meet the requirements for the Sales Manaager Position. 

You need at least:
- {MIN_RHINO_EGGS} number of rhino eggs laid
- {MIN_YEARS_TOP_AWARD} years as salesperson of the year
Better luck next time you silly goose.
''')
    