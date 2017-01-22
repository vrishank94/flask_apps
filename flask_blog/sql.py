import sqlite3
with sqlite3.connect("blog.db") as connection:
	c=connection.cursor()
	c.execute("CREATE TABLE posts(Title TEXT, Post TEXT)")
	c.execute("INSERT INTO posts VALUES('Good','I am Good')")
	