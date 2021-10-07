import random as rand
print('Welcome to Word RPG')
print('You must type your actions, for example if you want to go to the Dungeon, type Dungeon, or if you want to Fight, type Fight.')
print('(Remember, you have to type the exact word in quotes given in the choices, it is caps sensitive)')
Lvl=0
XP=0
XPtillLvl=0
HP=10
HPLimit=10
BonusHPLimit=0
MP=10
MPLimit=10
BonusMPLimit=0
TrueStr=0
TrueAgl=0
TrueInt=0
TrueAmr=0
BonusStr=0
BonusAgl=0
BonusInt=0
BonusAmr=0
Gold=0
Head=''
Body=''
Feet=''
Weapon=''
Inventory=[]
ShopItems=[]
UsrImp=''
GameZone=0
monster=''
MonHP=0
MonInt=0
MonStr=0
MonAgl=0
MonAmr=0
MonXP=0
MonGD=0

def Help():
    global GameZone
    print("""In this game, you goal is todefeat the final boss. 
 To do this you will need to make yourself more powerful by defeating monsters and buying items. 
 Items increase mainly 4 stats, STRENGTH, AGILITY, INTELLIGENCE, and ARMOR.
 Some items can increase your Health(HP) or Mana(MP) limit, but are rare and hard to obtain.
 STRENGTH increases your attack, mainly how much damage you do.
 AGILITY increases your chance to attack, dodge, and to flee from a battle.
 INTELLIGENCE increases your magic attack, how much damage they do and increases the slight change to use less mana.
 ARMOR decreases how much damage you take and increases a chance to block damage.
 There are four item slots, HEAD, CHEST, FEET, and WEAPON. Each Slot mains in a certain stat, though other stats 
 can be on an item in that slot.
 HEAD mainly has items that increase INTELLIGENCE.
 CHEST mainly has items that increase ARMOR.
 FEET mainly has items that increase AGILITY.
 WEAPON mainly has items that increase STRENGTH.
 Items can be bought from shops in exchange for gold.
 Items have a specific format in which they are shown, in the shop it is "Gold price-Item name: stats given", in the
 inventory it is just "Item name: stats given".
 Stats are also abreviated on items, STRENGTH is STR, AGILITY is AGL, INTELLIGENCE is INT, ARMOR is AMR, health is 
 HP, and mana is MP.
 defeating monsters will also grant you XP, which in turn is used to level up.
 Leveling up automatically grants you an increase in your STRENGTH, AGILITY, and INTELLIGENCE stats, is the main way
 you gain HP and MP, and has a chance to increase your ARMOR.
 Leveling up also allows you to advance into new zones whith stronger enemies and greater rewards.""")
    if GameZone==1:
        StarterTown()

def Talk():
    global HP
    global HPLimit
    global MP
    global MPLimit
    global XP
    global Gold
    def MonsterStats():
        global GameZone
        print('What monster would you like to know about?')
        if GameZone==1:
            KnownMonsters=['Slime','Goblin','Zombie']
        print(*KnownMonsters,sep='\n')
        print("Type 'Back' to go back.")
        UsrImp=input()
        print('')
        if GameZone==1 or GameZone>1:
            if UsrImp=='Slime':
                print("""    Slime,
    HP-5
    Int-0
    Str-1
    Agl-1
    Amr-0
    10XP gained when defeated
    2Gold gained when defeated 
    The most common enemny found in the Dungeon? a slime. Slimes are brainless blobs of organic matter with one direcive, kill. Their slippery bodies and lack of difinitive shape allow them to go almost anywhere and make them hard to hit.""")
                input()
                MonsterStats()
            if UsrImp=='Goblin':
                print("""    Goblin,
    HP-5
    Int-1
    Str-1
    Agl-2
    Amr-0
    15XP gained when defeated
    3Gold gained when defeated 
    Small and fast, goblins may not strike hard, but have minor intelligence and are hard to escape due to their speed.""")
                input()
                MonsterStats()
            if UsrImp=='Zombie':
                print("""    Zombie,
    HP-7
    Int-0
    Str-2
    Agl-1
    Amr-1
    20XP gained when defeated
    5Gold gained when defeated 
    Zombies are a strong and powerful enemy rarely found in the dungeon. They may be mindless, but they hit hard and have some defence against attacks.""")
                input()
                MonsterStats()
        if UsrImp=='Back':
            Talk()

    print('')
    print('You are in town sqare')
    print('What would you like to talk about?')
    print("""    1-Monsters
    2-Healing 
    3-Pray
    4-Go back to town""")
    UsrImp=input()
    if UsrImp=='2':
        print('You convince a local medic to heal you for free.')
        print('Your Health is now filled!')
        HP=HPLimit
        Talk()
    if UsrImp=='3':
        print('You go to a church and pray.')
        print('Your mana is filled!')
        MP=MPLimit
        Talk()
    if UsrImp=='1':
        print('You find a monster logger.')
        if XP==0:
            print('He wants your help finding monsters and gives you a gift to start off.')
            print('You got 10 gold and 10 XP')
            Gold=Gold+10
            XP=XP+10
        print('He will follow you and log all the monsters in the dungeon near the city you are in.')
        input()
        MonsterStats()
    if UsrImp=='4':
        StarterTown()

