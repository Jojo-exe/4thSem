.MODEL SMALL
.STACK 100H
.DATA
M1 DB "ENTER A NUMBER $"
M2 DB 0AH,0DH,"YOU HAVE TYPED $"

MAIN PROC
    MOV AX, @DATA
    MOV DS, AX
    
    MOV AH, 9
    LEA DX, M1
    INT 21H
    
    CALL DECIN:
    PUSH AX                         
    
    MOV AH, 9
    LEA DX, M2
    INT 21H
    
    POP AX
    
    CALL DECOUT
    
    MOV AH, 4CH
    INT 21H
    MAIN ENDP


    
    DECIN ENDP

DECOUT PROC
    PUSH AX
    PUSH BX
    PUSH CX
    PUSH DX
    
    CMP AX, 0
    JG ALPHA
    
    PUSH AX
    
    MOV DL, '-'
    MOV AH, 2
    INT 21H
    
    POP AX
    NEG AX
    
    ALPHA:
    XOR CX,CX
    MOV BX, 10
    
    WHILE:
    XOR DX, DX
    DIV BX
    PUSH DX
    INC CX
    
    CMP AX, 0
    JNE WHILE
    
    MOV AH, 2
    
    PRINT:
    POP DX 
    ADD DL, 48
    INT 21H
    LOOP PRINT
    
    POP DX
    POP CX
    POP BX
    POP AX
    
    RET
    
    DECOUT ENDP
   
END MAIN