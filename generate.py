import sqlite3 as sql
from test import recurListComp
import time

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
		if scheduleSum[78] == 0:
			scheduleSum[79] = 0

	#Update Team Schedule Entry in DB
	#Add all the Schedule checkboxes in
	cur.execute("UPDATE TeamSchedule SET " + \
		"TM1=?, TM2=?, TM3=?, TM4=?," + \
		"TM5=?, TM6=?, TM7=?, TM8=?," + \
		"TM9=?, TM10=?, TM11=?, TM12=?," + \
		"TM13=?, TM14=?, TM15=?, TM16=?," + \
		"TT1=?, TT2=?, TT3=?, TT4=?," + \
		"TT5=?, TT6=?, TT7=?, TT8=?," + \
		"TT9=?, TT10=?, TT11=?, TT12=?," + \
		"TT13=?, TT14=?, TT15=?, TT16=?," + \
		"TW1=?, TW2=?, TW3=?, TW4=?," + \
		"TW5=?, TW6=?, TW7=?, TW8=?," + \
		"TW9=?, TW10=?, TW11=?, TW12=?," + \
		"TW13=?, TW14=?, TW15=?, TW16=?," + \
		"TR1=?, TR2=?, TR3=?, TR4=?," + \
		"TR5=?, TR6=?, TR7=?, TR8=?," + \
		"TR9=?, TR10=?, TR11=?, TR12=?," + \
		"TR13=?, TR14=?, TR15=?, TR16=?," + \
		"TF1=?, TF2=?, TF3=?, TF4=?," + \
		"TF5=?, TF6=?, TF7=?, TF8=?," + \
		"TF9=?, TF10=?, TF11=?, TF12=?," + \
		"TF13=?, TF14=?, TF15=?, TF16=? " + \
		"WHERE ActName=? AND TeamName=?",(\
		scheduleSum[0],scheduleSum[1],\
		scheduleSum[2],scheduleSum[3],\
		scheduleSum[4],scheduleSum[5],\
		scheduleSum[6],scheduleSum[7],\
		scheduleSum[8],scheduleSum[9],\
		scheduleSum[10],scheduleSum[11],\
		scheduleSum[12],scheduleSum[13],\
		scheduleSum[14],scheduleSum[15],\
		scheduleSum[16],scheduleSum[17],\
		scheduleSum[18],scheduleSum[19],\
		scheduleSum[20],scheduleSum[21],\
		scheduleSum[22],scheduleSum[23],\
		scheduleSum[24],scheduleSum[25],\
		scheduleSum[26],scheduleSum[27],\
		scheduleSum[28],scheduleSum[29],\
		scheduleSum[30],scheduleSum[31],\
		scheduleSum[32],scheduleSum[33],\
		scheduleSum[34],scheduleSum[35],\
		scheduleSum[36],scheduleSum[37],\
		scheduleSum[38],scheduleSum[39],\
		scheduleSum[40],scheduleSum[41],\
		scheduleSum[42],scheduleSum[43],\
		scheduleSum[44],scheduleSum[45],\
		scheduleSum[46],scheduleSum[47],\
		scheduleSum[48],scheduleSum[49],\
		scheduleSum[50],scheduleSum[51],\
		scheduleSum[52],scheduleSum[53],\
		scheduleSum[54],scheduleSum[55],\
		scheduleSum[56],scheduleSum[57],\
		scheduleSum[58],scheduleSum[59],\
		scheduleSum[60],scheduleSum[61],\
		scheduleSum[62],scheduleSum[63],\
		scheduleSum[64],scheduleSum[65],\
		scheduleSum[66],scheduleSum[67],\
		scheduleSum[68],scheduleSum[69],\
		scheduleSum[70],scheduleSum[71],\
		scheduleSum[72],scheduleSum[73],\
		scheduleSum[74],scheduleSum[75],\
		scheduleSum[76],scheduleSum[77],\
		scheduleSum[78],scheduleSum[79],\
		actName,teamName))

	conn.commit()
	cur.close()
	conn.close()

#This generates a possibility list of all teams for an act
def actToList(actName,dbName):

	conn = sql.connect(dbName)
	cur = conn.cursor()

	#Pull Performer Names
	cur.execute("SELECT TeamName FROM Team WHERE ActName=?", \
	(actName,))

	rows = cur.fetchall()

	#Initialize outputs
	output = []
	
	#Pull Schedules
	for row in rows:
		cur.execute("SELECT * From TeamSchedule Where ActName=? and TeamName=?",\
			(actName,row[0]))
		templist = cur.fetchall()
		tempsched = []
		for item in templist[0]:
			tempsched.append(item)
		tempList = scheduleToList(tempsched[2:])
		output.append(tempList)
	start = time.time()
	test = recurListComp(output[0],output[1:])
	end=time.time()-start

	print ("Time Elapsed: " + str(end) + " seconds")
	print ("Num of possibilities: " + str(len(test)))
	print (test[5:50])

def recursiveChecker():
	pass

#This translates the markes for the schedule into
#a list of possible 3 day schedules by using an integer
#to represent the position of possibilities
def scheduleToList(schedule):

	positionList = []
	output = []

	#Convert avaliability to slots
	for i in range(0,len(schedule)):
		if schedule[i] == 1:
			positionList.append(i)

	#Ugly nesting to brute force triple selections
	for i in range(0,len(positionList)-2):
		for j in range(0,len(positionList)-i-1):
			for k in range(0,len(positionList)-i-j):
				if checkDay(positionList[i], positionList[(j+i)], positionList[(k+j+i)]):
					output.append([positionList[i], positionList[(j+i)], positionList[(k+j+i)]])

	#print (output)
	print ("Num of possibles: " + str(len(output)))
	return output


#This is a helper method to make sure the list is only using different day
#Little clunky, but should be quick enough
def checkDay(a,b,c):

	if a < 15:
		a1 = 1
	elif a < 31 and a >= 15:
		a1 = 2
	elif a < 47 and a >= 31:
		a1 = 3
	elif a < 63 and a >= 47:
		a1 = 4
	else: 
		a1 = 5

	if b < 15:
		b1 = 1
	elif b < 31 and b >= 15:
		b1 = 2
	elif b < 47 and b >= 31:
		b1 = 3
	elif b < 63 and b >= 47:
		b1 = 4
	else: 
		b1 = 5

	if c < 15:
		c1 = 1
	elif c < 31 and c >= 15:
		c1 = 2
	elif c < 47 and c >= 31:
		c1 = 3
	elif c < 63 and c >= 47:
		c1 = 4
	else: 
		c1 = 5

	if a1!=b1 and b1!=c1 and a1!=c1:
		return True
	else:
		return False
if __name__=="__main__":
	generateTeam("Juggling", "2", "test.db")
 
