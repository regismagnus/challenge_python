'''
Consider integer numbers from 0 to n - 1 written down along the circle in such a way that the distance between any two neighboring numbers is equal (note that 0 and n - 1 are neighboring, too).

Given n and firstNumber, find the number which is written in the radially opposite position to firstNumber.

Example

For n = 10 and firstNumber = 2, the output should be
circleOfNumbers(n, firstNumber) = 7.

best solution by andrew_pubge
    return (firstNumber + n/2)%n
'''
def circleOfNumbers(n, firstNumber):
    m=n/2
    return abs(m-firstNumber) if m<=firstNumber else m+firstNumber
print(circleOfNumbers(4, 3))