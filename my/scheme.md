# scheme project

## Part 1: The Evaluator

In Part 1, you will develop the following features of the interpreter:

- Symbol evaluation
- Calling built-in procedures
- Definitions

### Problem 1 (1 pt)

```python
class Frame:
    """An environment frame binds Scheme symbols to Scheme values."""

    def __init__(self, parent):
        """An empty frame with parent frame PARENT (which may be None)."""
        self.bindings = {}
        self.parent = parent

    def __repr__(self):
        if self.parent is None:
            return '<Global Frame>'
        s = sorted(['{0}: {1}'.format(k, v) for k, v in self.bindings.items()])
        return '<{{{0}}} -> {1}>'.format(', '.join(s), repr(self.parent))

    def define(self, symbol, value):
        """Define Scheme SYMBOL to have VALUE."""
        # BEGIN PROBLEM 1
        "*** YOUR CODE HERE ***"
        self.bindings[symbol] = value
        # END PROBLEM 1

    def lookup(self, symbol):
        """Return the value bound to SYMBOL. Errors if SYMBOL is not found."""
        # BEGIN PROBLEM 1
        "*** YOUR CODE HERE ***"
        current_frame = self
        while current_frame is not None:
            if symbol in current_frame.bindings:
                return current_frame.bindings[symbol]
            current_frame = current_frame.parent
        # END PROBLEM 1
        raise SchemeError('unknown identifier: {0}'.format(symbol))
```

### Problem 2 (2 pt)

```python
def scheme_apply(procedure, args, env):
    """Apply Scheme PROCEDURE to argument values ARGS (a Scheme list) in
    Frame ENV, the current environment."""
    validate_procedure(procedure)
    if not isinstance(env, Frame):
        assert False, "Not a Frame: {}".format(env)
    if isinstance(procedure, BuiltinProcedure):
        # BEGIN PROBLEM 2
        "*** YOUR CODE HERE ***"
        # py_args = pair_to_list(args)
        py_args = []
        while args:
            py_args.append(args.first)
            args = args.rest
        if procedure.need_env:
            py_args.append(env)
        # END PROBLEM 2
        try:
            # BEGIN PROBLEM 2
            "*** YOUR CODE HERE ***"
            result = procedure.py_func(*py_args)
            return result
            # END PROBLEM 2
        except TypeError as err:
            raise SchemeError(
                'incorrect number of arguments: {0}'.format(procedure))
```

### Problem 3 (2 pt)

```python
def scheme_eval(expr, env, _=None):  # Optional third argument is ignored
    """Evaluate Scheme expression EXPR in Frame ENV.

    >>> expr = read_line('(+ 2 2)')
    >>> expr
    Pair('+', Pair(2, Pair(2, nil)))
    >>> scheme_eval(expr, create_global_frame())
    4
    """
    # Evaluate atoms
    # expr是一个符号symbol
    if scheme_symbolp(expr):
        return env.lookup(expr)  # 查找符号在当前环境中的值
    # expr是一个自求值表达式，比如数字
    elif self_evaluating(expr):
        return expr

    # All non-atomic expressions are lists (combinations)
    # 是否是一个列表（非原子表达式）
    if not scheme_listp(expr):
        raise SchemeError('malformed list: {0}'.format(repl_str(expr)))

    # first 第一个元素，通常为操作符或函数
    # rest 剩余元素，通常为操作数或参数
    first, rest = expr.first, expr.rest
    # 是否是special form (if cond define lambda)
    if scheme_symbolp(first) and first in scheme_forms.SPECIAL_FORMS:
        return scheme_forms.SPECIAL_FORMS[first](rest, env)
    else:   # + - *的情况下
        # BEGIN PROBLEM 3
        "*** YOUR CODE HERE ***"
        operator = scheme_eval(first, env)
        operands = rest.map(lambda operand: scheme_eval(operand, env))
        return scheme_apply(operator, operands, env)
        # END PROBLEM 3
```

### Problem 4 (2 pt)

