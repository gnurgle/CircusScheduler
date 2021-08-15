import sqlite3 as sql

def generateTeam(actName, teamName, dbFile):

	conn = sql.connect(dbFile)
	cur = conn.cursor()

	#Pull Performer Names
	cur.execute("SELECT PerfName FROM Performer WHERE (Act1=? AND Team1=?) " + \
	"OR (Act2=? AND Team2=?) " + \
	"OR (Act3=? AND Team3=?) " + \
	"OR (Act4=? AND Team4=?) " + \
	"OR (Act5=? AND Team5=?) ", \
	(actName,teamName,actName,teamName,actName,teamName,actName,teamName,actName,teamName))

	rows = cur.fetchall()

	#Convert from dict
	perfNames = []
	for row in rows:
		perfNames.append(row[0])

	#Empty schedule list
	scheduleSum = []
	for i in range(80):
		scheduleSum.append(0)

	#Pull and sum schedule for all performers
	for name in perfNames:
		cur.execute("SELECT * FROM Schedule WHERE PerfName=?",(name,))
		rows = cur.fetchall()
		for i in range(1,81):
			scheduleSum[i-1] += rows[0][i]

	#Pick the times when all can meet
	for i in range(80):
		if scheduleSum[i] == len(perfNames):
			scheduleSum[i] = 1
		else:
			scheduleSum[i] = 0

	#Filter out times if hour long practice
	cur.execute("Select Hour FROM Act WHERE ActName=?",(actName,))

	hourCheck = cur.fetchone()

	#Checks
	leftSide = False
	prevMatch = False

	#Sort
	if hourCheck[0] == 1:
		for i in range(1,80):
			#Check left set
			if scheduleSum[i-1] + scheduleSum[i] == 2:
				leftSide = True
				prevMatch = True
			else:
				leftSide = False
			if leftSide==False and prevMatch==False:
				scheduleSum[i-1]=0
			elif leftSide==False and prevMatch==True:
				prevMatch=False

		#Final space check
		if scheduleSum[79] == 0:
			scheduleSum[80] = 0
	print(scheduleSum)

if __name__=="__main__":
	generateTeam("Juggling", "2", "test.db")
