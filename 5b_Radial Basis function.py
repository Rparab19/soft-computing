import numpy as np
from scipy.linalg import norm, pinv from matplotlib import pyplot as plt

class RBF:
def  init (self, indim, numCenters, outdim): self.indim = indim
self.outdim = outdim self.numCenters = numCenters



self.centers = [np.random.uniform(-1, 1, self.indim) for _ in range(self.numCenters)] self.beta = 8
self.W = np.random.random((self.numCenters, self.outdim))


def _basisfunc(self, c, d):
''' Radial basis function (RBF) for a given center and data point ''' assert len(d) == self.indim
return np.exp(-self.beta * norm(c - d) ** 2)

def _calcAct(self, X):
''' Calculate activations of RBFs for each input point in X ''' G = np.zeros((X.shape[0], self.numCenters), float)
for ci, c in enumerate(self.centers): for xi, x in enumerate(X):
G[xi, ci] = self._basisfunc(c, x)
 
return G


def train(self, X, Y):
''' Train the RBF network using the input X and output Y '''


rnd_idx = np.random.permutation(X.shape[0])[:self.numCenters] self.centers = [X[i, :] for i in rnd_idx]
print("Centers:", self.centers)



G = self._calcAct(X) print("Activations:", G)



self.W = np.dot(pinv(G), Y) def test(self, X):
G = self._calcAct(X) Y = np.dot(G, self.W) return Y

# Main program
if   name   == '  main  ': n = 100
x = np.linspace(-1, 1, n).reshape(n, 1)



y = np.sin(3 * (x + 0.5) ** 3 - 1) rbf = RBF(1, 10, 1)
rbf.train(x, y)
 
z = rbf.test(x) plt.figure(figsize=(12, 8))
plt.plot(x, y, 'k-', label="Original Data")
plt.plot(x, z, 'r-', linewidth=2, label="Learned Model") plt.plot(rbf.centers, np.zeros(rbf.numCenters), 'gs', label="RBF Centers") for c in rbf.centers:
cx = np.arange(c - 0.7, c + 0.7, 0.01)
cy = [rbf._basisfunc(np.array([cx_]), np.array([c])) for cx_ in cx] plt.plot(cx, cy, '-', color='gray', linewidth=0.2)

plt.xlim(-1.2, 1.2) plt.legend() plt.show()