```python
def do_define_form(expressions, env):
    """Evaluate a define form.
    >>> env = create_global_frame()
    >>> do_define_form(read_line("(x 2)"), env) # evaluating (define x 2)
    'x'
    >>> scheme_eval("x", env)
    2
    >>> do_define_form(read_line("(x (+ 2 8))"), env) # evaluating (define x (+ 2 8))
    'x'
    >>> scheme_eval("x", env)
    10
    >>> # problem 10
    >>> env = create_global_frame()
    >>> do_define_form(read_line("((f x) (+ x 2))"), env) # evaluating (define (f x) (+ x 8))
    'f'
    >>> scheme_eval(read_line("(f 3)"), env)
    5
    """
    validate_form(expressions, 2)  # Checks that expressions is a list of length at least 2
    signature = expressions.first
    if scheme_symbolp(signature):
        # assigning a name to a value e.g. (define x (+ 1 2))
        validate_form(expressions, 2, 2)  # Checks that expressions is a list of length exactly 2
        # BEGIN PROBLEM 4
        "*** YOUR CODE HERE ***"
        value = scheme_eval(expressions.rest.first,env)
        env.define(signature,value)
        return signature
        # END PROBLEM 4
```

### Problem 5 (1 pt)

```python
def do_quote_form(expressions, env):
    """Evaluate a quote form.

    >>> env = create_global_frame()
    >>> do_quote_form(read_line("((+ x 2))"), env) # evaluating (quote (+ x 2))
    Pair('+', Pair('x', Pair(2, nil)))
    """
    validate_form(expressions, 1, 1)
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"
    return expressions.first
    # END PROBLEM 5
```

## Part 2: Procedures

In Part 2, you will add the ability to create and call user-defined procedures. You will add the following features to the interpreter:

- Lambda procedures, using the `(lambda ...)` special form
- Named procedures, using the `(define (...) ...)` special form
- Dynamically scoped mu procedures, using the `(mu ...)` special form.

### User-Defined Procedures

User-defined lambda procedures are represented as instances of the `LambdaProcedure` class. A `LambdaProcedure` instance has three instance attributes:

- `formals` is a Scheme list of the formal parameters (symbols) that name the arguments of the procedure.
- `body` is a Scheme list of expressions; the body of the procedure.
- `env` is the environment in which the procedure was **defined**.

### Problem 6 (1 pt)

```python
def eval_all(expressions, env):
    """Evaluate each expression in the Scheme list EXPRESSIONS in
    Frame ENV (the current environment) and return the value of the last.

    >>> eval_all(read_line("(1)"), create_global_frame())
    1
    >>> eval_all(read_line("(1 2)"), create_global_frame())
    2
    >>> x = eval_all(read_line("((print 1) 2)"), create_global_frame())
    1
    >>> x
    2
    >>> eval_all(read_line("((define x 2) x)"), create_global_frame())
    2
    """
    # BEGIN PROBLEM 6
    # replace this with lines of your own code
    # return scheme_eval(expressions.first, env)
    if expressions is nil:
        return None
    while expressions.rest is not nil:
        scheme_eval(expressions.first,env)
        expressions = expressions.rest
    return scheme_eval(expressions.first,env)
    # END PROBLEM 6

```

### Problem 7 (2 pt)

```python
def do_lambda_form(expressions, env):
    """Evaluate a lambda form.

    >>> env = create_global_frame()
    >>> do_lambda_form(read_line("((x) (+ x 2))"), env) # evaluating (lambda (x) (+ x 2))
    LambdaProcedure(Pair('x', nil), Pair(Pair('+', Pair('x', Pair(2, nil))), nil), <Global Frame>)
    """
    validate_form(expressions, 2)
    formals = expressions.first
    validate_formals(formals)
    # BEGIN PROBLEM 7
    "*** YOUR CODE HERE ***"
    body = expressions.rest
    return LambdaProcedure(formals, body, env)
    # END PROBLEM 7
```

### Problem 8 (2 pt)

```python
    def make_child_frame(self, formals, vals):
        """Return a new local frame whose parent is SELF, in which the symbols
        in a Scheme list of formal parameters FORMALS are bound to the Scheme
        values in the Scheme list VALS. Both FORMALS and VALS are represented
        as Pairs. Raise an error if too many or too few vals are given.

        >>> env = create_global_frame()
        >>> formals, expressions = read_line('(a b c)'), read_line('(1 2 3)')
        >>> env.make_child_frame(formals, expressions)
        <{a: 1, b: 2, c: 3} -> <Global Frame>>
        """
        if len(formals) != len(vals):
            raise SchemeError('Incorrect number of arguments to function call')
        # BEGIN PROBLEM 8
        "*** YOUR CODE HERE ***"
        child_frame = Frame(self)
        while formals is not nil:
            child_frame.define(formals.first,vals.first)
            formals = formals.rest
            vals = vals.rest 
        return child_frame
        # END PROBLEM 8
```

