"""
Implementação simples de uma Fila usando uma lista Python e deques.

Objetivos: 1. Escrever as duas classes QueueUsingList e QueueUsingDeque
              de modo a passar todos os testes.
           2. Avaliar complexidade temporal das implementações, usando profile.py.

Na implementação deve ter em conta a complexidade temporal das operações
sobre listas. Pode obter essa informação aqui: https://wiki.python.org/moin/TimeComplexity

O Python tem, no módlo collections, uma implementação de double ended queues que tem
operações O(1) em ambas es extremidades da fila.
Ver: https://docs.python.org/3/library/collections.html#collections.deque

Recorde também que as versões mais recentes do Python são "Open Source".
O código-fonte do Python está disponível aqui: https://github.com/python/cpython

Carlos Limão
Outubro 2022
"""
from collections import deque


class QueueUsingList:
    """ Implementação de uma fila usando uma lista Python. """

    def __init__(self):
        """ Cria uma fila vazia. """
        pass

    def is_empty(self):
        """ Devolve True se a fila está vazia. """
        pass

    def enqueue(self, item):
        """ Adiciona um elemento ao fim da fila. """
        pass

    def dequeue(self):
        """
        Remove um elemento do início da fila.
        Gera exceção EmptyError (definida abaixo) se lista estiver vazia.

        """
        pass

    def __len__(self):
        """
        Para uma fila f, permite usar len(f) para obter a rspetiva dimensão.
        """
        pass

    def first(self):
        """
        Devolve o elemento no início da fila, sem o remover.
        Gera exceção EmptyError (definida abaixo) se lista estiver vazia.
        """
        pass


class QueueUsingDeque:
    """ Implementação de uma fila usando uma Double Ended Queue. """

    def __init__(self):
        """ Cria uma fila vazia. """
        pass

    def is_empty(self):
        """ Devolve True se a fila está vazia. """
        pass

    def enqueue(self, item):
        """ Adiciona um elemento ao fim da fila. """
        pass

    def dequeue(self):
        """
        Remove um elemento do início da fila.
        Gera exceção EmptyError (definida abaixo) se lista estiver vazia.
        """
        pass

    def __len__(self):
        """
        Para uma fila f, permite usar len(f) para obter a rspetiva dimensão.
        """
        pass

    def first(self):
        """
        Devolve o elemento no início da fila, sem o remover.
        Gera exceção EmptyError (definida abaixo) se lista estiver vazia.
        """
        pass


class EmptyError(Exception):
    pass


def test_queue_implementation(queue_class, values=[5, 4, 3, 2, 1]):
    """
    Testa a implementação de uma fila fornecida pela classe passada como parâmetro.

    :param queue_class: A classe a testar.
                        Assume que o nome desta classe inclui a palavra "List" quando usa uma lista Python.
                        Quando não inclui a palavra "List", assume-se que usa uma dequeue.
    :param: values: Lista de valores a usar para teste da Fila.
    :return: None
    """

    if "List" in queue_class.__name__:
        test_desc  = "Teste à implementação de uma Fila usando uma lista                         "
    else:
        test_desc = "Teste à implementação de uma Fila usando uma dequeue                       "

    print(f"+-------------------------------------------------------------------------------+")
    print(f"| {test_desc}   |")
    print(f"+-------------------------------------------------------------------------------+")


    # Cria uma fila.
    q = queue_class()

    # Adiciona e remove um elemento.
    print(f"Inserir {values[0]} na fila ...")
    q.enqueue(values[0])
    assert q.is_empty() is False
    assert len(q) == 1
    assert q.first() == values[0]

    print("Remover da fila: ", end=" ")
    el = q.dequeue()
    assert q.is_empty()
    assert len(q) == 0
    print(el)

    # Adicionar elementos do array values
    nelements = 0
    for i in values:
        print(f"Inserir na fila: {i} ...")
        q.enqueue(i)
        nelements += 1
        assert not q.is_empty()
        assert len(q) == nelements
        assert q.first() == values[0]

    # Verificar a fila
    assert len(q) == len(values)
    print(f"Dimensão da fila: {len(q)}")

    try:
        # Tentar remover len(values) + 1 valores
        # (No último deve gerar uma exceção)
        el_index = 0
        for _ in range(len(values) + 1):
            el = q.dequeue()
            nelements -= 1
            print(f"Removeu da fila: {el}")
            assert el == values[el_index]
            el_index += 1
            assert len(q) == nelements
            if nelements:
                assert q.first() == values[el_index]

            # Quando a fila está vazia, acesso ao primeiro deve gerar exceção.
            try:
                print(f"Cabeça da fila: {q.first()}")
            except EmptyError:
                assert q.is_empty()
                assert len(q) == 0
                print("Tentativa de aceder à cabeça da fila com fila vazia gera exceção!")

    except EmptyError:
        assert q.is_empty()
        assert len(q) == 0
        print("Tentativa de retirar da fila com fila vazia gera exceção!")

    # Verifica estado final da fila
    print(f"Fila está vazia? {q.is_empty()}")

    print("+-------------------------------------------------------------------------------+")
    print("| Testes concluidos com sucesso.                                                |")
    print("+-------------------------------------------------------------------------------+")


def main():
    import profile

    testq = None

    def setup_queue_list(n):
        """
        Setup de uma Fila implementada com uma Lista, para teste de desempenho.
        Para usar em profile.profile_algorithm().

        :param n: Dimensão do stack.
        :return:  None
        """
        nonlocal testq
        testq = QueueUsingList()
        for i in range(n):
            testq.enqueue(i)

    def setup_queue_deque(n):
        """
        Setup de uma Fila implementada com uma deque, para teste de desempenho.
        Para usar em profile.profile_algorithm().

        :param n: Dimensão do stack.
        :return:  None
        """
        nonlocal testq
        testq = QueueUsingDeque()
        for i in range(n):
            testq.enqueue(i)

    def test_queue(n):
        """
        Para teste aos tempos de execução dos algoritmos que implementam Queues.
        Noatr que este teste, executa um valor fixo de operações, mas sobre
        uma fila de n valores.

        :param n: Número de elementos na queue (não usado)
        :return: None
        """
        for i in range(100000):
            testq.enqueue(i)
            testq.dequeue()

    test_queue_implementation(QueueUsingList)
    test_queue_implementation(QueueUsingDeque)

    #
    # Remover os comentários seguintes para avaliar os tempos de execução das
    # duas implementações.
    # Note que, se estas usarem listas Python, as operações "no fim" são O(1),
    # mas as operações no início são O(n).
    # Usando o módulo Double Ended Queue (deque) as operações em ambas as
    # extremidades da fila são O(1).
    #
    # profile.profile_algorithm(test_queue,
    #                           [10000, 20000, 30000, 40000, 50000],
    #                           "Queue - Implementação com lista.",
    #                           use_number_list=False,
    #                           setup=setup_queue_list,
    #                           adjust_for_length=False)
    #
    # profile.profile_algorithm(test_queue,
    #                           [10000, 20000, 30000, 40000, 50000],
    #                           "Queue - Implementação com deque.",
    #                           use_number_list=False,
    #                           setup=setup_queue_deque,
    #                           adjust_for_length=False)


if __name__ == "__main__":
    main()

