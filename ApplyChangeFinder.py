import pandas as pd
from change_finder import ChangeFinder
import matplotlib.pyplot as plt


data = pd.read_csv('Xdados.txt', sep=" ", header=None)

print(data)


cf = ChangeFinder()


for x in range(51):
    coluna = data[x]

    plt.clf()

    scores = [cf.update(p) for p in coluna]

    plt.plot(scores)

    #plt.show()
    nome = str(x)+".png"
    plt.savefig(nome)



