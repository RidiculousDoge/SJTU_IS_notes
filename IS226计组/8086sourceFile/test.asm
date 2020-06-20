; multi-segment executable file template.

data segment
    ; add your data here!
    ;pkey db "press any key...$"
    a dw 13,14  ;数组
    db 'hello HAPPY!!!','$'     ;需要输出的字符串以$结尾
data ends

stack segment
    dw   10  dup(0)    ; 定义dw类型�?，重�?28次（栈深�?28个字�
end
CODESEG segment
start:
     mov ax,data
     mov ds,ax
     mov dx,0
     mov ah,9
     int 21h
     
     mov ax,4c00h
     int 21h
end