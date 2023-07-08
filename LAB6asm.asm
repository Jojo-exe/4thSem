.MODEL SMALL
.STACK 100H
.DATA 
        
        M1 DB "eNTER A cHARACTER:$"
        M2 DB "EVEN:$"
        M3 DB "ODD:$"
        
        
.CODE 
MAIN PROC 
    MOV AX,@DATA
    MOV DS,AX
    
    MOV AH,9
    LEA DX,M1
    INT 21H
    
    MOV AH,1
    INT 21H         
    MOV BL,AL 
    
    MOV CL, 8
    MOV CL, BL
    JC ODD
    
    MOV AH, 9
    LEA DX, M2
    INT 21H
    
    JMP EXIT 
    ODD:
    MOV AH, 9
    LEA DX, M3
    INT 21H
     
    
    
    EXIT:
    MOV AH,4CH
    INT 21H
    MAIN ENDP
END MAIN