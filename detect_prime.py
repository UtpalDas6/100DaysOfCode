#prim_func(1,2,3,4,5,6) => 2,3,5
def prim_func(lis):
  op = []
  for el in lis:
    factor_count = 0
    for i in range(1,el+1):
      if el%i == 0:
        factor_count+=1
    if factor_count == 2:
      op.append(el)
  return op
print(prim_func([2,3,4,5,6]))
