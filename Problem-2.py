
def generate_odds(a: int):
    return [2*i+1 for i in range(a)]

def main():
    a = int(input("Enter a (positive integer): ").strip())
    seq = generate_odds(a)
    print(", ".join(map(str, seq)))

if __name__ == "__main__":
    main()
