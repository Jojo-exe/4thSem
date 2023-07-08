.MODEL SMALL
.STACK 100H 
.DATA
     
     M1 DB "ENTER A NUMBER :$"
     M2 DB 0AH, 0DH, "ITS FACTORIAL :$"
     
.CODE
MAIN PROC
    MOV AX, @DATA
    MOV DS, AX
    XOR CX, CX
    
    MOV AH, 9
    LEA DX, M1
    INT 21H 
    
    MOV AH, 1
    INT 21H 
    
    SUB AL, 30H 
    
    MOV CL, AL
    MOV AX, 1 
    
FACT:
    MUL CX
    LOOP FACT
    
    XOR CX, CX
    MOV BX, 10
    
REPEAT:
    XOR DX, DX
    DIV BX
    INC CX
    PUSH DX
    
    CMP AX, 0
    JNE REPEAT 
    
    MOV AH, 9
    LEA DX, M2
    INT 21H
    
    MOV AH, 2  
     
DISP:
    
    
    POP DX
    ADD DL, 30H
    INT 21H
    LOOP DISP
    
    MOV AH, 4CH
    INT 21H
    MAIN ENDP
END MAIN