def LvlUp():
    global Lvl
    global XP
    global XPtillLvl
    global HP
    global HPLimit
    global MP
    global MPLimit
    global TrueInt
    global TrueStr
    global TrueAgl
    global TrueAmr
    if XP==XPtillLvl or XP>XPtillLvl:
        Lvlup=True
        print('Youve leveled up!')
        Lvl=Lvl+1
        StatPoints=2
        if Lvl==1:
            XPtillLvl=125
            HPLimit=HPLimit+2
            MPLimit=MPLimit+2
        if Lvl==2:
            XPtillLvl=230
            HPLimit=HPLimit+2
            MPLimit=MPLimit+2
        if Lvl==3:
            XPtillLvl=305
            HPLimit=HPLimit+3
            MPLimit=MPLimit+4
        if Lvl==4:
            XPtillLvl=400
            HPLimit=HPLimit+3
            MPLimit=MPLimit+2
        if Lvl==5:
            XPtillLvl=525
            HPLimit=HPLimit+2
            MPLimit=MPLimit+4
        if Lvl==6:
            XPtillLvl=625
            HPLimit=HPLimit+4
            MPLimit=MPLimit+4
        if Lvl==7:
            XPtillLvl=750
            HPLimit=HPLimit+3
            MPLimit=MPLimit+2
        if Lvl==8:
            XPtillLvl=900
            HPLimit=HPLimit+2
            MPLimit=MPLimit+4
        if Lvl==9:
            XPtillLvl=1100
            HPLimit=HPLimit+4
            MPLimit=MPLimit+4
        if Lvl==10:
            XPtillLvl=1300
            HPLimit=HPLimit+2
            MPLimit=MPLimit+2
        print('Your HP increased to '+HPLimit)
        print('Your MP increased to '+MP)
        while Lvlup==True:
            print('What stat would you like to increase?')
            print('1-Inteligence\n2-Strength\n3-Agility')
            if Lvl==3 or Lvl>3:
                print('4-Armor')
            UsrImp=input()
            if UsrImp=='1':
                TrueInt=TrueInt+1
                StatPoints=StatPoints-1
            if UsrImp=='2':
                TrueStr=TrueStr+1
                StatPoints=StatPoints-1
            if UsrImp=='3':
                TrueAgl=TrueAgl+1
                StatPoints=StatPoints-1
            if Lvl==3 or Lvl>3:
                if UsrImp=='4':
                    TrueAmr=TrueAmr+1
                    StatPoints=StatPoints-1
            if StatPoints==0:
                Lvlup=False

