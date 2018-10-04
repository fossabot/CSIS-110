import random # To do the random choice stuff.

lab1 = ["Nishant & Trey", "Robert and William", "Bob and Kisha"]

allNames = ["Nishant,Trey,Robert,William,Bob,Kisha"]
newAllNames = allNames[0].split(',')

#newPartners = <> New partners assigned here


# If lab1 is in any part of newPartners, it should reshuffle the entire list.

# If newPartners contains the same name twice, reshuffle the entire list.

def labPartners():
    name1 = random.choice(newAllNames)
    name2 = random.choice(newAllNames)
    test = name1, "&", name2
    print(name1)
    print(name2)
    if name1 == name2:
      print("ERROR || Both names are matching || ERROR")
    elif ((name1,"&",name2 == lab1) or (name2,"&",name1 == lab1)):
        print("ERROR || One or more groups have been identified to contain two names that've worked with each other before || ERROR")
    else:
      print(name1,"&",name2)
