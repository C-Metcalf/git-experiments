def main():
    print("Hello from gitexperiments!")
    results = feature()
    print(results)

def trunk():
    x = 40
    y = 20
    backend()
    return x * y

def backend():
    print("we do backend shiiii. you know how we do.")

def test():
    x =3
    y =2
    v = 3000
    print(x + y + v)
    
def feature():
    res = trunk()
    new_res = res / 5 + 300
    return new_res

if __name__ == "__main__":
    main()
    test()
