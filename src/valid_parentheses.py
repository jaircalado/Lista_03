from src.my_stack import MyStack


def is_valid_parentheses(string: str) -> bool:
    stack = MyStack()

    pares = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for caractere in string:

        if caractere in "([{":
            stack.push(caractere)

        elif caractere in ")]}":

            if stack.is_empty():
                return False

            topo = stack.pop()

            if topo != pares[caractere]:
                return False

    return stack.is_empty()
