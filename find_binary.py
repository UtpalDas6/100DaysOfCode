def binary(num):
  val = ''
  while num>0:
    val += str(num%2)
    num = num//2
  return val
num = input("Enter any number: ")
print("Binary Equivalent: ",binary(int(num))[::-1])
