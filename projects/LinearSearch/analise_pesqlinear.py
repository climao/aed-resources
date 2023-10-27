#
# Avaliação dos algoritmos de pesquisa linear.
#
# Cada algoritmo é avaliado no melhor (pesquisa de valor existente no array) e no pior (pesquisa de valor
# não existente no array) caso. Notar que o array é sempre o mesmo, qulquer que seja a dimensão.
#
# IMPORTANTE: Não esquecer de ajustar os eixos verticais para que gráficos sejam comparáveis.
#
#
# UC: Algoritmos e estruturas de dados.
# Autor: Carlos Limão
# Data: 22/10/2023
#

import profile
import pesqlinear

#################################################################################################################
# A função profile.profile_algorithm() invoca o algoritmo especificado com apenas um parâmetro: um array/lista.
#
# As funções seguintes limitam-se a invocar os algoritmos definidos no módulo pesqlinear com os três parâmetros
# necessários.
#
#################################################################################################################

################################################################################################################
# As funções seguintes ilustram o melhor caso, procurando valor existente no array.
################################################################################################################
def avaliacao_pesquisa_linear_melhor_caso(arr):
    pesqlinear.pesquisa_linear(arr, len(arr), arr[ns[0] - 1])


def avaliacao_pesquisa_linear_melhorada_melhor_caso(arr):
    pesqlinear.pesquisa_linear_melhorada(arr, len(arr), arr[ns[0] - 1])


def avaliacao_pesquisa_linear_com_sentinela_melhor_caso(arr):
    pesqlinear.pesquisa_linear_com_sentinela(arr, len(arr), arr[ns[0] - 1])

################################################################################################################
# As funções seguintes ilustram o pior caso, procurando valor não existente no array.
################################################################################################################
def avaliacao_pesquisa_linear_pior_caso(arr):
    pesqlinear.pesquisa_linear(arr, len(arr), ns[-1] + 1)


def avaliacao_pesquisa_linear_melhorada_pior_caso(arr):
    pesqlinear.pesquisa_linear_melhorada(arr, len(arr), ns[-1] + 1)


def avaliacao_pesquisa_linear_com_sentinela_pior_caso(arr):
    pesqlinear.pesquisa_linear_com_sentinela(arr, len(arr), ns[-1] + 1)


# Dimensões das listas de números a usar para invocar os algoritmos especificados.
ns = [10000000, 11000000, 12000000, 13000000, 14000000, 15000000, 16000000, 17000000, 18000000, ]


profile.profile_algorithm(algorithm=avaliacao_pesquisa_linear_melhor_caso,
                          input_sizes=ns,
                          algorithm_name="Pesquisa Linear - Melhor caso",
                          can_repeat=False)

profile.profile_algorithm(algorithm=avaliacao_pesquisa_linear_melhorada_melhor_caso,
                          input_sizes=ns,
                          algorithm_name="Pesquisa Linear Melhorada - Melhor caso",
                          can_repeat=False)

profile.profile_algorithm(algorithm=avaliacao_pesquisa_linear_com_sentinela_melhor_caso,
                          input_sizes=ns,
                          algorithm_name="Pesquisa Linear com Sentinela - Melhor caso",
                          can_repeat=False)

#######################################################################################

profile.profile_algorithm(algorithm=avaliacao_pesquisa_linear_pior_caso,
                          input_sizes=ns,
                          algorithm_name="Pesquisa Linear - Pior caso",
                          can_repeat=False)

profile.profile_algorithm(algorithm=avaliacao_pesquisa_linear_melhorada_pior_caso,
                          input_sizes=ns,
                          algorithm_name="Pesquisa Linear Melhorada - Pior caso",
                          can_repeat=False)

profile.profile_algorithm(algorithm=avaliacao_pesquisa_linear_com_sentinela_pior_caso,
                          input_sizes=ns,
                          algorithm_name="Pesquisa Linear com Sentinela - Pior caso",
                          can_repeat=False)
