import re
t = "hello world hello"
p = re.compile(r'h.llo')
# x = p.match(t)
# x = p.search(t)
x = p.findall(t)
print(x)
x = p.finditer(t)
print(list(x))
x = re.finditer(r'h.llo',t)
print(list(x))
t = """ Hello
    hi
    how 
    world
"""
p = re.compile(r'h',flags=re.I|re.M)
print(p.findall(t))

