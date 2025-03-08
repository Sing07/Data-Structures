
s = "abcdefg"

new = list(s)

print(new)

reverse = ""

print(reverse)

for _ in range(len(new)):
    reverse += new.pop()
    print(1)

print(reverse)

