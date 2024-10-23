def main():
    print("Hello from gitexperiments!")
    results = feature()
    print(results)

def trunk():
    x = 40
    y = 20
    return x * y

def feature():
    res = trunk()
    new_res = res / 5 + 300
    return new_res

if __name__ == "__main__":
    main()
