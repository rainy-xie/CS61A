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


def store_digits(n,current_link):
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
    