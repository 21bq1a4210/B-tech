'''
REGULAR EXPRESSIONS ::
* RE or REgEx is an expression containing a sequence of charecters for
    matching patterns in strings.
* Almost all the major programming languages have implementation for RegEx.
* The 're' module of Python is used for patteren matching using RegEx in Python.
* Following functions are available the 're' module;
    * findall()
    * search()
    * sub()
'''
import pandas as pd

'''
re.findall()
* re.findall() is used to match all the occurrences of a pattern in a str.
* In the given code, we find how many times does the word 'Python' appear in
    the given str.
'''
import re
txt = 'Python is my fav programming language. I love Python and I live in Python'
x = re.findall("Python", txt)
print(f"no.of times:{len(x)}, x is {x}")
#output: no.of times:3, x is ['Python', 'Python', 'Python']

'''
* In the given below code, we check if the str 'x' starts with the word 'Python or not.
* The '^' character returns a match only if the str with the pattern given after '^'
    symbol.
* The str y contains the word 'Python' but doesnt begin with it, hence we get an
    empty list.
'''
x = 'Python is my fav programming language. I love Python and I live in Python'
print(re.findall("^Python", x)) #['Python']

y = 'I love Python'
print(re.findall("^Python", y)) #[]

'''
* To match numbers in a str, we use the \d sequence
* A + sign at the end of \d makes sure that numbers such a 50 is treated as 50 and 
    not as 5 and 0
* You can find list of sequences at https://www.w3schools.com/python/python_regex.asp
'''
txt = "Python was released in 1991."
print(re.findall('\d', txt)) #['1', '9', '9', '1']

txt = 'Python was released in 1991.'
print(re.findall("\d+", txt)) #['1991']

'''
* To find matches in a Series, we first convert the Series into a
    str using the .to_string().
'''
txtList = ['India', 'Pakistan', 'Indonesia', 'India']
txt = pd.Series(txtList)
# print(txt)
# output:
# 0        India
# 1     Pakistan
# 2    Indonesia
# 3        India
# dtype: object
print(re.findall('India', txt.to_string())) #['India', 'India']

'''
re.search()
* re.search() returns a Match Object in caase of a pattern match in the str
* We can get the position of the match using the .span() of the Match Object.
'''
txt = 'Hello World'
match_object = re.search('World', txt)
print(match_object) #<re.Match object; span=(6, 11), match='World'>
print(match_object.span()) #(6, 11)

'''
re.sub()
* To replace text in a str with a different text, use the re,sub()
'''
txt = 'C is my favorite programming language,'
txt = re.sub('C', 'Python', txt)
print(txt) #Python is my favorite programming language,