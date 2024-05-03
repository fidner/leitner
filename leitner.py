import datetime
from time import sleep

flashcards = {
    "USA": "country",
    "Europe": "continent",
    "South Africa": "country",
    "Australia": "continent",
    "America": "continent",
    "Pakistan": "country"
}

day = datetime.datetime.now().strftime("%A")

everyday = {}
tuesThur = {}
fri = {}

e = "everyday.txt"
t = "tuesthur.txt"
f = "fri.txt"

def updateDict(file, d):
    with open(file, "r") as file:
        c = file.readlines()
        for line in c:
            k = line.strip() 
            if k:
                v = flashcards[k] 
                d[k] = v

def change(file, i):
    with open(file, "w") as file:
        for item in i:
            file.write(f"{item}\n")

updateDict(e, everyday)
updateDict(t, tuesThur)
updateDict(f, fri)

def mainCode(cDict, ncDict):
    for q in flashcards:
        sleep(0.5)
        if q in cDict:
            a = input(f"Continent or country: {q}?\n")
            sleep(0.5)
            if a.lower() == flashcards[q]:
                print("Correct")
                ncDict[q] = cDict[q]
                del cDict[q]
            else:
                print("Incorrect")
                cDict[q] = ncDict[q]
                del ncDict[q]
    sleep(0.5)
    change(e, everyday.keys())
    change(t, tuesThur.keys())
    change(f, fri.keys())

if day == "Tuesday" or day == "Thursday":
    mainCode(everyday, tuesThur)
elif day == "Friday":
    mainCode(everyday, tuesThur, fri)

sleep(0.5)
print("Done for today.")