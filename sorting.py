#input data
files    = open('generate.txt','r')
datas = [int(file) for file in files]
files.close()



#mencari min max (bisa memakai built in, bisa manual seperti ini)
maximal = -999
minimal =  999
for data in datas:
    if data > maximal:
        maximal = data
    elif data < minimal:
        minimal = data


#proses sorting
sort = [0 for x in range(maximal+1)]

for data in datas:
    sort[data]+= 1



#menulis data yang telah disorting
pos = 0
Files = open('results.txt','w')
for data in sort:
    if data > 0 :
        for i in range(data):
            Files.write(str(pos)+'\n')
    pos += 1
Files.close()
