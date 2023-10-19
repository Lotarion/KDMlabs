from labwork1 import DmSet


def cartesian_product(set_a: DmSet, set_b: DmSet):
    result = DmSet()
    for i in set_a:
        for j in set_b:
            result.add(DmSet(i, j))
    return result


def is_relation_valid(relation, set_a, set_b):
    cartesian = cartesian_product(set_a, set_b)

    for element in relation:
        if element not in cartesian:
            return False

    return True


def find_relations(set_a, relation_func):
    relations = DmSet()
    for i in set_a:
        for j in set_a:
            if relation_func(i, j) and i != j:
                relations.add((i, j))
    return relations


def filtered_cartesian_product(set_a, set_b, filter_func):
    result = DmSet()
    for i in set_a:
        for j in set_b:
            if filter_func(i, j) and i != j:
                result.add((i, j))
    return result


def main():
    set1 = DmSet(1, 2)
    set2 = DmSet("a", "b")
    print(cartesian_product(set1, set2))

    set1 = DmSet(1, 2)
    set2 = DmSet("a", "b")
    relation = DmSet(DmSet(1, "a"), DmSet(2, "b"))
    print(is_relation_valid(relation, set1, set2))

    set1 = DmSet(1, 2, 3, 4, 6)
    print(find_relations(set1, lambda a, b: a % b == 0))

    set1 = DmSet(1, 2, 3)
    set2 = DmSet(3, 4, 5)
    print(filtered_cartesian_product(set1, set2, lambda a, b: a < b))


if __name__ == '__main__':
    main()
