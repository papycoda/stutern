def isOldEnoughToDrink(num,**country):
    if country == "us":
        age=21 
    else:
        age = 18
    
    if num<= age:
        return (False)
    else :
        return  (True)

result = isOldEnoughToDrink(16)
print (result)
result = isOldEnoughToDrink(18)
print (result)
result = isOldEnoughToDrink(19)
print (result)
result = isOldEnoughToDrink(26)
print (result)


def isOldEnoughToDrinkAndDrive(num):
    #call the isOldEnoughToDrink function and check the age, noting whether they are even allowed to drink, then parse it with the factual statemnt that "it is illegal regardless of the age to drink and drive"
    #or you can just brute force your way and return false regardless of age.
    res = isOldEnoughToDrink(num,country="us")
    if res== False:
        return("This person shouldn't even be drinking let alone driving, IT IS ILLEGAL TO DRINK AND DRIVE!!!")
    else:
        return("FALSE, While this peron is definitely old enough to drink, It is expected that they should also be wise enough to know, IT IS ILLEGAL TO DRINK AND DRIVE!!!")

result = isOldEnoughToDrinkAndDrive(16)
print (result)
result = isOldEnoughToDrinkAndDrive(18)
print (result)
result = isOldEnoughToDrinkAndDrive(19)
print (result)
result = isOldEnoughToDrinkAndDrive(22)
print (result)
result = isOldEnoughToDrinkAndDrive(26)
print (result)


ahmed ={'age':45}
def getProperty(obj, key):
    if key in obj:
        return (obj[key])
    else:
        return ("undefined")



get1 =getProperty(ahmed,'age')
print(get1)


def addProperty(obj, key):
    if key not in obj:
        obj[key] = True
        return (obj[key])
    else:
        return ("already existing")

add1 = addProperty(ahmed, "isHuman")
#print(ahmed)
print(add1)


def isPersonOldEnoughToDrinkAndDrive(obj):
    num = getProperty(obj,"age")
    ans = isOldEnoughToDrinkAndDrive(num)
    return (ans)

fam = isPersonOldEnoughToDrinkAndDrive(ahmed)
print(fam)


def computeAverageLengthOfWords(*words):
    wordbag = list(words)
    tlow = [len(word) for word in wordbag]
    res = (float(sum(tlow)) / len(tlow))
    return res

animals = computeAverageLengthOfWords("cow","ram")
print(animals)

def transformFirstAndLast(arr):
    fal = { arr[0]: arr[-1] }
    return fal

arr =['Queen', 'Elizabeth', 'Of Hearts', 'Beyonce']
sad = transformFirstAndLast(arr)
print (sad)
arr =['Kevin', 'Bacon', 'Love', 'Hart', 'Costner', 'Coleman']
sad = transformFirstAndLast(arr)
print (sad)
# print(arr) to show, nothing changed

def getAllKeys(obj):
    skipper= list(obj)
    print(skipper)

getAllKeys(ahmed)