import csv
import pandas as pd

df = pd.read_csv('Documents/allMidiNotes.csv', delimiter=',')
allNotes : list = df.values.tolist()
allNotes.reverse()

with open('Documents/allMidiNotesReordered.csv', 'w') as f:
    write = csv.writer(f)  
    for x in allNotes:
        # print(x)
        write.writerow(x)
        if any('C' in word for word in allNotes[1]):
            print(x)
exit()
