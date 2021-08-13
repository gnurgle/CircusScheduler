from tkinter import filedialog as fd
from tkinter import ttk
from tkinter import *
from DBSetup import createDB
import sqlite3 as sql

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
#=         Fetch Act Values
#==================================
def fetchPerfValues(e):

	statusBar.configure(text="Loaded " + perfCombo.get())

#==================================
#=         Fetch Team Values
#==================================
def fetchTeamValues(e):

	statusBar.configure(text="Loaded " + perfCombo.get())


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

		#Insert New Performer
		cur.execute("DELETE FROM Team WHERE TeamName=? AND ActName=?",(oldTeam,teamActCombo.get()))

		conn.commit()
		cur.close()
		conn.close()

		statusBar.configure(text="Removed Team " + oldTeam + " from " + teamActCombo.get())


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
#=           Update Window
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
gen.add_command(label ='1 - Generate Team Schedules', command = None)
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
hourCheck.grid(column=3,row=3,padx=10,pady=10)

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
ttk.Label(perfFrame, text="Act 1").grid(column=0, row=2, padx=5, pady=5)
ttk.Label(perfFrame, text="Act 2").grid(column=1, row=2, padx=5, pady=5)
ttk.Label(perfFrame, text="Act 3").grid(column=2, row=2, padx=5, pady=5)
ttk.Label(perfFrame, text="Act 4").grid(column=3, row=2, padx=5, pady=5)
ttk.Label(perfFrame, text="Act 5").grid(column=4, row=2, padx=5, pady=5)

#Performer Act Comboboxes
perfAct1Combo = ttk.Combobox(perfFrame,postcommand=lambda: perfAct1Combo.configure(values=fetchActs()))
perfAct1Combo['values'] = fetchActs()
perfAct1Combo['width'] = 15
perfAct1Combo.grid(column=0,row=3,padx=5,pady=5)
perfAct2Combo = ttk.Combobox(perfFrame,postcommand=lambda: perfAct2Combo.configure(values=fetchActs()))
perfAct2Combo['values'] = fetchActs()
perfAct2Combo['width'] = 15
perfAct2Combo.grid(column=1,row=3,padx=5,pady=5)
perfAct3Combo = ttk.Combobox(perfFrame,postcommand=lambda: perfAct3Combo.configure(values=fetchActs()))
perfAct3Combo['values'] = fetchActs()
perfAct3Combo['width'] = 15
perfAct3Combo.grid(column=2,row=3,padx=5,pady=5)
perfAct4Combo = ttk.Combobox(perfFrame,postcommand=lambda: perfAct4Combo.configure(values=fetchActs()))
perfAct4Combo['values'] = fetchActs()
perfAct4Combo['width'] = 15
perfAct4Combo.grid(column=3,row=3,padx=5,pady=5)
perfAct5Combo = ttk.Combobox(perfFrame,postcommand=lambda: perfAct5Combo.configure(values=fetchActs()))
perfAct5Combo['values'] = fetchActs()
perfAct5Combo['width'] = 15
perfAct5Combo.grid(column=4,row=3,padx=5,pady=5)

#Performer Team  text
ttk.Label(perfFrame, text="Team 1").grid(column=0, row=4, padx=10, pady=5)
ttk.Label(perfFrame, text="Team 2").grid(column=1, row=4, padx=10, pady=5)
ttk.Label(perfFrame, text="Team 3").grid(column=2, row=4, padx=10, pady=5)
ttk.Label(perfFrame, text="Team 4").grid(column=3, row=4, padx=10, pady=5)
ttk.Label(perfFrame, text="Team 5").grid(column=4, row=4, padx=10, pady=5)

#Performer Act Comboboxes
perfTeam1Combo = ttk.Combobox(perfFrame,postcommand=lambda: perfTeam1Combo.configure(values=fetchSTeams(perfAct1Combo)))
perfTeam1Combo['values'] = fetchSTeams(perfAct1Combo)
perfTeam1Combo['width'] = 15
perfTeam1Combo.grid(column=0,row=5,padx=5,pady=5)
perfTeam2Combo = ttk.Combobox(perfFrame,postcommand=lambda: perfTeam2Combo.configure(values=fetchSTeams(perfAct2Combo)))
perfTeam2Combo['values'] = fetchSTeams(perfAct2Combo)
perfTeam2Combo['width'] = 15
perfTeam2Combo.grid(column=1,row=5,padx=5,pady=5)
perfTeam3Combo = ttk.Combobox(perfFrame,postcommand=lambda: perfTeam3Combo.configure(values=fetchSTeams(perfAct3Combo)))
perfTeam3Combo['values'] = fetchSTeams(perfAct3Combo)
perfTeam3Combo['width'] = 15
perfTeam3Combo.grid(column=2,row=5,padx=5,pady=5)
perfTeam4Combo = ttk.Combobox(perfFrame,postcommand=lambda: perfTeam4Combo.configure(values=fetchSTeams(perfAct4Combo)))
perfTeam4Combo['values'] = fetchSTeams(perfAct4Combo)
perfTeam4Combo['width'] = 15
perfTeam4Combo.grid(column=3,row=5,padx=5,pady=5)
perfTeam5Combo = ttk.Combobox(perfFrame,postcommand=lambda: perfTeam5Combo.configure(values=fetchSTeams(perfAct5Combo)))
perfTeam5Combo['values'] = fetchSTeams(perfAct5Combo)
perfTeam5Combo['width'] = 15
perfTeam5Combo.grid(column=4,row=5,padx=5,pady=5)

#Clear Performer Act/Team
clearPerfButton = Button(perfFrame, text='clear', command=clearPerfCombos)
clearPerfButton.grid(column=4,row=6,padx=5,pady=5)

#Schedule Textboxes
ttk.Label(perfFrame, text="Monday").grid(column=0, row=7, padx=10, pady=5)
ttk.Label(perfFrame, text="Tuesday").grid(column=1, row=7, padx=10, pady=5)
ttk.Label(perfFrame, text="Wednesday").grid(column=2, row=7, padx=10, pady=5)
ttk.Label(perfFrame, text="Thursday").grid(column=3, row=7, padx=10, pady=5)
ttk.Label(perfFrame, text="Friday").grid(column=4, row=7, padx=10, pady=5)



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


#==================================
#=           Loop
#==================================



#Loop
window.mainloop()

