def main():
    # Output using our own function
    name = input("What's your name? ")
    hello(name)
    
    # Output without passing the expected arguments
    hello()


def hello(to="world"):    # add a default value
    print("hello,", to)


main()