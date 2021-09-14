from tkinter import filedialog as fd
from tkinter import ttk
from tkinter import *
from DBSetup import createDB
import sqlite3 as sql
from generate import generateTeam, actToList
from test import recurListComp
#==================================
#=        Generate Team Schedules
#==================================
def genTeams():

	conn = sql.connect(dbName)
	cur = conn.cursor()
	cur.execute("SELECT ActName FROM Act")
	rows = cur.fetchall()

	acts=[]
	for row in rows:
		acts.append(row[0])

	for act in acts:
		cur.execute("SELECT TeamName FROM Team Where ActName=?",((act,)))
		rows = cur.fetchall()
		teams = []

		for row in rows:
			teams.append(row[0])

		for team in teams:
			statusBar.configure(text="Generating " + act + " Team " + str(team,))
			generateTeam(act,team,dbName)

	
	cur.close()
	conn.close()

	statusBar.configure(text="Generated all Team Schedules")


#==================================
#=         Fetch Act Values
#==================================
def fetchActValues(e):

	print (actCombo.get())
	conn = sql.connect(dbName)
	cur = conn.cursor()
	cur.execute("SELECT * FROM Act WHERE ActName = ?",(actCombo.get(),))

	rows = cur.fetchall()
	if rows[0][6] is not None:
		coachCombo.set(rows[0][6])
	if rows[0][1] is None or rows[0][1] == 0:
		ring1Check.deselect()
	else:
		ring1Check.select()
	if rows[0][2] is None or rows[0][2] == 0:
		ring2Check.deselect()
	else:
		ring2Check.select()
	if rows[0][3] is None or rows[0][3] == 0:
		ring3Check.deselect()
	else:
		ring3Check.select()
	if rows[0][4] is None or rows[0][4] == 0:
		hutCheck.deselect()
	else:
		hutCheck.select()
	if rows[0][5] is None or rows[0][5] == 0:
		hourCheck.deselect()
	else:
		hourCheck.select()

	cur.close()
	conn.close()

	statusBar.configure(text="Loaded " + actCombo.get())

#==================================
#=         Fetch Perf Values
#==================================
def fetchPerfValues(e):

	conn = sql.connect(dbName)
	cur = conn.cursor()
	cur.execute("SELECT * FROM Schedule WHERE perfName = ?",(perfCombo.get(),))
	rows = cur.fetchall()

	#Checkbox flipper
	checkSwitcher(M1Check,rows[0][1])
	checkSwitcher(M2Check,rows[0][2])
	checkSwitcher(M3Check,rows[0][3])
	checkSwitcher(M4Check,rows[0][4])
	checkSwitcher(M5Check,rows[0][5])
	checkSwitcher(M6Check,rows[0][6])
	checkSwitcher(M7Check,rows[0][7])
	checkSwitcher(M8Check,rows[0][8])
	checkSwitcher(M9Check,rows[0][9])
	checkSwitcher(M10Check,rows[0][10])
	checkSwitcher(M11Check,rows[0][11])
	checkSwitcher(M12Check,rows[0][12])
	checkSwitcher(M13Check,rows[0][13])
	checkSwitcher(M14Check,rows[0][14])
	checkSwitcher(M15Check,rows[0][15])
	checkSwitcher(M16Check,rows[0][16])
	checkSwitcher(T1Check,rows[0][17])
	checkSwitcher(T2Check,rows[0][18])
	checkSwitcher(T3Check,rows[0][19])
	checkSwitcher(T4Check,rows[0][20])
	checkSwitcher(T5Check,rows[0][21])
	checkSwitcher(T6Check,rows[0][22])
	checkSwitcher(T7Check,rows[0][23])
	checkSwitcher(T8Check,rows[0][24])
	checkSwitcher(T9Check,rows[0][25])
	checkSwitcher(T10Check,rows[0][26])
	checkSwitcher(T11Check,rows[0][27])
	checkSwitcher(T12Check,rows[0][28])
	checkSwitcher(T13Check,rows[0][29])
	checkSwitcher(T14Check,rows[0][30])
	checkSwitcher(T15Check,rows[0][31])
	checkSwitcher(T16Check,rows[0][32])
	checkSwitcher(W1Check,rows[0][33])
	checkSwitcher(W2Check,rows[0][34])
	checkSwitcher(W3Check,rows[0][35])
	checkSwitcher(W4Check,rows[0][36])
	checkSwitcher(W5Check,rows[0][37])
	checkSwitcher(W6Check,rows[0][38])
	checkSwitcher(W7Check,rows[0][39])
	checkSwitcher(W8Check,rows[0][40])
	checkSwitcher(W9Check,rows[0][41])
	checkSwitcher(W10Check,rows[0][42])
	checkSwitcher(W11Check,rows[0][43])
	checkSwitcher(W12Check,rows[0][44])
	checkSwitcher(W13Check,rows[0][45])
	checkSwitcher(W14Check,rows[0][46])
	checkSwitcher(W15Check,rows[0][47])
	checkSwitcher(W16Check,rows[0][48])
	checkSwitcher(R1Check,rows[0][49])
	checkSwitcher(R2Check,rows[0][50])
	checkSwitcher(R3Check,rows[0][51])
	checkSwitcher(R4Check,rows[0][52])
	checkSwitcher(R5Check,rows[0][53])
	checkSwitcher(R6Check,rows[0][54])
	checkSwitcher(R7Check,rows[0][55])
	checkSwitcher(R8Check,rows[0][56])
	checkSwitcher(R9Check,rows[0][57])
	checkSwitcher(R10Check,rows[0][58])
	checkSwitcher(R11Check,rows[0][59])
	checkSwitcher(R12Check,rows[0][60])
	checkSwitcher(R13Check,rows[0][61])
	checkSwitcher(R14Check,rows[0][62])
	checkSwitcher(R15Check,rows[0][63])
	checkSwitcher(R16Check,rows[0][64])
	checkSwitcher(F1Check,rows[0][65])
	checkSwitcher(F2Check,rows[0][66])
	checkSwitcher(F3Check,rows[0][67])
	checkSwitcher(F4Check,rows[0][68])
	checkSwitcher(F5Check,rows[0][69])
	checkSwitcher(F6Check,rows[0][70])
	checkSwitcher(F7Check,rows[0][71])
	checkSwitcher(F8Check,rows[0][72])
	checkSwitcher(F9Check,rows[0][73])
	checkSwitcher(F10Check,rows[0][74])
	checkSwitcher(F11Check,rows[0][75])
	checkSwitcher(F12Check,rows[0][76])
	checkSwitcher(F13Check,rows[0][77])
	checkSwitcher(F14Check,rows[0][78])
	checkSwitcher(F15Check,rows[0][79])
	checkSwitcher(F16Check,rows[0][80])

	#Team Act Selecter
	cur.execute("SELECT * FROM Performer WHERE perfName = ?",(perfCombo.get(),))
	rows = cur.fetchall()

	comboSwitcher(perfAct1Combo,rows[0][1])
	comboSwitcher(perfAct2Combo,rows[0][2])
	comboSwitcher(perfAct3Combo,rows[0][3])
	comboSwitcher(perfAct4Combo,rows[0][4])
	comboSwitcher(perfAct5Combo,rows[0][5])
	comboSwitcher(perfTeam1Combo,rows[0][6])
	comboSwitcher(perfTeam2Combo,rows[0][7])
	comboSwitcher(perfTeam3Combo,rows[0][8])
	comboSwitcher(perfTeam4Combo,rows[0][9])
	comboSwitcher(perfTeam5Combo,rows[0][10])

	cur.close()
	conn.close()

	statusBar.configure(text="Loaded " + perfCombo.get())

