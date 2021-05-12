"""
Course: CS 2302 
Date of last modification: June 19, 2020
Purpose: Implement different operations through loops and slicing independently 
    in order to analyze and gain a better understanding of the relative 
    efficiency of both methods to deal with arrays.  
"""
import numpy as np
import matplotlib.pyplot as plt
import time

def display_image(im,dpi = 160,figname='',save=True):
    height, width= im.shape[0], im.shape[1]
    figsize = width / float(dpi), height / float(dpi)
    fig, ax = plt.subplots(figsize=figsize)
    ax.imshow(im, cmap='gray')
    if figname!='':
        fig.suptitle(figname, fontsize=16)
        if save: fig.savefig(figname+'.jpg')

# The following 9 functions are manipulating arrays through loops.

# Function returns a copy of the original image upside down.
# A new array is created with the same dimensions as the original image.
# The original image is copied to the new array through nested loops.
# The new array is traversed halfways through the rows where each row is swapped with its respective row at the end.
def upside_down_loops(im):
    im_upside_down = np.zeros((im.shape[0],im.shape[1],im.shape[2]))
    for r in range(im.shape[0]):
        for c in range(im.shape[1]):
            for color in range(3):
                im_upside_down[r,c,color] =  im[r,c,color]
                
    for r in range((im_upside_down.shape[0]//2)-1):
        # Swap each row with the row that has equivalent distance to the end as the current row does to the beginning.
        temp = im[r]
        im_upside_down[r] = im_upside_down[-(r+1)]
        im_upside_down[-(r+1)] = temp
    return im_upside_down

# Function returns a copy of the original image mirrored.
# A new array is created with the same dimensions as the original image.
# The original image is copied to the new array through nested loops.
# The new array is traversed halfways through the columns where each column is swapped with its respective column at the end.
def mirrored_loops(im):
    im_mirrored = np.zeros((im.shape[0],im.shape[1],im.shape[2]))
    for r in range(im.shape[0]):
        for c in range(im.shape[1]):
            for color in range(3):
                im_mirrored[r,c,color] =  im[r,c,color]
                
    for r in range(im_mirrored.shape[0]):
        for c in range(im_mirrored.shape[1]//2 -1):
            # Swap each column with the column that has equivalent distance to the end as the current column does to the beginning.
            temp = im[r,c]
            im_mirrored[r,c] = im_mirrored[r][-(c+1)]
            im_mirrored[r][-(c+1)] = temp
    return im_mirrored
 
# Function returns a copy of the original image with the blue and red channels swapped.
# A new array is created with the same dimensions as the original image.
# The original image is copied to the new array through nested loops, then some modifications are made to the color.
# If the color is red for a cell, then the color blue is saved in that cell.
# If the color is blue for a cell, then the color red is saved in that cell.
def channels_swapped_loops(im):  
    im_channels_swapped = np.zeros((im.shape[0],im.shape[1],im.shape[2]))
    for r in range(im.shape[0]):
        for c in range(im.shape[1]):
            for color in range(3):
                im_channels_swapped[r,c,color] = im[r,c,color]
                if color == 0:
                    im_channels_swapped[r,c,color] = im[r,c,2] 
                elif color == 2:
                    im_channels_swapped[r,c,color] = im[r,c,0]
    return im_channels_swapped

# Function returns a copy of the original image at half resolution.
# A new array is created with the dimensions as the original image halved.
# The even indices of the original image are copied to the new array through nested loops.
# Separate iterators are used in order to iterate through the two arrays simultaneously. 
def half_resolution_loops(im):
    # Add 1 to the size in order to accomodate for odd sizes. 
    im_half_resolution = np.zeros(((im.shape[0]+1)//2,(im.shape[1]+1)//2,im.shape[2]))
    row_copy = 0
    col_copy = 0
    for r in range(0,im.shape[0],2):
        for c in range(0,im.shape[1],2):
            for color in range(3):
                im_half_resolution[row_copy,col_copy,color] =  im[r,c,color]
            col_copy += 1
        # Set the column iterator to 0 in order to start at the beginning of the next row. 
        col_copy = 0
        row_copy += 1
    return im_half_resolution

# Function returns a copy of the original image in gray level.
# A new array is created with the same dimensions as the original image.
# The original image is copied to the new array through nested loops with modifications to the color.
# Every value with the same row and column is set to a weighted average of the red, green, and blue channels to create a gray image. 
def gray_level_loops(im):
    im_gray_level = np.zeros((im.shape[0],im.shape[1],im.shape[2]))
    for r in range(im.shape[0]):
        for c in range(im.shape[1]):
            for color in range(3):
                # Compute a weighted average in order to create a more realistic gray image.
                im_gray_level[r,c,color] = im[r,c,0]*0.3 + im[r,c,1]*0.59 + im[r,c,2]*0.11
    return im_gray_level 

# Function returns a copy of the gray level image as a negative.
# A new array is created with the same dimensions as the gray level image.
# The gray level image is copied to the new array through nested loops with modifications to the color.
# Every value in the third dimension is set to one minus the value of the gray level image.
# This creates the negative of the gray level image.
def negative_loops(im_gray_level):
    im_negative_gray_level = np.zeros((im_gray_level.shape[0],im_gray_level.shape[1],im_gray_level.shape[2]))
    for r in range(im_gray_level.shape[0]):
        for c in range(im_gray_level.shape[1]):
            for color in range(3):
                im_negative_gray_level[r,c,color] =  1 - im_gray_level[r,c,color]
    return im_negative_gray_level        

# Function returns a copy of the gray level image as a binary version.
# A new array is created with the same dimensions as the gray level image.
# The gray level image is copied to the new array through nested loops with modifications to the color.
# If a cell has a value greater than 0.5, then it is set to 1. Otherwise it is set to 0.         
def binary_loops(im_gray_level):
    im_binary_gray_level = np.zeros((im_gray_level.shape[0],im_gray_level.shape[1],im_gray_level.shape[2]))
    for r in range(im_gray_level.shape[0]):
        for c in range(im_gray_level.shape[1]):
            for color in range(3):
                if im_gray_level[r,c,color] > 0.5:
                    im_binary_gray_level[r,c,color] =  1
                else:
                    im_binary_gray_level[r,c,color] =  0
    return im_binary_gray_level

# Function returns a copy of the gray level image with only the vertical edges.
# A new array is created with the same dimensions as the gray level image with the exception of the column size being 1 index smaller.
# The gray level image is copied to the new array through nested loops with modifications to the value of each index with a row and column.
# Each cell is set to the absolute value of the subtraction of the current index to the next index one column above.        
def vertical_edges_loops(im_gray_level):
    # Set the column size 1 value less because there is no column to subtract the last column of the gray image with.
    im_vertical_edges = np.zeros((im_gray_level.shape[0],im_gray_level.shape[1]-1,im_gray_level.shape[2]))
    for r in range(im_vertical_edges.shape[0]):
        for c in range(im_vertical_edges.shape[1]):
            for color in range(3):
                im_vertical_edges[r,c,color] = abs(im_gray_level[r,c,color] - im_gray_level[r,c+1,color])
    return im_vertical_edges

# Function returns a copy of the gray level image with only the horizontal edges.
# A new array is created with the same dimensions as the gray level image with the exception of the row size being 1 index smaller.
# The gray level image is copied to the new array through nested loops with modifications to the value of each index with a row and column.
# Each cell is set to the absolute value of the subtraction of the current index to the index one row above.        
def horizontal_edges_loops(im_gray_level):
    # Set the row size 1 value less because there is no row to subtract the last row of the gray image with.
    im_horizontal_edges = np.zeros((im_gray_level.shape[0]-1,im_gray_level.shape[1],im_gray_level.shape[2]))
    for r in range(im_horizontal_edges.shape[0]):
        for c in range(im_horizontal_edges.shape[1]):
            for color in range(3):
                im_horizontal_edges[r,c,color] = abs(im_gray_level[r,c,color] - im_gray_level[r+1,c,color])
    return im_horizontal_edges 

# The following 9 functions are manipulating arrays through slicing.

# Function returns a copy of the original image upside down.
# A new array is created with the same dimensions as the original image.
# The original image is copied to the new array through slicing.
# The step index in the first dimension is set to -1 in order to copy the image from bottom to top.
def upside_down_slicing(im): 
    im_upside_down = np.zeros((im.shape[0],im.shape[1],im.shape[2]))
    # The -1 saves the last row as the first row until the whole image is copied.
    im_upside_down[:,:,:]= im[::-1,:,:] 
    return im_upside_down

# Function returns a copy of the original image mirrored.
# A new array is created with the same dimensions as the original image.
# The original image is copied to the new array through slicing.
# The step index in the second dimension is set to -1 in order to copy the image from right to left.
def mirrored_slicing(im):
    im_mirrored = np.zeros((im.shape[0],im.shape[1],im.shape[2]))
    # The -1 saves the last column as the first column until the whole image is copied.
    im_mirrored[:,:,:]= im[:,::-1,:] 
    return im_mirrored

# Function returns a copy of the original image with the blue and red channels swapped.
# A new array is created with the same dimensions as the original image.
# The original image is copied to the new array through slicing.
# The index 0 in the first dimension of the copied array is set to the value of the original array at index 2.
# The index 2 in the first dimension of the copied array is set to the value of the original array at index 0.
# This swaps the channels of the copied array. 
def channels_swapped_slicing(im):
    im_channels_swapped = np.zeros((im.shape[0],im.shape[1],im.shape[2]))
    im_channels_swapped[:,:,:]= im[:,:,:]
    im_channels_swapped[:,:,0] = im[:,:,2]
    im_channels_swapped[:,:,2] = im[:,:,0]
    return im_channels_swapped 

# Function returns a copy of the original image with half resolution.
# A new array is created with the dimensions of the original image halved.
# The original image is copied to the new array through slicing.
# The step index of the first and second dimension of the original array are set to 2 in order to only copy the even indexes.
def half_resolution_slicing(im):  
    # Add 1 to the size in order to accomodate for odd sizes.
    im_half_resolution = np.zeros(((im.shape[0]+1)//2,(im.shape[1]+1)//2,im.shape[2]))
    im_half_resolution[:,:,:]= im[::2,::2,:]
    return im_half_resolution

# Function returns a copy of the original image in gray level.
# A new array is created with the same dimensions as the original image.
# The original image is copied to the new array through slicing with a modification to the color of each cell.
# Every value with the same row and column is set to a weighted average of the red, green, and blue channels to create a gray image. 
def gray_level_slicing(im):
    im_gray_level = np.zeros((im.shape[0],im.shape[1],im.shape[2]))
    im_gray_level[:,:] = im[:,:,0:1:] * .3 + im[:,:,1:2:] * .59 + im[:,:,2::] * .11
    return im_gray_level

# Function returns a copy of the gray level image in negative.
# A new array is created with the same dimensions as the original image.
# The original image is copied to the new array through slicing with a modification to the color of each cell.
# Every cell in the new array is set to 1 minus the value in the gray level image. 
def negative_slicing(im_gray_level):
    im_negative_gray_level = np.zeros((im_gray_level.shape[0],im_gray_level.shape[1],im_gray_level.shape[2]))
    im_negative_gray_level[:,:] = 1 - im_gray_level[:,:]
    return im_negative_gray_level 

# Function returns a copy of the gray level image in binary.
# A new array is created with the same dimensions as the original image.
# The original image is copied to the new array through slicing with a modification to the color of each cell.
# Each cell in the array is set to 1 if its value was greater than 0.5 and 0 otherwise.
def binary_slicing(im_gray_level):  
    im_binary_gray_level = np.zeros((im_gray_level.shape[0],im_gray_level.shape[1],im_gray_level.shape[2]))
    # A boolean is used in order to set all the designated values to 0 and 1.
    im_binary_gray_level[im_gray_level>0.5] = 1
    im_binary_gray_level[im_gray_level<=0.5] = 0
    return im_binary_gray_level

# Function returns a copy of the gray level image with only the vertical edges.
# A new array is created with the same dimensions as the original image with the exception of the column size being 1 index smaller.
# The original image is copied to the new array through slicing with a modification to the color of each cell.
# Each cell in the array is set to the absolute value of the difference between the current column and the next column.
def vertical_edges_slicing(im_gray_level):     
    im_vertical_edges = np.zeros((im_gray_level.shape[0],im_gray_level.shape[1]-1,im_gray_level.shape[2]))
    # Place a -1 in the end of the first value's second dimension because there is no following column to subtract from.
    # Place a 1 in the starting point of the second value's second dimension because it is the first index following the current index.
    im_vertical_edges[:,:] = abs(im_gray_level[:,:-1] - im_gray_level[:,1:])
    return im_vertical_edges

# Function returns a copy of the gray level image with only the horizontal edges.
# A new array is created with the same dimensions as the original image with the exception of the row size being 1 index smaller.
# The original image is copied to the new array through slicing with a modification to the color of each cell.
# Each cell in the array is set to the absolute value of the difference between the current row and the next row.
def horizontal_edges_slicing(im_gray_level):
    im_horizontal_edges = np.zeros((im_gray_level.shape[0]-1,im_gray_level.shape[1],im_gray_level.shape[2]))
    # Place a -1 in the end of the first value's first dimension because there is no following row to subtract from.
    # Place a 1 in the starting point of the second value's first dimension because it is the first index following the current index.
    im_horizontal_edges[:,:] = abs(im_gray_level[:-1,:] - im_gray_level[1:,:])
    return im_horizontal_edges
    
    
if __name__ == "__main__":
    
    plt.close('all')
    img = plt.imread('UTEP.JPG').astype(float)/255
    display_image(img,figname='original')

    # Create an upside down copy of the image through looping and display the time it took.
    start = time.time()
    img2 = upside_down_loops(img)
    end = time.time()
    time_loop = end - start
    print('Time to build upside down image copy using loops: {:5.3f} seconds'.format(time_loop))
    display_image(img2,figname='Upside Down Copy 1')
    
    # Create an upside down copy of the image through slicing and display the time it took. 
    # Display the difference between the time it took for slicing versus looping.
    start = time.time()
    img3 = upside_down_slicing(img)
    end = time.time()
    time_slice = end - start
    print('Time to build upside down image copy using slicing: {:5.3f} seconds'.format(time_slice))
    display_image(img3,figname='Upside Down Copy 2')
    print('Loop took {:5.3f} times as long as slicing'.format(time_loop/time_slice))
    print('Slicing saved {:5.2f}% of the time compared to loops'.format(100*(time_loop-time_slice)/time_loop))
    print()
    
    # Create a mirrored copy of the image through looping and display the time it took.
    start = time.time()
    img2 = mirrored_loops(img)
    end = time.time()
    time_loop = end - start
    print('Time to build mirrored image copy using loops: {:5.3f} seconds'.format(time_loop))
    display_image(img2,figname='Mirrored Copy 1')
    
    # Create an mirrored copy of the image through slicing and display the time it took.
    # Display the difference between the time it took for slicing versus looping.
    start = time.time()
    img3 = mirrored_slicing(img)
    end = time.time()
    time_slice = end - start
    print('Time to build mirrored image copy using slicing: {:5.3f} seconds'.format(time_slice))
    display_image(img3,figname='Mirrored Copy 2')
    print('Loop took {:5.3f} times as long as slicing'.format(time_loop/time_slice))
    print('Slicing saved {:5.2f}% of the time compared to loops'.format(100*(time_loop-time_slice)/time_loop))
    print()
    
    # Create a copy of the image with its blue and red channels swapped through looping and display the time it took.
    start = time.time()
    img2 = channels_swapped_loops(img)
    end = time.time()
    time_loop = end - start
    print('Time to build red and blue channels swapped image copy using loops: {:5.3f} seconds'.format(time_loop))
    display_image(img2,figname='Red & Blue Channels Swapped Copy 1')
    
    # Create a copy of the image with its blue and red channels swapped through slicing and display the time it took.
    # Display the difference between the time it took for slicing versus looping.
    start = time.time()
    img3 = channels_swapped_slicing(img)
    end = time.time()
    time_slice = end - start
    print('Time to build red and blue channels swapped image copy using slicing: {:5.3f} seconds'.format(time_slice))
    display_image(img3,figname='Red & Blue Channels Swapped Copy 2')
    print('Loop took {:5.3f} times as long as slicing'.format(time_loop/time_slice))
    print('Slicing saved {:5.2f}% of the time compared to loops'.format(100*(time_loop-time_slice)/time_loop))
    print()
    
    # Create a half resolution copy of the image through looping and display the time it took.
    start = time.time()
    img2 = half_resolution_loops(img)
    end = time.time()
    time_loop = end - start
    print('Time to build half resolution image copy using loops: {:5.3f} seconds'.format(time_loop))
    display_image(img2,figname='Half Resolution Copy 1')
    
    # Create a half resolution copy of the image through slicing and display the time it took.
    # Display the difference between the time it took for slicing versus looping.
    start = time.time()
    img3 = half_resolution_slicing(img)
    end = time.time()
    time_slice = end - start
    print('Time to build half resolution image copy using slicing: {:5.3f} seconds'.format(time_slice))
    display_image(img3,figname='Half Resolution Copy 2')
    print('Loop took {:5.3f} times as long as slicing'.format(time_loop/time_slice))
    print('Slicing saved {:5.2f}% of the time compared to loops'.format(100*(time_loop-time_slice)/time_loop))
    print()
 
    # Create a gray level copy of the image through looping and display the time it took.
    start = time.time()
    gray_level = gray_level_loops(img)
    end = time.time()
    time_loop = end - start
    print('Time to build gray level image copy using loops: {:5.3f} seconds'.format(time_loop))
    display_image(gray_level,figname='Gray Level Copy 1')
    
    # Create a gray level copy of the image through looping and display the time it took.
    # Display the difference between the time it took for slicing versus looping.
    start = time.time()
    img3 = gray_level_slicing(img)
    end = time.time()
    time_slice = end - start
    print('Time to build gray level image copy using slicing: {:5.3f} seconds'.format(time_slice))
    display_image(img3,figname='Gray Level Copy 2')
    print('Loop took {:5.3f} times as long as slicing'.format(time_loop/time_slice))
    print('Slicing saved {:5.2f}% of the time compared to loops'.format(100*(time_loop-time_slice)/time_loop))
    print()
  
    # Create a negative copy of the gray level image through looping and display the time it took.
    start = time.time()
    img2 = negative_loops(gray_level)
    end = time.time()
    time_loop = end - start
    print('Time to build negative of gray level image copy using loops: {:5.3f} seconds'.format(time_loop))
    display_image(img2,figname='Negative of Gray Level Copy 1')
    
    # Create a negative copy of the gray level image through slicing and display the time it took.
    # Display the difference between the time it took for slicing versus looping.
    start = time.time()
    img3 = negative_slicing(gray_level)
    end = time.time()
    time_slice = end - start
    print('Time to build negative of gray level image copy using slicing: {:5.3f} seconds'.format(time_slice))
    display_image(img3,figname='Negative of Gray Level Copy 2')
    print('Loop took {:5.3f} times as long as slicing'.format(time_loop/time_slice))
    print('Slicing saved {:5.2f}% of the time compared to loops'.format(100*(time_loop-time_slice)/time_loop))
    print()
    
    # Create a binary copy of the gray level image through looping and display the time it took.
    start = time.time()
    img2 = binary_loops(gray_level)
    end = time.time()
    time_loop = end - start
    print('Time to build binary of gray level image copy using loops: {:5.3f} seconds'.format(time_loop))
    display_image(img2,figname='Binary of Gray Level Copy 1')
    
    # Create a binary copy of the gray level image through slicing and display the time it took.
    # Display the difference between the time it took for slicing versus looping.
    start = time.time()
    img3 = binary_slicing(gray_level)
    end = time.time()
    time_slice = end - start
    print('Time to build binary of gray level image copy using slicing: {:5.3f} seconds'.format(time_slice))
    display_image(img3,figname='Binary of Gray Level Copy 2')
    print('Loop took {:5.3f} times as long as slicing'.format(time_loop/time_slice))
    print('Slicing saved {:5.2f}% of the time compared to loops'.format(100*(time_loop-time_slice)/time_loop))
    print()
    
    # Create a copy of the vertical edges of the gray level image through looping and display the time it took.
    start = time.time()
    img2 = vertical_edges_loops(gray_level)
    end = time.time()
    time_loop = end - start
    print('Time to build vertical edges in gray level image copy using loops: {:5.3f} seconds'.format(time_loop))
    display_image(img2,figname='Vertical Edges in Gray Level Copy 1')
    
    # Create a copy of the vertical edges of the gray level image through slicing and display the time it took.
    # Display the difference between the time it took for slicing versus looping.
    start = time.time()
    img3 = vertical_edges_slicing(gray_level)
    end = time.time()
    time_slice = end - start
    print('Time to build vertical edges in gray level image copy using slicing: {:5.3f} seconds'.format(time_slice))
    display_image(img3,figname='Vertical Edges in Gray Level Copy 2')
    print('Loop took {:5.3f} times as long as slicing'.format(time_loop/time_slice))
    print('Slicing saved {:5.2f}% of the time compared to loops'.format(100*(time_loop-time_slice)/time_loop))
    print()
    
    # Create a copy of the horizontal edges of the gray level image through looping and display the time it took.
    start = time.time()
    img2 = horizontal_edges_loops(gray_level)
    end = time.time()
    time_loop = end - start
    print('Time to build horizontal edges in gray level image copy using loops: {:5.3f} seconds'.format(time_loop))
    display_image(img2,figname='Horizontal Edges in Gray Level Copy 1')
    
    # Create a copy of the horizontal edges of the gray level image through slicing and display the time it took.
    # Display the difference between the time it took for slicing versus looping.
    start = time.time()
    img3 = horizontal_edges_slicing(gray_level)
    end = time.time()
    time_slice = end - start
    print('Time to build horizontal edges in gray level image copy using slicing: {:5.3f} seconds'.format(time_slice))
    display_image(img3,figname='Horizontal Edges in Gray Level Copy 2')
    print('Loop took {:5.3f} times as long as slicing'.format(time_loop/time_slice))
    print('Slicing saved {:5.2f}% of the time compared to loops'.format(100*(time_loop-time_slice)/time_loop))
    print()
