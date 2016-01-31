from sys import argv
from re import sub
from os.path import isfile

templateString = ""
with open(argv[1], "r") as template:
	templateString = template.read()

result = []
with open(argv[2], "r") as input:

	for line in input.readlines():
		cell = line.split(",")

		copyString = templateString
		team = cell[0]
		first = cell[2]
		last = cell[3].strip()		#Get rid of \r and \n
		
		if not isfile("{0}/{1}_{2}.JPG".format(argv[3],first, last)):
			#Insert blank photo members without a roster picture
			copyString = copyString.replace("$FIRST_$LAST", "Blank")
		
		if "Lead" in team:
			copyString = copyString.replace("<li>", "<li class=\"teamlead\">")

		copyString = copyString.replace("$FIRST", first)
		copyString = copyString.replace("$LAST", last)
		copyString = copyString.replace("$TEAM", team)


		result.append(copyString+"\n\n")

with open(argv[2][:-4]+".txt", "w") as output:
	output.writelines(result)
