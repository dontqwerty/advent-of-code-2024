from typing import Tuple, List


def parse_input() -> Tuple[List[List[int]], List[List[int]]]:
    rules, updates = [v.splitlines() for v in open("input").read().split("\n\n")]
    rules = list(map(lambda r: list(map(int, r.split("|"))), rules))
    updates = list(map(lambda u: list(map(int, u.split(","))), updates))
    return rules, updates


def get_update_indices(update):
    update_ixs = {}
    for ix, v in enumerate(update):
        update_ixs[v] = ix
    return update_ixs


def find_sorted_updates(rules, updates):
    sorted_updates = []
    for update in updates:
        update_ixs = get_update_indices(update)
        is_sorted = True
        for first, last in rules:
            try:
                if not update_ixs[first] < update_ixs[last]:
                    is_sorted = False
                    break
            except KeyError:
                pass
        if is_sorted:
            sorted_updates.append(update)
    return sorted_updates
