



def ascending_sorting_function(array,j,gap,temporary):
    return j >= gap and array[j-gap] >temporary


def descending_sorting_function(array,j,gap,temporary):
    return j <= gap and array[j-gap] <temporary
    
    
    
def shellSort(array,sorting_function): 
    
    
    # Start with a big gap, then reduce the gap 
    length = len(array) 
    gap = length//2
  
    # Do a gapped insertion sort for this gap size. 
    # The first gap elements a[0..gap-1] are already in gapped  
    # order keep adding one more element until the entire array 
    # is gap sorted 
    while gap > 0: 
  
        for index in range(gap,length): 
  
            # add a[index] to the elements that have been gap sorted 
            # save a[index] in temporary and make a hole at position index 
            temporary = array[index] 
  
            # shift earlier gap-sorted elements up until the correct 
            # location for a[index] is found 
            index2 = index 
            while  sorting_function(array,index2,gap,temporary): 
                array[index2] = array[index2-gap] 
                index2 -= gap 
  
            # put temporary (the original a[index]) in its correct location 
            array[index2] = temporary 
        gap //= 2
    




def filter_contains(array,thingToBeInArray):
    return thingToBeInArray in array    
        
def filter_function(array,thingToBeInArray):
    for i in range(len(array)):
        if(filter_contains(array,thingToBeInArray) == False):
            del array[i]
        
    
        
