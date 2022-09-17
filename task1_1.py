modern_family = ['CLaiRe_DunPhY', 'PHiL_dUnpHY', 'GLoRiA_PriTCheTt', 'CaMErOn_TuCKEr', 'StELLa']

X = enumerate(modern_family)

indices = [] 
characters = []

for i in X:
    indices.append(i[0])
    characters.append(i[1])

length = len(indices)

for i in range(length):
    element = characters[i]
    element = element.lower().replace('_', '-')
    characters[i] = element

def lambda_f(a):
    return len(a)

temp = map(lambda_f, characters)

k = zip(indices,temp)

for i in k:
    indices[i[0]] = sum(i)

indices.sort(reverse=True)

Phew_finally = {}

for i in range(length):
    Phew_finally[indices[i]] = characters[i]

print(Phew_finally)