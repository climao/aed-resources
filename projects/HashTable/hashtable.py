#
# Simple hash table implementation.
#
# Author: CJL
#
class Pair:
    # Construtor, Time O(1), Space O(1)
    def __init__(self, key, val):
        self.key = key
        self.value = val

    # Verifica se par (k,v) é igual a outro, comparando os valores de k e v, não os objetos, Time O(1), Space O(1)
    def equals(self, entry):
        if str(self.key) != str(entry.key):
            return False
        return str(self.value) == str(entry.value)

    # Redefine str(), Time O(1), Space O(1)
    def __str__(self):
        return "(" + str(self.key) + ", " + str(self.value) + ")"


class HashTable:
    # Construtor, Time O(1), Space O(1)
    def __init__(self, capacity):
        self.max_size = capacity
        self.entries = [None] * self.max_size

    # Função de Hash. Calcula código de hash a partir de uma chave, Time O(1), Space O(1)
    def hash_func(self, key):
        return int(key) % self.max_size

    # Adiciona entrada na tabela de hash, Time O(1), Space O(1)
    def put(self, key, value):
        x = self.hash_func(key)

        if self.entries[x] is None:
            self.entries[x] = []
        l = self.entries[x]
        pair = Pair(key, value)
        l.append(pair)

    # Apaga entrada definida pela chave especificada, Time O(n), Space O(n), n é a dimensão da lista na entrada
    def delete(self, key) :
        x = self.hash_func(key)
        if self.entries[x] is None:
            return
        l = self.entries[x]
        l2 = []
        for pair in l:
            if str(pair.key) != str(key):
                l2.append(pair)
        self.entries[x] = None if len(l2) == 0 else l2

    # Devolve valor a partir da chave, Time O(n), Space O(1), n é a dimensão da lista na entrada
    def get(self, key):
        x = self.hash_func(key)

        if self.entries[x] is None:
            return None
        l = self.entries[x]
        for pair in l:
            if pair.key == key:
                return pair.value
        return None

    # Printa toda a tabela de hash chamando print_list, Time O(m*n), Space O(1),
    # m é o número de entadas, n é a dimensão máxima da lista
    def print(self) :
        for i in range(0 , self.max_size):
            l = self.entries[i]
            if l is not None:
                self.print_list(l)

    # Printa a lista numa entrada, Time O(n), Space O(1), n é a dimensão da lista
    def print_list(self, l):
        if len(l) == 0:
            return
        for pair in l:
            print(str(pair) , end =" ")
        print()


ht = HashTable(100)
ht.put("SLB", "Sport Lisboa e Benfica")
ht.put("WHO", "World Health Organization")
ht.put("JSON", "JavaScript Object Notation")
ht.put("UNICEF", "United Nations Children’s Fund")
ht.print()
