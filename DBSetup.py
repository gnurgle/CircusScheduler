import sqlite3 as sql

def createDB(name):

	conn = sql.connect(name)

	conn.execute('DROP TABLE IF EXISTS Act')
	conn.execute('DROP TABLE IF EXISTS Performer')
	conn.execute('DROP TABLE IF EXISTS Team')
	conn.execute('DROP TABLE IF EXISTS Schedule')
	conn.execute('DROP TABLE IF EXISTS TeamSchedule')
	conn.execute('DROP TABLE IF EXISTS Coaches')

	conn.execute('CREATE TABLE Coaches (CoachName Char(30),\
		PRIMARY KEY(CoachName))')

	conn.execute('CREATE TABLE Act (ActName Char(30),\
		Ring1 INT,\
		Ring2 INT,\
		Ring3 INT,\
		Hut INT,\
		Hour INT,\
		Coach CHAR(30),\
		FOREIGN KEY(Coach) REFERENCES Coaches(CoachName),\
		PRIMARY KEY(ActName))')

	conn.execute('CREATE TABLE Performer (PerfName Char(30),\
		Act1 Char(20),\
		Act2 Char(20),\
		Act3 Char(20),\
		Act4 Char(20),\
		Act5 Char(20),\
		Team1 INT,\
		Team2 INT,\
		Team3 INT,\
		Team4 INT,\
		Team5 INT,\
		FOREIGN KEY (Act1) REFERENCES Act(ActName),\
		FOREIGN KEY (Act2) REFERENCES Act(ActName),\
		FOREIGN KEY (Act3) REFERENCES Act(ActName),\
		FOREIGN KEY (Act4) REFERENCES Act(ActName),\
		FOREIGN KEY (Act5) REFERENCES Act(ActName),\
		FOREIGN KEY (Team1) REFERENCES Team(TeamName),\
		FOREIGN KEY (Team2) REFERENCES Team(TeamName),\
		FOREIGN KEY (Team3) REFERENCES Team(TeamName),\
		FOREIGN KEY (Team4) REFERENCES Team(TeamName),\
		FOREIGN KEY (Team5) REFERENCES Team(TeamName),\
		PRIMARY KEY(PerfName))')

	conn.execute('CREATE TABLE Team (ActName Char(30),\
		TeamName INT,\
		FOREIGN KEY (ActName) REFERENCES Act(ActName),\
		PRIMARY KEY(ActName,TeamName))')

	conn.execute('CREATE TABLE Schedule (PerfName Char(30),\
		M1 INT,\
		M2 INT,\
		M3 INT,\
		M4 INT,\
		M5 INT,\
		M6 INT,\
		M7 INT,\
		M8 INT,\
		M9 INT,\
		M10 INT,\
		M11 INT,\
		M12 INT,\
		M13 INT,\
		M14 INT,\
		M15 INT,\
		M16 INT,\
		T1 INT,\
		T2 INT,\
		T3 INT,\
		T4 INT,\
		T5 INT,\
		T6 INT,\
		T7 INT,\
		T8 INT,\
		T9 INT,\
		T10 INT,\
		T11 INT,\
		T12 INT,\
		T13 INT,\
		T14 INT,\
		T15 INT,\
		T16 INT,\
		W1 INT,\
		W2 INT,\
		W3 INT,\
		W4 INT,\
		W5 INT,\
		W6 INT,\
		W7 INT,\
		W8 INT,\
		W9 INT,\
		W10 INT,\
		W11 INT,\
		W12 INT,\
		W13 INT,\
		W14 INT,\
		W15 INT,\
		W16 INT,\
		R1 INT,\
		R2 INT,\
		R3 INT,\
		R4 INT,\
		R5 INT,\
		R6 INT,\
		R7 INT,\
		R8 INT,\
		R9 INT,\
		R10 INT,\
		R11 INT,\
		R12 INT,\
		R13 INT,\
		R14 INT,\
		R15 INT,\
		R16 INT,\
		F1 INT,\
		F2 INT,\
		F3 INT,\
		F4 INT,\
		F5 INT,\
		F6 INT,\
		F7 INT,\
		F8 INT,\
		F9 INT,\
		F10 INT,\
		F11 INT,\
		F12 INT,\
		F13 INT,\
		F14 INT,\
		F15 INT,\
		F16 INT,\
		FOREIGN KEY (PerfName) REFERENCES Performer(PerfName) ON UPDATE CASCADE ON DELETE CASCADE,\
		PRIMARY KEY(PerfName))')

	conn.execute('CREATE TABLE TeamSchedule (ActName Char(30),\
		TeamName INT,\
		TM1 INT,\
		TM2 INT,\
		TM3 INT,\
		TM4 INT,\
		TM5 INT,\
		TM6 INT,\
		TM7 INT,\
		TM8 INT,\
		TM9 INT,\
		TM10 INT,\
		TM11 INT,\
		TM12 INT,\
		TM13 INT,\
		TM14 INT,\
		TM15 INT,\
		TM16 INT,\
		TT1 INT,\
		TT2 INT,\
		TT3 INT,\
		TT4 INT,\
		TT5 INT,\
		TT6 INT,\
		TT7 INT,\
		TT8 INT,\
		TT9 INT,\
		TT10 INT,\
		TT11 INT,\
		TT12 INT,\
		TT13 INT,\
		TT14 INT,\
		TT15 INT,\
		TT16 INT,\
		TW1 INT,\
		TW2 INT,\
		TW3 INT,\
		TW4 INT,\
		TW5 INT,\
		TW6 INT,\
		TW7 INT,\
		TW8 INT,\
		TW9 INT,\
		TW10 INT,\
		TW11 INT,\
		TW12 INT,\
		TW13 INT,\
		TW14 INT,\
		TW15 INT,\
		TW16 INT,\
		TR1 INT,\
		TR2 INT,\
		TR3 INT,\
		TR4 INT,\
		TR5 INT,\
		TR6 INT,\
		TR7 INT,\
		TR8 INT,\
		TR9 INT,\
		TR10 INT,\
		TR11 INT,\
		TR12 INT,\
		TR13 INT,\
		TR14 INT,\
		TR15 INT,\
		TR16 INT,\
		TF1 INT,\
		TF2 INT,\
		TF3 INT,\
		TF4 INT,\
		TF5 INT,\
		TF6 INT,\
		TF7 INT,\
		TF8 INT,\
		TF9 INT,\
		TF10 INT,\
		TF11 INT,\
		TF12 INT,\
		TF13 INT,\
		TF14 INT,\
		TF15 INT,\
		TF16 INT,\
		FOREIGN KEY (ActName) REFERENCES Act(ActName) ON UPDATE CASCADE ON DELETE CASCADE,\
		FOREIGN KEY (TeamName) REFERENCES Team(TeamName) ON UPDATE CASCADE ON DELETE CASCADE,\
		PRIMARY KEY(ActName,TeamName))')

	conn.close()

if __name__ == "__main__":
	createDB("test")
