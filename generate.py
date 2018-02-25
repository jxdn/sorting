import random

maxIterasi = 500000
maxUmur    = 79

Files = open('generate.txt','w')
[Files.write(str(random.randint(1,79))+'\n') for i in range (0,maxIterasi)]
Files.close()

