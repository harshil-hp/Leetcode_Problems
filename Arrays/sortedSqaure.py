def checkIfExist(arr) -> bool:
    for index in range(len(arr)):
        if 2 * arr[index] in arr[index+1:] or arr[index]/2 in arr[index+1:]:
            return True
    return False

checkIfExist([-2,0,10,-19,4,6,-8])