import matplotlib.pyplot as plt
import numpy as np
from change_finder import ChangeFinder
#
# # GERAÇÃO DO DATA SET 1



mu, sigma = 0.0, 1.0
ent1 = np.zeros((10000))
for i in range(10):
    print(mu)
    for j in range(1000):
        ent1[1000*i+j] = np.random.normal(mu, sigma)
    mu = mu + 9 - i

cf = ChangeFinder()

scores = [cf.update(p) for p in ent1]

#Remover comentário para exibir o score de mudança do CF
#plt.plot(scores)

#Remover comentário para exibir o dataset
#plt.plot(ent1)
plt.show()
#



a1 = 0.6
a2 = -0.5
ds1 = np.zeros((10000))
ds1[0] = ent1[0]
ds1[1] = ent1[1]
for i in range(2,10000):
    ds1[i] = a1*ds1[i-1] + a2*ds1[i-2] + ent1[i]
#plt.plot(ds1)

cf = ChangeFinder()

scores2 = [cf.update(p) for p in ent1]

#Remover comentário para exibir o score de mudança do CF
#plt.plot(scores2)

#Remover comentário para exibir o dataset
#plt.plot(ds1)

plt.show()
#


# # GERAÇÃO DO DATA SET 2
mu = 0.0
ent2 = np.zeros((10000))
for i in range(10):
    print(mu)
    for j in range(1000):
        sigma = 0.1/(0.01 + (10000 - (i*1000 + j))/10000)
        ent2[1000*i+j] = np.random.normal(mu, sigma)
    mu = mu + 1

cf = ChangeFinder()

scores3 = [cf.update(p) for p in ent2]

#Remover comentário para exibir o score de mudança do CF
#plt.plot(scores3)

#Remover comentário para exibir o dataset
#plt.plot(ent2)

plt.show()
#

a1 = 0.6
a2 = -0.5
ds2 = np.zeros((10000))
ds2[0] = ent1[0]
ds2[1] = ent1[1]
for i in range(2,10000):
    ds2[i] = a1*ds2[i-1] + a2*ds2[i-2] + ent2[i]
#plt.plot(ds2)

cf = ChangeFinder()

scores4 = [cf.update(p) for p in ds2]

#Remover comentário para exibir o score de mudança do CF
#plt.plot(scores4)

#Remover comentário para exibir o dataset
#plt.plot(ds2)


plt.show()
#

# # GERAÇÃO DO DATA SET 3
mu, sigma1, sigma3 = 0.0, 1.0, 3.0
ds3 = np.zeros((10000))
for i in range(10):
    if i in {0,2,4,6,8}:
        for j in range(1000):
            ds3[1000*i+j] = np.random.normal(mu, sigma1)
    else:
        for j in range(1000):
            ds3[1000*i+j] = np.random.normal(mu, sigma3) 
#plt.plot(ds3)

cf = ChangeFinder()

scores5 = [cf.update(p) for p in ds3]

#Remover comentário para exibir o score de mudança do CF
#plt.plot(scores5)

#Remover comentário para exibir o dataset
#plt.plot(ds3)

plt.show()

