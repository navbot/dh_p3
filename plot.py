import pandas
import numpy as np
import matplotlib.pyplot as plt

events = pandas.read_csv('events_harmony_new.csv')
#print(char_harmony)
single = events['Single'].values
group = events['Group'].values
male = events['Group.Male-dominant'].values
female = events['Group.Female-dominant'].values


# plotting the line 1 points
plt.bar(range(len(single)), single, label = "Single", alpha=0.75)
plt.bar(range(len(group)), group, label = "Group", alpha=0.75)
plt.bar(range(len(male)), male, label = "Male-dominant Group", alpha=0.75)
plt.bar(range(len(female)), female, label = "Female-dominant Group", alpha=0.75)
 
# naming the x axis
plt.xlabel('Events')
# naming the y axis
plt.ylabel('Plurality of Characters')
# giving a title to my graph
plt.title('Plurality of Characters in Harmonious Events')
 
# show a legend on the plot
plt.legend()
 
# function to show the plot
plt.show()