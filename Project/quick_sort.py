def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


if __name__ == "__main__":
    try:
        input_str = input("Enter numbers to sort (space separated): ")
        if input_str.strip():
            arr = list(map(int, input_str.split()))
            print(f"Original: {arr}")
            print(f"Sorted: {quick_sort(arr)}")
        else:
            print("No input provided.")
    except ValueError:
        print("Error: Please enter valid integers.")