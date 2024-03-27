'''
# Name: Tom Gilligan, Leonie Troeger, Deonta Williams 
# email: gilligtp@mail.uc.edu, troegele@mail.uc.edu, willi6d3@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date: 2/28/24
# Course/Section: 002
# Semester/Year: Spring 24
# Brief Description of the assignment: Github project using MSSQL
# Brief Description of what this module does: 3 packages that run sql queries invoked by mainPackage 
# Citations: w3scools, stackoverflow, google
'''
#main.py


import pyodbc
from sqlcodePackage.sqlcode import Data


if __name__ =="__main__":
    
    data = Data()
    query_result = data.run_query1("""
    SELECT TOP (10) i.Ingredient, SUM(tod.Quantity) AS TotalSold
    FROM dbo.tIngredient i
    INNER JOIN dbo.tProductIngredient pi ON pi.IngredientID = i.IngredientID
    INNER JOIN dbo.tProduct p ON p.ProductID = pi.ProductID
    INNER JOIN dbo.tOrderDetail tod ON tod.ProductID = p.ProductID
    GROUP BY i.Ingredient
    ORDER BY TotalSold DESC;
    """)