
(declare-const vs0 Real)    ; value function s0
(declare-const vs1 Real)    ; value function s1
(declare-const vs2 Real)    ; value function s2
(declare-const vs3 Real)    ; value function s3
(declare-const vs4 Real)    ; value function s4
(declare-const vs5 Real)    ; value function s5
(declare-const vs6 Real)    ; value function s6
(declare-const vs7 Real)    ; value function s7
(declare-const vs8 Real)    ; value function s8

(declare-const re Real)     ; reward for moving to empty position
(declare-const rg Real)     ; reward for reaching goal
(declare-const rt Real)     ; reward for falling into trap

(declare-const p Real)      ; transfer probabilities

(declare-const gamma Real)  ; discount

(declare-const s0n Real)    ; partial sum: moving north in s0
(declare-const s0e Real)    ; partial sum: moving east in s0
(declare-const s0s Real)    ; partial sum: moving south in s0
(declare-const s0w Real)    ; partial sum: moving west in s0

(declare-const s1n Real)    ; partial sum: moving north in s1
(declare-const s1e Real)    ; partial sum: moving east in s1
(declare-const s1s Real)    ; partial sum: moving south in s1
(declare-const s1w Real)    ; partial sum: moving west in s1

(declare-const s4n Real)    ; partial sum: moving north in s4
(declare-const s4e Real)    ; partial sum: moving east in s4
(declare-const s4s Real)    ; partial sum: moving south in s4
(declare-const s4w Real)    ; partial sum: moving west in s4

(declare-const s5n Real)    ; partial sum: moving north in s5
(declare-const s5e Real)    ; partial sum: moving east in s5
(declare-const s5s Real)    ; partial sum: moving south in s5
(declare-const s5w Real)    ; partial sum: moving west in s5

(declare-const s6n Real)    ; partial sum: moving north in s6
(declare-const s6e Real)    ; partial sum: moving east in s6
(declare-const s6s Real)    ; partial sum: moving south in s6
(declare-const s6w Real)    ; partial sum: moving west in s6

(declare-const s7n Real)    ; partial sum: moving north in s7
(declare-const s7e Real)    ; partial sum: moving east in s7
(declare-const s7s Real)    ; partial sum: moving south in s7
(declare-const s7w Real)    ; partial sum: moving west in s7

(declare-const s8n Real)    ; partial sum: moving north in s8
(declare-const s8e Real)    ; partial sum: moving east in s8
(declare-const s8s Real)    ; partial sum: moving south in s8
(declare-const s8w Real)    ; partial sum: moving west in s8

; setting constants
(assert (and (= vs2 0.0) (= vs3 0.0)
             (= re -1.0) (= rg 10.0) (= rt -10.0)
             (= p 1.0) (= gamma 0.8)))

; calculating partial sums
(assert (= s0n (* p (+ re (* gamma vs0)))))
(assert (= s0e (* p (+ re (* gamma vs1)))))
(assert (= s0s (* p (+ rt (* gamma vs3)))))
(assert (= s0w (* p (+ re (* gamma vs0)))))
(assert (= s1n (* p (+ re (* gamma vs1)))))
(assert (= s1e (* p (+ rg (* gamma vs2)))))
(assert (= s1s (* p (+ re (* gamma vs4)))))
(assert (= s1w (* p (+ re (* gamma vs0)))))
(assert (= s4n (* p (+ re (* gamma vs1)))))
(assert (= s4e (* p (+ re (* gamma vs5)))))
(assert (= s4s (* p (+ re (* gamma vs7)))))
(assert (= s4w (* p (+ rt (* gamma vs3)))))
(assert (= s5n (* p (+ rg (* gamma vs2)))))
(assert (= s5e (* p (+ re (* gamma vs5)))))
(assert (= s5s (* p (+ re (* gamma vs8)))))
(assert (= s5w (* p (+ re (* gamma vs4)))))
(assert (= s6n (* p (+ rt (* gamma vs3)))))
(assert (= s6e (* p (+ re (* gamma vs7)))))
(assert (= s6s (* p (+ re (* gamma vs6)))))
(assert (= s6w (* p (+ re (* gamma vs6)))))
(assert (= s7n (* p (+ re (* gamma vs4)))))
(assert (= s7e (* p (+ re (* gamma vs8)))))
(assert (= s7s (* p (+ re (* gamma vs7)))))
(assert (= s7w (* p (+ re (* gamma vs6)))))
(assert (= s8n (* p (+ re (* gamma vs5)))))
(assert (= s8e (* p (+ re (* gamma vs8)))))
(assert (= s8s (* p (+ re (* gamma vs8)))))
(assert (= s8w (* p (+ re (* gamma vs7)))))

; Bellman optimality equations
(define-fun max2 ((a Real) (b Real)) Real
                  (ite (> a b) a b))

(define-fun max4 ((a Real) (b Real) (c Real) (d Real)) Real
                  (max2 (max2 a b) (max2 c d)))
(assert (and (= vs0 (max4 s0n s0e s0s s0w))
             (= vs1 (max4 s1n s1e s1s s1w))
             (= vs4 (max4 s4n s4e s4s s4w))
             (= vs5 (max4 s5n s5e s5s s5w))
             (= vs6 (max4 s6n s6e s6s s6w))
             (= vs7 (max4 s7n s7e s7s s7w))
             (= vs8 (max4 s8n s8e s8s s8w))))

(check-sat)
(get-model)