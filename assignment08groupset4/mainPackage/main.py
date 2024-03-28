# main.py
'''
# Name: Tom Gilligan, Leonie Troeger, Deonta Williams
# email: gilligtp@mail.uc.edu, troegele@mail.uc.edu, willi6d3@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date: 03/28/24
# Course/Section: 002
# Semester/Year: Spring 24
# Brief Description of the assignment: GitHub collaboration Project using SSMS in Eclipse
'''
 
from sqlcodePackage.sqlcode import Data
 
def main():
    
    data = Data()
    myData = Data()
    myData2 = Data()
    
    while True:
        print("\n Choose an option:")
        print("1. Option 1")
        print("2. Option 2")
        print("3. Option 3")
        print("q. Quit")
 
        choice = input("Enter your choice:")
 
        if choice == '1':
            # Option 1: Retrieve employee with most sales
            print("Option 1 selected")
            employee_most_sales = data.GetEmployeeWithMostSales() # Call the function to get results
            print(employee_most_sales)
            print("LastName + FirstName + Transactions made.")
            
        elif choice == '2':
            # Implement option 2
            print("Option 2 selected")
            LargesttoSmallestPrice = myData.LargesttoSmallestPrice() # Call the function to get results
            print(LargesttoSmallestPrice)
        
        elif choice == '3':
            # Implement option 3
            print("Option 3 selected")
            Top10Ingredients = myData2.Top10Ingedrients()  # Call the function to get results
            #clean up the data, its ugly
            formatted_output = ",\n".join([f"{ingredient[0]:<50} ({ingredient[1]:>5})" for ingredient in Top10Ingredients])
            print(formatted_output)
            
        elif choice.lower() == 'q':
            print("Exiting the program...")
            break  # Exit the loop and end the program
            
        else:
            print("Invalid choice. Please choose again.")
 
if __name__ == "__main__":
    main()
