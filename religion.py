import pandas
import numpy as np
import matplotlib.pyplot as plt

char_harmony = pandas.read_csv('char_harmony.csv')
#print(char_harmony)

events_harmony = pandas.read_csv('events_harmony.csv')
#print(events_harmony)

religions = ["Atheist", "Christian", "Hindu", "Muslim", "Sikh", "Unknown"]
single = [0]*len(religions)
group = [0]*len(religions)
male_dominated = [0]*len(religions)
female_dominated = [0]*len(religions)

for ind in events_harmony.index:
	chars_in_event = str(events_harmony['Characters(s) in Event H-ID'][ind]).split("|")
	
	if(len(chars_in_event) > 0):
		for char in chars_in_event:
			#print(char)
			if (char != 'nan'):
				number = char_harmony.loc[char_harmony['Character H-ID'] == int(char)]['Number']
				religion = char_harmony.loc[char_harmony['Character H-ID'] == int(char)]['Religion']
				#print(type(str(number)))
				#print(str(number))
				#print(number.values[0])

				if(number.values[0] == 'Single') and (religion.values[0] in religions):
					single[religions.index(religion.values[0])] += 1
				if(number.values[0] == 'Group') and (religion.values[0] in religions):
					group[religions.index(religion.values[0])] += 1
				if(number.values[0] == 'Group.Female-dominant') and (religion.values[0] in religions):
					female_dominated[religions.index(religion.values[0])] += 1
				if(number.values[0] == 'Group.Male-dominant') and (religion.values[0] in religions):
					male_dominated[religions.index(religion.values[0])] += 1

#print(single)
#print(group)


# plotting the line 1 points
plt.bar(religions, single, label = "Single", alpha=0.75)
plt.bar(religions, group, label = "Group", alpha=0.75)
plt.bar(religions, male_dominated, label = "Male-dominant Group", alpha=0.75)
plt.bar(religions, female_dominated, label = "Female-dominant Group", alpha=0.75)

# naming the x axis
plt.xlabel('Religion')
# naming the y axis
plt.ylabel('Plurality of Characters')
# giving a title to my graph
plt.title('Plurality of Characters in Harmonious Events')
 
# show a legend on the plot
plt.legend()
 
# function to show the plot
plt.show()
