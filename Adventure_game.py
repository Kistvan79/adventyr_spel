import random as rand
import time
import threading

# Här uppe ligger alla våra classer och deras egenskaper

class Fiende(): 
    def __init__(self, monster_namn, monster_styrka, monster_hp):
        self.namn = monster_namn
        self.styrka = monster_styrka
        self.hp = monster_hp
            
class Cockroach_type(Fiende):
    def __init__(self, monster_namn, monster_styrka, monster_hp):
        super().__init__(monster_namn, monster_styrka, monster_hp)
        

    
class Sheep_type(Fiende):
    def __init__(self, monster_namn, monster_styrka, monster_hp):
        super().__init__(monster_namn, monster_styrka, monster_hp)
    


class item_attribut():
    def __init__(self,dmg,Type):
        self.dmg = dmg
        self.Type = Type

class Spelare():

    def __init__(self,namn, strength, hp, lvl, inventory, exp, exp_multi):
        self.strength = strength
        self.hp = hp
        self.lvl = lvl
        self.inventory = inventory
        self.namn = namn
        self.exp = exp
        self.exp_multi = exp_multi

    def intro(self):
        spelare.namn = input("Namn ---> ")
        time.sleep(0.25)

    def stats(self): # en funktion som skriver ut spelarens nuvarande stats
        return print(f"""Namn: {spelare.namn}   STR: {spelare.strength} + {item_dmg()}    HP: {spelare.hp}
    LVL: {spelare.lvl}  EXP: {spelare.exp}/{40*spelare.exp_multi}""")
    
    def backpack(self): # en funtkion som skriver ut spelarens föremål
        count = 1
        for föremål in self.inventory: # Listar upp alla föremål i inventory
            print(f"{count}.",föremål.Type,"DMG:",föremål.dmg,)
            count += 1
        if len(self.inventory) > 5:
            manadge_items()
        elif len(self.inventory) > 0:
            while len(self.inventory)>0:
                user_choice = input("\nVill du ta bort ett item Ja/Nej--> ")
                if user_choice.lower() in ("j","ja"):
                    manadge_items()
                elif user_choice.lower() in ("n","nej"):
                    break
                else:
                    print("Du skrev in något förbjudet")
                    continue
        else:
            print("\nDin ryggsäck är tom")

    def lvl_up(self): # Är en level up metod för spelaren.
        spelare.exp += 40
        if spelare.exp >= 40*spelare.exp_multi: # spelaren har en exp_multiplier som multipliceras med det första exp målet (40)
            spelare.exp -= 40*spelare.exp_multi
            spelare.strength += 3
            spelare.lvl += 1
            spelare.hp += 5
            spelare.exp_multi += 0.5
            print(f"""\nDu levlade upp! 
[Nuvarande STR: {spelare.strength}]   [Nuvarande LVL: {spelare.lvl}]    [Nuvarande HP: {spelare.hp}]""")

class Scoreboard(Spelare):
    def __init__(self, namn, strength, hp, lvl, inventory, exp, exp_multi):
        super().__init__(namn, strength, hp, lvl, inventory, exp, exp_multi)
    
    def board(self):
        print(f"""               SCOREBOARD
                STRENGTH    HEALTH POINTS   LEVEL   TIME
{spelare.namn}:         {spelare.strength}          {spelare.hp}            {spelare.lvl}  """)
      

def manadge_items():# en funktion som hanterar spelarens föremål 
    while True:
        val_item = input("\nVälj positionen på itemet du vill ta bort: ")
        if val_item.isdigit() and int(val_item) <= len(spelare.inventory): 
            skräp_item = spelare.inventory.pop(int(val_item)-1)
            print("Du tog bort:", skräp_item.Type, "DMG:", skräp_item.dmg)
            break
        else:
            print("Inmätnings fel")
            continue          
                
def kista():
    while True:
        items = ["Penna", "Sudd", "Sword", "Hund"] # Är items som hittas i kista
        item_chans = rand.randint(0,len(items)-1) # Definerar ett slumpmässigt item som "item_chans"
        item = item_attribut(rand.randint(1,5),items.pop(item_chans)) # Ger ett slumpmässigt föremål en slumpmässig styrka 
        print("\nDu hittade en kista")
        print(f"Du fick en [{item.Type}] DMG: {item.dmg}")
        spelare.lvl_up()
        print("Du fick 40 EXP ")
        spelare.inventory.append(item)
        if len(spelare.inventory) > 5:
            print("\nDin ryggsäck är full")
            spelare.backpack()
            break
        else:
            if item_dmg() >= 25:
                random_dialogue = rand.randint(1,10) #En generös funktion som ger spelaren ännu mer HP
                if random_dialogue == 6:            
                    print("\nExploit the DPS God! \n + 30 HP")
                    spelare.hp += 30
                else:
                    print("\n Du är en med DPS Guden! \n + 30 HP")
                    spelare.hp += 30
            return 
           

