name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def makeDictionary(arr1, arr2):
    new_dict = {}
    for i in range(len(arr1)):
        new_dict[arr1[i]] = arr2[i]
    return new_dict

print makeDictionary(name, favorite_animal)
