l = ['magical unicorns',19,'hello',98.98,'world']

sentence = ""
sum = 0
type = ""
for val in l:
    if isinstance(val, float):
        sum += val
    elif isinstance(val, str):
        sentence += val + " "

if sum and sentence:
    type = "mixed"
elif sum:
    type = "integer"
elif sentence:
    type = "string"
print sentence
print "Sum: " + str(sum)
print "The list you entered is of " + type