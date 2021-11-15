import pandas
import numpy as np

char_harmony = pandas.read_csv('char_harmony.csv')
#print(char_harmony)

events_harmony = pandas.read_csv('events_harmony.csv')
#print(events_harmony)

single = [0]*len(events_harmony.index)
group = [0]*len(events_harmony.index)
male_dominated = [0]*len(events_harmony.index)
female_dominated = [0]*len(events_harmony.index)

#print(char_harmony.loc[char_harmony['Character H-ID'] == 293]['Number'])

for ind in events_harmony.index:
	chars_in_event = str(events_harmony['Characters(s) in Event H-ID'][ind]).split("|")
	
	if(len(chars_in_event) > 0):
		for char in chars_in_event:
			print(char)
			if (char != 'nan'):
				number = char_harmony.loc[char_harmony['Character H-ID'] == int(char)]['Number']
				#print(type(str(number)))
				#print(str(number))
				#print(number.values[0])

				if(number.values[0] == 'Single'):
					single[ind] += 1
				if(number.values[0] == 'Group'):
					group[ind] += 1
				if(number.values[0] == 'Group.Female-dominant'):
					female_dominated[ind] += 1
				if(number.values[0] == 'Group.Male-dominant'):
					male_dominated[ind] += 1


events_harmony['Single'] = single
events_harmony['Group'] = group
events_harmony['Group.Male-dominant'] = male_dominated
events_harmony['Group.Female-dominant'] = female_dominated

#print(events_harmony)

events_harmony.to_csv("events_harmony_new.csv")