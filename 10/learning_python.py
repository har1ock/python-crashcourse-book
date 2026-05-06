filename = "what_i_learn_in_python.txt"

with open(filename) as file_object:
    #for line in file_object:
        #line.replace('Python', 'Ruby')
        #print(line.rstrip())
    #content = file_object.read()
    lines = file_object.readlines()

what_i_learn = ''
for sentense in lines:
    sentense.replace('python', 'Ruby')
    what_i_learn += sentense.rstrip()

#print(content)
print(what_i_learn)
