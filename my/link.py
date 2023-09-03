class Link:
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest:
            rest_repr = ", " + repr(self.rest)
        else:
            rest_repr = ""
        return 'Link('+repr(self.first)+rest_repr+')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + " "
            self = self.rest
        return string + str(self.first) + ">"


def range_link(start, end):
    if start >= end:
        return Link.empty
    else:
        return Link(start, range_link(start+1, end))


square, odd = lambda x: x*x, lambda x: x % 2 == 1


def map_link(f, s):
    if s is Link.empty:
        return s
    else:
        return Link(f(s.first), map_link(f, s.rest))


def filter_link(f, s):
    if s is Link.empty:
        return s
    filter_rest = filter_link(f, s.rest)
    if f(s):
        return Link(s.first, filter_rest)
    else:
        return filter_rest


def store_digits(n, current_link):
    """Stores the digits of a positive number n in a linked list.

    >>> s = store_digits(1)
    >>> s
    Link(1)
    >>> store_digits(2345)
    Link(2, Link(3, Link(4, Link(5))))
    >>> store_digits(876)
    Link(8, Link(7, Link(6)))
    >>> # a check for restricted functions
    >>> import inspect, re
    >>> cleaned = re.sub(r"#.*\\n", '', re.sub(r'"{3}[\s\S]*?"{3}', '', inspect.getsource(store_digits)))
    >>> print("Do not use str or reversed!") if any([r in cleaned for r in ["str", "reversed"]]) else None
    >>> link1 = Link(3, Link(Link(4), Link(5, Link(6))))
    """
    "*** YOUR CODE HERE ***"
    # s = Link.empty
    # while n:
    #     s = Link(n % 10, s)
    #     n = n // 10
    # return s

    # if n == 0:
    #     return Link.empty
    # else:
    #     rest = store_digits(n//10)
    #     return Link(n % 10, rest)
    '''
    >>> s = store_digits(123)
    >>> s
    Link(3, Link(2, Link(1)))
    '''

    if n == 0:
        return current_link
    else:
        new_link = Link(n % 10, current_link)
        return store_digits(n // 10, new_link)


def deep_map_mut(func, lnk):
    """Mutates a deep link lnk by replacing each item found with the
    result of calling func on the item.  Does NOT create new Links (so
    no use of Link's constructor).

    Does not return the modified Link object.

    >>> link1 = Link(3, Link(Link(4), Link(5, Link(6))))
    >>> # Disallow the use of making new Links before calling deep_map_mut
    >>> Link.__init__, hold = lambda *args: print("Do not create any new Links."), Link.__init__
    >>> try:
    ...     deep_map_mut(lambda x: x * x, link1)
    ... finally:
    ...     Link.__init__ = hold
    >>> print(link1)
    <9 <16> 25 36>
    """
    "*** YOUR CODE HERE ***"
    if lnk is Link.empty:
        return lnk
    if isinstance(lnk.first, Link):
        return Link(deep_map_mut(func, lnk.first), deep_map_mut(func, lnk.rest))
    return Link(func(lnk.first), deep_map_mut(func, lnk.rest))


def two_list(vals, counts):
    """
    Returns a linked list according to the two lists that were passed in. Assume
    vals and counts are the same size. Elements in vals represent the value, and the
    corresponding element in counts represents the number of this value desired in the
    final linked list. Assume all elements in counts are greater than 0. Assume both
    lists have at least one element.

    >>> a = [1, 3, 2]
    >>> b = [1, 1, 1]
    >>> c = two_list(a, b)
    >>> c
    Link(1, Link(3, Link(2)))
    >>> a = [1, 3, 2]
    >>> b = [2, 2, 1]
    >>> c = two_list(a, b)
    >>> c
    Link(1, Link(1, Link(3, Link(3, Link(2)))))
    """
    "*** YOUR CODE HERE ***"
    result = Link(None)
    for count in counts:
        index = 0
        for _ in range(count):
            if result is Link.empty:
                result = Link(vals[index])
            temp = result.rest
            while temp:
                temp = temp.rest
            temp.rest = Link(vals[index])
        index += 1
    return result


class Tree:
    """
    >>> t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
    >>> t.label
    3
    >>> t.branches[0].label
    2
    >>> t.branches[1].is_leaf()
    True
    """

    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(self.label, branch_str)

    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.label) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str
        return print_tree(self).rstrip()


def is_bst(t):
    """Returns True if the Tree t has the structure of a valid BST.

    >>> t1 = Tree(6, [Tree(2, [Tree(1), Tree(4)]), Tree(7, [Tree(7), Tree(8)])])
    >>> is_bst(t1)
    True
    >>> t2 = Tree(8, [Tree(2, [Tree(9), Tree(1)]), Tree(3, [Tree(6)]), Tree(5)])
    >>> is_bst(t2)
    False
    >>> t3 = Tree(6, [Tree(2, [Tree(4), Tree(1)]), Tree(7, [Tree(7), Tree(8)])])
    >>> is_bst(t3)
    False
    >>> t4 = Tree(1, [Tree(2, [Tree(3, [Tree(4)])])])
    >>> is_bst(t4)
    True
    >>> t5 = Tree(1, [Tree(0, [Tree(-1, [Tree(-2)])])])
    >>> is_bst(t5)
    True
    >>> t6 = Tree(1, [Tree(4, [Tree(2, [Tree(3)])])])
    >>> is_bst(t6)
    True
    >>> t7 = Tree(2, [Tree(1, [Tree(5)]), Tree(4)])
    >>> is_bst(t7)
    False
    """
    "*** YOUR CODE HERE ***"
    if t.is_leaf():
        return True
    if len(t.branches) >= 2:
        return False
    if t.branches[0].label <= t.label <= t.branches[1].label:
        return is_bst(t.branches[0]) and is_bst(t.branches[1])
    else:
        return False


def bst_max(t):
    if t.is_leaf():
        return t.label
    # if len(t.branches) == 2:
    #     return max([max(bst_max(t.branches[0])), max(bst_max(t.branches[1]))])
    # if len(t.branches) == 1:
    #     return max(bst_max(t.branches[0]))
    max_child_label = max(bst_max(branch) for branch in t.branches)
    return max(t.label, max_child_label)


def bst_min(t):
    if t.is_leaf():
        return t.label
    max_child_label = min(bst_min(branch) for branch in t.branches)
    return min(t.label, max_child_label)


t1 = Tree(6, [Tree(2, [Tree(1), Tree(4)]), Tree(7, [Tree(7), Tree(8)])])
t2 = Tree(8, [Tree(2, [Tree(9), Tree(1)]), Tree(3, [Tree(6)]), Tree(5)])
t3 = Tree(6, [Tree(2, [Tree(4), Tree(1)]), Tree(7, [Tree(7), Tree(8)])])
t4 = Tree(1, [Tree(2, [Tree(3, [Tree(0)])])])
t6 = Tree(1, [Tree(4, [Tree(2, [Tree(3)])])])
# is_bst(t6)
# print(t6)
t7 = Tree(2, [Tree(1, [Tree(5)]), Tree(4)])
bst_max(t6)
bst_max(t7)
