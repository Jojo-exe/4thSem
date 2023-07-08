.MODEL SMALL
.STACK 100H
.DATA
    A DB 0AH,0DH,"ENTER A CHARACTER : $" 
    INV DB 0AH,0DH,"INVALID - ENTER AGIAN : $"
.CODE
MAIN PROC
    MOV AX,@DATA
    MOV DS,AX
  
  MOV AH,9
  LEA DX,A
  INT 21H 
  
  AGAIN:  
  MOV AH,1
  INT 21H
  MOV DL,AL

cmp DL, "A"   
jb INVALID   
cmp DL, "Z"  
jbe CTOS  

cmp DL, 61h  
jb INVALID   
cmp DL, 7Ah   
jbe STOC    

cmp DL, 30h   
jb INVALID  
cmp DL, 39h   
jbe INVALID   

jmp INVALID   
  
  
  
 
  
  STOC:
  AND DL,0DFH ;SMALL TO CAPITAL
  MOV AH,2
  INT 21H
  JMP EXIT
   
  CTOS:
 
  OR DL,20H  ;CAPITAL TO SMALL
  MOV AH,2
  INT 21H
  
  JMP EXIT
  
  INVALID:
   MOV AH,9
  LEA DX,INV
  INT 21H
  
  JMP AGAIN:
   
  EXIT:  
    MOV AH,4CH
    INT 21H
    MAIN ENDP
END MAIN