### Problem 9 (2 pt)

```python
def scheme_apply(procedure, args, env):
    """Apply Scheme PROCEDURE to argument values ARGS (a Scheme list) in
    Frame ENV, the current environment."""
    validate_procedure(procedure)
    if not isinstance(env, Frame):
        assert False, "Not a Frame: {}".format(env)
    if isinstance(procedure, BuiltinProcedure):
        # BEGIN PROBLEM 2
        "*** YOUR CODE HERE ***"
        # py_args = pair_to_list(args)
        py_args = []
        while args:
            py_args.append(args.first)
            args = args.rest
        if procedure.need_env:
            py_args.append(env)
        # END PROBLEM 2
        try:
            # BEGIN PROBLEM 2
            "*** YOUR CODE HERE ***"
            result = procedure.py_func(*py_args)
            return result
            # END PROBLEM 2
        except TypeError as err:
            raise SchemeError(
                'incorrect number of arguments: {0}'.format(procedure))
    elif isinstance(procedure, LambdaProcedure):
        # BEGIN PROBLEM 9
        "*** YOUR CODE HERE ***"
        child_frame = procedure.env.make_child_frame(procedure.formals,args)
        return eval_all(procedure.body,child_frame)
        # END PROBLEM 9
```

### Problem 10 (1 pt)

```python
def do_define_form(expressions, env):
    """Evaluate a define form.
    >>> env = create_global_frame()
    >>> do_define_form(read_line("(x 2)"), env) # evaluating (define x 2)
    'x'
    >>> scheme_eval("x", env)
    2
    >>> do_define_form(read_line("(x (+ 2 8))"), env) # evaluating (define x (+ 2 8))
    'x'
    >>> scheme_eval("x", env)
    10
    >>> # problem 10
    >>> env = create_global_frame()
    >>> do_define_form(read_line("((f x) (+ x 2))"), env) # evaluating (define (f x) (+ x 8))
    'f'
    >>> scheme_eval(read_line("(f 3)"), env)
    5
    """
    validate_form(
        expressions, 2)  # Checks that expressions is a list of length at least 2
    signature = expressions.first
    if scheme_symbolp(signature):
        # assigning a name to a value e.g. (define x (+ 1 2))
        # Checks that expressions is a list of length exactly 2
        validate_form(expressions, 2, 2)
        # BEGIN PROBLEM 4
        "*** YOUR CODE HERE ***"
        value = scheme_eval(expressions.rest.first, env)
        env.define(signature, value)
        return signature
        # END PROBLEM 4
    elif isinstance(signature, Pair) and scheme_symbolp(signature.first):
        # defining a named procedure e.g. (define (f x y) (+ x y))
        # BEGIN PROBLEM 10
        "*** YOUR CODE HERE ***"
        formals = signature.rest
        validate_formals(formals)
        body = expressions.rest
        env.define(signature.first,LambdaProcedure(formals,body,env))
        return signature.first
        # END PROBLEM 10
    else:
        bad_signature = signature.first if isinstance(
            signature, Pair) else signature
        raise SchemeError('non-symbol: {0}'.format(bad_signature))
```

### Problem 11 (1 pt)

```python
def do_mu_form(expressions, env):
    """Evaluate a mu form."""
    validate_form(expressions, 2)
    formals = expressions.first
    validate_formals(formals)
    # BEGIN PROBLEM 11
    "*** YOUR CODE HERE ***"
    body = expressions.rest
    validate_formals(formals)
    return MuProcedure(formals, body)
    # END PROBLEM 11
```

