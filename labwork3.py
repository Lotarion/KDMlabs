import itertools

logic_dict = {
    "AND": "and",
    "OR": "or",
    "NOT": "not"
}

operators = {
    "AND": "and",
    "OR": "or",
    "NOT": "not",
    "(": "(",
    ")": ")",
}


def replacer(expression: str, values: dict):
    for key in values.keys():
        expression = expression.replace(key, str(values[key]))
    return expression


def generate_table(expression: str):
    values = expression
    for key in operators.keys():
        values = values.replace(key, "")

    values = values.split(" ")

    while "" in values:
        values.remove("")

    table = itertools.product(["True", "False"], repeat=len(values))

    result_table = []
    for row in table:
        expr_dict = dict(zip(values, row))
        result = replacer(replacer(expression, logic_dict), expr_dict)
        row += (result,)
        result_table.append(row)

    return list((result_table, tuple(value for value in values) + (expression,)))


def pretty_print_table(table: list, header: list) -> None:
    string = ()
    for column in header:
        string += (f"{column:<7}",)

    print("|".join(string))
    print("-" * (len(header) * 7))

    for row in table:
        string = ()
        for column in row:
            string += (f"{column:<7}",)
        print("|".join(string), )


def main():
    command = replacer(replacer("(A AND B) OR (NOT C)", logic_dict), {"A": True, "B": False, "C": True})
    print(eval(command))

    expr: str = "(A AND B) OR C"
    table, header = generate_table(expr)
    pretty_print_table(table, header)

    print(expr)


if __name__ == '__main__':
    main()