#==================================
#=         Fetch Team Values
#==================================
def fetchTeamValues(e):

	conn = sql.connect(dbName)
	cur = conn.cursor()

	a = teamActCombo.get()
	t = teamCombo.get() 
	#Fetch Members
	cur.execute("SELECT PerfName FROM Performer WHERE (Act1=? AND Team1=?) " + \
	"OR (Act2=? AND Team2=?) " + \
	"OR (Act3=? AND Team3=?) " + \
	"OR (Act4=? AND Team4=?) " + \
	"OR (Act5=? AND Team5=?) ", \
	(a,t,a,t,a,t,a,t,a,t))

	output = ""
	rows = cur.fetchall()
	counter = 0
	for row in rows:
		counter += 1
		if counter <= 2:
			output += str(row[0]) + "\t"
		else:
			output += str(row[0]) + "\n"
			counter = 0
	teamMemLabel.configure(text=output)

	cur.execute("SELECT * FROM TeamSchedule WHERE ActName=? AND TeamName=?",(a,t))
	rows = cur.fetchall()

	#Checkbox flipper
	checkSwitcher(TM1Check,rows[0][2])
	checkSwitcher(TM2Check,rows[0][3])
	checkSwitcher(TM3Check,rows[0][4])
	checkSwitcher(TM4Check,rows[0][5])
	checkSwitcher(TM5Check,rows[0][6])
	checkSwitcher(TM6Check,rows[0][7])
	checkSwitcher(TM7Check,rows[0][8])
	checkSwitcher(TM8Check,rows[0][9])
	checkSwitcher(TM9Check,rows[0][10])
	checkSwitcher(TM10Check,rows[0][11])
	checkSwitcher(TM11Check,rows[0][12])
	checkSwitcher(TM12Check,rows[0][13])
	checkSwitcher(TM13Check,rows[0][14])
	checkSwitcher(TM14Check,rows[0][15])
	checkSwitcher(TM15Check,rows[0][16])
	checkSwitcher(TM16Check,rows[0][17])
	checkSwitcher(TT1Check,rows[0][18])
	checkSwitcher(TT2Check,rows[0][19])
	checkSwitcher(TT3Check,rows[0][20])
	checkSwitcher(TT4Check,rows[0][21])
	checkSwitcher(TT5Check,rows[0][22])
	checkSwitcher(TT6Check,rows[0][23])
	checkSwitcher(TT7Check,rows[0][24])
	checkSwitcher(TT8Check,rows[0][25])
	checkSwitcher(TT9Check,rows[0][26])
	checkSwitcher(TT10Check,rows[0][27])
	checkSwitcher(TT11Check,rows[0][28])
	checkSwitcher(TT12Check,rows[0][29])
	checkSwitcher(TT13Check,rows[0][30])
	checkSwitcher(TT14Check,rows[0][31])
	checkSwitcher(TT15Check,rows[0][32])
	checkSwitcher(TT16Check,rows[0][33])
	checkSwitcher(TW1Check,rows[0][34])
	checkSwitcher(TW2Check,rows[0][35])
	checkSwitcher(TW3Check,rows[0][36])
	checkSwitcher(TW4Check,rows[0][37])
	checkSwitcher(TW5Check,rows[0][38])
	checkSwitcher(TW6Check,rows[0][39])
	checkSwitcher(TW7Check,rows[0][40])
	checkSwitcher(TW8Check,rows[0][41])
	checkSwitcher(TW9Check,rows[0][42])
	checkSwitcher(TW10Check,rows[0][43])
	checkSwitcher(TW11Check,rows[0][44])
	checkSwitcher(TW12Check,rows[0][45])
	checkSwitcher(TW13Check,rows[0][46])
	checkSwitcher(TW14Check,rows[0][47])
	checkSwitcher(TW15Check,rows[0][48])
	checkSwitcher(TW16Check,rows[0][49])
	checkSwitcher(TR1Check,rows[0][50])
	checkSwitcher(TR2Check,rows[0][51])
	checkSwitcher(TR3Check,rows[0][52])
	checkSwitcher(TR4Check,rows[0][53])
	checkSwitcher(TR5Check,rows[0][54])
	checkSwitcher(TR6Check,rows[0][55])
	checkSwitcher(TR7Check,rows[0][56])
	checkSwitcher(TR8Check,rows[0][57])
	checkSwitcher(TR9Check,rows[0][58])
	checkSwitcher(TR10Check,rows[0][59])
	checkSwitcher(TR11Check,rows[0][60])
	checkSwitcher(TR12Check,rows[0][61])
	checkSwitcher(TR13Check,rows[0][62])
	checkSwitcher(TR14Check,rows[0][63])
	checkSwitcher(TR15Check,rows[0][64])
	checkSwitcher(TR16Check,rows[0][65])
	checkSwitcher(TF1Check,rows[0][66])
	checkSwitcher(TF2Check,rows[0][67])
	checkSwitcher(TF3Check,rows[0][68])
	checkSwitcher(TF4Check,rows[0][69])
	checkSwitcher(TF5Check,rows[0][70])
	checkSwitcher(TF6Check,rows[0][71])
	checkSwitcher(TF7Check,rows[0][72])
	checkSwitcher(TF8Check,rows[0][73])
	checkSwitcher(TF9Check,rows[0][74])
	checkSwitcher(TF10Check,rows[0][75])
	checkSwitcher(TF11Check,rows[0][76])
	checkSwitcher(TF12Check,rows[0][77])
	checkSwitcher(TF13Check,rows[0][78])
	checkSwitcher(TF14Check,rows[0][79])
	checkSwitcher(TF15Check,rows[0][80])
	checkSwitcher(TF16Check,rows[0][81])

	cur.close()
	conn.close()


	statusBar.configure(text="Loaded " + a + " Team " + t)

#==================================
#=         CheckSwitcher
#==================================
def checkSwitcher(chkBox,value):

	if value is None or value == 0:
		chkBox.deselect()
	else:
		chkBox.select()

#==================================
#=         ComboSwitcher
#============== ====================
def comboSwitcher(combo,value):

	if value is None:
		combo.set('')
	else:
		combo.set(value)


#==================================
#=      Act Save
#==================================

def actSave():
	conn = sql.connect(dbName)
	cur = conn.cursor()

	#Pull last 30 days of resident results
	cur.execute("UPDATE Act SET Ring1=?, Ring2=?, Ring3=?, Hut=?, Hour=?, Coach=? WHERE ActName=?",\
		(ring1Result.get(), ring2Result.get(), ring3Result.get(), hutResult.get(),\
		hourResult.get(), coachCombo.get(), actCombo.get()))

	conn.commit()
	cur.close()
	conn.close()

	statusBar.configure(text="Saved " + actCombo.get())


#==================================
#=     Perf Save
#==================================

def savePerf():
	conn = sql.connect(dbName)
	cur = conn.cursor()

	#Add all the Schedule checkboxes in
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
		M1Result.get(),M2Result.get(),\
		M3Result.get(),M4Result.get(),\
		M5Result.get(),M6Result.get(),\
		M7Result.get(),M8Result.get(),\
		M9Result.get(),M10Result.get(),\
		M11Result.get(),M12Result.get(),\
		M13Result.get(),M14Result.get(),\
		M15Result.get(),M16Result.get(),\
		T1Result.get(),T2Result.get(),\
		T3Result.get(),T4Result.get(),\
		T5Result.get(),T6Result.get(),\
		T7Result.get(),T8Result.get(),\
		T9Result.get(),T10Result.get(),\
		T11Result.get(),T12Result.get(),\
		T13Result.get(),T14Result.get(),\
		T15Result.get(),T16Result.get(),\
		W1Result.get(),W2Result.get(),\
		W3Result.get(),W4Result.get(),\
		W5Result.get(),W6Result.get(),\
		W7Result.get(),W8Result.get(),\
		W9Result.get(),W10Result.get(),\
		W11Result.get(),W12Result.get(),\
		W13Result.get(),W14Result.get(),\
		W15Result.get(),W16Result.get(),\
		R1Result.get(),R2Result.get(),\
		R3Result.get(),R4Result.get(),\
		R5Result.get(),R6Result.get(),\
		R7Result.get(),R8Result.get(),\
		R9Result.get(),R10Result.get(),\
		R11Result.get(),R12Result.get(),\
		R13Result.get(),R14Result.get(),\
		R15Result.get(),R16Result.get(),\
		F1Result.get(),F2Result.get(),\
		F3Result.get(),F4Result.get(),\
		F5Result.get(),F6Result.get(),\
		F7Result.get(),F8Result.get(),\
		F9Result.get(),F10Result.get(),\
		F11Result.get(),F12Result.get(),\
		F13Result.get(),F14Result.get(),\
		F15Result.get(),F16Result.get(),\
		perfCombo.get()))

	conn.commit()

	conn.execute("UPDATE Performer SET " + \
		"Act1=?, Team1=?, Act2=?, Team2=?," + \
		"Act3=?, Team3=?, Act4=?, Team4=?," + \
		"Act5=?, Team5=? WHERE PerfName=?",(\
		perfAct1Combo.get(), perfTeam1Combo.get(),\
		perfAct2Combo.get(), perfTeam2Combo.get(),\
		perfAct3Combo.get(), perfTeam3Combo.get(),\
		perfAct4Combo.get(), perfTeam4Combo.get(),\
		perfAct5Combo.get(), perfTeam5Combo.get(),\
		perfCombo.get()))
	conn.commit()
	cur.close()
	conn.close()

	statusBar.configure(text="Saved Schedule for " + perfCombo.get())

#==================================
#=         New Coach Add
#==================================

def addNewCoach():
	input = simpledialog.askstring("Add New Coach", "Enter the name of the coach")

	conn = sql.connect(dbName)
	cur = conn.cursor()

	#Add Coach
	cur.execute("INSERT OR IGNORE INTO Coaches (CoachName) VALUES(?)",(input,))

	conn.commit()
	cur.close()
	conn.close()

	statusBar.configure(text="Added " + input + " to Coaches")

	
#==================================
#=         New Act Add
#==================================

def addNewAct():
	input = simpledialog.askstring("Add New Act", "Enter the name of the new act")

	conn = sql.connect(dbName)
	cur = conn.cursor()

	#Insert New Act
	cur.execute("INSERT OR IGNORE INTO Act (ActName) VALUES(?)",(input,))

	conn.commit()
	cur.close()
	conn.close()

	statusBar.configure(text="Added " + input + " to Acts")

#==================================
#=         Edit Performer
#==================================

def editPerf():

	oldPerf = perfCombo.get()
	input = simpledialog.askstring(title="Edit Performer Name",prompt="Change the name of the performer",\
		initialvalue=oldPerf)

	conn = sql.connect(dbName)
	cur = conn.cursor()

	#Insert New Performer
	cur.execute("UPDATE Performer SET PerfName=? WHERE PerfName=?",(input,oldPerf))

	conn.commit()
	cur.close()
	conn.close()

	statusBar.configure(text= oldPerf + " changed to " + input)

#==================================
#=         Remove Performer
#==================================

def removePerf():

	oldPerf = perfCombo.get()

	answer = messagebox.askyesno(title="Confirmation", message="Do you want to remove "+oldPerf)

	if answer:
		conn = sql.connect(dbName)
		cur = conn.cursor()

		#Insert New Performer
		cur.execute("DELETE FROM Performer WHERE PerfName=?",(oldPerf,))

		conn.commit()
		cur.close()
		conn.close()

		statusBar.configure(text="Removed " + oldPerf)


#==================================
#=         New Performer Add
#==================================

