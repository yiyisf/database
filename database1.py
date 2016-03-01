import sqlite3


conn = sqlite3.connect("yiyi.db")

c = conn.cursor()

def createTable():
	c.execute("CREATE TABLE FIRST(ID INT,UNIX REAL,DATESTEMP  TEXT,KETWORD TEXT,VALUE REAL)")

def dataEntry():
	c.execute("INSERT INTO stuffToPlot VALUES(1, 1365952181.288,'2013-04-14 10:09:41','Python Sentiment',5)")
	c.execute("INSERT INTO stuffToPlot VALUES(2, 1365952257.905,'2013-04-14 10:10:57','Python Sentiment',6)")
	c.execute("INSERT INTO stuffToPlot VALUES(3, 1365952264.123,'2013-04-14 10:11:04','Python Sentiment',4)")
	conn.commit()