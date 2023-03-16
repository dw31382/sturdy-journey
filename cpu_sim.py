#!/usr/bin/env python3

import sys
import time

# .text / code segment
text = sys.argv[1]
f = open(text, 'r')
text = f.readlines()
f.close()
text = [line.strip() for line in text]

# registers
r = {"rax": 0, "rbx": 0, "rcx": 0, "rdx": 0,
     "rsi": 0, "rdi": 0, "rbp": 0, "rsp": 0,
     "r8" : 0, "r9" : 0, "r10": 0, "r11": 0,
     "r12": 0, "r13": 0, "r14": 0, "r15": 0,
     "rip": 0, "rflags": 0,
     "cs": 0, "ss": 0, "ds": 0,
     "es": 0, "fs": 0, "gs": 0
}

# flags
f = {"zf": 0, "sf": 0, "of": 0}
# zero, sign, overflow

# memory
m = [0] * 100

def cpu(text):

    while r["rip"] < len(text):

        x = text[r["rip"]]

        x = x.split()

        # move, load / store, copy
        if x[0] == "mov":
            if x[2].isdigit():
                r[x[1]] = int(x[2])
            # elif memory address
            elif "[" in x[2]:
                r[x[1]] = m[int(x[2][1:-1])]
            elif "[" in x[1]:
                m[int(x[1][1:-1])] = r[x[2]]
            else:
                r[x[1]] = r[x[2]]
            r["rip"] += 1
        
        # addition
        elif x[0] == "add":
            if x[2].isdigit():
                r[x[1]] += int(x[2])
            else:
                r[x[1]] += r[x[2]]
            if r[x[1]] == 0:
                f["zf"] = 1
            r["rip"] += 1

        # subtraction
        elif x[0] == "sub":
            if x[2].isdigit():
                r[x[1]] -= int(x[2])
            else:
                r[x[1]] -= r[x[2]]
            if r[x[1]] == 0:
                f["zf"] = 1
            r["rip"] += 1

        # multiplication
        elif x[0] == "mul":
            if x[2].isdigit():
                r[x[1]] *= int(x[2])
            else:
                r[x[1]] *= r[x[2]]
            if r[x[1]] == 0:
                f["zf"] = 1
            r["rip"] += 1

        # division
        elif x[0] == "div":
            if x[2].isdigit():
                r[x[1]] /= int(x[2])
            else:
                r[x[1]] /= r[x[2]]
            if r[x[1]] == 0:
                f["zf"] = 1
            r["rip"] += 1

        # comparison
        elif x[0] == "cmp":
            if x[2].isdigit():
                if r[x[1]] == int(x[2]):
                    f["zf"] = 1
                else:
                    f["zf"] = 0
            else:
                if r[x[1]] == r[x[2]]:
                    f["zf"] = 1
                else:
                    f["zf"] = 0
            r["rip"] += 1

        # push to stack
        elif x[0] == "push":
            if x[1].isdigit():
                m[r["rsp"]] = int(x[1])
            else:
                m[r["rsp"]] = r[x[1]]
            # update stack pointer
            r["rsp"] -= 1
            r["rip"] += 1

        # pop from stack
        elif x[0] == "pop":
            m[r["rsp"]] = m.pop()
            # update stack pointer
            r["rsp"] += 1
            r["rip"] += 1

        # jump
        elif x[0] == "jmp":
            r["rip"] = int(x[1])

        # jump if zero
        elif x[0] == "je":
            if f["zf"] == 1:
                r["rip"] = int(x[1])
            else:
                r["rip"] += 1

        # jump if not zero
        elif x[0] == "jne":
            if f["zf"] == 0:
                r["rip"] = int(x[1])
            else:
                r["rip"] += 1

        # call function
        elif x[0] == "call":
            m.append(r["rip"] + 1)
            r["rip"] = int(x[1])
        
        # return from function
        elif x[0] == "ret":
            r["rip"] = m.pop()
        
        # increment
        elif x[0] == "inc":
            r[x[1]] += 1
            r["rip"] += 1
        
        # decrement
        elif x[0] == "dec":
            r[x[1]] -= 1
            r["rip"] += 1

        # logical and
        elif x[0] == "and":
            if x[2].isdigit():
                r[x[1]] &= int(x[2])
            else:
                r[x[1]] &= r[x[2]]
            r["rip"] += 1

        # logical or
        elif x[0] == "or":
            if x[2].isdigit():
                r[x[1]] |= int(x[2])
            else:
                r[x[1]] |= r[x[2]]
            r["rip"] += 1

        # logical xor
        elif x[0] == "xor":
            if x[2].isdigit():
                r[x[1]] ^= int(x[2])
            else:
                r[x[1]] ^= r[x[2]]
            r["rip"] += 1

        # logical not
        elif x[0] == "not":
            r[x[1]] = ~r[x[1]]
            r["rip"] += 1
        
        # bitwise shift left
        elif x[0] == "shl":
            if x[2].isdigit():
                r[x[1]] <<= int(x[2])
            else:
                r[x[1]] <<= r[x[2]]
            r["rip"] += 1
        
        # bitwise shift right
        elif x[0] == "shr":
            if x[2].isdigit():
                r[x[1]] >>= int(x[2])
            else:
                r[x[1]] >>= r[x[2]]
            r["rip"] += 1
        
        # no operation
        elif x[0] == "nop":
            r["rip"] += 1
        
        # jump if carry
        elif x[0] == "jc":
            if f["cf"] == 1:
                r["rip"] = int(x[1])
            else:
                r["rip"] += 1
        
        # jump if not carry
        elif x[0] == "jnc":
            if f["cf"] == 0:
                r["rip"] = int(x[1])
            else:
                r["rip"] += 1
        
        # jump if greater
        elif x[0] == "jg":
            if f["sf"] == f["of"]:
                r["rip"] = int(x[1])
            else:
                r["rip"] += 1
        
        # jump if greater or equal
        elif x[0] == "jge":
            if f["sf"] == f["of"] or f["zf"] == 1:
                r["rip"] = int(x[1])
            else:
                r["rip"] += 1

        # jump if less
        elif x[0] == "jl":
            if f["sf"] != f["of"]:
                r["rip"] = int(x[1])
            else:
                r["rip"] += 1
        
        # jump if less or equal
        elif x[0] == "jle":
            if f["sf"] != f["of"] or f["zf"] == 1:
                r["rip"] = int(x[1])
            else:
                r["rip"] += 1
        
        # jump if overflow
        elif x[0] == "jo":
            if f["of"] == 1:
                r["rip"] = int(x[1])
            else:
                r["rip"] += 1
        
        # jump if not overflow
        elif x[0] == "jno":
            if f["of"] == 0:
                r["rip"] = int(x[1])
            else:
                r["rip"] += 1
        
        # jump if sign
        elif x[0] == "js":
            if f["sf"] == 1:
                r["rip"] = int(x[1])
            else:
                r["rip"] += 1

        # jump if not sign
        elif x[0] == "jns":
            if f["sf"] == 0:
                r["rip"] = int(x[1])
            else:
                r["rip"] += 1
        
    return(r, f, m)

r, f, m = cpu(text)

print(r)
print(f)
print(m)
