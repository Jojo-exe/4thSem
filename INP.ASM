.MODEL SMALL
.STACK 100H
.DATA
       ARR DW 3 DUP(?)
       M1 DB 0AH,0DH,"ENTER A NUMBER: $" 
       M2 DB 0AH,0DH, "SUM: $"
       M3 DB 0AH,0DH,"AVERAGE: $"
.CODE
MAIN PROC
    MOV AX,@DATA
    MOV DS, AX
    
    LEA SI, ARR
    MOV CX, 3
    
    INP:
    MOV AH, 9
    INT 21H
    LEA DX, M1
    
    CALL DECIMAL_INPUT
    
    MOV [SI], AL
    INC SI
    INC SI 
    
    LOOP INP
    
    LEA SI, ARR
    MOV AX, 0
     MOV CX, 3
     
    ADD_UP:
    ADD AX, [SI]
    INC SI
    INC SI
    LOOP ADD_UP
    
    PUSH AX
     
    MOV AH, 9
    LEA DX, M2
    INT 21H
    
    POP AX 

    CALL DECOUT   
    
      PUSH AX
     MOV AH, 9
     LEA DX, M3
     INT 21H
     POP AX 
     
     MOV CL,2
     DIV CL
     
     
     
     
     
     
        
           
    
     CALL DECOUT     
    
    MOV AH, 4CH
    INT 21H
    
    MAIN ENDP
INCLUDE DECIN.ASM
INCLUDE DECO.ASM
END MAIN