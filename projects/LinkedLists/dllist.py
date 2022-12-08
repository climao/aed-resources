#
# Lista Duplamente Ligada.
#
# Autor: CJL
# Data: Setembro 2022
#
import sys


# Nó de uma Lista Duplamente Ligada (LDL).
class Node:

    def __init__(self, data=None, next=None, prev=None):
        """
        Construtor de um nó de uma LDL.
        Inicializa os campos do nó.

        :param data: os dados a armazenar no nó.
        :param next: o próximo nó na lista. None se não existir.
        :param prev: o nó anterior na lista. None se não existir.
        """
        self.data = data
        self.next = next
        self.prev = prev


# Lista Duplamente Ligada (LDL).
class DoublyLinkedList:

    def __init__(self):
        """
        Construtor de uma LDL.
        Inicializa os campos da lista.
        """
        self._head = None
        self._tail = None
        self._size = 0

    def insert_before(self, data, node):
        """
        Insere um novo nó, antes do nó especificado.
        O algoritmo usado garante que esta operação é O(1).

        :param data: dados a inserir.
        :param node: o nó, existente na lista, antes do qual inserir.
        :return: o novo nó, que foi inserido na lista.
        """
        if node is not None:
            new_node = Node(data, node, node.prev)
            if node.prev:
                node.prev.next = new_node
            node.prev = new_node
            if node == self._head:
                self._head = new_node
            self._size += 1
            return node
        else:
            raise RuntimeError("O nó não existe!")

    def insert_after(self, data, node):
        """
        Insere após o nó especificado.

        :param data: dados a inserir.
        :param node: o nó depois do qual inserir.
        :return: None
        """
        new_node = Node(data, node.next, node)
        node.next.prev = new_node
        node.next = new_node
        if new_node.next is None:
            self._tail = new_node
        self._size += 1

    def insert_head(self, data):
        """
        Inserir à cabeça da LDL.

        :param data: dados a inserir.
        :return:  None
        """
        if self._head:
            new_node = Node(data, self._head)
            self._head.prev = new_node
            self._head = new_node
        else:
            self._head = self._tail = Node(data)
        self._size += 1

    def insert_tail(self, data):
        """
        Inserir no fim da LSL.

        :param data: dados a inserir.
        :return: None
        """
        new_node = Node(data)
        if self._tail:
            self._tail.next = new_node
            new_node.prev = self._tail
            self._tail = new_node
        else:
            self._head = self._tail = new_node
        self._size += 1

    def remove_head(self):
        """
        Remove o elemento à cabeça da lista.

        :return: None
        """
        if self._head:
            if self._head.next:
                self._head.next.prev = None
            self._head = self._head.next
            if self._head is None:
                self._tail = None
            self._size -= 1
        else:
            raise RuntimeError("A lista está vazia!")

    def remove_tail(self):
        """
        Remove elemento na cauda da lista.

        :return: None
        """
        if self._tail:
            if self._tail.prev:
                self._tail.prev.next = None
                self._tail = self._tail.prev
            else:
                self._tail = self._head = None
            self._size -= 1
        else:
            raise RuntimeError("A lista está vazia!")

    def remove_after(self, node):
        """
        Remove o nó após o nó especificado.

        :param node: o nó depois do qual remover.
        :return: None.
        """
        if node.next:
            node.next = node.next.next
            if node.next:
                node.next.prev = node
            self._size -= 1

    def remove(self, node):
        """
        Remove o nó especificado da lista.
        Numa LDL o algoritmo é O(1) para todos os nós, incluindo o último.

        :param node: o nó a remover.
        :return: None
        """
        if node.prev:
            node.prev.next = node.next
        else:
            self._head = node.next
        if node.next:
            node.next.prev = node.prev
        else:
            self._tail = node.prev
        self._size -= 1

    def head(self):
        """
        Devolve o elemento à cabeça da lista.

        :return: None
        """
        if self._head:
            return self._head
        else:
            return None

    def tail(self):
        """
        Devolve o elemento na cauda da lista.

        :return: None
        """
        if self._tail:
            return self._tail
        else:
            return None

    def size(self):
        """
        Devolve o número de elementos na lista.

        :return: None
        """
        return self._size

    def print(self):
        """
        Escreve o conteúdo aa lista.

        :return: None.
        """
        current = self._head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()


