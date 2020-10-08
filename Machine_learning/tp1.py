import os, scipy.io
import matplotlib.pyplot as plt

path = os.getcwd()
print(path)

new_path = "/home/stou/Documents/Master/Machine_learning/data1/"
os.chdir(new_path)

data5 = scipy.io.loadmat("../data2/diabetes.mat")

for key in data5.keys():
    print(key)
    
abs5 = []
ord5 = []

for n5 in data5['t']:
    ord5.append(int(data5['t'][n5]))
    
print(data5['X'])