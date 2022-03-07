def top_n(items, n):
    """Return top n items in array in a descending order

    Args:
        items (array): list or array-like object
        n (int): num of items to return
        
    Returns:
        array: top n items in desc order
        
    Example:
        >>> top_n([8,3,2,7,4], 3)
        [8,7,4]
    """
    
    # keep sorting until we have the top n items
    for i in range(n):
        for j in range(len(items)-1-i): # iterate from the ith item in index
            
            if items[j] > items[j+1]: # if this item is bigger than the next item...
                items[j], items[j+1] = items[j+1], items[j] # swap the two!
                
    # get the last n items
    top_n = items[-n:]
    
    # return in descending order
    return top_n[::-1]
                