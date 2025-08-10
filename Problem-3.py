
def generate_pattern(a: int):
    count = a if a % 2 == 1 else a - 1
    return [2*i+1 for i in range(count)]

def main():
    a = int(input("Enter a (positive integer): ").strip())
    seq = generate_pattern(a)
    print(", ".join(map(str, seq)))

if __name__ == "__main__":
    main()
