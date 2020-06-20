datas segment
    count dw 6
    data db 6,5,4,3,2,1
datas ends

codes segment
assume cs:codes,ds:datas
start:
   mov ax,datas
   mov ds,ax

   mov si,offset data
   mov di,offset data
   mov bi,offset data 
   add bx,count     
   dec bx   ;bx为数组结束地址
   call qsort
   mov cx,count 
   call show

   mov ah,4ch
   int 21h
    
 ;di,bx分别为数组起始和结束地址
 ;实现快速排序   
qsort proc near
    push di
    push bx
    cmp di,bx
    jnb next    ;如果di>=bx则转next，否则开始快速排序

    push di
    push bx
    call divide ;一趟分割返回mid
    pop bx      ;bx=mid
    pop di
    push bx
    mov bx,ax
    dec bx
    push di
    push bx
    call qsort
    pop bx
    pop di
    pop bx
    mov di,ax
    inc di
    push di
    push bx
    call qsort
    pop bx
    pop di
next:
    pop bx
    pop di
    ret
    qsort endp

;dl=&array[low],bx=&array[high]
divide proc near
    mov cl,[di]         ;cl保存array[low]，是standard元素
ag: cmp di,bx           
    jnb next2            ;如果low>=high则转next，否则开始分割
moveHigh:  
    cmp di,bx         
    jne exchangeOne     ;如果low>=high则转one，否则从high向后找，直到找到比array[low]小的为止
    cmp [bx],cl
    jb exchangeOne      ;如果array[high]<array[low]，转one
    dec bx              ;high--
    jmp moveHigh               
exchangeOne: 
     mov ch,[bx]        ;ch保存array[high]
     mov ah,[di]        ;ah保存array[low]
     mov [di],ch        ;把array[low]中保存的值换成array[high]
     mov [bx],ah        ;把array[high]中保存的值换成array[low]
moveLow:   
     cmp di,bx
     jnb exchangeTwo    ;如果low>=high 交换array[low]和array[high]
     cmp [di],cl
     ja exchangeTwo     ;如果array[low]>标准元素则换
     inc di             ;di++
     jmp moveLow                
exchangeTwo: 
     mov ch,[bx]
     mov ah,[di]
     mov [di],ch
     mov [bx],ah
     jmp ag
next2:
     mov ax,di      ;mid
     ret
divide endp

show proc near
ag:
    xor al,al
    add al,[si]
    add al,'0'
    mov dl,al
    inc si
    mov ah,02
    int 21h
    mov dl,''
    mov ah,02
    int 21h
    loop ag
    ret
show endp
codes ends
end start