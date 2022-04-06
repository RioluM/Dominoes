

def check_left_reversed(dominoes, index):
    for left_index in range(index-1, -1, -1):
        if dominoes[left_index] != "\\":
            return "|"
    return None


def check_right_reversed(dominoes, index):
    for right_index in range(index + 1, len(dominoes)):
        if dominoes[right_index] != "/":
            return "|"
    return None


def get_reversed_iteration_result(domino_string, iterations):
    domino_length = len(domino_string)
    dominoes = []
    for index in range(domino_length):
        if domino_string[index] != "|":
            first_index = index - iterations if index - iterations >= 0 else 0
            last_index = index + iterations if index + iterations <= domino_length - 1 else domino_length - 1
            subdominoe = list(domino_string[first_index:last_index + 1])
            subdominoe_index = iterations if index - iterations >= 0 else index

            if domino_string[index] == "/" and check_right_reversed(subdominoe, subdominoe_index) is not None:
                dominoes.append("|")
            elif domino_string[index] == "\\" and check_left_reversed(subdominoe, subdominoe_index) is not None:
                dominoes.append("|")
            else:
                dominoes.append(domino_string[index])
        else:
            dominoes.append(domino_string[index])
    return "".join(dominoes)