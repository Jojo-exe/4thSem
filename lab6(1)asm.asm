.MODEL SMALL
.STACK 100H
.DATA
     I DB "ENTER A CHARACTER$" 
     R DB "YOU ENTERED CAPITAL CHARACTER$"
     R2 DB "YOU ENTERED SMALL CHARACTER$" 
     R3 DB "YOU ENTERED SPECIAL CHARACTER$"
     
.CODE
MAIN PROC
    MOV AX,@DATA
    MOV DS,AX      

     MOV AH,9
     LEA DX,I
     INT 21H
     
     MOV AH,1
     INT 21H
     
     CMP AL,5AH 
     JL CAPITAL
                
     CMP AL,61H 
     JG SMALL 
     
     JMP EXIT
     
     
CAPITAL:
     CMP AL,41
     JL SPECIAL
   
     MOV AH,9
     LEA DX,R
     INT 21H 
     
     JMP  EXIT 
SMALL:  
     CMP AL,7AH
     JG SPECIAL
 
     MOV AH,9
     LEA DX,R2
     INT 21H 
     
     JMP  EXIT
     
SPECIAL:
     MOV AH,9
     LEA DX,R3
     INT 21H
     
     JMP EXIT
    
EXIT:               
    MOV AH,4CH
    INT 21H
    MAIN ENDP
END MAIN