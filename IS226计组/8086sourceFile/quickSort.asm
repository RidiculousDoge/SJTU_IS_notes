; multi-segment executable file template.
;要用到什么参数就按照顺序进栈
data segment
    ; add your data here!
    array dw 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20, -21, -22, -23, -24, -25
    num dw 49
    begin dw 0
    tail dw 49
    x dw ?
    low dw ?
    high dw ?
    standard dw ?
data ends

stack segment
     stack db 100 dup(0)
     top equ 100
stack ends

code segment
assume ds:data cs:code ss:stack
start:
    mov ax,data
    mov ds,ax
    mov ax,stack 
    mov ss,ax
    mov sp,top
    
    call quicksort
    
    mov ax,4c00h
    int 21h

quicksort proc near
    mov ax,begin 
    cmp ax,tail     ;比较high和low的值
    jge quit1       ;high<low则返回
     
    call divide

    quit1:
        ret

divide proc near
    mov si,offset array 
    mov ax,begin 
    shl ax,1        ;ax左移一位，因为数组是dw
    add si,ax
    mov low,si      
    move ax,[si]
    move standard,ax       ;standard=array[low]
     
     
    for_high:
        mov si,offset array 
        mov ax,j 
        shl ax,1
        add si,ax
        mov ax,[si] ;ax=array[j]
         
        cmp ax,x 
        jl deschigh    ;若array[j]<array[high]不交换,执行high--
        ;交换:
        ;i++
        ;exchange A[i]
        inc i 

        
        deschigh:
         inc j 
         mov ax,tail 
         cmp j,ax
         jl for_j   ;若j<tail则继续循环
     
divide endp
    
code ends
end start ; set entry point and stop the assembler.
