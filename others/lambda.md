## I've just discovered the lambda function in Python and I want to try it out! I got some of this from: https://www.w3schools.com/python/python_lambda.asp
### SYNTAX: lambda *arguments* : *expression*

## Example 1: Add 10 to argument a, and return the result.

``` Python
x = lambda a : a + 10
print(x(5))
```

## Example 2: Multiply argument a with argument b and return the result.
Lambda can take any num of arguments.

``` Python
x = lambda a, b : a * b
print(x(5, 6))
```

## Example 3: Summarize argument a, b, and c and return the result.

``` Python
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))
```

## Example 4: Double number in function. Then triple it.
The power of lambda is better shown when you use them as an anonymous function inside another function.

``` Python
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))
```
