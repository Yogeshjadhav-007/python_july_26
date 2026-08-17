print("This is myfile1")
print("__name__:", __name__)

x = 10
y = 20

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

if __name__ == "__main__":
    print("Sub:", sub(10, 20))