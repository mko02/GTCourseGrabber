

.orig x3000

    ADD R6, R6, #-1
    STR R2, R6, 0       ;   push c onto the stack

    ADD R6, R6, #-1
    STR R1, R6, 0       ;   push b onto the stack

    ADD R6, R6, #-1
    STR R0, R6, 0       ;   push a onto the stack

    JSR ADDTHREE


    ADD R6, R6, #-1     ;   make space for RV on the stack

    ADD R6, R6, #-1
    STR R7, R6, 0       ;   push old RA onto the stack

    ADD R6, R6, #-1
    STR R5, R6, 0       ;   push old FP onto the stack

    ADD R6, R6, #-1     ;   make space for one LV on the stack
    ADD	R5,	R6,	0       ;   set current FP = SP

    ADD	R6,	R6,	-5       ;    save sapce for 5 regs
    STR	R0,	R6,	0       
    STR	R1,	R6,	1
    STR	R2,	R6,	2       
    STR	R3,	R6,	3
    STR	R4,	R6,	4      



    LDR	R4,	R6,	4   ;   restore R4
    LDR	R3,	R6,	3
    LDR	R2,	R6,	2
    LDR	R1,	R6,	1
    LDR	R0,	R6,	0   ;   restore R0
    
    ADD R6, R5, 0   ;   pop registers off stack

    LDR	R7,	R5,	2   ;   R7 = RA
    LDR	R5,	R5,	1   ;   FP = old FP
    ADD R6, R6, 3   ;   pop first lc, old FP, RA

    RET

    LDR	R4,	R6,	0   ;   R4 = add3num(R0, R1, R2)
    ADD R6, R6, 1   ;   pop RV

    STR	R0,	R5,	3   ;   RV = BINARY_SEARCH(root.left, data)

    ADD R6, R6, 3   ;   pop args






    