'''
Q1: WWPD: Mutability
>>> x = [1,2,3]
>>> y = x
>>> x += [4]
>>> y
[1, 2, 3, 4]
>>> x
[1, 2, 3, 4]

>>> x = [1,2,3]
>>> y = x
>>> x = x+[4]
>>> x
[1, 2, 3, 4]
>>> y
[1, 2, 3]

reason: 
在Python中:
= 是赋值操作符，用于将一个变量绑定到一个对象。
+= 是增强赋值操作符，用于就地修改可变对象（例如列表、集合等）而不创建新对象。

>>> s1 = [1,2,3]
>>> s2 = s1
>>> s1 is s2
True
>>> s2.extend([5,6])
>>> s1[4]
6
>>> s1.append([-1,0,1])
>>> s2[5]
[-1, 0, 1]
>>> s3 = s2[:]
>>> s3.insert(3,s2.pop(3))
>>> len(s1)
5
>>> s3 is s2
False
>>> len(s2)
5
>>> len(s3)
7
>>> s1[4] is s3[6]
True
>>> s3[s2[4][1]]
1
>>> s3[-1]
[-1, 0, 1]
>>> s2[4]
[-1, 0, 1]
>>> s1[:3] == s2[:3]
True
>>> s1[4].append(2)
>>> s3[6][3]
2
'''


def add_this_many(x, el, s):
    """ Adds el to the end of s the number of times x occurs in s.
    >>> s = [1, 2, 4, 2, 1]
    >>> add_this_many(1, 5, s)
    >>> s
    [1, 2, 4, 2, 1, 5, 5]
    >>> add_this_many(2, 2, s)
    >>> s
    [1, 2, 4, 2, 1, 5, 5, 2, 2]
    """
    "*** YOUR CODE HERE ***"
    # ok
    # count = 0
    # for i in s:
    #     if i == x:
    #         count += 1
    # for i in range(count):
    #     s.append(el)

    for i in range(len(s)):
        if s[i] == x:
            s.append(el)


def filter_iter(iterable, f):
    """
    >>> is_even = lambda x: x % 2 == 0
    >>> list(filter_iter(range(5), is_even)) # a list of the values yielded from the call to filter_iter
    [0, 2, 4]
    >>> all_odd = (2*y-1 for y in range(5))
    >>> list(filter_iter(all_odd, is_even))
    []
    >>> naturals = (n for n in range(1, 100))
    >>> s = filter_iter(naturals, is_even)
    >>> next(s)
    2
    >>> next(s)
    4
    """
    "*** YOUR CODE HERE ***"
    for i in iterable:
        if f(i) == True:
            yield i


def is_prime(n):
    """Returns True if n is a prime number and False otherwise.
    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    def helper(i):
        if i > (n ** 0.5):  # Could replace with i == n
            return True
        elif n % i == 0:
            return False
        return helper(i + 1)
    return helper(2)


def primes_gen(n):
    """Generates primes in decreasing order.
    >>> pg = primes_gen(7)
    >>> list(pg)
    [7, 5, 3, 2]
    """
    if n == 1:
        return
    if is_prime(n):
        yield n
    yield from primes_gen(n-1)

    # while n > 1:
    #     if is_prime(n):
    #         yield n
    #     n -= 1


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
    # ok
    # if is_leaf(t):
    #     return [label(t)]
    # else:
    result = [label(t)]
    for branch in branches(t):
        result.extend(preorder(branch))
    return result


def generate_preorder(t):
    """Yield the entries in this tree in the order that they
    would be visited by a preorder traversal (see problem description).

    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> gen = generate_preorder(numbers)
    >>> next(gen)
    1
    >>> list(gen)
    [2, 3, 4, 5, 6, 7]
    """
    "*** YOUR CODE HERE ***"
    # ok
    # if is_leaf(t):
    #     yield label(t)
    # else:
    #     yield label(t)
    #     for branch in branches(t):
    #         yield from preorder(branch)
    yield label(t)
    for branch in branches(t):
        yield from generate_preorder(branch)


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
