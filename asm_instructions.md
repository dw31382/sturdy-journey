 mov [destination], [source] copy value between locations
 cmp [value1], [value2] compare two values
 je [label] jump if equal
 jne [label] jump if not equal
 jmp [label] unconditional jump
 call [label] call a subroutine
 ret return from a subroutine
 push [value] push a value onto the stack
 pop [value] pop a value off of the stack
 int [interrupt number] call an interrupt handler
 add [value1], [value2] add two values
 sub [value1], [value2] subtract two values
 mul [value1], [value2] multiply two values
 div [value1], [value2] divide two values
 inc [value] increment a value
 dec [value] decrement a value
 and [value1], [value2] logical and two values
 or [value1], [value2] logical or two values
 xor [value1], [value2] logical exclusive or two values
 not [value] logical not of a value
 shl [value], [count] shift left
 shr [value], [count] shift right
 rol [value], [count] rotate left
 ror [value], [count] rotate right
 sal [value], [count] arithmetic shift left
 sar [value], [count] arithmetic shift right
 neg [value] negate a value
 cwd convert word to doubleword
 cdq convert doubleword to quadword
 idiv [value] signed divide
 imul [value] signed multiply
 iret return from interrupt
 in [port], [value] input from port
 out [port], [value] output to port
 jc [label] jump if carry
 jnc [label] jump if not carry
 jz [label] jump if zero
 jnz [label] jump if not zero
 jo [label] jump if overflow
 jno [label] jump if not overflow
 js [label] jump if sign
 jns [label] jump if not sign
 loop [label] decrement ecx and jump if not zero
 jecxz [label] jump if ecx is zero
 movsx [destination], [source] move and sign extend
 movzx [destination], [source] move and zero
 test [value1], [value2] test bits
 xchg [value1], [value2] exchange values
 leave pop ebp and use as esp
 enter [size], [nesting level] push ebp, allocate stack space, and adjust ebp