def Stats():
    global GameZone
    global TrueInt
    global BonusInt
    global TrueAgl
    global BonusAgl
    global TrueStr
    global BonusStr
    global TrueAmr
    global BonusAmr
    global HP
    global HPLimit
    global BonusHPLimit
    global MP
    global MPLimit
    global BonusMPLimit
    global Head
    global Body
    global Feet
    global Weapon
    INT=BonusInt+TrueInt
    STR=TrueStr+BonusStr
    AGL=TrueAgl+BonusAgl
    AMR=TrueAmr+BonusAmr
    HPLim=HPLimit+BonusHPLimit
    MPLim=MPLimit+BonusMPLimit
    print(f"GAMEZONE= {GameZone}")
    print(f"INTELLIGENCE= {INT}")
    print(f"STRENGTH= {STR}")
    print(f"AGILITY= {AGL}")
    print(f"ARMOR= {AMR}")
    print(f"CURRENT HEALTH= {HP}")
    print(f"MAXIMUM HEALTH= {HPLim}")
    print(f"CURRENT MANA= {MP}")
    print(f"MAXIMUM MANA= {MPLim}")
    print('Head- '+Head)
    print('Body- '+Body)
    print('Feet- '+Feet)
    print('Weapon- '+Weapon)
    input('')
    if GameZone==1:
        StarterTown()

