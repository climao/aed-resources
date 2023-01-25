#
# Simple hash table implementation.
# Uses Linear probing for collision resolution.
#
# Author: CJL
#

class Pair:

    def __init__(self, key, value):
        """
        Construtor. O(1)

        :param key: Chave
        :param value: Valor
        """
        self.key = key
        self.value = value

    def __str__(self):
        """
        Redefine str(). O(1)

        :return: representação de um Pair como uma string.
        """
        return "(" + str(self.key) + ", " + str(self.value) + ")"


class HashTable:
    TOMBSTONE = object()

    def __init__(self, capacity):
        """
        Construtor. O(1)

        :param capacity: dimensão da tabela de hash.
        """
        self.max_size = capacity                # Hash table capacity
        self.entries = [None] * self.max_size   # Hash table entries. This is faster than a list of empty lists.
        self.size = 0                           # Current hash table size.

    def hash_func(self, key):
        """
        Calcula código de hash a partir de uma chave. O(1)
        Função de Hash h2(h1(k)) -> h1 = Código de hash; h2 -> função de compressão

        :param key: Chave
        :return: Código de hash.
        """
        return sum(index*ord(char) for index, char in enumerate(repr(key).lstrip("'"), start=1)) % self.max_size

    def put(self, key, value):
        """
        Adiciona entrada na tabela de hash. O(n), n é a dimensão da lista na entrada

        :param key: Chave.
        :param value: Valor.
        :return: None.
        """
        i = self.hash_func(key)

        if self.entries[i] is None or self.entries[i] == self.TOMBSTONE:
            self.entries[i] = Pair(key, value)
            self.size += 1
        else:
            # Colisão!
            counter = 0
            while self.entries[i] is not None and self.entries[i].key != key and counter < self.max_size:
                i = (i + 1) % self.max_size

            if counter == self.max_size:
                raise RuntimeError("A tabela de hash está cheia!")

            if self.entries[i] is None or self.entries[i] == self.TOMBSTONE:
                self.entries[i] = Pair(key, value)
                self.size += 1
            else:
                self.entries[i].value = value

    def get(self, key):
        """
        Devolve o valor do item com a chave especificada. , Time O(n), n é a dimensão da lista na entrada.

        :param key: Chave.
        :return: valor associado à chave especificada ou None se não existir.
        """
        i = self.hash_func(key)

        if self.entries[i] is None:
            return None
        else:
            counter = 0
            while self.entries[i] == self.TOMBSTONE or (self.entries[i] is not None and self.entries[i].key != key and counter < self.max_size):
                i = (i + 1) % self.max_size
                counter += 1

            if counter < self.max_size:
                # Encontrei key ou None
                if self.entries[i] is None:
                    return None
                else:
                    return self.entries[i].value
            else:
                # Procurei em todas as posições e não encontrei
                return None

    def delete(self, key):
        """
        Apaga entrada definida pela chave especificada. O(n), n é a dimensão da lista na entrada.

        :param key: Chave.
        :return: None
        """
        i = self.hash_func(key)

        if self.entries[i] is None:
            return None

        counter = 0
        while self.entries[i] != self.TOMBSTONE and self.entries[i] is not None and self.entries[i].key != key and counter < self.max_size:
            i = (i + 1) % self.max_size
            counter += 1

        if counter < self.max_size:
            # Encontrei key ou None
            if self.entries[i] is None:
                return
            else:
                self.entries[i] = self.TOMBSTONE
                self.size -= 1
                return
        else:
            # Procurei em todas as posições e não encontrei
            return

    def __len__(self):
        return self.size

    def print(self) :
        """
        Escreve na consola toda a tabela de hash chamando print_list.
        O(m*n), m é o número de entradas, n é a dimensão da maior lista.

        :return: None
        """
        for i in range(0 , self.max_size):
            l = self.entries[i]
            if l is not None:
                self.print_list(l)

    def print_list(self, l):
        """
        Escreve conteúdo de uma lista. O(n), n é a dimensão da lista.

        :param l: lista
        :return: None.
        """
        if len(l) == 0:
            return
        for pair in l:
            print(str(pair), end =" ")
        print()


def main():
    DIM_HASH_TABLE = 100
    MAX_ITEMS      = 100

    print("*******************************************")
    print("* A testar implementação da Hash Table... *")
    print("*******************************************")

    ht = HashTable(DIM_HASH_TABLE)

    # Insere MAX_ITEMS pares chave/valor
    for i in range(MAX_ITEMS):
        ht.put("KEY" + str(i), "VALUE " + str(i))
        assert ht.get("KEY" + str(i)) == "VALUE " + str(i)
    assert len(ht) == MAX_ITEMS
    print("* Inserção de valores com sucesso!        *")

    #############################################################################################
    # Descomentar linha seguinte para mostrar entradas da tabela de hash. Permite ver colisões. #
    #############################################################################################
    #ht.print()

    # Assegura que todos os pares chave/valor inseridos estão na tabela de hash
    for i in range(MAX_ITEMS):
        v = ht.get("KEY" + str(i))
        assert v == "VALUE " + str(i)
    print("* Pesquisa de chaves com sucesso!         *")

    # Altera os valores associados às chaves
    for i in range(MAX_ITEMS):
        ht.put("KEY" + str(i), "MODIFIED VALUE " + str(i))
    assert len(ht) == MAX_ITEMS
    print("* Modificação de valores com sucesso!     *")

    # Assegura que todos os pares chave/valor estão na tabela de hash e não há duplicados
    for i in range(MAX_ITEMS):
        v = ht.get("KEY" + str(i))
        assert v == "MODIFIED VALUE " + str(i)
    print("* Chaves não podem ser duplicadas!        *")

    # Apaga todas as entradas e garante que foram eliminadas da tabela de hash
    for i in range(MAX_ITEMS):
        ht.delete("KEY" + str(i))
        assert ht.get("VALUE " + str(i)) is None
    assert len(ht) == 0
    print("* Valores apagados com sucesso!           *")

    print("*******************************************")
    print("* Testes concluidos com sucesso.          *")
    print("*******************************************")


if __name__ == "__main__":
    main()