def item_dmg(): # räknar ut totala dmg bonusen spelare ska få 
    dmg_bonus = 0
    for föremål in spelare.inventory:
        dmg_bonus += föremål.dmg
    return(dmg_bonus)

def combat(): # Är combat systemet
    full_dmg = item_dmg()
    fiende.hp = rand.randint(20,30)
    sheep.hp = rand.randint(10,20)
    roaches.hp = rand.randint(20,40)
    list_of_fiende = [fiende, sheep, roaches] #Lista av alla möjliga fiender
    fiende_chans = rand.randint(0,len(list_of_fiende)-1) #Slumpar fram en av 3 möjliga fiender
    random_fiende = list_of_fiende.pop(fiende_chans) #Väljer ut en av 3 möjliga fiender och definerar de som "random_fiende"
    random_fiende.hp = rand.uniform(random_fiende.hp,random_fiende.hp*spelare.exp_multi)
    print(f"\nStriden har börjat! {spelare.namn} vs {random_fiende.namn}")

    while spelare.hp > 0 or random_fiende.hp: # random_fiende sätts in i en loop för att sloss för sitt liv
        if input("\nTryck ENTER för att sloss ") == "":
            pass
        else:
            print("Som sagt, tryck enter för att sloss")
            continue
        time.sleep(0.5)
        fiende.styrka = rand.randint(9,11)# Definerar styrkan inom loopen för att få fram slumpad monster_dmg
        sheep.styrka = rand.randint(5,10)
        roaches.styrka = rand.randint(0,9)
        spelare.strength = round(rand.uniform(10, spelare.strength + full_dmg ))

        random_fiende.hp -= spelare.strength

        if random_fiende.hp <= 0:
            print(f"\n{random_fiende.namn} dealt: N/A       {spelare.namn} dealt: {spelare.strength} ") #När fienden besegras behövs inte
                                                                                                        # DMG och HP värden vissas igen
            print(f"""{random_fiende.namn}'s HP = -DECEASED-       {spelare.namn}'s HP = {spelare.hp} """)
            time.sleep(0.5)
            print(f"\n{random_fiende.namn} besegrades!")
            spelare.lvl_up()
            print("Du fick 40 EXP")
            break
        else:
            spelare.hp -= random_fiende.styrka
          
        print(f"\n{random_fiende.namn} dealt: {random_fiende.styrka}        {spelare.namn} dealt: {spelare.strength} ")
    
        print(f"""{random_fiende.namn}'s HP = {round(random_fiende.hp)}       {spelare.namn}'s HP = {spelare.hp} """)
        if spelare.hp <= 0:
            print("\nDu förlora striden!")
            break

#Ger alternativ att alltingen fly eller attakera monstret.
def monster():
    while True:
        choice = input("Spring iväg? [Ja/Nej]: ")
        if choice in ("j","ja","J","Ja"):
            chance = rand.randint(1,5)
            if chance in (1,2,3):
                print("Du lyckades fly från monstret")
                break 
            else:
                print("Du lyckades inte fly")
                combat()
                break
        elif choice in ("n","nej","N","Nej"):
            combat()
            break
        else:
            print("Du skrev något förbjudet")
            continue
        
# Ignorence is bliss, ger illusionen av att man väljer 1 unik dörr när alla tre dörrar är igentligen samma dörr          
def door():
    print("TRYCK 'M' FÖR ATT KOMMA TILLBAKS TILL MENYN")
    while spelare.hp > 0 and spelare.lvl < 10:
        door = input("""\nVälj en av tre dörrar (1-3)
---> """)
        if door in ("m", "M"):
            break
        elif door in("1","2","3"):
            chans = rand.randint(1,3)
            if chans == 1:
                print("\nDu trillade ned i en fälla")
                print(f"HP:{spelare.hp} -1")
                spelare.hp -= 1   
            elif chans == 2:
                kista()
            elif chans == 3:
                print("\nDu stötte på ett monster")
                monster()
        else:
            print("\nDet fins bara tre dörrar!")
            continue

# Object för classerna
roaches = Cockroach_type("Roach", rand.randint(0,9), 1)
sheep = Sheep_type("Sheep", rand.randint(5,12), 1)
fiende = Fiende("Bertil", rand.randint(6,9), 1)
spelare = Spelare("", 10, 1, 1,[], 0, 1)
scoreboard = Scoreboard(spelare.namn, spelare.strength, spelare.hp, spelare.lvl, spelare.inventory, spelare.exp, spelare.exp_multi)

# Huvud program
spelare.intro()
while spelare.hp > 0 and spelare.lvl < 10:
    choice = input(""" \nVad vill du göra
1.Öppna en dörr     2.Status    3.Inventory 
    ---> """)
    if choice in ("1","2","3","4"):
        if choice == "1":
            door()
        elif choice == "2":
            spelare.stats()
        elif choice == "3":
            spelare.backpack()
    else:
        print("Du skrev in något förbjudet")
        continue
if spelare.lvl == 10:
    print("DU VANN!")
else:
    print("GAME OVER :(")
