import collections
defd = collections.defaultdict(lambda : 'key not found')
defd['a'] = 89
defd['b'] = 91
print("Value associated with a: ",defd['a'])
print("Value associated with c: ",defd['c'])