import numpy as np
voticos=np.random.randint(high=31,low=1, size=5000)
organizaditos=np.unique_counts(voticos).counts
print("Conteo de votos: ",organizaditos, "\n")
candidatos_organizados = np.argsort(organizaditos)
print("Candidatos normal", candidatos_organizados, "\n")

for i in candidatos_organizados[::-1]:
    print("candidato ",i+1, "votos: ", organizaditos[i])