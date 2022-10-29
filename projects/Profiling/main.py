import profile
import quicksort
import mergesort

def my_algorithm(lst):
    #quicksort.quicksort(lst, 0, len(lst) - 1)
    mergesort.mergeSort(lst, 0, len(lst) - 1)


#
# Dimensões das listas a usar para invocar o algoritmo especificado.
#
ns = [1000000, 2000000, 3000000, 4000000, 5000000, 6000000, 7000000, 8000000, 9000000,
      10000000, 11000000, 12000000, 13000000, 14000000, 15000000, 16000000, 17000000, 18000000, 19000000,
      #20000000, #21000000, 22000000, 23000000, 24000000, 25000000, 26000000, 27000000, 28000000, 29000000,
      #30000000, #31000000, 32000000, 33000000, 34000000, 35000000, 36000000, 37000000, 38000000, 39000000,
     ]

if __name__ == '__main__':
    profile.profile_algorithm(my_algorithm, ns, "Algoritmo Merge")