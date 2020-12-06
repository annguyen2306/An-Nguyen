import numpy as np

np.set_printoptions(precision=2)

row = int(input('Fill in number of rows'))
col = int(input('Fill in number of cols'))

print('matrix:')

entries = list(map(int,input().split()))

matrix = np.array(entries).reshape(row,col)

col_sets = []

for i in range(col):
    col_sub=[]
    for f in range(row):
        col_sub.append(matrix[f,i])
    col_sets.append(col_sub)

ortho_set = []
for i in range(col):
    if i == 0:
        ortho_set.append(np.array(col_sets[0]))
    else:
        frac = (np.dot(col_sets[i],ortho_set[i-1]))/(np.linalg.norm(ortho_set[i-1]))
        ortho_vec = np.array(col_sets[i]).__add__((-1)*frac*np.array(ortho_set[i-1]))
        ortho_set.append(ortho_vec)

ortho_norm = []
for i in range(len(ortho_set)):
    norm = np.linalg.norm(ortho_set[i])    
    vec_norm = ortho_set[i]*(1/norm)
    ortho_norm.append(vec_norm)
ortho_norm1 = np.array(ortho_norm)

vec_q = np.transpose(ortho_norm1)

vec_r = np.array(vec_q)
for i in range(row):
    for j in range(col):
        if i>j:
            vec_r[i][j] = 0
        else:
            vec_r[i][j] = np.dot(col_sets[j],ortho_norm[i])
    
print('Vec Q is\n',vec_q, '\nVec_R is\n',vec_r )