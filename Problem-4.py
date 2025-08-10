
import re

def parse_input(s: str):
    parts = re.split(r'[\s,]+', s.strip())
    return [int(p) for p in parts if p]

def count_multiples(nums):
    return {i: sum(1 for n in nums if n % i == 0) for i in range(1, 10)}

def main():
    s = input("Enter numbers (comma or space separated), e.g. 1,2,8,9,12: ").strip()
    nums = parse_input(s)
    result = count_multiples(nums)
    print(result)

if __name__ == "__main__":
    main()
