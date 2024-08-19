import random
from quick_select import QuickSelect

if __name__ == "__main__":
    # Generate a random array of 1000 unique elements in the range 1 to 10000
    array = [random.randint(1, 1000) for _ in range(1000)]
    # Get user input for the desired k-th smallest element
    k = int(input('Enter the value of k (1 to 1000): '))
    # Validate the user input for k
    if 1 <= k <= 1000:
        # Find the k-th smallest element using the QuickSelect algorithm
        kth_smallest = QuickSelect(array, k)
        print(f'The {k}-th smallest element is: {kth_smallest}')
    else:
        print('k must be between 1 and 1000')
