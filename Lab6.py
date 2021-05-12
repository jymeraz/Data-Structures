"""
Course: CS 2302 
Date of last modification: August 2, 2020
Purpose: Implement dynamic programming to determine the similarity of protein sequences. 
    In addition, edit the given dynamic programming function by choosing the neighbor 
    that maximizes the similarity value influenced by the given blosum matrix.         
"""

import numpy as np
import math

# Function reads the file with the 500 proteins and the blosum file. 
# The proteins are saved to a list, and the blosum matrix is saved in a 2D list.
# The letters corresponding to the blosum matrix are saved in a list. 
# The list of proteins, blosum matrix, and list of amino acids are returned.  
def read_files(protein_file,blosum_file):           
    file = open(protein_file,'r')
    line = file.readline().rstrip('\n')
    proteins = []
    while line:
        proteins += [line]
        line = file.readline().rstrip('\n')
    file.close()
    
    file = open(blosum_file,'r')
    line = file.readline().rstrip('\n').split(',')
    blosum = []
    while line != ['']:
        ints = []
        # The strings in the blosum file are each saved as an integer.
        for i in line:
            ints += [int(i)]
        blosum += [ints]
        line = file.readline().rstrip('\n').split(',')
    file.close()
    
    amino_acids = ['C','S','T','P','A','G','N','D','E','Q','H','R','K','M','I','L','V','F','Y','W']
    return proteins,blosum,amino_acids

# Function creates a similarify matrix and returns the similarity value between two strings.
# An array is created and the last row and column are first initialzed to values decreasing by 3
# The array is traversed from the second to last row and the second to last column to the first row and first column.
# If the letters of the strings match or the maximum neighbor is diagonal to it, then the value from the blosum matrix is used.
# Otherwise, the value of -3 is added to the maximum neighbor. 
def similarity_value(s1,s2,blosum,acids,return_array=False):
    d = np.zeros((len(s1)+1,len(s2)+1),dtype=int)
    d[-1,:] = np.arange(-(len(s2)*3),3,3) 
    d[:,-1] = np.arange(-(len(s1)*3),3,3) 
    for i in range(len(s1)-1,-1,-1):
        for j in range(len(s2)-1,-1,-1):
            # Save the value of the maximum to avoid recomputation. 
            m = max(d[i,j+1],d[i+1,j+1],d[i+1,j])
            if s1[i] == s2[j] or m == d[i+1,j+1]:
                d[i,j] =  d[i+1,j+1] + blosum[acids.index(s1[i])][acids.index(s2[j])]
            else:
                d[i,j] = -3 + m
    if not return_array:
        d = d[0,0]
    return d

# Function creates a function with each protein, its most similar protein, and their similarity score.
# For each protein, its similarity score is computed for every other protein.
# The protein with the largest similarity score is saved and written to a file.
# Print message is displayed to notify the user of the file created.
def most_similar_protein(proteins,blosum,acids):
    f = open('Meraz_Janeth_Similarity_Scores.txt','w+')
    for i in range(len(proteins)):
        similar_protein = proteins[i]
        max_similarity_value = -math.inf
        for k in range(len(proteins)):
            # Check that the protein is different than the original protein.
            if i != k:
                sim_value = similarity_value(proteins[i],proteins[k],blosum,acids)
                if sim_value > max_similarity_value:
                    similar_protein = proteins[k]
                    max_similarity_value = sim_value
        f.write('{}.\tOriginal protein: {}\n'.format(i+1,proteins[i]))
        f.write('  \tBest Match: {}\n'.format(similar_protein))
        f.write('  \tSimilarity Score: {}\n\n'.format(max_similarity_value))
    f.close()
    print('File created named "Meraz_Janeth_Similarity_Scores.txt".')


# Experiments
proteins_list,blosum_matrix,amino_acids = read_files('proteinSequences_500.txt', 'blosum.txt')

# Check if the contents of the files were read correctly.
print('-- 1. Reading the files:')
file = open('proteinSequences_500.txt','r')
line = file.readline().rstrip('\n')
for protein in proteins_list:
    if protein != line:
        print('File proteinSequences_500.txt not properly read.')
    line = file.readline().rstrip('\n')
file.close()
print('a) Experiment checking if file proteinSequences_500.txt was properly read is complete.')

