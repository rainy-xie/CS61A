# Tree ADT
def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)


def label(tree):
    return tree[0]


def branches(tree):
    return tree[1:]


def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True


def is_leaf(tree):
    return not branches(tree)

# lab05 Trees


def berry_finder(t):
    """Returns True if t contains a node with the value 'berry' and
    False otherwise.

    >>> scrat = tree('berry')
    >>> berry_finder(scrat)
    True
    >>> sproul = tree('roots', [tree('branch1', [tree('leaf'), tree('berry')]), tree('branch2')])
    >>> berry_finder(sproul)
    True
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> berry_finder(numbers)
    False
    >>> t = tree(1, [tree('berry',[tree('not berry')])])
    >>> berry_finder(t)
    True
    """
    "*** YOUR CODE HERE ***"
    # if label(t) == 'berry':
    #     return True
    # for branch in branches(t):
    #     if label(branch) == 'berry':
    #         return True
    #     elif is_leaf(branch):
    #         continue
    #     else:
    #         return berry_finder(branch)
    # return False
    if label(t) == 'berry':
        return True
    for branch in branches(t):
        if berry_finder(branch):
            return True
    return False


def sprout_leaves(t, leaves):
    """Sprout new leaves containing the data in leaves at each leaf in
    the original tree t and return the resulting tree.

    >>> t1 = tree(1, [tree(2), tree(3)])
    >>> print_tree(t1)
    1
      2
      3
    >>> new1 = sprout_leaves(t1, [4, 5])
    >>> print_tree(new1)
    1
      2
        4
        5
      3
        4
        5

    >>> t2 = tree(1, [tree(2, [tree(3)])])
    >>> print_tree(t2)
    1
      2
        3
    >>> new2 = sprout_leaves(t2, [6, 1, 2])
    >>> print_tree(new2)
    1
      2
        3
          6
          1
          2
    """
    "*** YOUR CODE HERE ***"
    # [1,2] -> [tree(1),tree(2)]
    # newbranches = []
    # for leave in leaves:
    #     newbranches = newbranches + [tree(leave)]

    # if is_leaf(t):
    #     t = tree(t, newbranches)
    # else:
    #     # for branch in branches(t)[:]:
    #     #     if is_leaf(branch):
    #     #         branch = tree(branch, newbranches)
    #     i = 0
    #     while i < len(branches(t)):
    #         if is_leaf(branches(t)[i]):
    #             branches(t)[i] = tree(branches(t)[i],newbranches)
    #         i = i + 1
    # return t
    if is_leaf(t):
        return tree(label(t), [tree(leaf) for leaf in leaves])
    else:
        return tree(label(t), [sprout_leaves(branch, leaves) for branch in branches(t)])

# Optional Questions


def preorder(t):
    """Return a list of the entries in this tree in the order that they
    would be visited by a preorder traversal (see problem description).

    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> preorder(numbers)
    [1, 2, 3, 4, 5, 6, 7]
    >>> preorder(tree(2, [tree(4, [tree(6)])]))
    [2, 4, 6]
    """
    "*** YOUR CODE HERE ***"
    if is_leaf(t):
        return [label(t)]
    else:
        result = [label(t)]
        for branch in branches(t):
            result.extend(preorder(branch))
        return result


numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
preorder(numbers)


def add_trees(t1, t2):
    """
    >>> numbers = tree(1,
    ...                [tree(2,
    ...                      [tree(3),
    ...                       tree(4)]),
    ...                 tree(5,
    ...                      [tree(6,
    ...                            [tree(7)]),
    ...                       tree(8)])])
    >>> print_tree(add_trees(numbers, numbers))
    2
      4
        6
        8
      10
        12
          14
        16
    >>> print_tree(add_trees(tree(2), tree(3, [tree(4), tree(5)])))
    5
      4
      5
    >>> print_tree(add_trees(tree(2, [tree(3)]), tree(2, [tree(3), tree(4)])))
    4
      6
      4
    >>> print_tree(add_trees(tree(2, [tree(3, [tree(4), tree(5)])]), \
    tree(2, [tree(3, [tree(4)]), tree(5)])))
    4
      6
        8
        5
      5
    """
    "*** YOUR CODE HERE ***"
    if not t1:
        return t2
    if not t2:
        return t1

    len_t1, len_t2 = len(branches(t1)), len(branches(t2))

    if len_t1 < len_t2:
        # 补齐 t1 的子树列表
        t1 = tree(label(t1), branches(t1) + [tree(0)] * (len_t2 - len_t1))
    elif len_t2 < len_t1:
        # 补齐 t2 的子树列表
        t2 = tree(label(t2), branches(t2) + [tree(0)] * (len_t1 - len_t2))
    new_label = label(t1)+label(t2)
    new_branch = [add_trees(b1, b2)
                  for b1, b2 in zip(branches(t1), branches(t2))]
    return tree(new_label, new_branch)
