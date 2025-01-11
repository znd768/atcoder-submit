n = int(input())
s = input()
parentheses = 0
output = ""
keep = []
tmp = ""
for char in s:
    if char =="(":
        parentheses += 1
        if len(tmp) > 0:
            keep.append(tmp)
            tmp = ""
        tmp += char
    elif char == ")":
        if parentheses > 0:
            parentheses -= 1
            if keep:
                tmp = keep.pop()
            else:
                tmp = ""
        else:
            output += char
    elif parentheses == 0:
        output += char
    else:
        tmp += char
if len(tmp) > 0:
    keep.append(tmp)
output += "".join(keep)

print(output)