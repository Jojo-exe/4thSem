.MODEL SMALL
.STACK 100H
.DATA
             M1 DB "eNTER A cHRACTER: $"
             M2 DB 0AH,0DH,"POSITIVE$"
             M3 DB 0AH,0DH,"NEGATIVE$"
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
 
     

    SHL BL, 1
    JC POSITIVE
     
    MOV AH,9
    LEA DX,M2
    INT 21H 
    JMP EXIT 
    
    POSITIVE:
    MOV AH,9
    LEA DX,M3
    INT 21H
    JMP EXIT
    

   
    
 
EXIT:    
    MOV AH,4CH
    INT 21H
    MAIN ENDP
END MAIN