def addNewPerf():
	input = simpledialog.askstring("Add New Performer", "Enter the name of the new performer")

	conn = sql.connect(dbName)
	cur = conn.cursor()

	#Insert New Performer
	cur.execute("INSERT OR IGNORE INTO Performer (PerfName) VALUES(?)",(input,))
	conn.commit()
	cur.execute("INSERT OR IGNORE INTO Schedule (PerfName) VALUES(?)",(input,))
	conn.commit()

	rlist = []
	for i in range(0,80):
		rlist.append(0)
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
		input))
	conn.commit()


	cur.close()
	conn.close()

	statusBar.configure(text="Added " + input + " to Performers")

#==================================
#=         New Team Add
#==================================

def addNewTeam():
	conn = sql.connect(dbName)
	cur = conn.cursor()

	#Check for num of Teams
	cur.execute("SELECT TeamName FROM Team WHERE ActName=?",(teamActCombo.get(),))
	rows = cur.fetchall()

	#Sort through existing Team #s and input missing/next
	newTeamNum = 1
	if len(rows) == 0:
		newTeamNum = 1
	else:
		for row in rows:
			if newTeamNum < row[0]:
				break
			else:
				newTeamNum += 1

	#Insert New Performer
	cur.execute("INSERT OR IGNORE INTO Team (TeamName,ActName) VALUES(?,?)",(newTeamNum,teamActCombo.get()))
	conn.commit()

	cur.execute("INSERT OR IGNORE INTO TeamSchedule (TeamName,ActName) VALUES(?,?)",(newTeamNum,teamActCombo.get()))
	conn.commit()

	cur.close()
	conn.close()

	statusBar.configure(text="Added Team " + str(newTeamNum) + " to " + teamActCombo.get())
	
#==================================
#=         Remove Team
#==================================

def removeTeam():

	oldTeam = teamCombo.get()

	answer = messagebox.askyesno(title="Confirmation", message="Do you want to remove Team " + oldTeam + " from " + teamActCombo.get() + "?")

	if answer:
		conn = sql.connect(dbName)
		cur = conn.cursor()

		#Remove Team
		cur.execute("DELETE FROM Team WHERE TeamName=? AND ActName=?",(oldTeam,teamActCombo.get()))
		conn.commit()

		cur.execute("DELETE FROM TeamSchedule WHERE TeamName=? AND ActName=?",(oldTeam,teamActCombo.get()))
		conn.commit()

		cur.close()
		conn.close()

		statusBar.configure(text="Removed Team " + oldTeam + " from " + teamActCombo.get())


#==================================
#=     Team Save Schedule
#==================================

def saveTeamSchedule():
	conn = sql.connect(dbName)
	cur = conn.cursor()

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
		TM1Result.get(),TM2Result.get(),\
		TM3Result.get(),TM4Result.get(),\
		TM5Result.get(),TM6Result.get(),\
		TM7Result.get(),TM8Result.get(),\
		TM9Result.get(),TM10Result.get(),\
		TM11Result.get(),TM12Result.get(),\
		TM13Result.get(),TM14Result.get(),\
		TM15Result.get(),TM16Result.get(),\
		TT1Result.get(),TT2Result.get(),\
		TT3Result.get(),TT4Result.get(),\
		TT5Result.get(),TT6Result.get(),\
		TT7Result.get(),TT8Result.get(),\
		TT9Result.get(),TT10Result.get(),\
		TT11Result.get(),TT12Result.get(),\
		TT13Result.get(),TT14Result.get(),\
		TT15Result.get(),TT16Result.get(),\
		TW1Result.get(),TW2Result.get(),\
		TW3Result.get(),TW4Result.get(),\
		TW5Result.get(),TW6Result.get(),\
		TW7Result.get(),TW8Result.get(),\
		TW9Result.get(),TW10Result.get(),\
		TW11Result.get(),TW12Result.get(),\
		TW13Result.get(),TW14Result.get(),\
		TW15Result.get(),TW16Result.get(),\
		TR1Result.get(),TR2Result.get(),\
		TR3Result.get(),TR4Result.get(),\
		TR5Result.get(),TR6Result.get(),\
		TR7Result.get(),TR8Result.get(),\
		TR9Result.get(),TR10Result.get(),\
		TR11Result.get(),TR12Result.get(),\
		TR13Result.get(),TR14Result.get(),\
		TR15Result.get(),TR16Result.get(),\
		TF1Result.get(),TF2Result.get(),\
		TF3Result.get(),TF4Result.get(),\
		TF5Result.get(),TF6Result.get(),\
		TF7Result.get(),TF8Result.get(),\
		TF9Result.get(),TF10Result.get(),\
		TF11Result.get(),TF12Result.get(),\
		TF13Result.get(),TF14Result.get(),\
		TF15Result.get(),TF16Result.get(),\
		teamActCombo.get(), teamCombo.get()))

	conn.commit()

	cur.close()
	conn.close()

	statusBar.configure(text="Saved Schedule for " + teamActCombo.get() + " Team  " + teamCombo.get())

#==================================
#=           New File
#==================================

def newFile():
	filetypes = (
		('DB Files', '*.db'),
		('All files', '*.*')
		)

	filename = fd.asksaveasfilename(
		title='Create a new file',
		initialdir='./',
		defaultextension='.db',
		filetypes=filetypes)

	#Skip steps if canceled
	if (len(filename)) == 0:
		return
	
	createDB(filename)

	global dbName
	dbName=filename

	loadTabs()
	global ready 
	ready=True
	statusBar.configure(text="Created " + filename)

#==================================
#=           Open File
#==================================

def openFile():
	filetypes = (
		('DB Files', '*.db'),
		('All files', '*.*')
		)

	filename = fd.askopenfilename(
		title='Open a file',
		initialdir='./',
		filetypes=filetypes)


	if len(filename) == 0:
		return

	global dbName
	dbName=filename

	loadTabs()
	global ready
	ready=True
	statusBar.configure(text="Opened " + filename)

#==================================
#=       Fetch Coaches
#==================================
def fetchCoaches():

	if len(dbName) == 0 or len(actCombo.get()) == 0:
		output = {}
		return output

	conn = sql.connect(dbName)
	cur = conn.cursor()

	#Pull last 30 days of resident results
	cur.execute("SELECT CoachName FROM Coaches GROUP BY CoachName")

	rows = cur.fetchall()

	cur.close()
	conn.close()

	return rows

#==================================
#=       Fetch Acts
#==================================
def fetchActs():

	if len(dbName) == 0:
		output = {}
		return output

	conn = sql.connect(dbName)
	cur = conn.cursor()

	#Pull Act names
	cur.execute("SELECT ActName FROM Act GROUP BY ActName")
	rows = cur.fetchall()

	cur.close()
	conn.close()
	output = []
	for row in rows:
		output.append(row[0])

	return output

#==================================
#=       Fetch Perf
#==================================
def fetchPerfs():

	if len(dbName) == 0:
		output = {}
		return output

	conn = sql.connect(dbName)
	cur = conn.cursor()

	#Pull Performer names
	cur.execute("SELECT PerfName FROM Performer GROUP BY PerfName")

	rows = cur.fetchall()
	output = []
	cur.close()
	conn.close()
	for row in rows:
		output.append(row[0])

	return output
#==================================
#=       Fetch Teams
#==================================
def fetchTeams():

	if len(dbName) == 0:
		output = {}
		return output

	conn = sql.connect(dbName)
	cur = conn.cursor()

	#Pull Act names
	cur.execute("SELECT TeamName FROM Team WHERE ActName = ? GROUP BY TeamName",(teamActCombo.get(),))
	rows = cur.fetchall()

	cur.close()
	conn.close()
	output = []
	for row in rows:
		output.append(row[0])

	return output

#==================================
#=       Fetch S Teams
#==================================
def fetchSTeams(combobox):

	if len(dbName) == 0:
		output = {}
		return output

	conn = sql.connect(dbName)
	cur = conn.cursor()

	#Pull Act names
	cur.execute("SELECT TeamName FROM Team WHERE ActName = ? GROUP BY TeamName",(combobox.get(),))
	rows = cur.fetchall()

	cur.close()
	conn.close()
	output = []
	for row in rows:
		output.append(row[0])

	return output

#==================================
#=       Clear Perf Combos
#==================================
def clearPerfCombos():
	perfAct1Combo.set('')
	perfAct2Combo.set('')
	perfAct3Combo.set('')
	perfAct4Combo.set('')
	perfAct5Combo.set('')
	perfTeam1Combo.set('')
	perfTeam2Combo.set('')
	perfTeam3Combo.set('')
	perfTeam4Combo.set('')
	perfTeam5Combo.set('')