file = open('blosum.txt','r')
line = file.readline().rstrip('\n').split(',')
for i in blosum_matrix:
    for j in range(len(i)):
        if i[j] != int(line[j]):
            print('File proteinSequences_500.txt not properly read.')
    line = file.readline().rstrip('\n').split(',')
file.close()
print('b) Experiment checking if file blosum.txt was properly read is complete.\n')   

# Compare results of the similarity matrix to results computed by hand.
print('-- 2. a) Creating the similarity matrix:')
# Text with two completely different strings.
print('\tTest 1: ')
print('\ts1 = RKMWY')
print('\ts2 = STPIVV')
print('\tExpected similarity matrix: ')
# The matrix computed by hand.
expected = np.array([[-8,-5,-7,-9,-12,-13,-15],[-10,-7,-4,-6,-9,-10,-12],[-12,-9,-6,-3,-6,-7,-9],[-16,-13,-11,-7,-4,-4,-6],[-16,-13,-10,-7,-4,-1,-3],[-18,-15,-12,-9,-6,-3,0]])
print(expected)
s1 = 'RKMWY'
s2 = 'STPIVV'
actual = similarity_value(s1, s2, blosum_matrix, amino_acids,return_array=True)
print('\tActual similarity matrix: ')
print(actual)
# Create list with rows that contain an element that is not equal between the expected and the actual.
not_equal = [i for i in (expected==actual) if (i == False).any()]
print('\tEquality between expected array and actual array: ',len(not_equal)==0)
print()

# Test with 50% similar strings.
print('\tTest 2: ')
print('\ts1 = SKNQ')
print('\ts2 = NKNF')
print('\tExpected similarity matrix: ')
# The matrix computed by hand.
expected = np.array([[9,5,0,-9,-12],[5,8,0,-6,-9],[-3,0,3,-3,-6],[-11,-9,-6,-3,-3],[-12,-9,-6,-3,0]])
print(expected)
s1 = 'NKNF'
s2 = 'SKNQ'
actual = similarity_value(s1, s2, blosum_matrix, amino_acids,return_array=True)
print('\tActual similarity matrix: ')
print(actual)
# Create list with rows that contain an element that is not equal between the expected and the actual.
not_equal = [i for i in (expected==actual) if (i == False).any()]
print('\tEquality between expected array and actual array: ',len(not_equal)==0)
print()

# Test with equal strings where one string has additional characters.
print('\tTest 3: ')
print('\ts1 = KLEQASVN')
print('\ts2 = QASVN')
print('\tExpected similarity matrix: ')
# The matrix computed by hand.
expected = np.array([[14,6,-1,-8,-15,-24],[17,9,2,-5,-12,-21],[20,12,5,-2,-9,-18],[23,15,8,1,-6,-15],[15,18,11,4,-3,-12],[8,11,14,7,0,-9],[1,4,7,10,3,-6],[-6,-3,0,3,6,-3],[-15,-12,-9,-6,-3,0]])
print(expected)
s1 = 'KLEQASVN'
s2 = 'QASVN'
actual = similarity_value(s1, s2, blosum_matrix, amino_acids,return_array=True)
print('\tActual similarity matrix: ')
print(actual)
# Create list with rows that contain an element that is not equal between the expected and the actual.
not_equal = [i for i in (expected==actual) if (i == False).any()]
print('\tEquality between expected array and actual array: ',len(not_equal)==0)
print()

# Test with equal strings. 
print('\tTest 4: ')
print('\ts1 = LQSLT')
print('\ts2 = LQSLT')
print('\tExpected similarity matrix: ')
# The matrix computed by hand.
expected = np.array([[21,14,6,-1,-8,-15],[14,17,9,2,-5,-12],[6,9,12,5,-2,-9],[-1,2,5,8,1,-6],[-8,-5,-2,1,4,-3],[-15,-12,-9,-6,-3,0]])
print(expected)
s1 = 'LQSLT'
s2 = 'LQSLT'
actual = similarity_value(s1, s2, blosum_matrix, amino_acids,return_array=True)
print('\tActual similarity matrix: ')
print(actual)
# Create list with rows that contain an element that is not equal between the expected and the actual.
not_equal = [i for i in (expected==actual) if (i == False).any()]
print('\tEquality between expected array and actual array: ',len(not_equal)==0)
print()

# Create the file with each protein's most similar protein
print('-- 2. b) Creating a file with each protein, it\'s most similar protein, and their similarity score: ')
most_similar_protein(proteins_list,blosum_matrix,amino_acids)


    







