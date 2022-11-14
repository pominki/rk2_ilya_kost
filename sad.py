'''Программа, проверяющая изограмма ли слово'''
outfile = open('stdin.txt', 'r')
string_ = outfile.read()
flag = 0
for i in range (len(string_)):
    for j in range (len(string_)):
        if string_[i] == string_[j] and i != j:
            flag = 1
if flag == 1:
    open('stdin.txt', 'w')
    infile = open('stdout.txt', 'w')
    infile.write('False')
else:
    infile = open('stdout.txt', 'w')
    infile.write('True')
