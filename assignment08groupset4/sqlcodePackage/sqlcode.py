#sqlcode.py
#the data class
import pyodbc
from pip._vendor.pyparsing import results

class Data:
    def Connect(self, myDatabase):
        '''
        connect to the database and create a cursor
        @return: the cursor object
        '''
        conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=lcb-sql.uccob.uc.edu\\nicholdw;'
                          'Database=GroceryStoreSimulator;'
                          'uid=IS4010Login;'
                          'pwd=P@ssword2;')
        # Submit a query to the SQL Server instance and store the results in the cursor object
        cursor = conn.cursor()
        return cursor
    
    def run_query1(self, query1):
        '''
        Execute query1 and return results
        @param query: the SSMS SQL query to execute 
        @return: results
        '''
        cursor = self.Connect("GroceryStoreSimulator")
        cursor.execute(query1)
        results = cursor.fetchall()
        return results
        