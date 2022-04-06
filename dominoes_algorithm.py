
def check_left_iteration(dominoes, index):
    for left_index in range(index-1, -1, -1):
        if dominoes[left_index] == "/":
            return "/", index - left_index
        elif dominoes[left_index] == "\\":
            break
    return None, 0


def check_right_iteration(dominoes, index):
    for right_index in range(index + 1, len(dominoes)):
        if dominoes[right_index] == "\\":
            return "\\", right_index - index
        elif dominoes[right_index] == "/":
            break
    return None, 0


def get_iteration_result(domino_string, iterations):
    domino_length = len(domino_string)
    dominoes = []
    for index in range(domino_length):
        if domino_string[index] == "|":
            first_index = index - iterations if index - iterations >= 0 else 0
            last_index = index + iterations if index + iterations <= domino_length - 1 else domino_length - 1
            subdominoe = list(domino_string[first_index:last_index + 1])
            subdominoe_index = iterations if index - iterations >= 0 else index
            left_result = check_left_iteration(subdominoe, subdominoe_index)
            right_result = check_right_iteration(subdominoe, subdominoe_index)

            if (left_result[1] < right_result[1] or right_result[1] == 0) and left_result[0] is not None:
                dominoes.append("/")
            elif (left_result[1] > right_result[1] or left_result[1] == 0) and right_result[0] is not None:
                dominoes.append("\\")
            else:
                dominoes.append("|")
        else:
            dominoes.append(domino_string[index])
    return "".join(dominoes)
