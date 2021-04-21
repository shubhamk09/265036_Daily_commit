import numpy as np
np.set_printoptions(legacy='1.13')
st = input()
li = st.split()
li = [float(i) for i in li]
print(np.floor(li))
print(np.ceil(li))
print(np.rint(li))
