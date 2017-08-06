word_list = ['hello','world','my','name','is','Anna']
char = 'o'

def findCharacter(list, char):
    new_list = []
    for word in word_list:
        if word.count(char) != 0:
            new_list.append(word)
    return new_list

new_list = findCharacter(word_list, char)

print new_list