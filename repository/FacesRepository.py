import sqlite3

class FacesRepository():
    def __init__(self):
        self.databaseUri = 'repository/faces.db'
        self.connection = None

    def SetDatabase(self, _database):
        self.databaseUri = _database

    def GetConnection(self):
        self.connection = sqlite3.connect(self.databaseUri)

    def CloseConnection(self):
        self.connection.close()

    def GetCursor(self):
        return self.connection.cursor()

    def Commit(self):
        self.connection.commit()

    def Roolback(self):
        self.connection.rollback()

    def NewUser(self, UserName):
        result = -1
        c = self.GetCursor()
        try:
            c.execute("INSERT INTO Users (UserName) VALUES('%s')" % UserName)
            #self.Commit()
            c.execute("SELECT UserId FROM Users WHERE UserName = '%s'" % UserName)
            result = c.fetchone()[0]
            self.Commit()
        except sqlite3.Error as ex:
            print(ex)
        
        return result

    def GetUser(self, UserName):
        c = self.GetCursor()
        try:
            c.execute("SELECT * FROM Users WHERE UserName = '%s'" % UserName)
            result = c.fetchone()
            self.Commit()
        except sqlite3.Error as ex:
            print(ex)
        return result

    def QueryUser(self, UserId):
        c = self.GetCursor()
        try:
            c.execute("SELECT * FROM Users WHERE UserId = '%d'" % UserId)
            result = c.fetchone()
            self.Commit()
        except sqlite3.Error as ex:
            print(ex)

        if result == None:
            result = (0, 'Usuário não encontrado')
        return result
        
    def ResetDatabase():
        fr = FacesRepository()
        fr.GetConnection()
        c = fr.GetCursor()
        c.execute("DELETE FROM Users")
        fr.Commit()
        fr.CloseConnection()

    def GetLastUserId(self) -> int:
        c = self.GetCursor()
        try:
            c.execute("SELECT MAX(UserId) FROM Users")
            result = c.fetchone()[0]
            self.Commit()
        except sqlite3.Error as ex:
            print(ex)

        if result == None:
            result = (0, 'Não foi possivel resgatar ultimo ID')
        return result

