
(declare-const vs11 Real)    ; value function s11
(declare-const vs12 Real)    ; value function s12
(declare-const vs13 Real)    ; value function s13
(declare-const vs21 Real)    ; value function s21
(declare-const vs22 Real)    ; value function s22
(declare-const vs23 Real)    ; value function s23
(declare-const vs31 Real)    ; value function s31
(declare-const vs32 Real)    ; value function s32
(declare-const vs33 Real)    ; value function s33

(declare-const re Real)     ; reward for moving to empty position
(declare-const rg Real)     ; reward for reaching goal
(declare-const rt Real)     ; reward for falling into trap
(declare-const ri Real)     ; reward for getting ice cream

(declare-const p1 Real)      ; transfer probability 1
(declare-const p6 Real)      ; transfer probability 0.6
(declare-const p4 Real)      ; transfer probability 0.4
(declare-const p9 Real)      ; transfer probability 0.9
(declare-const pp1 Real)      ; transfer probability 0.1

(declare-const gamma Real)  ; discount

(declare-const s11n Real)    ; partial sum: moving north in s11
(declare-const s11e Real)    ; partial sum: moving east in s11
(declare-const s11s Real)    ; partial sum: moving south in s11
(declare-const s11w Real)    ; partial sum: moving west in s11

(declare-const s12n Real)    ; partial sum: moving north in s12
(declare-const s12e Real)    ; partial sum: moving east in s12
(declare-const s12s Real)    ; partial sum: moving south in s12
(declare-const s12w Real)    ; partial sum: moving west in s12

(declare-const s21n Real)    ; partial sum: moving north in s21
(declare-const s21e Real)    ; partial sum: moving east in s21
(declare-const s21s Real)    ; partial sum: moving south in s21
(declare-const s21w Real)    ; partial sum: moving west in s21

(declare-const s23n Real)    ; partial sum: moving north in s23
(declare-const s23e Real)    ; partial sum: moving east in s23
(declare-const s23s Real)    ; partial sum: moving south in s23
(declare-const s23w Real)    ; partial sum: moving west in s23

(declare-const s31n Real)    ; partial sum: moving north in s31
(declare-const s31e Real)    ; partial sum: moving east in s31
(declare-const s31s Real)    ; partial sum: moving south in s31
(declare-const s31w Real)    ; partial sum: moving west in s31

(declare-const s32n Real)    ; partial sum: moving north in s32
(declare-const s32e Real)    ; partial sum: moving east in s32
(declare-const s32s Real)    ; partial sum: moving south in s32
(declare-const s32w Real)    ; partial sum: moving west in s32

(declare-const s33n Real)    ; partial sum: moving north in s33
(declare-const s33e Real)    ; partial sum: moving east in s33
(declare-const s33s Real)    ; partial sum: moving south in s33
(declare-const s33w Real)    ; partial sum: moving west in s33

; setting constants
(assert (and (= vs13 0.0) (= vs22 0.0)
             (= re -1.0) (= rg 10.0) (= rt -10.0) (= ri 5.0)
             (= p1 1.0) (= p6 0.6) (= p4 0.4) (= p9 0.9) (= pp1 0.1) (= gamma 0.8)))

; calculating partial sums
(assert (= s11n (+ (* p1 (+ re (* gamma vs11))))))
(assert (= s11e (+ (* p1 (+ re (* gamma vs12))))))
(assert (= s11s (+ (* p1 (+ re (* gamma vs21))))))
(assert (= s11w (+ (* p1 (+ re (* gamma vs11))))))

(assert (= s12n (+ (* p6 (+ re (* gamma vs12))) (* p4 (+ rt (* gamma vs22))))))
(assert (= s12e (+ (* p6 (+ rg (* gamma vs13))) (* p4 (+ rt (* gamma vs22))))))
(assert (= s12s (+ (* p1 (+ rt (* gamma vs22))))))
(assert (= s12w (+ (* p6 (+ re (* gamma vs11))) (* p4 (+ rt (* gamma vs22))))))

(assert (= s21n (+ (* p1 (+ re (* gamma vs11))))))
(assert (= s21e (+ (* p1 (+ rt (* gamma vs22))))))
(assert (= s21s (+ (* p1 (+ re (* gamma vs31))))))
(assert (= s21w (+ (* p1 (+ re (* gamma vs21))))))

(assert (= s23n (+ (* p1 (+ rg (* gamma vs13))))))
(assert (= s23e (+ (* p1 (+ re (* gamma vs23))))))
(assert (= s23s (+ (* p1 (+ re (* gamma vs33))))))
(assert (= s23w (+ (* p1 (+ rt (* gamma vs22))))))

(assert (= s31n (+ (* p1 (+ re (* gamma vs21))))))
(assert (= s31e (+ (* p9 (+ re (* gamma vs32))) (* pp1 (+ ri (* gamma vs32))))))
(assert (= s31s (+ (* p1 (+ re (* gamma vs31))))))
(assert (= s31w (+ (* p1 (+ re (* gamma vs31))))))

(assert (= s32n (+ (* p1 (+ rt (* gamma vs22))))))
(assert (= s32e (+ (* p1 (+ re (* gamma vs33))))))
(assert (= s32s (+ (* p1 (+ re (* gamma vs32))))))
(assert (= s32w (+ (* p1 (+ re (* gamma vs31))))))

(assert (= s33n (+ (* p1 (+ re (* gamma vs23))))))
(assert (= s33e (+ (* p1 (+ re (* gamma vs33))))))
(assert (= s33s (+ (* p1 (+ re (* gamma vs33))))))
(assert (= s33w (+ (* p9 (+ re (* gamma vs32))) (* pp1 (+ ri (* gamma vs32))))))

; Bellman optimality equations
(define-fun max2 ((a Real) (b Real)) Real
                  (ite (> a b) a b))

(define-fun max4 ((a Real) (b Real) (c Real) (d Real)) Real
                  (max2 (max2 a b) (max2 c d)))
(assert (and (= vs11 (max4 s11n s11e s11s s11w))
             (= vs12 (max4 s12n s12e s12s s12w))
             (= vs21 (max4 s21n s21e s21s s21w))
             (= vs23 (max4 s23n s23e s23s s23w))
             (= vs31 (max4 s31n s31e s31s s31w))
             (= vs32 (max4 s32n s32e s32s s32w))
             (= vs33 (max4 s33n s33e s33s s33w))))

(check-sat)
(get-model)