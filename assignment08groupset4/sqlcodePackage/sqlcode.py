#the data class
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