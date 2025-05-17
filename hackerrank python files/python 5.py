
import re
d='27-03-2025'
date_reg=re.compile("(\d{2}),(\d{2}),(\d{4})")
match=date_reg.match(d)
a=match.group(1)
b=match.group(2)
c=match.group(3)
print(a,b,c)
