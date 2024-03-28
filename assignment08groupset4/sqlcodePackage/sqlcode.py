#sqlcode.py
 
import pyodbc
class Data:
    def Connect(self, myDatabase):
        '''
        connect to the database and create a cursor
        @return: the cursor object
        '''
        conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=lcb-sql.uccob.uc.edu\\nicholdw;'
                          'Database=' + myDatabase + ';'
                          'uid=IS4010Login;'
                          'pwd=P@ssword2;')
        # Submit a query to the SQL Server instance and store the results in the cursor object
        cursor = conn.cursor()
        return cursor
    
    def LargesttoSmallestPrice(self):
        #troegele
        '''
        Retrieve the Prices for all Products and sort it from largest to smallest price
        @return: Largest to Smallest Price list with Description and ProductID
        '''
        cursor = self.Connect("GroceryStoreSimulator")
        
        query2 = """
                SELECT ProductID, Description, InitialPricePerSellableUnit AS LargestoSmallestPrice
                FROM dbo.tProduct
                ORDER BY [LargestoSmallestPrice] DESC;
                """
        
        cursor.execute(query2)
        results = cursor.fetchall()
        # Close the cursor and connection
        cursor.close()
        return results
    
    def GetEmployeeWithMostSales(self):
        #willi6d3
        '''
        Retrieve the employee who sold the most products
        @return: Employee information with the highest number of transactions
        '''
        cursor = self.Connect("GroceryStoreSimulator")  
 
        # SQL query to find the employee who sold the most products
        query = '''
            SELECT LTRIM(RTRIM(e.[LastName])) AS LastName,
               LTRIM(RTRIM(e.[FirstName])) AS FirstName,
               COUNT(t.[TransactionID]) AS TotalTransactions
               FROM [dbo].[tEmpl] e
               INNER JOIN [dbo].[tTransaction] t ON e.[EmplID] = t.[EmplID]
               GROUP BY e.[EmplID], e.[Empl], e.[LastName], e.[FirstName]
               ORDER BY TotalTransactions DESC;
        '''
        
        cursor.execute(query)
        result = cursor.fetchall()
        # Close the cursor and connection
        cursor.close()
        return result
    
    def Top10Ingedrients(self):
        #gilligtp
        '''
        Execute query1 and return results
        @param query: the SSMS SQL query to execute
        @return: results
        '''
        cursor = self.Connect("GroceryStoreSimulator")
        
        query3 = """
            SELECT TOP (10)
        CASE
            WHEN CHARINDEX('(', i.Ingredient) > 0 THEN SUBSTRING(i.Ingredient, 1, CHARINDEX('(', i.Ingredient) - 1)
            ELSE i.Ingredient
        END AS Ingredient,
        SUM(tod.Quantity) AS TotalSold
        FROM dbo.tIngredient i
        INNER JOIN dbo.tProductIngredient pi ON pi.IngredientID = i.IngredientID
        INNER JOIN dbo.tProduct p ON p.ProductID = pi.ProductID
        INNER JOIN dbo.tOrderDetail tod ON tod.ProductID = p.ProductID
        GROUP BY
        CASE
            WHEN CHARINDEX('(', i.Ingredient) > 0 THEN SUBSTRING(i.Ingredient, 1, CHARINDEX('(', i.Ingredient) - 1)
            ELSE i.Ingredient
        END
        ORDER BY TotalSold DESC;
        """
        cursor.execute(query3)
        results = cursor.fetchall()  # Store the fetched results
        cursor.close()
        return results  # Return the retrieved results