#==================================
#=       Clear Perf Combos
#==================================
def clearScheduleCombos():
	M1Check.deselect()
	M2Check.deselect()
	M3Check.deselect()
	M4Check.deselect()
	M5Check.deselect()
	M6Check.deselect()
	M7Check.deselect()
	M8Check.deselect()
	M9Check.deselect()
	M10Check.deselect()
	M11Check.deselect()
	M12Check.deselect()
	M13Check.deselect()
	M14Check.deselect()
	M15Check.deselect()
	M16Check.deselect()
	T1Check.deselect()
	T2Check.deselect()
	T3Check.deselect()
	T4Check.deselect()
	T5Check.deselect()
	T6Check.deselect()
	T7Check.deselect()
	T8Check.deselect()
	T9Check.deselect()
	T10Check.deselect()
	T11Check.deselect()
	T12Check.deselect()
	T13Check.deselect()
	T14Check.deselect()
	T15Check.deselect()
	T16Check.deselect()
	W1Check.deselect()
	W2Check.deselect()
	W3Check.deselect()
	W4Check.deselect()
	W5Check.deselect()
	W6Check.deselect()
	W7Check.deselect()
	W8Check.deselect()
	W9Check.deselect()
	W10Check.deselect()
	W11Check.deselect()
	W12Check.deselect()
	W13Check.deselect()
	W14Check.deselect()
	W15Check.deselect()
	W16Check.deselect()
	R1Check.deselect()
	R2Check.deselect()
	R3Check.deselect()
	R4Check.deselect()
	R5Check.deselect()
	R6Check.deselect()
	R7Check.deselect()
	R8Check.deselect()
	R9Check.deselect()
	R10Check.deselect()
	R11Check.deselect()
	R12Check.deselect()
	R13Check.deselect()
	R14Check.deselect()
	R15Check.deselect()
	R16Check.deselect()
	F1Check.deselect()
	F2Check.deselect()
	F3Check.deselect()
	F4Check.deselect()
	F5Check.deselect()
	F6Check.deselect()
	F7Check.deselect()
	F8Check.deselect()
	F9Check.deselect()
	F10Check.deselect()
	F11Check.deselect()
	F12Check.deselect()
	F13Check.deselect()
	F14Check.deselect()
	F15Check.deselect()
	F16Check.deselect()

#==================================
#=           Update Window
#==================================
def loadTabs():
	print("LT")

dbName = ""
ready = False


#Make window
window = Tk()
#Set Size
window.geometry('800x660')

#Add Title
window.title("Circus Practice Scheduler")

#Create menubar
menubar = Menu(window)

#==================================
#=          Status Bar
#==================================
statusBar=Label(window, text="Create a new file or Load one to start", bd=1, relief=SUNKEN, anchor=E)
statusBar.pack(side=BOTTOM, fill=X) 



#==================================
#=           File Menu
#==================================
	
#File Menu
file = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='File', menu = file)
file.add_command(label ='New File', command = newFile)
file.add_command(label ='Open...', command = openFile)
file.add_separator()
file.add_command(label ='Exit', command = window.destroy)

#Generate Menu
gen = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Generate', menu = gen)
gen.add_command(label ='1 - Generate Team Schedules', command = genTeams)
gen.add_separator()
gen.add_command(label ='2a - Generate Full Schedules', command = None)
gen.add_separator()
gen.add_command(label ='2b - Generate Partial Schedules', command = None)

#Display Menu
window.config(menu = menubar)

#==================================
#=           Tabs
#==================================

notebook = ttk.Notebook(window)
#actFrame
actFrame = ttk.Frame(notebook)
notebook.add(actFrame, text='Acts')
#perfFrame
perfFrame = ttk.Frame(notebook)
notebook.add(perfFrame, text='Performers')
#teamFrame
teamFrame = ttk.Frame(notebook)
notebook.add(teamFrame, text='Teams')
notebook.pack(expand=1, fill="both")
#Tab Name Labels
ttk.Label(actFrame, text=" ").grid(column=0, row=0, padx=10, pady=10)
ttk.Label(perfFrame, text=" ").grid(column=0, row=0, padx=10, pady=10)


#==================================
#=           Act Frame
#==================================

#Act text
ttk.Label(actFrame, text="Act Name:").grid(column=0, row=1, padx=10, pady=10)
#Combo Box Act
actCombo = ttk.Combobox(actFrame,postcommand=lambda: actCombo.configure(values=fetchActs()))
actCombo['values'] = fetchActs()
actCombo.grid(column=1,row=1,padx=10,pady=10)
actCombo.bind("<<ComboboxSelected>>", fetchActValues)
#New Act
newActButton = Button(actFrame, text='New Act', command=addNewAct)
newActButton.grid(column=2,row=1,padx=10,pady=10)

#Coach text
ttk.Label(actFrame, text="Coach Name:").grid(column=0, row=3, padx=10, pady=10)
#Combo Box Coach
coachCombo = ttk.Combobox(actFrame,postcommand=lambda: coachCombo.configure(values=fetchCoaches()))
coachCombo['values'] = fetchCoaches()
coachCombo.grid(column=1,row=3,padx=10,pady=10)
#New Act
newCoachButton = Button(actFrame, text='New Coach', command=addNewCoach)
newCoachButton.grid(column=2,row=3,padx=10,pady=10)

#HourLong Practice
hourResult = IntVar()
hourCheck = Checkbutton(actFrame,text="Hour long practice?",variable=hourResult)
hourCheck.grid(column=4,row=3,padx=10,pady=10)

#Spacer text
ttk.Label(actFrame, text="Select Practice Areas").grid(column=2, row=4, padx=10, pady=10)

#Image Display
img = PhotoImage(file="location.gif")
ttk.Label(actFrame, image=img).grid(column=1, columnspan=4, row=5, padx=10, pady=10)

#Hut CheckBox
hutResult = IntVar()
hutCheck = Checkbutton(actFrame,text="Hut",variable=hutResult)
hutCheck.grid(column=1,row=6,padx=10,pady=10)

#Ring3 CheckBox
ring3Result = IntVar()
ring3Check = Checkbutton(actFrame,text="Ring 3",variable=ring3Result)
ring3Check.grid(column=2,row=6,padx=10,pady=10)

#Ring2 CheckBox
ring2Result = IntVar()
ring2Check = Checkbutton(actFrame,text="Ring 2",variable=ring2Result)
ring2Check.grid(column=3,row=6,padx=10,pady=10)

#Ring1 CheckBox
ring1Result = IntVar()
ring1Check = Checkbutton(actFrame,text="Ring 1",variable=ring1Result)
ring1Check.grid(column=4,row=6,padx=10,pady=10)

#Save Act
actSaveButton = Button(actFrame, text='Save Act', command=actSave)
actSaveButton.grid(column=4,row=7,padx=10,pady=10)


#==================================
#=           Performer Frame
#==================================

#Performer text
ttk.Label(perfFrame, text="Performer Name:").grid(column=0, row=0, padx=5, pady=0)
#Combo Box Act
perfCombo = ttk.Combobox(perfFrame,postcommand=lambda: perfCombo.configure(values=fetchPerfs()))
perfCombo['values'] = fetchPerfs()
perfCombo.grid(column=1,row=0,padx=5,pady=0)
perfCombo.bind("<<ComboboxSelected>>", fetchPerfValues)
#New Act
newPerfButton = Button(perfFrame, text='New Performer', command=addNewPerf)
newPerfButton.grid(column=2,row=0,padx=5,pady=0)
#Edit Act
editPerfButton = Button(perfFrame, text='Change Name', command=editPerf)
editPerfButton.grid(column=3,row=0,padx=5,pady=0)
#Remove Act
removePerfButton = Button(perfFrame, text='Remove Performer', command=removePerf)
removePerfButton.grid(column=4,row=0,padx=5,pady=0)

#Performer Act  text
ttk.Label(perfFrame, text="Act 1").grid(column=0, row=1, padx=5, pady=3)
ttk.Label(perfFrame, text="Act 2").grid(column=1, row=1, padx=5, pady=3)
ttk.Label(perfFrame, text="Act 3").grid(column=2, row=1, padx=5, pady=3)
ttk.Label(perfFrame, text="Act 4").grid(column=3, row=1, padx=5, pady=3)
ttk.Label(perfFrame, text="Act 5").grid(column=4, row=1, padx=5, pady=3)

#Performer Act Comboboxes
perfAct1Combo = ttk.Combobox(perfFrame,postcommand=lambda: perfAct1Combo.configure(values=fetchActs()))
perfAct1Combo['values'] = fetchActs()
perfAct1Combo['width'] = 15
perfAct1Combo.grid(column=0,row=2,padx=5,pady=3)
perfAct2Combo = ttk.Combobox(perfFrame,postcommand=lambda: perfAct2Combo.configure(values=fetchActs()))
perfAct2Combo['values'] = fetchActs()
perfAct2Combo['width'] = 15
perfAct2Combo.grid(column=1,row=2,padx=5,pady=3)
perfAct3Combo = ttk.Combobox(perfFrame,postcommand=lambda: perfAct3Combo.configure(values=fetchActs()))
perfAct3Combo['values'] = fetchActs()
perfAct3Combo['width'] = 15
perfAct3Combo.grid(column=2,row=2,padx=5,pady=3)
perfAct4Combo = ttk.Combobox(perfFrame,postcommand=lambda: perfAct4Combo.configure(values=fetchActs()))
perfAct4Combo['values'] = fetchActs()
perfAct4Combo['width'] = 15
perfAct4Combo.grid(column=3,row=2,padx=5,pady=3)
perfAct5Combo = ttk.Combobox(perfFrame,postcommand=lambda: perfAct5Combo.configure(values=fetchActs()))
perfAct5Combo['values'] = fetchActs()
perfAct5Combo['width'] = 15
perfAct5Combo.grid(column=4,row=2,padx=5,pady=5)

#Performer Team  text
ttk.Label(perfFrame, text="Team 1").grid(column=0, row=3, padx=10, pady=2)
ttk.Label(perfFrame, text="Team 2").grid(column=1, row=3, padx=10, pady=2)
ttk.Label(perfFrame, text="Team 3").grid(column=2, row=3, padx=10, pady=2)
ttk.Label(perfFrame, text="Team 4").grid(column=3, row=3, padx=10, pady=2)
ttk.Label(perfFrame, text="Team 5").grid(column=4, row=3, padx=10, pady=2)