def Dungeon():
    global GameZone
    global TrueInt
    global BonusInt
    global TrueAgl
    global BonusAgl
    global TrueStr
    global BonusStr
    global TrueAmr
    global BonusAmr
    global HP
    global HPLimit
    global MP
    global MPLimit
    global XP
    global Lvl
    global Gold
    global monster
    global MonHP
    global MonInt
    global MonStr
    global MonAgl
    global MonAmr
    global MonXP
    global MonGD
    Int=TrueInt+BonusInt
    Str=TrueStr+BonusStr
    Agl=TrueAgl+BonusAgl
    Amr=TrueAmr+BonusAmr
    print('You have '+str(HP)+'/'+str(HPLimit)+' Health, and '+str(MP)+'/'+str(MPLimit)+' Mana.')
    print('Do you want to continue? Y/N')
    Usr=input()
    def Zone1Monster():
        global monster
        global MonHP
        global MonInt
        global MonStr
        global MonAgl
        global MonAmr
        global MonXP
        global MonGD
        MonSel=rand.randrange(1,101)
        if MonSel>0 and MonSel<51:
            monster='Slime'
            MonHP=5
            MonInt=0
            MonStr=1
            MonAgl=1
            MonAmr=0
            MonXP=10
            MonGD=2
        if MonSel>50 and MonSel<81:
            monster='Goblin'
            MonHP=5
            MonInt=1
            MonStr=1
            MonAgl=2
            MonAmr=0
            MonXP=15
            MonGD=3
        if MonSel>80 and MonSel<101:
            monster='Zombie'
            MonHP=7
            MonInt=0
            MonStr=2
            MonAgl=1
            MonAmr=1
            MonXP=20
            MonGD=5
    if Usr=='N':
        StarterTown()
    else:
        if GameZone==1:
            Zone1Monster()
    print('')
    print('You encountered a '+monster)
    input()
    MonHPLim=MonHP
    MonDefeat=False
    while MonDefeat==False:
        print('')
        print(monster)
        print(str(MonHP)+'/'+str(MonHPLim))
        print('')
        print('You:')
        print('HP: '+str(HP)+'/'+str(HPLimit))
        print('MP: '+str(MP)+'/'+str(MPLimit))
        print('Actions:')
        print('1-Attack   2-Magic   3-Run')
        print('What would you like to do?')
        PlrAct=input()
        if PlrAct=='3':
            HitChance=rand.randrange(1,101)
            if MonAgl==Agl*3 or MonAgl>Agl*3:
                print('You failed to run from the monster.')
            else:
                if MonAgl==Agl*2 or MonAgl>Agl*2:
                    if HitChance>0 and HitChance<76:
                        print('You Failed to run from the monster.')
                    if HitChance>75 and HitChance<101:
                        print('You ran from the monster!')
                        MonDefeat=True
                else:
                    if MonAgl>Agl or MonAgl==Agl:
                        if HitChance>0 and HitChance<51:
                            print('You Failed to run from the monster.')
                        if HitChance>50 and HitChance<101:
                            print('You ran from the monster!')
                            MonDefeat=True
                    else:
                        if Agl>MonAgl*2 or Agl==MonAgl*2:
                            if HitChance>0 and HitChance<11:
                                print('You Failed to run from the monster.')
                            if HitChance>10 and HitChance<101:
                                print('You ran from the monster!')
                                MonDefeat=True
                        else:
                            if Agl>MonAgl:
                                if HitChance>0 and HitChance<51:
                                    print('You Failed to run from the monster.')
                                if HitChance>50 and HitChance<101:
                                    print('You ran from the monster!')
                                    MonDefeat=True
        if PlrAct=='2':
            HitDmg=Int
            HitChance=rand.randrange(1,101)
            if MonInt==0:
                if HitChance>0 and HitChance<76:
                    HitDmg=HitDmg*2
                if HitChance>90 and HitChance<101:
                    HitDmg=HitDmg*3
            else:
                if Int>MonInt or Int==MonInt:
                    if HitChance>50 and HitChance<101:
                        HitDmg=HitDmg*2
            MonHP=MonHP-HitDmg
            MP=MP-2
        if PlrAct=='1':
            HitDmg=Str
            if MonAmr==0:
                print('You hit the monster!')
            else:
                HitChance=rand.randrange(1,101)
                if MonAmr==Str*3 or MonAmr>Str*3:
                    print('You failed to hit the monster.')
                else:
                    if MonAmr==Str*2 or MonAmr>Str*2:
                        if HitChance>0 and HitChance<76:
                            print('The monster blocked some damage.')
                            HitDmg=25%HitDmg
                        if HitChance>75 and HitChance<101:
                            print('You hit the monster!')
                    else:
                        if MonAmr>Str or MonStr==Str:
                            if HitChance>0 and HitChance<51:
                                print('The monster blocked some damage.')
                                HitDmg=50%HitDmg
                            if HitChance>50 and HitChance<101:
                                print('You hit the monster!')
                        else:
                            if Str>MonAmr*2 or Str==MonAmr*2:
                                if HitChance>0 and HitChance<11:
                                    print('The monster blocked some damage.')
                                    HitDmg=90%HitDmg
                                if HitChance>10 and HitChance<101:
                                    print('You ran hit monster!')
                            else:
                                if Str>MonAmr:
                                    if HitChance>0 and HitChance<51:
                                        print('The monster blocked some damage.')
                                        HitDmg=75%HitDmg
                                    if HitChance>50 and HitChance<101:
                                        print('You hit the monster!')
            print(HitDmg)
            if HitDmg<1:
                HitDmg=1
            MonHP=MonHP-HitDmg
        if MonHP==0 or MonHP<0:
            MonDefeat=True
            print('You defeated the monster!')
            XP=XP+MonXP
            print('You now have '+str(XP)+' XP')
            Gold=Gold+MonGD
            print('You now have '+str(Gold)+' Gold')
        if MonDefeat==False:
            MonAttack=MonStr-Amr
            if MonAgl<Agl or MonAgl==Agl:
                chance=rand.randrange(1,101)
                if chance>0 and chance<51:
                    HP=HP-MonAttack
                if chance>50 and chance<101:
                    print('The monster missed!')
            if MonAgl>Agl:
                HP=HP-MonAttack
    input()
    Dungeon()

