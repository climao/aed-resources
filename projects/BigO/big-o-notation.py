#
# Permite visualizar diferentes funções tipicamente usadas com a notação O-Grande.
#
# Date created: 22/03/2017
#

#  Big-O  |	Name
# --------+---------------
# 1       | Constant
# log(n)  |	Logarithmic
# n   	  | Linear
# nlog(n) |	Log Linear
# n^2 	  | Quadratic
# n^3 	  | Cubic
# 2^n 	  | Exponential

import numpy as np
import matplotlib.pyplot as plt


# Tipo de gráfico a usar
plt.style.use('bmh')

# Definir dados das curvas a traçar.
n = np.linspace(1, 50, 1000)
labels = ['O(1) - Constante', 'O(log n) - Logarítmica', 'O(n) - Linear', 'O(n.log n) - Linear Logarítmica', 'O(n^2) - Quadrática', 'O(n^3) - Cúbica', 'O(2^n) - Exponencial']
big_o = [np.ones(n.shape), np.log(n), n, n * np.log(n), n**2, n**3, 2**n]

# Setup do plot
plt.figure(figsize=(16, 9))                 # formato da imagem
plt.ylim(0, 50)                             # Tamanho do eixo dos y (x é determinado por n)

for i in range(len(big_o)):
    plt.plot(n, big_o[i], label=labels[i])

plt.legend(loc=0)
plt.ylabel('Tempo de Execução')
plt.xlabel('Dimensão dos dados de entrada')
# plt.savefig('big-o-notation.png')   # Remover comentário para gerar ficheiro png.
plt.show()
