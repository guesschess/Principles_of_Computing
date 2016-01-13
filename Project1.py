"""
Merge function for 2048 game.
"""

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    # input original list 
    origi = []
    origi = line[:]
    # create a new list
    new = []
    
    # Iterate the original list and find non-zero number and 
    # put it into the new list
    for ori_index in range(0, len(origi)):
        if origi[ori_index]:
            new.append(origi[ori_index])
    if len(new) < len(origi):
        gap = len(origi) - len(new)
        for gap_index in range(1, gap+1):
            new.append(0)
    # Iterate the new list and find two consecutive number that 
    # are same
    for new_index in range(0, len(new)-1):
        if new[new_index] == new[new_index+1]:
            new[new_index] = 2 * new[new_index] 
            new[new_index+1] = 0
    # Iterate the new list and remove 0s between any two non-zero numbers
    # and add it to the end of the lis
    
    for new_index in range(0, len(new)-1):
        if new[new_index] ==0:
            new.remove(0)
            new.append(0)            
   
    return new
