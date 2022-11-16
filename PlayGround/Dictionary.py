modesDictionary = {
  1 : "Gated",
  2 : "Latched",
  3 : "Clocked",
  4 : "TBD"
}

print(len(modesDictionary))     # get number of elementes in the dictionary
print(modesDictionary[1])       # get value corresponding to the first key
print(modesDictionary.keys())   # list all Keys inside the dictionary
print(modesDictionary.values()) # list all Values inside the dictionary
print(modesDictionary.items())  # list all Key:Value pairs inside the dictionary

# print all Keys one by one using for loop
for mode in modesDictionary:
    print(mode)

# print all Values one by one using for loop
for mode in modesDictionary:
    print(modesDictionary[mode])
    
# print all Key:Value Pairs using for loop
for x, y in modesDictionary.items():
  print(x, y)


exit()