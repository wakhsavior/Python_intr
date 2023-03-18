def math(op, x, y):
    print(op(x, y))

def main():
    calc1 = lambda a, b: a + b
    calc2 = lambda a, b: a * b
    

    math(calc2,5, 15)
    math(calc1,5, 15)
    

if __name__ == "__main__":
    main() 