#Performer Act Comboboxes
perfTeam1Combo = ttk.Combobox(perfFrame,postcommand=lambda: perfTeam1Combo.configure(values=fetchSTeams(perfAct1Combo)))
perfTeam1Combo['values'] = fetchSTeams(perfAct1Combo)
perfTeam1Combo['width'] = 15
perfTeam1Combo.grid(column=0,row=4,padx=5,pady=3)
perfTeam2Combo = ttk.Combobox(perfFrame,postcommand=lambda: perfTeam2Combo.configure(values=fetchSTeams(perfAct2Combo)))
perfTeam2Combo['values'] = fetchSTeams(perfAct2Combo)
perfTeam2Combo['width'] = 15
perfTeam2Combo.grid(column=1,row=4,padx=5,pady=3)
perfTeam3Combo = ttk.Combobox(perfFrame,postcommand=lambda: perfTeam3Combo.configure(values=fetchSTeams(perfAct3Combo)))
perfTeam3Combo['values'] = fetchSTeams(perfAct3Combo)
perfTeam3Combo['width'] = 15
perfTeam3Combo.grid(column=2,row=4,padx=5,pady=3)
perfTeam4Combo = ttk.Combobox(perfFrame,postcommand=lambda: perfTeam4Combo.configure(values=fetchSTeams(perfAct4Combo)))
perfTeam4Combo['values'] = fetchSTeams(perfAct4Combo)
perfTeam4Combo['width'] = 15
perfTeam4Combo.grid(column=3,row=4,padx=5,pady=3)
perfTeam5Combo = ttk.Combobox(perfFrame,postcommand=lambda: perfTeam5Combo.configure(values=fetchSTeams(perfAct5Combo)))
perfTeam5Combo['values'] = fetchSTeams(perfAct5Combo)
perfTeam5Combo['width'] = 15
perfTeam5Combo.grid(column=4,row=4,padx=5,pady=3)

#Clear Performer Act/Team
clearPerfButton = Button(perfFrame, text='Clear Acts', command=clearPerfCombos)
clearPerfButton.grid(column=0,row=5,padx=5,pady=5)
#Clear Performer Act/Team
clearPerfButton = Button(perfFrame, text='Clear Schedule', command=clearScheduleCombos)
clearPerfButton.grid(column=1,row=5,padx=5,pady=5)
#Clear Performer Act/Team
clearPerfButton = Button(perfFrame, text='Save Schedule', command=savePerf)
clearPerfButton.grid(column=4,row=5,padx=5,pady=5)

#Schedule Textboxes
ttk.Label(perfFrame, text="Monday").grid(column=0, row=7, padx=10, pady=5)
ttk.Label(perfFrame, text="Tuesday").grid(column=1, row=7, padx=10, pady=5)
ttk.Label(perfFrame, text="Wednesday").grid(column=2, row=7, padx=10, pady=5)
ttk.Label(perfFrame, text="Thursday").grid(column=3, row=7, padx=10, pady=5)
ttk.Label(perfFrame, text="Friday").grid(column=4, row=7, padx=10, pady=5)

#Schedule Textbox
ttk.Label(perfFrame, text="Check for Avaliable:").grid(column=2, row=6, padx=10, pady=5)


#Monday CheckBoxes
M1Result = IntVar()
M1Check = Checkbutton(perfFrame,text="  9:00",variable=M1Result,justify=LEFT)
M1Check.grid(column=0,row=8,padx=5,pady=0)
M2Result = IntVar()
M2Check = Checkbutton(perfFrame,text="  9:30",variable=M2Result,justify=LEFT)
M2Check.grid(column=0,row=9,padx=5,pady=0)
M3Result = IntVar()
M3Check = Checkbutton(perfFrame,text="10:00",variable=M3Result,justify=LEFT)
M3Check.grid(column=0,row=10,padx=5,pady=0)
M4Result = IntVar()
M4Check = Checkbutton(perfFrame,text="10:30",variable=M4Result,justify=LEFT)
M4Check.grid(column=0,row=11,padx=5,pady=0)
M5Result = IntVar()
M5Check = Checkbutton(perfFrame,text="11:00",variable=M5Result,justify=LEFT)
M5Check.grid(column=0,row=12,padx=5,pady=0)
M6Result = IntVar()
M6Check = Checkbutton(perfFrame,text="11:30",variable=M6Result,justify=LEFT)
M6Check.grid(column=0,row=13,padx=5,pady=0)
M7Result = IntVar()
M7Check = Checkbutton(perfFrame,text="  1:00",variable=M7Result,justify=LEFT)
M7Check.grid(column=0,row=14,padx=5,pady=0)
M8Result = IntVar()
M8Check = Checkbutton(perfFrame,text="  1:30",variable=M8Result,justify=LEFT)
M8Check.grid(column=0,row=15,padx=5,pady=0)
M9Result = IntVar()
M9Check = Checkbutton(perfFrame,text="  2:00",variable=M9Result,justify=LEFT)
M9Check.grid(column=0,row=16,padx=5,pady=0)
M10Result = IntVar()
M10Check = Checkbutton(perfFrame,text="  2:30",variable=M10Result,justify=LEFT)
M10Check.grid(column=0,row=17,padx=5,pady=0)
M11Result = IntVar()
M11Check = Checkbutton(perfFrame,text="  3:00",variable=M11Result,justify=LEFT)
M11Check.grid(column=0,row=18,padx=5,pady=0)
M12Result = IntVar()
M12Check = Checkbutton(perfFrame,text="  3:30",variable=M12Result,justify=LEFT)
M12Check.grid(column=0,row=19,padx=5,pady=0)
M13Result = IntVar()
M13Check = Checkbutton(perfFrame,text="  4:00",variable=M13Result,justify=LEFT)
M13Check.grid(column=0,row=20,padx=5,pady=0)
M14Result = IntVar()
M14Check = Checkbutton(perfFrame,text="  4:30",variable=M14Result,justify=LEFT)
M14Check.grid(column=0,row=21,padx=5,pady=0)
M15Result = IntVar()
M15Check = Checkbutton(perfFrame,text="  5:00",variable=M15Result,justify=LEFT)
M15Check.grid(column=0,row=22,padx=5,pady=0)
M16Result = IntVar()
M16Check = Checkbutton(perfFrame,text="  5:30",variable=M16Result,justify=LEFT)
M16Check.grid(column=0,row=23,padx=5,pady=0)

#Tuesday CheckBoxes
T1Result = IntVar()
T1Check = Checkbutton(perfFrame,text="  9:00",variable=T1Result,justify=LEFT)
T1Check.grid(column=1,row=8,padx=5,pady=0)
T2Result = IntVar()
T2Check = Checkbutton(perfFrame,text="  9:30",variable=T2Result,justify=LEFT)
T2Check.grid(column=1,row=9,padx=5,pady=0)
T3Result = IntVar()
T3Check = Checkbutton(perfFrame,text="10:00",variable=T3Result,justify=LEFT)
T3Check.grid(column=1,row=10,padx=5,pady=0)
T4Result = IntVar()
T4Check = Checkbutton(perfFrame,text="10:30",variable=T4Result,justify=LEFT)
T4Check.grid(column=1,row=11,padx=5,pady=0)
T5Result = IntVar()
T5Check = Checkbutton(perfFrame,text="11:00",variable=T5Result,justify=LEFT)
T5Check.grid(column=1,row=12,padx=5,pady=0)
T6Result = IntVar()
T6Check = Checkbutton(perfFrame,text="11:30",variable=T6Result,justify=LEFT)
T6Check.grid(column=1,row=13,padx=5,pady=0)
T7Result = IntVar()
T7Check = Checkbutton(perfFrame,text="  1:00",variable=T7Result,justify=LEFT)
T7Check.grid(column=1,row=14,padx=5,pady=0)
T8Result = IntVar()
T8Check = Checkbutton(perfFrame,text="  1:30",variable=T8Result,justify=LEFT)
T8Check.grid(column=1,row=15,padx=5,pady=0)
T9Result = IntVar()
T9Check = Checkbutton(perfFrame,text="  2:00",variable=T9Result,justify=LEFT)
T9Check.grid(column=1,row=16,padx=5,pady=0)
T10Result = IntVar()
T10Check = Checkbutton(perfFrame,text="  2:30",variable=T10Result,justify=LEFT)
T10Check.grid(column=1,row=17,padx=5,pady=0)
T11Result = IntVar()
T11Check = Checkbutton(perfFrame,text="  3:00",variable=T11Result,justify=LEFT)
T11Check.grid(column=1,row=18,padx=5,pady=0)
T12Result = IntVar()
T12Check = Checkbutton(perfFrame,text="  3:30",variable=T12Result,justify=LEFT)
T12Check.grid(column=1,row=19,padx=5,pady=0)
T13Result = IntVar()
T13Check = Checkbutton(perfFrame,text="  4:00",variable=T13Result,justify=LEFT)
T13Check.grid(column=1,row=20,padx=5,pady=0)
T14Result = IntVar()
T14Check = Checkbutton(perfFrame,text="  4:30",variable=T14Result,justify=LEFT)
T14Check.grid(column=1,row=21,padx=5,pady=0)
T15Result = IntVar()
T15Check = Checkbutton(perfFrame,text="  5:00",variable=T15Result,justify=LEFT)
T15Check.grid(column=1,row=22,padx=5,pady=0)
T16Result = IntVar()
T16Check = Checkbutton(perfFrame,text="  5:30",variable=T16Result,justify=LEFT)
T16Check.grid(column=1,row=23,padx=5,pady=0)

