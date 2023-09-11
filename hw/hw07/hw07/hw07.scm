(define (cddr s) (cdr (cdr s)))

(define (cadr s) (car (cdr s)))

(define (caddr s) (car (cdr (cdr s))))

(define (ascending? asc-lst) 
    (cond 
        ((or (null? asc-lst) (null? (cdr asc-lst))) #t) ; 如果列表为空或只有一个元素，认为是非降序
        ((<= (car asc-lst) (cadr asc-lst)) (ascending? (cdr asc-lst))); 当前元素小于等于下一个元素，递归检查其余部分
        (else #f); 当前元素大于下一个元素，不是非降序
        )
    )


(define (square n) (* n n))

(define (pow base exp) 'YOUR-CODE-HERE)
