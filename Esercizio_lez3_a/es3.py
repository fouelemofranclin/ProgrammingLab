def scambia_elementi(A,i,j):

    if i < len(A) and j < len(A):
        A[i],A[j] = A[j] ,A[i]
    return A

print(scambia_elementi([10,20,30],0,2))