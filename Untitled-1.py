import re

str= "string integer float"
repl="function"
str_to_be_replaced= "integer"
x=re.sub(r'\b'+ re.escape(str_to_be_replaced) + r'\b', repl, str)
print(x)
