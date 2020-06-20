data segment
;----------------------------------------------------------------------------------------------------------------------------
    arr dw 1458, 77, 1962, 2594, 3213, 1977, 3973, 3582, 2562, 3533, 3979, 2991, 1412, 2105, 2823, 2227, 3966, 247, 2433, 2681, 2659, 2549, 1125, 2460, 2847, 1067, 2506, 1998, 4054, 3546, 265, 3739, 2968, 2698, 3947, 221, 2877, 1619, 1454, 2380, 1226, 789, 2617, 3875, 813, 1621, 2888, 1769, 304, 2615
;----------------------------------------------------------------------------------------------------------------------------
    i       dw  ? 
    j       dw  ?
    low     dw  0                           
    high    dw 49                         
    q       dw  ?
    x       dw  ?
    tmp     dw  ?


ends

stack segment

    stk db  100  dup(0)
    top equ 100

ends

code segment

    assume cs: code, ds: data, ss:stack

    start:

        mov  ax, @data
        mov  ds, ax
        mov  ax, stack
        mov  ss, ax
        mov  sp, top


        call quicksort
    ;for debug
        lea si,arr
    loooop:    
        mov ax,[si]
        add si,2
        jmp loooop

        mov  ah, 7
        int  21h
        mov  ax, 4c00h
        int  21h

        quicksort proc
            ; if(low>high) quit();else divide();
            mov  ax, low 
            cmp  ax, high                  
            jge  quit                

            call divide

            mov  q, ax

            inc  ax
            push ax
            push high 

            mov  ax, q 
            mov  high, ax
            dec  high
            call quicksort

            pop  high
            pop  low 
            call quicksort 

            quit:
                ret

        quicksort endp

        ;-----------------------------------------
        ;divide(arr, low, high)
        ;    x = arr[high]
        ;    i = low - 1
        ;    for j = low to high-1
        ;        if arr[j] ≤ x
        ;            i = i + 1
        ;            exchange arr[i] with arr[j]
        ;    exchange arr[i+1] with arr[r]
        ;    return i+1

        divide proc
            ;x=arr[high]
            mov  si, offset arr
            mov  ax, high
            shl  ax, 1              ;critical! as ax is dw type       
            add  si, ax
            mov  ax, [ si ]       
            mov  x,  ax              


            mov  ax, low
            mov  i,  ax
            dec  i
            ;j=low
            mov  ax, low
            mov  j,  ax
            ;for_loop 
            j_loop:
                ;get arr[j]
                mov  si, offset arr
                mov  ax, j
                shl  ax, 1              
                add  si, ax
                mov  ax, [ si ]       

                cmp  ax, x
                jg   bigger           

                inc  i
                
                mov  di, offset arr
                mov  cx, i
                shl  cx, 1             
                add  di, cx
                mov  cx, [ di ]        

                mov  [ di ], ax
                mov  [ si ], cx
            
                bigger:
                    inc  j           
                    mov  ax, high
                    cmp  j,  ax       
                    jl   j_loop         

            inc  i
            mov  si, offset arr
            mov  ax, i
            shl  ax, 1                
            add  si, ax
            mov  ax, [ si ]            

            mov  di, offset arr
            mov  cx, high
            shl  cx, 1                 
            add  di, cx
            mov  cx, [ di ]            

            mov  [ di ], ax
            mov  [ si ], cx  

            mov  ax, i
            ret
        divide endp  
ends
    end start
