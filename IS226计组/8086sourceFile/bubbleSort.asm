; multi-segment executable file template.
; bubble sort
; cpp算法：
; for(int i=0;i<N;i++){
;   for (int j=i+1;j<N;j++){
;       if(array[i]>=array[j])
;           continue;
;       else{
;           //交换
;           int tmp=array[i]
;           array[i]=array[j]
;           array[j]=tmp
;       }
;   }
;}
data segment
    ; add your data here!
    SCORE DB 11H,02H,15H,32H,5H,6H,7H,8H,9H,10H,90 DUP(05H)
    MAX DB ?
    MIN DB ?
ends


code segment
    assume ds:data,cs:code
start:
    ; set segment registers:
    mov ax, data
    mov ds, ax
    
    lea bx,score    ;取数组首地址
    mov cx,100      ; 定义循环次数变量
    xor si,si       ; int i=0
    xor di,di       ; int j=0
L1: mov ah,[bx+si]  ;l1为外循环，取数据
L2: mov al,[bx+di]  ;L2为内循环
    cmp ah,al
    jae L3          ;若ah>=al,跳转到L3，否则交换两个数
    ;交换开始
    mov dh,ah       
    mov ah,al
    mov al,dh
    ; 交换结束
    mov [bx+di],al  ;将交换后的数存进主存
    mov [bx+si],ah  ;将交换后的数存进主存
L3: inc di          ;若ah>=al,di自增(j++)
    cmp di,100      ;判断内层循环是否结束
    jb L2           ;若di<100，则跳转到l2,继续内层循环；否则结束内层循环，进入外层
    inc si          ;i++
    mov di,si       ;j=i
    loop L1         ;继续外循环
    mov ah,byte ptr[bx] ;基址寻址，数组开头
    mov al,byte ptr[bx+99];基址寻址，数组末尾
    mov max,ah
    mov min,al

    mov ax, 4c00h ; exit to operating system.
    int 21h    
code ends

end start ; set entry point and stop the assembler.
