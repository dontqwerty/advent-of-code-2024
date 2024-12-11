line = list(map(int, open("input").readline().strip().split()))

known_trees = {}


class Tree:
    def __init__(self, root: int) -> None:
        self.root = root

    def get_size(self, level) -> int:
        size = 1
        if level == 0:
            return size
        if (self.root, level) in known_trees:
            return known_trees[(self.root, level)]
        str_root = str(self.root)
        if self.root == 0:
            size = Tree(1).get_size(level - 1)
        elif len(str_root) % 2 == 0:
            size = Tree(int(str_root[: len(str_root) // 2])).get_size(level - 1) + Tree(
                int(str_root[len(str_root) // 2 :])
            ).get_size(level - 1)
        else:
            size = Tree(self.root * 2024).get_size(level - 1)
        known_trees[(self.root, level)] = size
        return size


size = 0
for n in line:
    size += Tree(n).get_size(75)
print(size)
