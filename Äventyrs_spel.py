import random as rand
 
class spelare():

    def __init__(self,namn, strength, hp, lvl, inventory):
        self.strength = strength
        self.hp = hp
        self.lvl = lvl
        self.inventory = inventory
        self.namn = namn

    def stats("2"):
        return print(f"Name: {namn.namn} STR: {namn.strength} , HP: {namn.hp}, LVL: {namn.lvl}\n{namn.inventory}")
    
    def inventory():
        
        invent = ["Slot_1","Slot_2","Slot_3","Slot_4","Slot_5"]
        return print(invent)

def kista():
    while True:
        items = ["penna", "sudd", "sword", "Dog"]
        item_chans = rand.randint(0,len(items)-1)
        item = items.pop(item_chans)
        print("du hittade en kista")
        print("Du fick en:",item)
        namn.inventory.append(item)
        return print(f"{item}, added to inventory \n {namn.inventory}")
def monster():
    monster_strength = rand.randint(1,10)
    if namn.strength > monster_strength:
        print("du besegrade monstret ")
    elif namn.strenghth < monster_strength:
        print("monstret var starkare än dig och du tog skada")
        namn.hp - monster_strength
        print(f"Current HP: {namn.hp}")
    else:
        print(f"{namn} och monstret va gämn starka ")
    
    
                
def door():
    while True:
        door = input("välje en av tre dörrar ('1' '2' '3'): 4 = Meny -->  ")
        if door == "4":
            break
        else:
            chans = rand.randint(1,3)
            if chans == 1:
                print("du trillade ned i en fälla")
            elif chans == 2:
                kista()
            elif chans == 3:
                print("du stötte på ett monster")
            else:
                print("det fins bara tre dörrar!")
                continue

namn = input("välje ett namn -> ") 
namn = spelare(namn, 5, 10, 1,[])

while True:
    choice = input(""" vad vill du göra
    1.öppna en dör      2.check status
    3.kolla ditt inventory 
    ->""")
    if choice in ("1","2","3","4"):
        if choice == "1":
            door()
        elif choice == "2":
            namn.stats()
        elif choice == "3":
            namn.inventory()
    else:
        print("du skrev in något förbjudet")
        continue
