import random # To do the random choice stuff.

lab1 = ["Nishant & Trey,Robert & William,Bob & Kisha"] # PartnameName & PartnerName
newlab1Names = lab1[0].split(',')

allNames = ["Nishant,Trey,Robert,William,Bob,Kisha"] # Name of all people in class
newAllNames = allNames[0].split(',')




# If lab1 is in any part of newPartners, it should reshuffle the entire list.

# If newPartners contains the same name twice, reshuffle the entire list.

def labPartners():

    for xx in range(len(newAllNames)):

        for x in range(len(newAllNames)):
            name1 = random.choice(newAllNames) # Stores a random name into name1
            name2 = random.choice(newAllNames) # Stores a random name into name2
            test = name1, "&", name2 # Stores both variables from above into one variable (test)
            if name1 == name2: # If name1 and name 2 are the same, return
                return
            elif ( ((name1, "&", name2) == newlab1Names) or ((name2, "&", name1) == newlab1Names) ): # If the new set of partners (for a group) are = to a set from newlab1Names, return.
                return
            else: # Everything else
                newPotentialLabPartners = (name1,"&",name2)
                newPotentialLabPartners1 = newPotentialLabPartners
            print(newPotentialLabPartners1)