```python
def scheme_apply(procedure, args, env):
    """Apply Scheme PROCEDURE to argument values ARGS (a Scheme list) in
    Frame ENV, the current environment."""
    validate_procedure(procedure)
    if not isinstance(env, Frame):
        assert False, "Not a Frame: {}".format(env)
    if isinstance(procedure, BuiltinProcedure):
        # BEGIN PROBLEM 2
        "*** YOUR CODE HERE ***"
        # py_args = pair_to_list(args)
        py_args = []
        while args:
            py_args.append(args.first)
            args = args.rest
        if procedure.need_env:
            py_args.append(env)
        # END PROBLEM 2
        try:
            # BEGIN PROBLEM 2
            "*** YOUR CODE HERE ***"
            result = procedure.py_func(*py_args)
            return result
            # END PROBLEM 2
        except TypeError as err:
            raise SchemeError(
                'incorrect number of arguments: {0}'.format(procedure))
    elif isinstance(procedure, LambdaProcedure):
        # BEGIN PROBLEM 9
        "*** YOUR CODE HERE ***"
        child_frame = procedure.env.make_child_frame(procedure.formals,args)
        return eval_all(procedure.body,child_frame)
        # END PROBLEM 9
    elif isinstance(procedure, MuProcedure):
        # BEGIN PROBLEM 11
        "*** YOUR CODE HERE ***"
        mu_env = env.make_child_frame(procedure.formals,args)
        return eval_all(procedure.body,mu_env)
        # END PROBLEM 11
    else:
        assert False, "Unexpected procedure: {}".format(procedure)
```

## Part 3: Special Forms

### Problem 12 (2 pt)

```python
def do_and_form(expressions, env):
    """Evaluate a (short-circuited) and form.

    Args:
        expressions: The expressions for the and form.
        env: The current environment.

    Returns:
        The result of the and form evaluation.
    """
    if expressions is nil:  # 如果没有子表达式，则返回 #t
        return True

    # 遍历并逐个评估子表达式
    while expressions.rest is not nil:
        value = scheme_eval(expressions.first, env)
        if is_scheme_false(value):  # 如果有子表达式为 #f，立即返回 #f
            return False
        expressions = expressions.rest

    # 返回最后一个子表达式的结果
    return scheme_eval(expressions.first, env)

def do_or_form(expressions, env):
    """Evaluate an or form.

    Args:
        expressions: The expressions for the or form.
        env: The current environment.

    Returns:
        The result of the or form evaluation.
    """
    if expressions is nil:  # 如果没有子表达式，则返回 #f
        return False

    # 遍历并逐个评估子表达式
    while expressions.rest is not nil:
        value = scheme_eval(expressions.first, env)
        if is_scheme_true(value):  # 如果有子表达式为 #t，立即返回 #t
            return value
        expressions = expressions.rest

    # 返回最后一个子表达式的结果
    return scheme_eval(expressions.first, env)
```

### Problem 13 (2 pt)

```python
def do_cond_form(expressions, env):
    """Evaluate a cond form.

    Args:
        expressions: The expressions for the cond form.
        env: The current environment.

    Returns:
        The result of the cond form evaluation.
    """
    while expressions is not nil:
        clause = expressions.first
        validate_form(clause, 1)
        if clause.first == 'else':
            test = True
            if expressions.rest != nil:
                raise SchemeError('else must be last')
        else:
            test = scheme_eval(clause.first, env)
        if is_scheme_true(test):
            # 如果找到真值子句
            if clause.rest is nil:
                return test  # 如果真值子句没有结果表达式，返回真值
            else:
                return eval_all(clause.rest, env)  # 评估真值子句的结果表达式
        expressions = expressions.rest

```



### Problem 14 (2 pt)

```python
def make_let_frame(bindings, env):
    """Create a child frame of Frame ENV that contains the definitions given in
    BINDINGS. The Scheme list BINDINGS must have the form of a proper bindings
    list in a let expression: each item must be a list containing a symbol
    and a Scheme expression."""
    if not scheme_listp(bindings):
        raise SchemeError('bad bindings list in let form')
    names = vals = nil
    # BEGIN PROBLEM 14
    "*** YOUR CODE HERE ***"
    while bindings is not nil:
        binding = bindings.first
        validate_form(binding, 2, 2)
        name, value = binding.first, binding.rest.first
        names = Pair(name, names)
        vals = Pair(scheme_eval(value, env), vals)
        bindings = bindings.rest
    validate_formals(names)
    # END PROBLEM 14
    return env.make_child_frame(names, vals)
```

