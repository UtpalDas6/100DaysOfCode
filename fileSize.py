#Day1.4 <Get Size of a file>
import os
size = os.path.getsize('/content/sample_data/mnist_test.csv')
print('Bytes =',size)
print('MB =',(size//1000000))
