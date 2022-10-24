"""Experimental evaluation of an algorithm running time.

This is a very simple module that shows a possible way of performing an experimental analysis of the running
time of an algorithm for different input sizes.

Important notes:
    * The specified algorithm receives a single argument: a list of numbers.

    * If your algorithm requires further arguments, you should specify an intermediate function that will be called
      with a list of numbers. Than, this function can call the algorithm function with all the necessary parameters.

    * For eficiency, the lists of random numbers with each of the specified lengths, are slices of the larger list.
      You should take this into consideration when analysing the results.

    * By default the number lists can have repetitions. You can use the argument can_repeat=False to generate lists
      whithout repetitions.

    * If you execute this module it will run an example, analysing thw simple algorithms.

    * The graphic with the result of the algorithm analysis will be shown in a web page using your default browser.

Author:
    CJL - 2022-10-04

License:
    MIT License

    Copyright (c) 2022 CJL

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
"""

import random
import timeit
import plotly.express as px
import pandas as pd
import locale


def profile_algorithm(algorithm, input_sizes, algorithm_name="Nome do Algoritmo", can_repeat=True,
                      x_axis_label="Dimensão da Lista", y_axis_label="Tempo de Execução"):
    """
    This function measures the running time of an algorithm for a set of input lists with different lengths.

    :param algorithm: Function whith the algorithm to evaluate. Called with a list of numbers for each length in input_sizes.
    :type  algorithm: function
    :param input_sizes: List of input legths with which to call the algorithm (used in the secified order)
    :type  input_sizes: list
    :param algorithm_name: Name that will be used to describe the algorithm in the graph title.
    :param can_repeat: Whether the number lists used to call the algorithm can have repetitions, or not.
    :param x_axis_label: X-axis label ('Dimensão da Lista', by default).
    :param y_axis_label: Y-axis label ('Tempo de Execução', by default).
    :return: Execution times, in seconds, for each of the lengths specified in input_sizes.
    """
    
    # List to store running times for each input length.
    times = []

    print(f"A avaliar algoritmo '{algorithm.__name__}'.")
    print(f"A gerar lista aleatória de {input_sizes[-1]:n} números, {'com' if can_repeat else 'sem'} repetições...", end=' ')
    
    # Generate the bigger list. The smaller ones will be slices of this one.
    if (not can_repeat):
        fulllist = random.sample(range(1, input_sizes[-1] + 1), input_sizes[-1])        # No repetitions (slower)
    else:
        fulllist = random.choices(range(1, input_sizes[-1] + 1), k=input_sizes[-1], )   # With repetitions
    print("OK")

    # Run the specified algorithm with a list of numbers for each of the lengths specified in 'input_sizes'.
    for n in input_sizes:
        # Use a sub-list with the specified length.
        randomlist = fulllist[:n]

        print(f"A invocar '{algorithm.__name__}' com lista de dimensão {n:n}...", end=" ")
        
        # Measure execution time.
        start = timeit.default_timer()
        algorithm(randomlist)
        stop = timeit.default_timer()
        print(f"OK ({round(stop - start, 4)} seg.)")

        # Store running time in 'times' list.
        times.append(stop - start)

    # Use pandas to generate a table (DataFrame) with data to include in the graph.
    
    # 'input_sizes' in x-axis, and 'times' in y-axis.
    df = pd.DataFrame(dict(n=input_sizes, time=times))

    # Use plotty to show the graph of running time as a function of n.
    fig = px.scatter(df, y="time", x="n",
                     title=algorithm_name,
                     labels={"n": x_axis_label, "time": y_axis_label})
    fig.update_traces(marker_size=10)
    fig.show()

    return times


# Just to make sure we have a dot as the thousands separator.
locale.setlocale(locale.LC_ALL, 'pt')

if __name__ == '__main__':
    # Number list's lengths to use when calling algorithm.
    ns = [1000000, 2000000, 3000000, 4000000, 5000000, 6000000, 7000000, 8000000, 9000000,
          10000000, 11000000, 12000000, 13000000, 14000000, 15000000, 16000000, 17000000, 18000000, 19000000,
          #20000000, 21000000, 22000000, 23000000, 24000000, 25000000, 26000000, 27000000, 28000000, 29000000,
          #30000000, 31000000, 32000000, 33000000, 34000000, 35000000, 36000000, 37000000, 38000000, 39000000,
         ]

    #
    # An intermediate function to show how to evaluate an algorithm that needs more parameters, or 
    # cannot be called directly for some reason.
    #
    def search_list(lst):
        for i in range(len(lst)):
            if lst[i] == 111111111:
                return i
        return -1

    #
    # You can evaluate more than one algorithm. Thow graphs (in two different pages) will be shown.
    #
    profile_algorithm(sorted, ns, "Ordenação de uma lista com builtin sorted().", False)
    profile_algorithm(search_list, ns, "Pesquisa numa lista com ciclo 'for'.", False)

