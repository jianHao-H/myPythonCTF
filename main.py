

file = open('./abc.txt', 'w')
for i in range(97,123):
    file.write(chr(i) + '\n')

for j in range(65,91):
    file.write(chr(j) + '\n')

file.close()