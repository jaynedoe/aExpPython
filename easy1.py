# def twoNumberSum(array, targetSum):
#     # Write your code here.
#     pass


print('Hello World')

numberArray = [1,2,3,4,5,6,7,8,9]
target = 10
result = []

def twoNumberSum(array, targetSum):
    for x in range(len(array) - 1):
        firstNum = array[x]
        for y in range(x + 1, len(array)):
            secondNum = array[y]
            if firstNum + secondNum == targetSum:
                return [firstNum, secondNum]
    return []


result = twoNumberSum(numberArray, target)
print(result)