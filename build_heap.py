# python3
def define_heap(data, n, i, swaps):
    smallest = i
    leftChild = 2*i+1
    rightChild = 2*i+2

    if leftChild < n and data[leftChild] < data[smallest]:
        smallest = leftChild
    if rightChild < n and data[rightChild] < data[smallest]:
        smallest = rightChild

    if smallest != i:
        data[i], data[smallest] = data[smallest], data[i]
        swaps.append((i, smallest))
        define_heap(data, n, smallest, swaps)
    
def build_heap(data):
    swaps = []
   n = len(data)
    i = n // 2-1
    while i>= 0:
        define_heap(data, n, i, swaps)
        i = i-1

           
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)


    return swaps


def main():
    text = input()
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
    if "F" in text:
           text = input()
    if "F" in text:
        filename = input()
        if "a" not in filename:
            path = "./tests/" + filename
            with open(path, "r") as file:
                n = int(file.readline())
                data = list(map(int, file.readline().split()))
    if "I" in text:

    # input from keyboard
       n = int(input())
        data = list(map(int, input().split()))

    # checks if lenght of data is the same as the said lenght
    assert len(data) == j

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)



if __name__ == "__main__":
    main()
