class Neuron:
def  init (self, weights): self.weightv = weights self.activation = 0
def act(self, m, x): a = 0
for i in range(m):
a += x[i] * self.weightv[i] return a
class Network:
def   init  (self, a, b, c, d):
self.nrn = [Neuron(a), Neuron(b), Neuron(c), Neuron(d)] self.output = [0] * 4
def threshld(self, k): if k >= 0:
return 1 else:
return 0
def activation(self, patrn): for i in range(4):
for j in range(4):
print(f"nrb[{i}].weightv[{j}] is {self.nrn[i].weightv[j]}") self.nrn[i].activation = self.nrn[i].act(4, patrn) print(f"activation is {self.nrn[i].activation}")
self.output[i] = self.threshld(self.nrn[i].activation) print(f"output value is {self.output[i]}\n")
 
def main():
patrn1 = [1, 0, 1, 0]
wt1 = [0, -3, 3, -3]
wt2 = [-3, 0, -3, 3]
wt3 = [3, -3, 0, -3]
wt4 = [-3, 3, -3, 0]


print("\nTHIS PROGRAM IS FOR A HOPFIELD NETWORK WITH A SINGLE LAYER OF 4 FULLY INTERCONNECTED NEURONS. THE NETWORK SHOULD RECALL THE PATTERNS 1010 AND 0101 CORRECTLY.\n")

# Create the network by calling its constructor h1 = Network(wt1, wt2, wt3, wt4)
# Present a pattern to the network and get the activations of the neurons h1.activation(patrn1)
# Check if the pattern is recalled correctly and print the results for i in range(4):
if h1.output[i] == patrn1[i]:
print(f"pattern = {patrn1[i]} output = {h1.output[i]} component matches") else:
print(f"pattern = {patrn1[i]} output = {h1.output[i]} discrepancy occurred") print("\n")

patrn2 = [0, 1, 0, 1] h1.activation(patrn2)

for i in range(4):
if h1.output[i] == patrn2[i]:
print(f"pattern = {patrn2[i]} output = {h1.output[i]} component matches") else:
print(f"pattern = {patrn2[i]} output = {h1.output[i]} discrepancy occurred")
 

if  name  == " main ": main()
