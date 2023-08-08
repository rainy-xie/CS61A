## lab06

```bash
append(el): Add el to the end of the list. Return None.
extend(lst): Extend the list by concatenating it with lst. Return None.
insert(i, el): Insert el at index i. This does not replace any existing elements, but only adds the new element el. Return None.
remove(el): Remove the first occurrence of el in list. Errors if el is not in the list. Return None otherwise.
pop(i): Remove and return the element at index i.


map(f, iterable) - Creates an iterator over f(x) for x in iterable. In some cases, computing a list of the values in this iterable will give us the same result as [func(x) for x in iterable]. However, it's important to keep in mind that iterators can potentially have infinite values because they are evaluated lazily, while lists cannot have infinite elements.
filter(f, iterable) - Creates an iterator over x for each x in iterable if f(x)
zip(iterables*) - Creates an iterator over co-indexed tuples with elements from each of the iterables
reversed(iterable) - Creates an iterator over all the elements in the input iterable in reverse order
list(iterable) - Creates a list containing all the elements in the input iterable
tuple(iterable) - Creates a tuple containing all the elements in the input iterable
sorted(iterable) - Creates a sorted list containing all the elements in the input iterable
reduce(f, iterable) - Must be imported with functools. Apply function of two arguments f cumulatively to the items of iterable, from left to right, so as to reduce the sequence to a single value.
```

Python's built-in `map`, `filter`, and `zip` functions return **iterators**, not lists.
