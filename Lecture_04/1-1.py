
def calk1(a):
    return a*a

def calk2(a):
    return a+a

def math(op, x):
    print(op(x))

def main():
    math(calk2,5)
    math(calk1,5)
    

if __name__ == "__main__":
    main() 