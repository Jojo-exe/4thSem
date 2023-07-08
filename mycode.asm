.MODEL SMALL
.STACK 100H
.DATA
M1 DB 0AH,0DH,"ENTER A NUMBER $"
M2 DB 0AH,0DH," SUM OF TWO NO:$"
I1 DB ?
I2 DB ? 
AD DB ?

MAIN PROC
    MOV AX, @DATA
    MOV DS, AX
    
    MOV AH, 9
    LEA DX, M1
    INT 21H 
    
    MOV AH,1
    INT 21H 
    MOV I1,AL
    
    MOV AH, 9  
    LEA DX,M1
    INT 21H
    
    MOV AH,1
    INT 21H
  
    CALL ADDITION: 
    CALL DISPLAY:
    
    MAIN ENDP
    
    ADDITION PROC
        
        
        ADD AL,I1
        MOV AD,AL  
        
        
     ADDITION ENDP
     DISPLAY PROC
        MOV AH,9 
        LEA DX,M2
        INT 21H
        
        MOV AH, 2
        SUB AD,30H
        MOV DL,AD
        
        INT 21H
                    
                    
        DISPLAY ENDP
  
        
END MAIN