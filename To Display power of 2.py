limit = 10
result = list(map(lambda x: 2 ** x, range(limit)))
print("total terms:",limit)
for i in range(limit):
   print("power",i,"is",result[i])