def Zone1Shop():
    global ShopItems
    global Inventory
    global Gold
    global BonusInt
    global BonusAgl
    global BonusStr
    global BonusAmr
    global Head
    global Body
    global Feet
    global Weapon
    print("""
    
    """)
    print('Welcome to the shop, \nyou can buy:')
    print(*ShopItems,sep='\n')
    print("Type 'Back' to return town.")
    UsrShp=input("""What would you like to buy?
    """)
    if UsrShp=='Back':
        StarterTown()
    else:
        if UsrShp=='Basic Armor':
            if '1- 10G-Basic Armor: ARM+1' in ShopItems:
                if Gold==10 or Gold>10:
                    Gold=Gold-10
                    ShopItems.remove('10G-Basic Armor: ARM+1')
                    Body='Basic Armor:ARM+1'
                    print('You now own Basic Armor!')
                else:
                    print('You dont have enough gold for that.')
        if UsrShp=='Basic Boots':
            if '2- 10G-Basic Boots: AGL+1'in ShopItems:
                if Gold==10 or Gold>10:
                    Gold=Gold-10
                    ShopItems.remove('10G-Basic Boots: AGL+1')
                    Feet='Basic Boots:AGL+1'
                    print('You now own Basic Boots!')
                else:
                    print('You dont have enough gold for that.')
        if UsrShp=='Lesser Pointy Hat':
            if '3- 10G-Lesser Pointy Hat: INT+1'in ShopItems:
                if Gold==10 or Gold>10:
                    Gold=Gold-10
                    ShopItems.remove('10G-Lesser Pointy Hat: INT+1')
                    Head='Lesser Pointy Hat:INT+1'
                    print('You now own Lesser Pointy Hat!')
                else:
                    print('You dont have enough gold for that.')
        if UsrShp=='Short Sword':
            if '4- 10G-Short Sword: STR+1'in ShopItems:
                if Gold==10 or Gold>10:
                    Gold=Gold-10
                    ShopItems.remove('10G-Short Sword: STR+1')
                    Weapon='Short Sword:STR+1'
                    print('You now own Short Sword!')
                    ShopItems.insert(3,'4- 20G-Basic Sword: STR+2')
                else:
                    print('You dont have enough gold for that.')
        if UsrShp=='Short Sword':
            if '4- 20G-Basic Sword: STR+2'in ShopItems:
                if Gold==20 or Gold>20:
                    Gold=Gold-20
                    ShopItems.remove('20G-Basic Sword: STR+2')
                    Weapon='Basic Sword:STR+2'
                    print('You now own Basic Sword!')
                else:
                    print('You dont have enough gold for that.')
        def BonusCheck():
            if not Head=='':
                BnsCal=Head.split(':')
                del BnsCal[0]
                BnsCal=''.join(BnsCal)
                BnsCal=BnsCal.split('+')
                del BnsCal[0]
                BnsCal=''.join(BnsCal)
                BonusInt=int(BnsCal)
            if not Body=='':
                BnsCal=Body.split(':')
                del BnsCal[0]
                BnsCal=''.join(BnsCal)
                BnsCal=BnsCal.split('+')
                del BnsCal[0]
                BnsCal=''.join(BnsCal)
                BonusAmr=int(BnsCal)
            if not Feet=='':
                BnsCal=Feet.split(':')
                del BnsCal[0]
                BnsCal=''.join(BnsCal)
                BnsCal=BnsCal.split('+')
                del BnsCal[0]
                BnsCal=''.join(BnsCal)
                BonusAgl=int(BnsCal)
            if not Weapon=='':
                BnsCal=Weapon.split(':')
                del BnsCal[0]
                BnsCal=''.join(BnsCal)
                BnsCal=BnsCal.split('+')
                del BnsCal[0]
                BnsCal=''.join(BnsCal)
                BonusStr=int(BnsCal)
        
        BonusCheck()
        Zone1Shop()

def StarterTown():
    global UsrImp
    print('')
    print('')
    print('You are in Starter Town \nYou can:')
    print("""    Go to the 'Shop'
    'Talk' to townsfolk
    Go to the 'Dungeon'
    Check your 'Stats'
    (If you need to, type 'Help' to get a understanding of how the game works)""")
    UsrImp=input()
    if UsrImp=='Shop':
        Zone1Shop()
    if UsrImp=='Help':
        Help()
    if UsrImp=='Stats':
        Stats()
    if UsrImp=='Dungeon':
        Dungeon()
    if UsrImp=='Talk':
        Talk()

def GameStart():
    global ShopItems
    global TrueStr
    global TrueAgl
    global TrueInt
    global GameZone
    global XPtillLvl
    ShopItems=['1- 10G-Basic Armor: ARM+1','2- 10G-Basic Boots: AGL+1','3- 10G-Lesser Pointy Hat: INT+1','4- 10G-Short Sword: STR+1']
    TrueStr=1
    TrueAgl=1
    TrueInt=1
    GameZone=1
    XPtillLvl=50
    StarterTown()



GameStart()