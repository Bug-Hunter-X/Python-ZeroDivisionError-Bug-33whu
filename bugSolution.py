def function(a, b):
    if b == 0:
        return 0  # Or raise a more informative exception
    else:
        return a / b

result = function(10, 0) 
print(result) # Output: 0