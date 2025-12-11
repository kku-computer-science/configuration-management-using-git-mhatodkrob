def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


if __name__ == "__main__":
    try:
        input_str = input("Enter numbers to sort (space separated): ")
        if input_str.strip():
            arr = list(map(int, input_str.split()))
            print(f"Original: {arr}")
            print(f"Sorted: {bubble_sort(arr)}")
        else:
            print("No input provided.")
    except ValueError:
        print("Error: Please enter valid integers.")
