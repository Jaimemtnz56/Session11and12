#Indicate the type of expression. choose between: Int, float, bool, NoneType, String, List, function or method
print(type(2+3)) #int
print(type(6/2)) #float (6//2) would be int
print(type(2 != 3)) #bool (True or false)
print(type(5 or 6)) #int
print(type("abc".find("b"))) #int (returns: 1 = position of b)
print(type("bubu" * 2)) #str
#"bubu"*(4/2) #Type Error not multiply by float
print(type(["abc",2])) #list
print(type("abc"[2])) #string (returns = 'c')
print(type("abcabcabc".split("a"))) #returns list of substrings

#Indicate the result of the following operations
print(2+3) #5
print(6/2) #3.0
print(2 != 3) #True
print(5 or 6) #5
print("abc".find("b")) #1
print("bubu" * 2) #'bubububu'
#"bubu"*(4/2) #Type Error not multiply by float
#print(len('abc', 2)) Type Error len() takes one argument
print(2+3*2**2) #14

#Assume the operations are executed in order, what will each print display
a = 2
b = 3
c = "abc"
print(a, b, c) # 2 3 abc
print(a, b, c, sep=",") # 2,3,abc
a += 2
a == 5
print(a) #4
print(c*(a-b)) #abc
d = c.find("b")
print(d) #1
print(d and b) #3
print(d == True) #True
e = str(a) + str(b) + str(c) + str(d)
print(e) #43abc1
print(e[1::2]) #3b1
print(e+e[::-1]) #43abc11cba34
