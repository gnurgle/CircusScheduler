import numpy as np
import sqlite3 as sql

class SchedulingClass:

	#Initialization
	def __init__(self, hardConstraintPenalty, dbName):

		#Hard Constraint penalty value
		self.hardConstraintPenalty = hardConstraintPenalty

		#Access DB and grab informations
		conn = sql.connect(dbName)
		cur = conn.cursor()

		cur.execute("SELECT rowid, ActName, TeamName FROM Team")

		rows = cur.fetchall()

		#lists of information
		self.ActName = []	
		self.TeamName = []		#Name of team relative to Act
		self.TeamNumber = []	#Universal Team number (rowid)
		self.Avalibility = []
		self.Coach = []
		self.Rings = []
		self.Hour = []

		#Split query into respective spots
		for row in rows:
			if len(row[1]) != 0:
				self.TeamNumber.append(row[0])
				self.ActName.append(row[1])
				self.TeamName.append(row[2])

		#Fetch Schedules for each and link
		for i in range(0,len(self.ActName)):
			cur.execute("SELECT * FROM TeamSchedule WHERE ActName=? AND TeamName=?",\
				(self.ActName[i], self.TeamName[i]))

			rows = cur.fetchall()
			#Strip out identifiers
			self.Avalibility.append([rows[0][2:]])

		#Fetch Schedules for each and link
		for i in range(0,len(self.ActName)):
			cur.execute("SELECT * FROM Act WHERE ActName=?",\
				(self.ActName[i],))

			rows = cur.fetchall()

			#Add rings information
			self.Rings.append([rows[0][1:5]])
			#Add Coach information
			self.Coach.append(rows[0][6])
			#Add Hour check
			self.Hour.append(rows[0][5])

		#Hardcoded practice values, left here for potential of change in future
		self.minPractice = 3
		self.maxPractice = 3
		self.numOfDays = 5

		#More values for portability if needed
		#print(self.Avalibility[0])
		#print(len(self.Avalibility[0][0]))
		self.slotsPerDay = len(self.Avalibility[0][0])/5
		self.slotsPerWeek = len(self.Avalibility[0][0])

	#Define length of class
	def __len__(self):
		return len(self.TeamNumber) * self.slotsPerWeek
		
	#Get total violations cost
	def getCost(self,schedule):
	
		#convert schedule to dict
		schedDict = self.getDictSchedule(schedule)
		
		#Count Violations
		vCoach = self.countSameCoachViolations(schedDict) 
		#vAct = self.countSameActViolations(schedDict) 
		vAval = self.countAvalibilityViolations(schedDict) 
		vCount = self.countPracticeViolations(schedDict) 
		vDay = self.countSameDayViolations(schedDict)
		vThreeD = self.countThreeDayMinViolations(schedDict)
		#temp values
		#vCoach = 0
		#vAct = 0
		#vCount = 0
		#Calculate Hard Constraints
		#hardCV = vCoach + vAct + vAval + vDay
		hardCV = vCoach + vAval + vDay + vThreeD
		#print(vAval)
		#print("Coach: " + str(vCoach) + " Act: " + str(vAct) + " Aval: " + str(vAval5) + " Count: " + str(vCount))
		return self.hardConstraintPenalty * hardCV + vCount

	#Convert Schedule to Dictionary
	def getDictSchedule(self, schedule):
		scheduleDict = {}
		slotIndex = 0

		for num in self.TeamNumber:
			scheduleDict[num] = schedule[slotIndex:slotIndex + self.slotsPerWeek]
			slotIndex += self.slotsPerWeek

		return scheduleDict

	#Define Violations...
	#Hard Violations
	#Not Scheduled Time

	#Count the number of violations where more than one
	#coach is listed on one time slot
	def countSameCoachViolations(self, dictSchedule):
		violations = 0

		#Check for Coach violations
		for i in range(0,self.slotsPerWeek):
			#Set empty list for coach checking
			coachCheck = []
			teamNum = -1
			for slot in dictSchedule.values():
				teamNum += 1
				#Check if schedule = 1 and coach is present
				if slot[i] == 1 and self.Coach[teamNum] in coachCheck:
					violations += 1
				elif slot[i] == 1:
					coachCheck.append(self.Coach[teamNum])

		return violations

	#Count the number of violations where more than one
	#of the same act is listed on one time slot
	def countSameActViolations(self, dictSchedule):
		violations = 0

		#Check for Coach violations
		for i in range(0,self.slotsPerWeek):
			#Set empty list for coach checking
			actCheck = []
			teamNum = -1
			for slot in dictSchedule.values():
				teamNum += 1
				#Check if schedule = 1 and coach is present
				if slot[i] == 1 and self.ActName[teamNum] in actCheck:
					violations += 1
				elif slot[i] == 1:
					actCheck.append(self.ActName[teamNum])

		return violations

	#Count number of Avalibility Violations
	def countAvalibilityViolations(self, dictSchedule):
		violations = 0

		#Check for Coach violations
		for i in range(0,self.slotsPerWeek):
			#Set empty list for coach checking
			actCheck = []
			teamNum = -1
			for slot in dictSchedule.values():
				teamNum += 1
				#Check if schedule = 1 and coach is present
				if slot[i] == 1 and self.Avalibility[teamNum][0][i] == 0:
					violations += 1


		#Heavier weight penalty
		return violations

	#Count number of Avalibility Violations
	def countPracticeViolations(self, dictSchedule):
		violations = 0

		#Check for # of practice violations
		for slot in dictSchedule.values():
			sumslot = sum(slot)
			if sumslot > 3:
				violations += 1
			elif sumslot < 3:
				violations += 100

		return violations

	def countSameDayViolations(self, dictSchedule):
		violations = 0

		
		for slot in dictSchedule.values():
			#Hardcoded seperations, if needed can be made dynamic
			sumM = sum(slot[:15])
			sumT = sum(slot[15:31])
			sumW = sum(slot[31:47])
			sumR = sum(slot[47:63])
			sumF = sum(slot[63:])
	
			#Add a violation for each instance that has more than one practice a day
			if sumM > 1:
				violations += sumM-1
			if sumT > 1:
				violations +=sumT-1
			if sumW > 1:
				violations +=sumW-1
			if sumR > 1:
				violations +=sumR-1
			if sumF > 1:
				violations +=sumF-1

		return violations

	def countThreeDayMinViolations(self, dictSchedule):
		violations = 0

		
		for slot in dictSchedule.values():
			#Hardcoded seperations, if needed can be made dynamic
			sumM = sum(slot[:15])
			sumT = sum(slot[15:31])
			sumW = sum(slot[31:47])
			sumR = sum(slot[47:63])
			sumF = sum(slot[63:])

			#Helper Flag
			flagCount = 0
			
			#Add a counter to flag for each day a practice is on
			if sumM > 0:
				flagCount +=1
			if sumT > 0:
				flagCount +=1
			if sumW > 1:
				flagCount += 1
			if sumR > 1:
				flagCount += 1
			if sumF > 1:
				flagCount += 1

			#Add violations for over/under 3 days a week
			if flagCount < 3:
				violations = 100
			if flagCount > 3:
				violations = 5-flagCount 

		return violations

	def printScheduleInfo(self,schedule):

		#convert schedule to dict
		schedDict = self.getDictSchedule(schedule)

		print("Schedule for each team:")
		for act in schedDict:
			print(self.ActName[act-1], ":", schedDict[act])
		#print (schedDict)

		#Count Violations
		vCoach = self.countSameCoachViolations(schedDict) 
		vAct = self.countSameActViolations(schedDict) 
		vAval = self.countAvalibilityViolations(schedDict) 
		vCount = self.countPracticeViolations(schedDict) 
		vDay = self.countSameDayViolations(schedDict)
		vThreeD = self.countThreeDayMinViolations(schedDict)

		print("Coach: " + str(vCoach) + " Act: " + str(vAct) + " Aval: " + str(vAval) + \
			" Count: " + str(vCount) + " Day: " + str(vDay) + " 3 Day Min: " + str(vThreeD))

		self.printCombined(schedule)

	def printCombined(self,schedule):

		#convert to dict
		schedDict = self.getDictSchedule(schedule)

		#Initialize array
		combined = []
		for i in range(0,80):
			combined.append("")
		
		for act in schedDict:
			for i in range(0,len(schedDict[act])):
				if schedDict[act][i] == 1:
					combined[i] += self.ActName[act-1] + " Team " + str(self.TeamName[act-1])

		for i in range(0,16):
			line = ""
			for j in range(0,5):
				line += combined[i*5+j] + "\t"
			print (line)
