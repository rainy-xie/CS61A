xie@ThinkXie:~/CS61A/lab/lab10/lab10$ python3 scheme
Welcome to the CS 61A Scheme Interpreter (version 1.2.5)
scm> (and 0 )
0
scm> (and 0 #f)
#f
scm> (and 0 #t)
#t
scm> (define a 1)
a
scm> a
1
scm> (define b a)
b
scm> b
1
scm> (define c 'a)
c
scm> c
a


xie@ThinkXie:~/CS61A/lab/lab10/lab10$ python3 scheme
Welcome to the CS 61A Scheme Interpreter (version 1.2.5)
scm> (define a (+ 1 2))
a
scm> a
3
scm> (define b (-(+(* 3 3)2)1))
b
scm> b
10
scm> (+ a b)
13
scm> (= (modulo b a) (quotient 5 3))
#t

xie@ThinkXie:~/CS61A/lab/lab10/lab10$ python3 scheme
Welcome to the CS 61A Scheme Interpreter (version 1.2.5)
scm> (and (and 14 0.0) (or (or (not 0) (define a 2) (/ 1 0)) 8))
a
scm> a
2
scm> (if (or #t (/ 1 0)) 1 (/ 1 0))
1
scm> ((if (< 4 3) + -) 4 100)
-96
scm> (cond
             ((and (- 4 4) (not #t)) 1)
             ((and (or (< 9 (/ 100 10)) (/ 1 0)) #t) -1)
             (else (/ 1 0))
         )
-1



xie@ThinkXie:~/CS61A/lab/lab10/lab10$ python3 scheme
Welcome to the CS 61A Scheme Interpreter (version 1.2.5)
scm> (define (vir-fib n)
        (if (<= n 1)
        n
        (+ (vir-fib (- n 1)) (vir-fib (- n 2))))
     )
vir-fib
scm> (vir-fib 0)
0
scm> (vir-fib 1)
1
scm> (vir-fib 2)
1
scm> (vir-fib 3)
2
scm> (vir-fib 4)
3
scm> (vir-fib 10)
55

(define with-list
    (list (list 'a 'b) 'c 'd (list 'e))
)
(draw with-list)


(define with-quote
     '((a b) c d (e))
)


(define helpful-list
   (cons 'a (cons 'b nil)))
(draw helpful-list)

(define another-helpful-list
    (cons 'c (cons 'd (cons (cons 'e nil) nil))))
(draw another-helpful-list)

(define with-cons
    (cons
        helpful-list another-helpful-list
    )
)
(draw with-cons)

(define (map-fn fn lst)
    (if (null? lst)
        nil
        (cons (fn (car lst)) (map-fn fn (cdr lst))))
)

(define (remove item lst)
    (if (null? lst)
        nil
        (if (= (car lst) item)
            (remove item (cdr lst))
            (cons (car lst) (remove item (cdr lst)))
        )
    )
)
