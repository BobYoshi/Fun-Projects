def fizzbuzz(fizz, buzz, limit=100):
    result = []

    for i in range(1, limit + 1):
        if i % fizz == 0 and i % buzz == 0:
            result.append("FizzBuzz")
        elif i % fizz == 0:
            result.append("Fizz")
        elif i % buzz == 0:
            result.append("Buzz")
        else:
            result.append(i)

    return result


if __name__ == "__main__":
    a = fizzbuzz(3, 5, 150)
    for i in a:
        print(i)
