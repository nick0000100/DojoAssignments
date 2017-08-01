my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

def toTuples(dict):
    newList = []
    for key in dict:
        newTuple = (key, dict[key])
        newList.append(newTuple)
    print newList

toTuples(my_dict)