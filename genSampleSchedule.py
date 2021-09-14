import sqlite3 as sql
import random

def genSample():

	conn = sql.connect('data.db')
	cur = conn.cursor()

	perfList = []

	cur.execute("SELECT PerfName From Performer")
	rows = cur.fetchall()

	print(rows)
	for row in rows:
		perfList.append(row[0])

	print (perfList)
	for perf in perfList:

		rlist=randomList()
	
		cur.execute("UPDATE Schedule SET " + \
			"M1=?, M2=?, M3=?, M4=?," + \
			"M5=?, M6=?, M7=?, M8=?," + \
			"M9=?, M10=?, M11=?, M12=?," + \
			"M13=?, M14=?, M15=?, M16=?," + \
			"T1=?, T2=?, T3=?, T4=?," + \
			"T5=?, T6=?, T7=?, T8=?," + \
			"T9=?, T10=?, T11=?, T12=?," + \
			"T13=?, T14=?, T15=?, T16=?," + \
			"W1=?, W2=?, W3=?, W4=?," + \
			"W5=?, W6=?, W7=?, W8=?," + \
			"W9=?, W10=?, W11=?, W12=?," + \
			"W13=?, W14=?, W15=?, W16=?," + \
			"R1=?, R2=?, R3=?, R4=?," + \
			"R5=?, R6=?, R7=?, R8=?," + \
			"R9=?, R10=?, R11=?, R12=?," + \
			"R13=?, R14=?, R15=?, R16=?," + \
			"F1=?, F2=?, F3=?, F4=?," + \
			"F5=?, F6=?, F7=?, F8=?," + \
			"F9=?, F10=?, F11=?, F12=?," + \
			"F13=?, F14=?, F15=?, F16=? " + \
			"WHERE PerfName=?",(\
			rlist[0],rlist[1],rlist[2],rlist[3],\
			rlist[4],rlist[5],rlist[6],rlist[7],\
			rlist[8],rlist[9],rlist[10],rlist[11],\
			rlist[12],rlist[13],rlist[14],rlist[15],\
			rlist[16],rlist[17],rlist[18],rlist[19],\
			rlist[20],rlist[21],rlist[22],rlist[23],\
			rlist[24],rlist[25],rlist[26],rlist[27],\
			rlist[28],rlist[29],rlist[30],rlist[31],\
			rlist[32],rlist[33],rlist[34],rlist[35],\
			rlist[36],rlist[37],rlist[38],rlist[39],\
			rlist[40],rlist[41],rlist[42],rlist[43],\
			rlist[44],rlist[45],rlist[46],rlist[47],\
			rlist[48],rlist[49],rlist[50],rlist[51],\
			rlist[52],rlist[53],rlist[54],rlist[55],\
			rlist[56],rlist[57],rlist[58],rlist[59],\
			rlist[60],rlist[61],rlist[62],rlist[63],\
			rlist[64],rlist[65],rlist[66],rlist[67],\
			rlist[68],rlist[69],rlist[70],rlist[71],\
			rlist[72],rlist[73],rlist[74],rlist[75],\
			rlist[76],rlist[77],rlist[78],rlist[79],\
			perf))
			
		conn.commit()

def randomList():

	randList = []

	for i in range(0,80):
		randList.append(random.randint(0,1))

	return randList

if __name__ == "__main__":
	genSample()