#Wednesday CheckBoxes
W1Result = IntVar()
W1Check = Checkbutton(perfFrame,text="  9:00",variable=W1Result,justify=LEFT)
W1Check.grid(column=2,row=8,padx=5,pady=0)
W2Result = IntVar()
W2Check = Checkbutton(perfFrame,text="  9:30",variable=W2Result,justify=LEFT)
W2Check.grid(column=2,row=9,padx=5,pady=0)
W3Result = IntVar()
W3Check = Checkbutton(perfFrame,text="10:00",variable=W3Result,justify=LEFT)
W3Check.grid(column=2,row=10,padx=5,pady=0)
W4Result = IntVar()
W4Check = Checkbutton(perfFrame,text="10:30",variable=W4Result,justify=LEFT)
W4Check.grid(column=2,row=11,padx=5,pady=0)
W5Result = IntVar()
W5Check = Checkbutton(perfFrame,text="11:00",variable=W5Result,justify=LEFT)
W5Check.grid(column=2,row=12,padx=5,pady=0)
W6Result = IntVar()
W6Check = Checkbutton(perfFrame,text="11:30",variable=W6Result,justify=LEFT)
W6Check.grid(column=2,row=13,padx=5,pady=0)
W7Result = IntVar()
W7Check = Checkbutton(perfFrame,text="  1:00",variable=W7Result,justify=LEFT)
W7Check.grid(column=2,row=14,padx=5,pady=0)
W8Result = IntVar()
W8Check = Checkbutton(perfFrame,text="  1:30",variable=W8Result,justify=LEFT)
W8Check.grid(column=2,row=15,padx=5,pady=0)
W9Result = IntVar()
W9Check = Checkbutton(perfFrame,text="  2:00",variable=W9Result,justify=LEFT)
W9Check.grid(column=2,row=16,padx=5,pady=0)
W10Result = IntVar()
W10Check = Checkbutton(perfFrame,text="  2:30",variable=W10Result,justify=LEFT)
W10Check.grid(column=2,row=17,padx=5,pady=0)
W11Result = IntVar()
W11Check = Checkbutton(perfFrame,text="  3:00",variable=W11Result,justify=LEFT)
W11Check.grid(column=2,row=18,padx=5,pady=0)
W12Result = IntVar()
W12Check = Checkbutton(perfFrame,text="  3:30",variable=W12Result,justify=LEFT)
W12Check.grid(column=2,row=19,padx=5,pady=0)
W13Result = IntVar()
W13Check = Checkbutton(perfFrame,text="  4:00",variable=W13Result,justify=LEFT)
W13Check.grid(column=2,row=20,padx=5,pady=0)
W14Result = IntVar()
W14Check = Checkbutton(perfFrame,text="  4:30",variable=W14Result,justify=LEFT)
W14Check.grid(column=2,row=21,padx=5,pady=0)
W15Result = IntVar()
W15Check = Checkbutton(perfFrame,text="  5:00",variable=W15Result,justify=LEFT)
W15Check.grid(column=2,row=22,padx=5,pady=0)
W16Result = IntVar()
W16Check = Checkbutton(perfFrame,text="  5:30",variable=W16Result,justify=LEFT)
W16Check.grid(column=2,row=23,padx=5,pady=0)

#Tuesday CheckBoxes
R1Result = IntVar()
R1Check = Checkbutton(perfFrame,text="  9:00",variable=R1Result,justify=LEFT)
R1Check.grid(column=3,row=8,padx=5,pady=0)
R2Result = IntVar()
R2Check = Checkbutton(perfFrame,text="  9:30",variable=R2Result,justify=LEFT)
R2Check.grid(column=3,row=9,padx=5,pady=0)
R3Result = IntVar()
R3Check = Checkbutton(perfFrame,text="10:00",variable=R3Result,justify=LEFT)
R3Check.grid(column=3,row=10,padx=5,pady=0)
R4Result = IntVar()
R4Check = Checkbutton(perfFrame,text="10:30",variable=R4Result,justify=LEFT)
R4Check.grid(column=3,row=11,padx=5,pady=0)
R5Result = IntVar()
R5Check = Checkbutton(perfFrame,text="11:00",variable=R5Result,justify=LEFT)
R5Check.grid(column=3,row=12,padx=5,pady=0)
R6Result = IntVar()
R6Check = Checkbutton(perfFrame,text="11:30",variable=R6Result,justify=LEFT)
R6Check.grid(column=3,row=13,padx=5,pady=0)
R7Result = IntVar()
R7Check = Checkbutton(perfFrame,text="  1:00",variable=R7Result,justify=LEFT)
R7Check.grid(column=3,row=14,padx=5,pady=0)
R8Result = IntVar()
R8Check = Checkbutton(perfFrame,text="  1:30",variable=R8Result,justify=LEFT)
R8Check.grid(column=3,row=15,padx=5,pady=0)
R9Result = IntVar()
R9Check = Checkbutton(perfFrame,text="  2:00",variable=R9Result,justify=LEFT)
R9Check.grid(column=3,row=16,padx=5,pady=0)
R10Result = IntVar()
R10Check = Checkbutton(perfFrame,text="  2:30",variable=R10Result,justify=LEFT)
R10Check.grid(column=3,row=17,padx=5,pady=0)
R11Result = IntVar()
R11Check = Checkbutton(perfFrame,text="  3:00",variable=R11Result,justify=LEFT)
R11Check.grid(column=3,row=18,padx=5,pady=0)
R12Result = IntVar()
R12Check = Checkbutton(perfFrame,text="  3:30",variable=R12Result,justify=LEFT)
R12Check.grid(column=3,row=19,padx=5,pady=0)
R13Result = IntVar()
R13Check = Checkbutton(perfFrame,text="  4:00",variable=R13Result,justify=LEFT)
R13Check.grid(column=3,row=20,padx=5,pady=0)
R14Result = IntVar()
R14Check = Checkbutton(perfFrame,text="  4:30",variable=R14Result,justify=LEFT)
R14Check.grid(column=3,row=21,padx=5,pady=0)
R15Result = IntVar()
R15Check = Checkbutton(perfFrame,text="  5:00",variable=R15Result,justify=LEFT)
R15Check.grid(column=3,row=22,padx=5,pady=0)
R16Result = IntVar()
R16Check = Checkbutton(perfFrame,text="  5:30",variable=R16Result,justify=LEFT)
R16Check.grid(column=3,row=23,padx=5,pady=0)

#Friday CheckBoxes
F1Result = IntVar()
F1Check = Checkbutton(perfFrame,text="  9:00",variable=F1Result,justify=LEFT)
F1Check.grid(column=4,row=8,padx=5,pady=0)
F2Result = IntVar()
F2Check = Checkbutton(perfFrame,text="  9:30",variable=F2Result,justify=LEFT)
F2Check.grid(column=4,row=9,padx=5,pady=0)
F3Result = IntVar()
F3Check = Checkbutton(perfFrame,text="10:00",variable=F3Result,justify=LEFT)
F3Check.grid(column=4,row=10,padx=5,pady=0)
F4Result = IntVar()
F4Check = Checkbutton(perfFrame,text="10:30",variable=F4Result,justify=LEFT)
F4Check.grid(column=4,row=11,padx=5,pady=0)
F5Result = IntVar()
F5Check = Checkbutton(perfFrame,text="11:00",variable=F5Result,justify=LEFT)
F5Check.grid(column=4,row=12,padx=5,pady=0)
F6Result = IntVar()
F6Check = Checkbutton(perfFrame,text="11:30",variable=F6Result,justify=LEFT)
F6Check.grid(column=4,row=13,padx=5,pady=0)
F7Result = IntVar()
F7Check = Checkbutton(perfFrame,text="  1:00",variable=F7Result,justify=LEFT)
F7Check.grid(column=4,row=14,padx=5,pady=0)
F8Result = IntVar()
F8Check = Checkbutton(perfFrame,text="  1:30",variable=F8Result,justify=LEFT)
F8Check.grid(column=4,row=15,padx=5,pady=0)
F9Result = IntVar()
F9Check = Checkbutton(perfFrame,text="  2:00",variable=F9Result,justify=LEFT)
F9Check.grid(column=4,row=16,padx=5,pady=0)
F10Result = IntVar()
F10Check = Checkbutton(perfFrame,text="  2:30",variable=F10Result,justify=LEFT)
F10Check.grid(column=4,row=17,padx=5,pady=0)
F11Result = IntVar()
F11Check = Checkbutton(perfFrame,text="  3:00",variable=F11Result,justify=LEFT)
F11Check.grid(column=4,row=18,padx=5,pady=0)
F12Result = IntVar()
F12Check = Checkbutton(perfFrame,text="  3:30",variable=F12Result,justify=LEFT)
F12Check.grid(column=4,row=19,padx=5,pady=0)
F13Result = IntVar()
F13Check = Checkbutton(perfFrame,text="  4:00",variable=F13Result,justify=LEFT)
F13Check.grid(column=4,row=20,padx=5,pady=0)
F14Result = IntVar()
F14Check = Checkbutton(perfFrame,text="  4:30",variable=F14Result,justify=LEFT)
F14Check.grid(column=4,row=21,padx=5,pady=0)
F15Result = IntVar()
F15Check = Checkbutton(perfFrame,text="  5:00",variable=F15Result,justify=LEFT)
F15Check.grid(column=4,row=22,padx=5,pady=0)
F16Result = IntVar()
F16Check = Checkbutton(perfFrame,text="  5:30",variable=F16Result,justify=LEFT)
F16Check.grid(column=4,row=23,padx=5,pady=0)

#==================================
#=           Team Frame
#==================================

#Team Act text
ttk.Label(teamFrame, text="Act Name:").grid(column=0, row=1, padx=5, pady=10)
#Combo Box Act
teamActCombo = ttk.Combobox(teamFrame,postcommand=lambda: teamActCombo.configure(values=fetchActs()))
teamActCombo['values'] = fetchActs()
teamActCombo.grid(column=1,row=1,padx=5,pady=10)

