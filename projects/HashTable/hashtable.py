#
# Simple hash table implementation.
#
# Author: CJL
#

class Pair:
    # Time O(1), Space (1)
    def __init__(self, key, value):
        self.key = key
        self.value = value

    # Verifica se par (k,v) é igual a outro, comparando os valores de k e v, não os objetos, Time O(1), Space O(1)
    def equals(self, other_pair):
        if str(self.key) != str(other_pair.key):
            return False
        return str(self.value) == str(other_pair.value)

    # Redefine str(), Time O(1), Space O(1)
    def __str__(self):
        return "(" + str(self.key) + ", " + str(self.value) + ")"


class HashTable:
    def __init__(self, capacity):
        self.max_size = capacity
        self.entries = [None] * self.max_size

    # Função de Hash. Calcula código de hash a partir de uma chave, Time O(1), Space O(1)
    def hash_func(self, key):
        return sum(index*ord(char) for index, char in enumerate(repr(key).lstrip("'"), start=1)) % self.max_size

    # Adiciona entrada na tabela de hash, Time O(1), Space O(1)
    def put(self, key, value):
        i = self.hash_func(key)
        if self.entries[i] is None:
            self.entries[i] = []
        l = self.entries[i]    # Devolve valor a partir da chave, Time O(n), Space O(1), n é a dimensão da lista na entrada
        pair = Pair(key, value)
        for p in l:
            if p.key == key:
                p.value = value
                return
        l.append(pair)

    def get(self, key):
        i = self.hash_func(key)
        if self.entries[i] is None:
            return None
        l = self.entries[i]
        for pair in l:
            if pair.key == key:
                return pair.value
        return None

    # Apaga entrada definida pela chave especificada, Time O(n), Space O(n), n é a dimensão da lista na entrada
    def delete(self, key):
        i = self.hash_func(key)
        if self.entries[i] is None:
            return
        l = self.entries[i]
        l2 = []
        for pair in l:
            if str(pair.key) != str(key):
                l2.append(pair)
        self.entries[i] = None if len(l2) == 0 else l2

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
            print(str(pair), end =" ")
        print()


def main():
    DIM_HASH_TABLE = 100
    MAX_ITEMS      = 100

    print("******************************************")
    print("* A testar implmentação da Hash Table... *")
    print("******************************************")

    ht = HashTable(DIM_HASH_TABLE)

    # Insere MAX_ITEMS pares chave/valore
    for i in range(MAX_ITEMS):
        ht.put("KEY" + str(i), "VALUE " + str(i))

    # Assegura que todos os pares chave/valor estão na tabela de hash
    for i in range(MAX_ITEMS):
        v = ht.get("KEY" + str(i))
        assert v == "VALUE " + str(i)

    # Alterar os valores associados às chaves
    for i in range(MAX_ITEMS):
        ht.put("KEY" + str(i), "MODIFIED VALUE " + str(i))

    # Assegura que todos os pares chave/valor estão na tabela de hash
    for i in range(MAX_ITEMS):
        v = ht.get("KEY" + str(i))
        assert v == "MODIFIED VALUE " + str(i)

    # Apaga todas as chaves e garante que desaparecem da tabela de hash
    for i in range(MAX_ITEMS):
        ht.delete("KEY" + str(i))
        assert ht.get("VALUE " + str(i)) is None

    ht.print()

    print("******************************************")
    print("* Concluido com sucesso                  *")
    print("******************************************")

if __name__ == "__main__":
    main()