def main() -> int:
    """
    Um teste básico para validar a implementação de uma LSL existente neste módulo.
    As instruções assert terminam a execução caso a expressão Booleana especificada seja falsa.

    :return: 0 se os testes executaram com sucesso.
    """

    def assert_head_tail_path(ll):
        """
        Confirmar que, percorrendo a lista a partir da cabeça, se chega à cauda.

        :param ll: lista
        :return: None
        """
        current = ll.head()
        print("Head->", end=" ")
        while current:
            prev = current
            print(current.data, end=" ")
            current = current.next
        print()
        assert (ll.head() is None and ll.tail() is None) or ll.tail() == prev

    def assert_tail_head_path(ll):
        """
        Confirmar que, percorrendo a lista a partir da cauda, se chega à cabeça.

        :param ll: lista
        :return: None
        """
        current = ll.tail()
        print("Tail->", end=" ")
        while current:
            prev = current
            print(current.data, end=" ")
            current = current.prev
        print()
        assert (ll.head() is None and ll.tail() is None) or ll.head() == prev

    print("+-----------------------------------------------------------------+")
    print("| Teste à implemementação de uma LSL existente neste módulo       |")
    print("+-----------------------------------------------------------------+")

    # Criação da lista
    ll = DoublyLinkedList()
    assert_head_tail_path(ll)
    assert_tail_head_path(ll)

    #  Estado depois da execução deste bloco:
    #  tail -> +----+
    #  head -> | 33 |-->None
    #          +----+
    ll.insert_head(33)
    assert ll.size() == 1
    assert ll.head().data == 33
    assert ll.tail().data == 33
    assert_head_tail_path(ll)
    assert_tail_head_path(ll)

    #  Estado depois da execução deste bloco:
    #          +----+   +----+ <- tail
    #  head -> | 34 |-->| 33 |-->None
    #          +----+   +----+
    ll.insert_head(34)
    assert ll.size() == 2
    assert ll.head().data == 34
    assert ll.tail().data == 33
    assert ll.head().next.data == 33
    assert ll.tail().prev.data == 34
    assert_head_tail_path(ll)
    assert_tail_head_path(ll)

    #  Estado depois da execução deste bloco:
    #          +----+   +----+   +----+ <- tail
    #  head -> | 35 |-->| 34 |-->| 33 |-->None
    #          +----+   +----+   +----+
    ll.insert_head(35)
    assert ll.size() == 3
    assert ll.head().data == 35
    assert ll.tail().data == 33
    assert ll.head().next.data == 34
    assert ll.tail().prev.data == 34
    assert_head_tail_path(ll)
    assert_tail_head_path(ll)

    #  Estado depois da execução deste bloco:
    #          +----+   +----+   +----+   +----+ <- tail
    #  head -> | 35 |-->| 34 |-->| 33 |-->| 36 |-->None
    #          +----+   +----+   +----+   +----+
    ll.insert_tail(36)
    assert ll.size() == 4
    assert ll.head().data == 35
    assert ll.tail().data == 36
    assert ll.head().next.data == 34
    assert ll.tail().prev.data == 33
    assert_head_tail_path(ll)
    assert_tail_head_path(ll)

    #  Estado depois da execução deste bloco:
    #          +----+   +----+   +----+   +----+   +----+ <- tail
    #  head -> | 35 |-->| 37 |-->| 34 |-->| 33 |-->| 36 |-->None
    #          +----+   +----+   +----+   +----+   +----+
    ll.insert_after(37, ll._head)
    assert ll.size() == 5
    assert ll.head().data == 35
    assert ll.tail().data == 36
    assert ll.head().next.data == 37
    assert ll.tail().prev.data == 33
    assert_head_tail_path(ll)
    assert_tail_head_path(ll)

    #  Estado depois da execução deste bloco:
    #          +----+   +----+   +----+   +----+   +----+   +----+ <- tail
    #  head -> | 35 |-->| 37 |-->| 38 |-->| 34 |-->| 33 |-->| 36 |-->None
    #          +----+   +----+   +----+   +----+   +----+   +----+
    current = ll.head()
    while current.data != 37 and current.next:
        current = current.next
    ll.insert_after(38, current)
    assert ll.size() == 6
    assert ll.head().data == 35
    assert current.next.data == 38
    assert current.next.prev.data == 37
    assert ll.tail().data == 36
    assert_head_tail_path(ll)
    assert_tail_head_path(ll)

    #  Estado depois da execução deste bloco:
    #          +----+   +----+   +----+   +----+   +----+ <- tail
    #  head -> | 35 |-->| 37 |-->| 34 |-->| 33 |-->| 36 |-->None
    #          +----+   +----+   +----+   +----+   +----+
    ll.remove_after(current)
    assert ll.size() == 5
    assert ll.head().data == 35
    assert current.next.data != 38
    assert current.next.prev.data == 37
    assert ll.tail().data == 36
    assert_head_tail_path(ll)
    assert_tail_head_path(ll)

    #  Estado depois da execução deste bloco:
    #          +----+   +----+   +----+   +----+ <- tail
    #  head -> | 37 |-->| 34 |-->| 33 |-->| 36 |-->None
    #          +----+   +----+   +----+   +----+
    ll.remove_head()
    assert ll.size() == 4
    assert ll.head().data == 37
    assert ll.tail().data == 36
    assert_head_tail_path(ll)
    assert_tail_head_path(ll)

    #  Estado depois da execução deste bloco:
    #          +----+   +----+   +----+ <- tail
    #  head -> | 37 |-->| 34 |-->| 33 |-->None
    #          +----+   +----+   +----+
    ll.remove_tail()
    assert ll.size() == 3
    assert ll.head().data == 37
    assert ll.tail().data == 33
    assert_head_tail_path(ll)
    assert_tail_head_path(ll)

    #  Estado depois da execução deste bloco:
    #          +----+   +----+ <- tail
    #  head -> | 34 |-->| 33 |-->None
    #          +----+   +----+
    ll.remove_head()
    assert ll.size() == 2
    assert ll.head().data == 34
    assert ll.tail().data == 33
    assert_head_tail_path(ll)
    assert_tail_head_path(ll)

    #  Estado depois da execução deste bloco:
    #          +----+ <- tail
    #  head -> | 33 |-->None
    #          +----+
    ll.remove_head()
    assert ll.size() == 1
    assert ll.head().data == 33
    assert ll.tail().data == 33
    assert_head_tail_path(ll)
    assert_tail_head_path(ll)

    #  Estado depois da execução deste bloco:
    #          +----+   +----+ <- tail
    #  head -> | 39 |-->| 33 |-->None
    #          +----+   +----+
    ll.insert_before(39, ll.head())
    assert ll.size() == 2
    assert ll.head().data == 39
    assert ll.tail().data == 33
    assert_head_tail_path(ll)
    assert_tail_head_path(ll)

    #  Estado depois da execução deste bloco:
    #          +----+   +----+   +----+ <- tail
    #  head -> | 39 |-->| 40 |-->| 33 |-->None
    #          +----+   +----+   +----+
    ll.insert_before(40, ll.tail())
    assert ll.size() == 3
    assert ll.head().data == 39
    assert ll.tail().data == 33
    assert_head_tail_path(ll)
    assert_tail_head_path(ll)

    #  Estado depois da execução deste bloco:
    #          +----+   +----+ <- tail
    #  head -> | 39 |-->| 33 |-->None
    #          +----+   +----+
    current = ll.head().next
    ll.remove(current)
    assert ll.size() == 2
    assert ll.head().data == 39
    assert ll.head().next.data != 40
    assert ll.tail().data == 33
    assert_head_tail_path(ll)
    assert_tail_head_path(ll)

    #  Estado depois da execução deste bloco:
    #          +----+ <- tail
    #  head -> | 39 |-->None
    #          +----+
    ll.remove(ll.tail())
    assert ll.size() == 1
    assert ll.head().data == 39
    assert ll.tail().data == 39
    assert_head_tail_path(ll)
    assert_tail_head_path(ll)

    #  Estado depois da execução deste bloco:
    #  tail -> None
    #  head -> None
    #
    ll.remove(ll.head())
    assert ll.size() == 0
    assert ll.head() is None
    assert ll.tail() is None
    assert_head_tail_path(ll)
    assert_tail_head_path(ll)

    print("+----------------------------------------------------------------+")
    print("| Todos os testes terminaram com sucesso!                        |")
    print("+----------------------------------------------------------------+")

    return 0


if __name__ == "__main__":
    sys.exit(main())
