import numpy as np

def format_strings(arr):
    centered = np.array([s.center(15, '*') for s in arr])
    left_justified = np.array([s.ljust(15, '*') for s in arr])
    right_justified = np.array([s.rjust(15, '*') for s in arr])
    
    return centered, left_justified, right_justified

def main():
    arr = np.array(["apple", "banana", "cherry", "date", "elderberry"])  
    centered, left_justified, right_justified = format_strings(arr)
    
    print("Centered:")
    print(centered)
    print("\nLeft-Justified:")
    print(left_justified)
    print("\nRight-Justified:")
    print(right_justified)

if __name__ == "__main__":
    main()
