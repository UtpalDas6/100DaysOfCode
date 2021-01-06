def sq(i):
  yield i**2
lis1 = [1,2,3,4,5,6,7,8,9,10]
def sum_even(lis1):
  sum =0
  for i in lis1[1::2]:
    sum+=i
  return sum
sum_even(lis1)
