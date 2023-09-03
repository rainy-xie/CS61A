import sys


class A:
    def __init__(self, x):
        self.x = x

    def __repr__(self):
        return self.x

    def __str__(self):
        return self.x * 2


class B:
    def __init__(self):
        print('boo!')
        self.a = []

    def add_a(self, a):
        self.a.append(a)

    def __repr__(self):
        print(len(self.a))
        ret = ''
        for a in self.a:
            ret += str(a)
        return ret


'''
 xie@ThinkXie:~/CS61A/disc/disc08$ python3 -i disc08.py 
>>> A("one")
one
>>> print(A("one"))
oneone
>>> repr(A("two"))
'two'
>>> b = B()
boo!
>>> b.add_a(A('a'))
>>> b.add_a(A('b'))
>>> b
2
aabb
'''


class Link:
    """A linked list."""
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'


'''
>>> ganondorf = Link('zelda', Link('link', Link('sheik', Link.empty)))
>>> ganondorf.rest.rest.first
'sheik'
>>> ganondorf.rest.first
'link'
>>> str(ganondorf)
'<zelda link sheik>'
'''

# Q3: Sum Nums


def sum_nums(s):
    """
    >>> a = Link(1, Link(6, Link(7)))
    >>> sum_nums(a)
    14
    """
    "*** YOUR CODE HERE ***"
    sum_s = 0
    while s:
        sum_s += s.first
        s = s.rest
    return sum_s

# Q4: Multiply Links


def multiply_lnks(lst_of_lnks):
    """
    >>> a = Link(2, Link(3, Link(5)))
    >>> b = Link(6, Link(4, Link(2)))
    >>> c = Link(4, Link(1, Link(0, Link(2))))
    >>> p = multiply_lnks([a, b, c])
    >>> p.first
    48
    >>> p.rest.first
    12
    >>> p.rest.rest.rest is Link.empty
    True
    """
    # Implementation Note: you might not need all lines in this skeleton code
    # ___________________ = ___________
    # for _______________________________________:
    #     if __________________________________________:
    #         _________________________________
    #     ___________________
    # ________________________________________________________
    # ________________________________________________________

    # dummy_head = Link(None)
    # temp = dummy_head
    # min_len = min(len(lnk) for lnk in lst_of_lnks)
    # for i in range(min_len):
    #     mul = 1
    #     p = Link(0)
    #     for j in range(len(lst_of_lnks)):
    #         mul *= lst_of_lnks[j].first
    #         lst_of_lnks[j] = lst_of_lnks[j].rest
    #     p.first = mul
    #     temp.rest = p
    #     temp = temp.rest
    # return dummy_head.rest

    product = 1
    for link in lst_of_lnks:
        if link is Link.empty:
            return Link.empty
        product *= link.first
    lst_of_lnks_rests = [lnk.rest for lnk in lst_of_lnks]
    return Link(product, multiply_lnks(lst_of_lnks_rests))


# Q5: Flip Two
def flip_two(s):
    """
    >>> one_lnk = Link(1)
    >>> flip_two(one_lnk)
    >>> one_lnk
    Link(1)
    >>> lnk = Link(1, Link(2, Link(3, Link(4, Link(5)))))
    >>> flip_two(lnk)
    >>> lnk
    Link(2, Link(1, Link(4, Link(3, Link(5)))))
    """
    "*** YOUR CODE HERE ***"
    # head = s
    # while s and s.rest:
    #     t = head
    #     t = s.rest
    #     s.rest = s.rest.rest
    #     t.rest = s
    #     s = s.rest
    #     head.rest = t

    # dummuy_head = Link(None, s)
    # head = dummuy_head
    # t = s
    # while t and t.rest:
    #     p = t.rest
    #     t = t.rest.rest
    #     p.rest = t
    #     head.rest = p
    #     head = t
    #     t = t.rest
    # s = dummuy_head.rest
    # For an extra challenge, try writing out an iterative approach as well below!
    "*** YOUR CODE HERE ***"
    if s and s.rest:
        s.first, s.rest.first = s.rest.first, s.first
    else:
        return
    flip_two(s.rest.rest)


class Tree:
    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = branches

    def is_leaf(self):
        return not self.branches


# Q6: Make Even
def make_even(t):
    """
    >>> t = Tree(1, [Tree(2, [Tree(3)]), Tree(4), Tree(5)])
    >>> make_even(t)
    >>> t.label
    2
    >>> t.branches[0].branches[0].label
    4
    """
    "*** YOUR CODE HERE ***"
    if t.label % 2 == 1:
        t.label += 1
    for b in t.branches:
        make_even(b)
    return


# Q7: Add Leaves
# 设置递归深度限制，例如增加到10000
sys.setrecursionlimit(100000)

# 现在您的递归函数可以更深入地递归，但请小心使用，不要设置得过高
# 但还是有写doctest没通过，递归太深了


def add_d_leaves(t, v):
    """Add d leaves containing v to each node at every depth d.

    >>> t_one_to_four = Tree(1, [Tree(2), Tree(3, [Tree(4)])])
    >>> print(t_one_to_four)
    1
      2
      3
        4
    >>> add_d_leaves(t_one_to_four, 5)
    >>> print(t_one_to_four)
    1
      2
        5
      3
        4
          5
          5
        5

    >>> t1 = Tree(1, [Tree(3)])
    >>> add_d_leaves(t1, 4)
    >>> t1
    Tree(1, [Tree(3, [Tree(4)])])
    >>> t2 = Tree(2, [Tree(5), Tree(6)])
    >>> t3 = Tree(3, [t1, Tree(0), t2])
    >>> print(t3)
    3
      1
        3
          4
      0
      2
        5
        6
    >>> add_d_leaves(t3, 10)
    >>> print(t3)
    3
      1
        3
          4
            10
            10
            10
          10
          10
        10
      0
        10
      2
        5
          10
          10
        6
          10
          10
        10
    """
    "*** YOUR CODE HERE ***"
    def add_leaves(t, d):
        for branch in t.branches:
            add_leaves(branch, d+1)
        t.branches.extend([Tree(v) for _ in range(d)])
    add_leaves(t, 0)
