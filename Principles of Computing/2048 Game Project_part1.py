'''This function reproduces a simple version of the game 2048'''

def merge(number_list):
    """This function takes a list as input, if two consecutive numbers are the same, we add those two numbers
       At the end we'll have a modified list that has the same length as the original one"""
    
    # we start creating a new list that contains all numbers passed in number_list, as long as they're not zero
    result = [element for element in number_list if element != 0]
   
    # using some logic, if a number in result is equal to its previos number, we add those two numbers
    for element in range(0, len(result) - 1):
        if result[element] == result[element + 1]:
            result[element] *= 2
            result[element + 1] = 0
        
    # we modify result so that it contains only numbers different from zero
    result = [element for element in result if element != 0]
    
    # to finish, we add as many zeros as needed to result, so that its length is the same as the original number_list
    while len(result) < len(number_list):
            result.append(0)
            
    # we return result        
    return result
    
        

