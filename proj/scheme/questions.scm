(define (caar x) (car (car x)))
(define (cadr x) (car (cdr x)))
(define (cdar x) (cdr (car x)))
(define (cddr x) (cdr (cdr x)))

;; Problem 15
;; Returns a list of two-element lists
(define (enumerate s)
  ; BEGIN PROBLEM 15
  (define (enumerate-helper s index)
    (cond
      ((null? s) '())                   ; 如果列表为空，返回空列表
      (else (cons (list index (car s))  ; 创建包含索引和元素的子列表
                  (enumerate-helper (cdr s) (+ index 1))))))  ; 递归处理剩余的元素
  (enumerate-helper s 0)  ; 从索引0开始递归处理输入列表
  )
  ; END PROBLEM 15

;; Problem 16

;; Merge two lists LIST1 and LIST2 according to ORDERED? and return
;; the merged lists.
(define (merge ordered? list1 list2)
  ; BEGIN PROBLEM 16
    (cond
    ((null? list1) list2)              ; 如果 list1 为空，返回 list2
    ((null? list2) list1)              ; 如果 list2 为空，返回 list1
    ((ordered? (car list1) (car list2))  ; 如果 list1 的第一个元素比 list2 的第一个元素小（或相等）
     (cons (car list1)                  ; 将 list1 的第一个元素添加到结果中
           (merge ordered? (cdr list1) list2))) ; 递归地合并剩余部分
    (else                              ; 否则， list2 的第一个元素更小
     (cons (car list2)                  ; 将 list2 的第一个元素添加到结果中
           (merge ordered? list1 (cdr list2)))))) ; 递归地合并剩余部分

  ; END PROBLEM 16

;; Optional Problem

;; Returns a function that checks if an expression is the special form FORM
(define (check-special form)
  (lambda (expr) (equal? form (car expr))))

(define lambda? (check-special 'lambda))
(define define? (check-special 'define))
(define quoted? (check-special 'quote))
(define let?    (check-special 'let))

;; Converts all let special forms in EXPR into equivalent forms using lambda
(define (let-to-lambda expr)
  (cond ((atom? expr)
         ; BEGIN OPTIONAL PROBLEM
         'replace-this-line
         ; END OPTIONAL PROBLEM
         )
        ((quoted? expr)
         ; BEGIN OPTIONAL PROBLEM
         'replace-this-line
         ; END OPTIONAL PROBLEM
         )
        ((or (lambda? expr)
             (define? expr))
         (let ((form   (car expr))
               (params (cadr expr))
               (body   (cddr expr)))
           ; BEGIN OPTIONAL PROBLEM
           'replace-this-line
           ; END OPTIONAL PROBLEM
           ))
        ((let? expr)
         (let ((values (cadr expr))
               (body   (cddr expr)))
           ; BEGIN OPTIONAL PROBLEM
           'replace-this-line
           ; END OPTIONAL PROBLEM
           ))
        (else
         ; BEGIN OPTIONAL PROBLEM
         'replace-this-line
         ; END OPTIONAL PROBLEM
         )))

; Some utility functions that you may find useful to implement for let-to-lambda

(define (zip pairs)
  'replace-this-line)
