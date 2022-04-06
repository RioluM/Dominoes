from dominoes_algorithm import get_iteration_result
from dominoes_reversed_algorithm import get_reversed_iteration_result

print("Choose algorithm:")
print("1 - Dominoes algorithm")
print("2 - Reversed dominoes algorithm")
try:
    algorithm = int(input())
    print("Type number of iterations")
    iterations = int(input())
except ValueError as e:
    print("Wrong input")
else:
    print("Type dominoes")
    domino_string = input()
    dominoes = []
    if algorithm == 1:
        print(get_iteration_result(domino_string, iterations))
    elif algorithm == 2:
        print(get_reversed_iteration_result(domino_string, iterations))
    else:
        print("Wrong option")
