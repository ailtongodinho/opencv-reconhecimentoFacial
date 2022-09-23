from FacesRepository import FacesRepository

fr = FacesRepository()

fr.GetConnection()

c = fr.GetCursor()

c.execute("DELETE FROM Users")

fr.Commit()

fr.CloseConnection()
