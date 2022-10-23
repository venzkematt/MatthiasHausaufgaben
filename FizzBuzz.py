import time

welcome = f"""

Welcome to FizzBuzz:

This game checks on your math skills. The game counts from 1 to 15. If the number given by the game is divisible by 3, enter
fizz. If the number is divisible by 5, enter buzz. If the number is divisible by 3 and 5, enter fizzbuzz. Otherwise just hit
the "return" key.
                                    HAVE FUN!

"""
print (welcome)

time.sleep(3)

def fizzbuzz(i):
    if i % 15 == 0:
        return "fizzbuzz"
    elif i % 3 == 0:
        return "fizz"
    elif i % 5 == 0:
        return "buzz"
    else:
        return str("")

x = 0

for i in range(1, 16):
    print(f"#>{i}: ")
    var = input("")
    x += 1
    # print(var, fizzbuzz(i))

    if var != fizzbuzz(i):
        print("Wrong answer, try again!")
        x -= 1
        print (f"You answered {x} times right, so far!")
        exit(0)

print (f"You answered {x} times right! Maximum score, congratulations!!!")
