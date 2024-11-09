import pyautogui
import time

Enchants = 1110, 268
Tiers = 1006, 270
Categories = 811, 269

BlackzoneMarket = 762, 246
RoyalMarket = 1221, 262



Tier4 = 984, 404
Tier5 = 980, 432
Tier6 = 977, 459
Tier7 = 983, 486

Armors = 793, 350
MagicWeapons = 803, 592
MeeleWeapons = 800, 647
OffHand = 804, 701
RangedWeapons = 803, 781

EnchantAll = 1103, 297
Enchant0 = 1114, 321
Enchant1 = 1117, 348
Enchant2 = 1117, 376
Enchant3 = 1118, 409
Enchant4 = 1118, 429


print("Tier4, Tier5, Tier6, Tier7")
tier = input("Input the tier you would like to target: \n").lower()


print("Armors, MagicWeapons, MeeleWeapons, OffHand, RangedWeapons")
Category = input("Input the category you would like to traget: \n").lower()


print("EnchantAll, Enchant0, Enchant1, Enchant2, Enchant3, Enchant4")
Enchantment = input("Input the enchantment tier you would like to target: \n").lower()

print("How many do you want to set to buy for each item?")
HowMuch = int(input("Enter the amount: \n")) 

WhatMarket = input("BlackzoneMarket or RoyalMarket?: \n").lower()

def WhatIWant(Category, Tier, Enchant):
    global STier
    global SCategory
    global SEnchant
    pyautogui.moveTo(Tiers)
    time.sleep(0.05)
    LeftClick()
    pyautogui.moveTo(STier)
    time.sleep(0.05)
    LeftClick()


    pyautogui.moveTo(Categories)
    time.sleep(0.05)
    LeftClick()
    pyautogui.moveTo(SCategory)
    time.sleep(0.05)
    LeftClick()


    pyautogui.moveTo(Enchants)
    time.sleep(0.05)
    LeftClick()
    pyautogui.moveTo(SEnchant)
    time.sleep(0.05)
    LeftClick()



def HoldKey(key, seconds):
    pyautogui.keyDown(key)
    time.sleep(seconds)
    pyautogui.keyUp(key)

def GetMousePosition():
    print(pyautogui.position())
    time.sleep(0.5)

def LeftClick():
    pyautogui.leftClick()
    time.sleep(0.1)

def ScrollForward():
    pyautogui.moveTo(962, 567)
    pyautogui.dragTo(961, 493, 1)
    time.sleep(0.1)
    
def MoveMouseToPosition(XCordinate, YCordinate):
    pyautogui.moveTo(XCordinate, YCordinate)
    time.sleep(0.1)
    LeftClick()

def CountDownOnStart():
    print("Starting")
    for i in range(0, 5):
        print(i+1)
        time.sleep(1)
    print("Go!")

def SetBuyOrders():
    time.sleep(0.1)
    MoveMouseToPosition(1273, 426)
    time.sleep(0.1)
    for i in range(0, HowMuch-1):
        MoveMouseToPosition(1130, 603)
        time.sleep(0.1)
    MoveMouseToPosition(1127, 634)
    time.sleep(0.1)
    MoveMouseToPosition(1138, 731)
    time.sleep(0.1)
    MoveMouseToPosition(794, 551)

def CheckSelection(Category, tier, Enchantment):
    global STier
    global SCategory
    global SEnchant
    if tier == "tier4":
        STier = Tier4
    if tier == "tier5":
        STier = Tier5
    if tier == "tier6":
        STier = Tier6
    if tier == "tier7":
        STier = Tier7


    if Category == "armors":
        SCategory = Armors
    if Category == "magicweapons":
        SCategory = MagicWeapons
    if Category == "meeleweapons":
        SCategory = MeeleWeapons
    if Category == "offhand":
        SCategory = OffHand
    if Category == "rangedweapons":
        SCategory = RangedWeapons


    if Enchantment == "enchantall":
        SEnchant = EnchantAll
    if Enchantment == "enchant0":
        SEnchant = Enchant0
    if Enchantment == "enchant1":
        SEnchant = Enchant1
    if Enchantment == "enchant2":
        SEnchant = Enchant2
    if Enchantment == "enchant3":
        SEnchant = Enchant3
    if Enchantment == "enchant4":
        SEnchant = Enchant4



def main():

    #FailSafe Move Mouse Top Left To Abort
    pyautogui.FAILSAFE = True

    #Countdown timer
    CountDownOnStart()

    #OpenMarket
    if WhatMarket == "blackzonemarket":
        MoveMouseToPosition(762, 246)
    if WhatMarket == "royalmarket":
        MoveMouseToPosition(1221, 262)

    #OpenBuyCategory
    MoveMouseToPosition(1383, 493)
    #Choose a tier and category
    CheckSelection(Category, tier, Enchantment)
    WhatIWant(SCategory, STier, SEnchant)

    while True:
        SetBuyOrders()
        time.sleep(0.1)
        ScrollForward()


if __name__ == "__main__":
    main()