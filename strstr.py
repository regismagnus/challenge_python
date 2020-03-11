'''
Avoid using built-in functions to solve this challenge.
Implement them yourself, since this is what you would be asked to do during a real interview.

Implement a function that takes two strings, s and x, as arguments and finds the first occurrence of the string x in s. 
The function should return an integer indicating the index in s of the first occurrence of x. 
If there are no occurrences of x in s, return -1.

Example

For s = "CodefightsIsAwesome" and x = "IA", the output should be
strstr(s, x) = -1;
For s = "CodefightsIsAwesome" and x = "IsA", the output should be
strstr(s, x) = 10.
'''
def strstr(s, x):
    #if out this result in timeout
    if x not in s:
        return -1
        
    sl=len(s)
    xl=len(x)
    for i in range(0,sl):
        if i+xl>sl:
            return -1
        if (sl-i)>=xl and s[i:i+xl]==x:
            return i
    return -1
print(strstr("CodefightsIsAwesome", "IsA"))