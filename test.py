def start():

	num1 = []
	num2 = []
	num3 = []
	num1.append([1,2,3])
	num1.append([4,5,6]) 
	num1.append([6,6,6])
	num2.append([4,4,4])
	num2.append([4,4,5])
	num2.append([4,4,7])
	num3.append([1,2,3])
	num3.append([9,9,7])
	num3.append([9,9,1])

	sched=[]
	sched.append(num1)
	sched.append(num2)
	sched.append(num3)
	depth=0
	match = []
	length = len(sched)


	test = recurListComp(sched[0],sched[1:])
	print (test)
	
#Recursivly runs until checks for matches from all
#of initial passed in list of lists
#returns a final list of combined potentials
def recurListComp(input, runList):
	output = []
	for i in input:
		for j in runList[0]:
			if not compareList(i,j):
				output.append([i,j])

	if len(runList) <=1:
		output = condenseList(output)
		return output

	output = condenseList(output)
	return recurListComp(output,runList[1:])


def condenseList(input):
	output = []
	if len(input[0]) == 3:
		return input
	elif any(isinstance(i,list) for i in input[0][0]):
		for entry in input:
			entry = entry[0]+[entry[1]]
			output.append(entry)
		return output
	return input 

#Returns true if there is a match, false if not
def compareList(list1, list2):
	print(list2)
	if any(isinstance(i,int) for i in list1):
		if len(set(list1).intersection(set(list2))) >0:
			return True
		else: 
			return False
	elif any(isinstance(i,list) for i in list1):
		for entry in list1:
			if compareList(entry,list2):
				return True
		return False

	#May not be needed
	if len(set(list1).intersection(set(list2))) > 0:
		return True
	return False	

if __name__=="__main__":
	start()
	
