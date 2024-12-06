import numpy as np


class ART:
def  init (self, n=5, m=10, rho=.5): # Comparison layer
self.F1 = np.ones(n) # Recognition layer self.F2 = np.ones(m)
# Feed-forward weights
self.Wf = np.random.random((m,n)) # Feed-back weights
self.Wb = np.random.random((n,m)) # Vigilance
self.rho = rho
# Number of active units in F2 self.active = 0

def learn(self, X):


self.F2[...] = np.dot(self.Wf, X)
I = np.argsort(self.F2[:self.active].ravel())[::-1]


for i in I:
d = (self.Wb[:,i]*X).sum()/X.sum() if d >= self.rho:
self.Wb[:,i] *= X
 
self.Wf[i,:] = self.Wb[:,i]/(0.5+self.Wb[:,i].sum()) return self.Wb[:,i], i

if self.active < self.F2.size: i = self.active self.Wb[:,i] *= X
self.Wf[i,:] = self.Wb[:,i]/(0.5+self.Wb[:,i].sum()) self.active += 1
return self.Wb[:,i], i return None,None
if   name   == '  main  ':


np.random.seed(1)


network = ART( 5, 10, rho=0.5) data = [
"  O ", " O O", "	O", " O O",
"	O", " O O", "	O", " OO O",
" OO ", " OO O", " OO ", "OOO ",
"OO ", "O	", "OO ", "OOO ", "OOOO ", "OOOOO", "O	", " O ",
" O ", " O ", "	O", " O O", " OO O",
" OO ", "OOO ", "OO ", "OOOO ", "OOOOO"
]
X = np.zeros(len(data[0])) for i in range(len(data)):
 
for j in range(len(data[i])): X[j] = (data[i][j] == 'O')
Z, k = network.learn(X) print("|%s|"%data[i],"-> class", k)
