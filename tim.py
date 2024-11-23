import time
import random
import alg
N = 10*10*10*10
M = [random.randint(1,100000) for i in range(N)]
Start = time.time()
alg.quick_sort(M)
Finish = time.time()
Res_msec = (Finish - Start)*1000



print (Res_msec)

