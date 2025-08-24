"""
FizzBuzz Implementation

Classic programming problem:
- Print numbers 1 to 100
- For multiples of 3: print "Fizz"
- For multiples of 5: print "Buzz"  
- For multiples of both 3 and 5: print "FizzBuzz"
"""


def fizzbuzz(n):
    """Generate FizzBuzz sequence up to n"""
    result = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result


def main():
    """Run FizzBuzz for numbers 1-100"""
    result = fizzbuzz(100)
    for item in result:
        print(item)


if __name__ == "__main__":
    main()
