#
# Propriedades desejáveis:
#   Rápida
#   Deterministica
#   Aceita qualquer tipo de chave
#   Gera resultado sempre com mesma dimensão
#   Uniformemente distribuída
#

#
# Tentativas:
#  1. sum(ord(character) for character in text)      -> Só com strings. Fraca distribuição. Anagramas originam colisões.
#  2. sum(ord(character) for character in str(key))  -> Só com tipos com __str__. Não distingue entre tipos.
#  3. sum(ord(character) for character in repr(key)) -> Acrescenta apostrofo a "não strings" para as distinguir de nºs.
#  4. sum(index*ord(char) for index, char in enumerate(repr(key), 1)) -> Resolve anagramas!
#  5. sum(index*ord(char) for index, char in enumerate(repr(key).lstrip("'"), 1)) ->


def hash_function(key):
    return sum(
        index * ord(char)
        for index, char in enumerate(repr(key).lstrip("'"), start=1)
    ) % 100

h = hash_function(33)
print(h)
h = hash_function(33.33)
print(h)
h = hash_function("33")
print(h)
h = hash_function('33')
print(h)
h = hash_function(['33'])
print(h)
