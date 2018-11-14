from multiprocessing import Pool
import numpy as np

'''
note: In commonly,function map_async for Pool only support one params of function
    if more params must be needed,that we can convert params list to tuple.
    the result from map and map_async is orderly, meanwhile, the result from appy
    and apply_async is not orderly.
'''

#step 1 params list to tuple
def add_foo((x, y, z)):
    return x+y, y+z, z+x

#step 2  instantiation pool
mp = Pool(5)

#step 3 convert data to tuple list
lst_x = np.random.randint(1, 10, 10)
lst_y = np.random.randint(10, 20, 10)
lst_z = np.random.randint(20, 30, 10)
lst = []
for i in range(len(lst_x)):
    lst.append((lst_x[i],lst_y[i],lst_z[i]))

#step 4 apply map_async
res = mp.map_async(add_foo, lst)
mp.close()
mp.join()
print 'success.\n'

print res._value