#Team Num text
ttk.Label(teamFrame, text="Team Num:").grid(column=2, row=1, padx=5, pady=10)
#Combo Box Act
teamCombo = ttk.Combobox(teamFrame,postcommand=lambda: teamCombo.configure(values=fetchTeams()))
teamCombo['values'] = fetchTeams()
teamCombo['width'] = 3
teamCombo.grid(column=3,row=1,padx=5,pady=10)
teamCombo.bind("<<ComboboxSelected>>", fetchTeamValues)
#New Team
newTeamButton = Button(teamFrame, text='New Team', command=addNewTeam)
newTeamButton.grid(column=4,row=1,padx=5,pady=10)
#Remove Team
removeTeamButton = Button(teamFrame, text='Remove Team', command=removeTeam)
removeTeamButton.grid(column=5,row=1,padx=5,pady=10)

#Team Num text
ttk.Label(teamFrame, text="Team Members:").grid(column=0, row=2, padx=5, pady=10)
teamMemLabel = Label(teamFrame, text=" ")
teamMemLabel.grid(column=1, columnspan=3, row=2, rowspan=3, padx=5, pady=10)

#save Team Schedule
saveTeamButton = Button(teamFrame, text='Save Overwrites', command=saveTeamSchedule)
saveTeamButton.grid(column=5,row=2,padx=5,pady=10)


#Generate reminder
ttk.Label(teamFrame, text="Remember to Generate Team Schedules").grid(column=2, columnspan=3,row=5, padx=10, pady=5)


#Schedule Textboxes
ttk.Label(teamFrame, text="Monday").grid(column=0, row=7, padx=10, pady=5)
ttk.Label(teamFrame, text="Tuesday").grid(column=1, row=7, padx=10, pady=5)
ttk.Label(teamFrame, text="Wednesday").grid(column=2, row=7, padx=10, pady=5)
ttk.Label(teamFrame, text="Thursday").grid(column=4, row=7, padx=10, pady=5)
ttk.Label(teamFrame, text="Friday").grid(column=5, row=7, padx=10, pady=5)

#Schedule Textbox
ttk.Label(teamFrame, text="Overwrite Team Avalability:").grid(column=2, columnspan = 3,row=6, padx=10, pady=5)


#Monday CheckBoxes
TM1Result = IntVar()
TM1Check = Checkbutton(teamFrame,text="  9:00",variable=TM1Result,justify=LEFT)
TM1Check.grid(column=0,row=8,padx=5,pady=0)
TM2Result = IntVar()
TM2Check = Checkbutton(teamFrame,text="  9:30",variable=TM2Result,justify=LEFT)
TM2Check.grid(column=0,row=9,padx=5,pady=0)
TM3Result = IntVar()
TM3Check = Checkbutton(teamFrame,text="10:00",variable=TM3Result,justify=LEFT)
TM3Check.grid(column=0,row=10,padx=5,pady=0)
TM4Result = IntVar()
TM4Check = Checkbutton(teamFrame,text="10:30",variable=TM4Result,justify=LEFT)
TM4Check.grid(column=0,row=11,padx=5,pady=0)
TM5Result = IntVar()
TM5Check = Checkbutton(teamFrame,text="11:00",variable=TM5Result,justify=LEFT)
TM5Check.grid(column=0,row=12,padx=5,pady=0)
TM6Result = IntVar()
TM6Check = Checkbutton(teamFrame,text="11:30",variable=TM6Result,justify=LEFT)
TM6Check.grid(column=0,row=13,padx=5,pady=0)
TM7Result = IntVar()
TM7Check = Checkbutton(teamFrame,text="  1:00",variable=TM7Result,justify=LEFT)
TM7Check.grid(column=0,row=14,padx=5,pady=0)
TM8Result = IntVar()
TM8Check = Checkbutton(teamFrame,text="  1:30",variable=TM8Result,justify=LEFT)
TM8Check.grid(column=0,row=15,padx=5,pady=0)
TM9Result = IntVar()
TM9Check = Checkbutton(teamFrame,text="  2:00",variable=TM9Result,justify=LEFT)
TM9Check.grid(column=0,row=16,padx=5,pady=0)
TM10Result = IntVar()
TM10Check = Checkbutton(teamFrame,text="  2:30",variable=TM10Result,justify=LEFT)
TM10Check.grid(column=0,row=17,padx=5,pady=0)
TM11Result = IntVar()
TM11Check = Checkbutton(teamFrame,text="  3:00",variable=TM11Result,justify=LEFT)
TM11Check.grid(column=0,row=18,padx=5,pady=0)
TM12Result = IntVar()
TM12Check = Checkbutton(teamFrame,text="  3:30",variable=TM12Result,justify=LEFT)
TM12Check.grid(column=0,row=19,padx=5,pady=0)
TM13Result = IntVar()
TM13Check = Checkbutton(teamFrame,text="  4:00",variable=TM13Result,justify=LEFT)
TM13Check.grid(column=0,row=20,padx=5,pady=0)
TM14Result = IntVar()
TM14Check = Checkbutton(teamFrame,text="  4:30",variable=TM14Result,justify=LEFT)
TM14Check.grid(column=0,row=21,padx=5,pady=0)
TM15Result = IntVar()
TM15Check = Checkbutton(teamFrame,text="  5:00",variable=TM15Result,justify=LEFT)
TM15Check.grid(column=0,row=22,padx=5,pady=0)
TM16Result = IntVar()
TM16Check = Checkbutton(teamFrame,text="  5:30",variable=TM16Result,justify=LEFT)
TM16Check.grid(column=0,row=23,padx=5,pady=0)

#Tuesday CheckBoxes
TT1Result = IntVar()
TT1Check = Checkbutton(teamFrame,text="  9:00",variable=TT1Result,justify=LEFT)
TT1Check.grid(column=1,row=8,padx=5,pady=0)
TT2Result = IntVar()
TT2Check = Checkbutton(teamFrame,text="  9:30",variable=TT2Result,justify=LEFT)
TT2Check.grid(column=1,row=9,padx=5,pady=0)
TT3Result = IntVar()
TT3Check = Checkbutton(teamFrame,text="10:00",variable=TT3Result,justify=LEFT)
TT3Check.grid(column=1,row=10,padx=5,pady=0)
TT4Result = IntVar()
TT4Check = Checkbutton(teamFrame,text="10:30",variable=TT4Result,justify=LEFT)
TT4Check.grid(column=1,row=11,padx=5,pady=0)
TT5Result = IntVar()
TT5Check = Checkbutton(teamFrame,text="11:00",variable=TT5Result,justify=LEFT)
TT5Check.grid(column=1,row=12,padx=5,pady=0)
TT6Result = IntVar()
TT6Check = Checkbutton(teamFrame,text="11:30",variable=TT6Result,justify=LEFT)
TT6Check.grid(column=1,row=13,padx=5,pady=0)
TT7Result = IntVar()
TT7Check = Checkbutton(teamFrame,text="  1:00",variable=TT7Result,justify=LEFT)
TT7Check.grid(column=1,row=14,padx=5,pady=0)
TT8Result = IntVar()
TT8Check = Checkbutton(teamFrame,text="  1:30",variable=TT8Result,justify=LEFT)
TT8Check.grid(column=1,row=15,padx=5,pady=0)
TT9Result = IntVar()
TT9Check = Checkbutton(teamFrame,text="  2:00",variable=TT9Result,justify=LEFT)
TT9Check.grid(column=1,row=16,padx=5,pady=0)
TT10Result = IntVar()
TT10Check = Checkbutton(teamFrame,text="  2:30",variable=TT10Result,justify=LEFT)
TT10Check.grid(column=1,row=17,padx=5,pady=0)
TT11Result = IntVar()
TT11Check = Checkbutton(teamFrame,text="  3:00",variable=TT11Result,justify=LEFT)
TT11Check.grid(column=1,row=18,padx=5,pady=0)
TT12Result = IntVar()
TT12Check = Checkbutton(teamFrame,text="  3:30",variable=TT12Result,justify=LEFT)
TT12Check.grid(column=1,row=19,padx=5,pady=0)
TT13Result = IntVar()
TT13Check = Checkbutton(teamFrame,text="  4:00",variable=TT13Result,justify=LEFT)
TT13Check.grid(column=1,row=20,padx=5,pady=0)
TT14Result = IntVar()
TT14Check = Checkbutton(teamFrame,text="  4:30",variable=TT14Result,justify=LEFT)
TT14Check.grid(column=1,row=21,padx=5,pady=0)
TT15Result = IntVar()
TT15Check = Checkbutton(teamFrame,text="  5:00",variable=TT15Result,justify=LEFT)
TT15Check.grid(column=1,row=22,padx=5,pady=0)
TT16Result = IntVar()
TT16Check = Checkbutton(teamFrame,text="  5:30",variable=TT16Result,justify=LEFT)
TT16Check.grid(column=1,row=23,padx=5,pady=0)

