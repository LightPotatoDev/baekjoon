import pickle

A = []
B = []
with open('bf_count_to_10000.pickle','rb') as fr:
    A = pickle.load(fr)

with open('dp_count_to_10000.pickle', 'rb') as fr:
    B = pickle.load(fr)

for i in range(len(A)):
    if A[i] != B[i]:
        print(i, A[i], B[i])