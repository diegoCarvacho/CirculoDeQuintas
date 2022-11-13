#imports allMidiNotes.csv file, reverses its order and saves it in a new file called allMidiNotesReordered.csv

import csv
import pandas as pd

df = pd.read_csv('Documents/allMidiNotes.csv', delimiter=',')
allNotes : list = df.values.tolist()
allNotes.reverse()

#print(allNotes)

with open('Documents/allMidiNotesReordered.csv', 'w') as f:
    write = csv.writer(f)  
    for x in allNotes:
        write.writerow(x)

exit()
