
def ostring_to_raisedpos(s):
    result = ""
    inds = "14253678"
    s = s.replace('\\n', '')
    for i in range(len(s)):
        if s[i] == 'o':
            result += inds[i]
    return result

print(ostring_to_raisedpos('..\\n..\\n..'))
print(ostring_to_raisedpos('oo\\noo\\noo'))
print(ostring_to_raisedpos('o.\\noo\\n..'))
print(ostring_to_raisedpos('o.\\noo\\n..\\n.o'))
