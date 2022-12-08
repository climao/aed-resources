#
# Implemntação de uma função para avaliação de palíndromas usando uma pilha e uma fila.
#
# Carlos Limão
# Outubro 2022
#
import stack
import fila


def is_palindrome(s):
    """
    Devolve True se s é um palíndroma.
    
    A utilização de uma pilha e de uma fila garante que os carateres da string,
    depois de colocados em cada uma, são removidos pela ordem oposta.  

    :param s: A string a avaliar.
    :return: True se s é um palíndroma. False caso contrário.
    """
    stk = stack.StackUsingListEnd()
    q = fila.QueueUsingDeque()
    for ch in "".join(s.lower().split()):       # "".join(s.split()) elimina espaços, TABs e mudanças de linha.
        stk.push(ch)
        q.enqueue(ch)
    while not stk.is_empty():
        if stk.pop() != q.dequeue():
            return False
    return True


def main():
    strings = ["ABBA",
               "whatever",
               "Amor a Roma",
               "Anotaram a data da maratona",
               "O lobo ama o bolo",
               "Arara"]

    for s in strings:
        print(f"'{s}' é um palíndroma? {is_palindrome(s)}")


if __name__ == "__main__":
    main()