#Wednesday CheckBoxes
TW1Result = IntVar()
TW1Check = Checkbutton(teamFrame,text="  9:00",variable=TW1Result,justify=LEFT)
TW1Check.grid(column=2,row=8,padx=5,pady=0)
TW2Result = IntVar()
TW2Check = Checkbutton(teamFrame,text="  9:30",variable=TW2Result,justify=LEFT)
TW2Check.grid(column=2,row=9,padx=5,pady=0)
TW3Result = IntVar()
TW3Check = Checkbutton(teamFrame,text="10:00",variable=TW3Result,justify=LEFT)
TW3Check.grid(column=2,row=10,padx=5,pady=0)
TW4Result = IntVar()
TW4Check = Checkbutton(teamFrame,text="10:30",variable=TW4Result,justify=LEFT)
TW4Check.grid(column=2,row=11,padx=5,pady=0)
TW5Result = IntVar()
TW5Check = Checkbutton(teamFrame,text="11:00",variable=TW5Result,justify=LEFT)
TW5Check.grid(column=2,row=12,padx=5,pady=0)
TW6Result = IntVar()
TW6Check = Checkbutton(teamFrame,text="11:30",variable=TW6Result,justify=LEFT)
TW6Check.grid(column=2,row=13,padx=5,pady=0)
TW7Result = IntVar()
TW7Check = Checkbutton(teamFrame,text="  1:00",variable=TW7Result,justify=LEFT)
TW7Check.grid(column=2,row=14,padx=5,pady=0)
TW8Result = IntVar()
TW8Check = Checkbutton(teamFrame,text="  1:30",variable=TW8Result,justify=LEFT)
TW8Check.grid(column=2,row=15,padx=5,pady=0)
TW9Result = IntVar()
TW9Check = Checkbutton(teamFrame,text="  2:00",variable=TW9Result,justify=LEFT)
TW9Check.grid(column=2,row=16,padx=5,pady=0)
TW10Result = IntVar()
TW10Check = Checkbutton(teamFrame,text="  2:30",variable=TW10Result,justify=LEFT)
TW10Check.grid(column=2,row=17,padx=5,pady=0)
TW11Result = IntVar()
TW11Check = Checkbutton(teamFrame,text="  3:00",variable=TW11Result,justify=LEFT)
TW11Check.grid(column=2,row=18,padx=5,pady=0)
TW12Result = IntVar()
TW12Check = Checkbutton(teamFrame,text="  3:30",variable=TW12Result,justify=LEFT)
TW12Check.grid(column=2,row=19,padx=5,pady=0)
TW13Result = IntVar()
TW13Check = Checkbutton(teamFrame,text="  4:00",variable=TW13Result,justify=LEFT)
TW13Check.grid(column=2,row=20,padx=5,pady=0)
TW14Result = IntVar()
TW14Check = Checkbutton(teamFrame,text="  4:30",variable=TW14Result,justify=LEFT)
TW14Check.grid(column=2,row=21,padx=5,pady=0)
TW15Result = IntVar()
TW15Check = Checkbutton(teamFrame,text="  5:00",variable=TW15Result,justify=LEFT)
TW15Check.grid(column=2,row=22,padx=5,pady=0)
TW16Result = IntVar()
TW16Check = Checkbutton(teamFrame,text="  5:30",variable=TW16Result,justify=LEFT)
TW16Check.grid(column=2,row=23,padx=5,pady=0)

#Thursday CheckBoxes
TR1Result = IntVar()
TR1Check = Checkbutton(teamFrame,text="  9:00",variable=TR1Result,justify=LEFT)
TR1Check.grid(column=4,row=8,padx=5,pady=0)
TR2Result = IntVar()
TR2Check = Checkbutton(teamFrame,text="  9:30",variable=TR2Result,justify=LEFT)
TR2Check.grid(column=4,row=9,padx=5,pady=0)
TR3Result = IntVar()
TR3Check = Checkbutton(teamFrame,text="10:00",variable=TR3Result,justify=LEFT)
TR3Check.grid(column=4,row=10,padx=5,pady=0)
TR4Result = IntVar()
TR4Check = Checkbutton(teamFrame,text="10:30",variable=TR4Result,justify=LEFT)
TR4Check.grid(column=4,row=11,padx=5,pady=0)
TR5Result = IntVar()
TR5Check = Checkbutton(teamFrame,text="11:00",variable=TR5Result,justify=LEFT)
TR5Check.grid(column=4,row=12,padx=5,pady=0)
TR6Result = IntVar()
TR6Check = Checkbutton(teamFrame,text="11:30",variable=TR6Result,justify=LEFT)
TR6Check.grid(column=4,row=13,padx=5,pady=0)
TR7Result = IntVar()
TR7Check = Checkbutton(teamFrame,text="  1:00",variable=TR7Result,justify=LEFT)
TR7Check.grid(column=4,row=14,padx=5,pady=0)
TR8Result = IntVar()
TR8Check = Checkbutton(teamFrame,text="  1:30",variable=TR8Result,justify=LEFT)
TR8Check.grid(column=4,row=15,padx=5,pady=0)
TR9Result = IntVar()
TR9Check = Checkbutton(teamFrame,text="  2:00",variable=TR9Result,justify=LEFT)
TR9Check.grid(column=4,row=16,padx=5,pady=0)
TR10Result = IntVar()
TR10Check = Checkbutton(teamFrame,text="  2:30",variable=TR10Result,justify=LEFT)
TR10Check.grid(column=4,row=17,padx=5,pady=0)
TR11Result = IntVar()
TR11Check = Checkbutton(teamFrame,text="  3:00",variable=TR11Result,justify=LEFT)
TR11Check.grid(column=4,row=18,padx=5,pady=0)
TR12Result = IntVar()
TR12Check = Checkbutton(teamFrame,text="  3:30",variable=TR12Result,justify=LEFT)
TR12Check.grid(column=4,row=19,padx=5,pady=0)
TR13Result = IntVar()
TR13Check = Checkbutton(teamFrame,text="  4:00",variable=TR13Result,justify=LEFT)
TR13Check.grid(column=4,row=20,padx=5,pady=0)
TR14Result = IntVar()
TR14Check = Checkbutton(teamFrame,text="  4:30",variable=TR14Result,justify=LEFT)
TR14Check.grid(column=4,row=21,padx=5,pady=0)
TR15Result = IntVar()
TR15Check = Checkbutton(teamFrame,text="  5:00",variable=TR15Result,justify=LEFT)
TR15Check.grid(column=4,row=22,padx=5,pady=0)
TR16Result = IntVar()
TR16Check = Checkbutton(teamFrame,text="  5:30",variable=TR16Result,justify=LEFT)
TR16Check.grid(column=4,row=23,padx=5,pady=0)

#Friday CheckBoxes
TF1Result = IntVar()
TF1Check = Checkbutton(teamFrame,text="  9:00",variable=TF1Result,justify=LEFT)
TF1Check.grid(column=5,row=8,padx=5,pady=0)
TF2Result = IntVar()
TF2Check = Checkbutton(teamFrame,text="  9:30",variable=TF2Result,justify=LEFT)
TF2Check.grid(column=5,row=9,padx=5,pady=0)
TF3Result = IntVar()
TF3Check = Checkbutton(teamFrame,text="10:00",variable=TF3Result,justify=LEFT)
TF3Check.grid(column=5,row=10,padx=5,pady=0)
TF4Result = IntVar()
TF4Check = Checkbutton(teamFrame,text="10:30",variable=TF4Result,justify=LEFT)
TF4Check.grid(column=5,row=11,padx=5,pady=0)
TF5Result = IntVar()
TF5Check = Checkbutton(teamFrame,text="11:00",variable=TF5Result,justify=LEFT)
TF5Check.grid(column=5,row=12,padx=5,pady=0)
TF6Result = IntVar()
TF6Check = Checkbutton(teamFrame,text="11:30",variable=TF6Result,justify=LEFT)
TF6Check.grid(column=5,row=13,padx=5,pady=0)
TF7Result = IntVar()
TF7Check = Checkbutton(teamFrame,text="  1:00",variable=TF7Result,justify=LEFT)
TF7Check.grid(column=5,row=14,padx=5,pady=0)
TF8Result = IntVar()
TF8Check = Checkbutton(teamFrame,text="  1:30",variable=TF8Result,justify=LEFT)
TF8Check.grid(column=5,row=15,padx=5,pady=0)
TF9Result = IntVar()
TF9Check = Checkbutton(teamFrame,text="  2:00",variable=TF9Result,justify=LEFT)
TF9Check.grid(column=5,row=16,padx=5,pady=0)
TF10Result = IntVar()
TF10Check = Checkbutton(teamFrame,text="  2:30",variable=TF10Result,justify=LEFT)
TF10Check.grid(column=5,row=17,padx=5,pady=0)
TF11Result = IntVar()
TF11Check = Checkbutton(teamFrame,text="  3:00",variable=TF11Result,justify=LEFT)
TF11Check.grid(column=5,row=18,padx=5,pady=0)
TF12Result = IntVar()
TF12Check = Checkbutton(teamFrame,text="  3:30",variable=TF12Result,justify=LEFT)
TF12Check.grid(column=5,row=19,padx=5,pady=0)
TF13Result = IntVar()
TF13Check = Checkbutton(teamFrame,text="  4:00",variable=TF13Result,justify=LEFT)
TF13Check.grid(column=5,row=20,padx=5,pady=0)
TF14Result = IntVar()
TF14Check = Checkbutton(teamFrame,text="  4:30",variable=TF14Result,justify=LEFT)
TF14Check.grid(column=5,row=21,padx=5,pady=0)
TF15Result = IntVar()
TF15Check = Checkbutton(teamFrame,text="  5:00",variable=TF15Result,justify=LEFT)
TF15Check.grid(column=5,row=22,padx=5,pady=0)
TF16Result = IntVar()
TF16Check = Checkbutton(teamFrame,text="  5:30",variable=TF16Result,justify=LEFT)
TF16Check.grid(column=5,row=23,padx=5,pady=0)

#==================================
#=           Loop
#==================================



#Loop
window.mainloop()

