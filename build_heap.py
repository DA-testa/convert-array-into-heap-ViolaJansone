# python3
def defline_heap(data, v, j, swaps);
smallest = v
leftChild = 2*v+1
rightChild= 2 I+2
if leftChild < j and data[leftChild] < data[smallest]:
    smallest = leftChild
if rightChild < j and data [rightChild] < data[smallest]:
    smallest = rightChild

if smalest !=v:
    data[v], data[smallest]= data[smallest], data[i]
    swaps.append((i,smalest))
    define-heap(data, v, smallest, swaps)
    
    
def build_heap(data):
    swaps = []
    j =len(data0
    v= j//2-1
    while v>= 0:
          define_heap(data, j, v, swaps)
           v=v-1
           
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)


    return swaps


def main():
    text = input()
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
if "F" in text:
           filename = input()
           if "a" not in filename:
           path = "./tests/" + filename
           with oprn(path, "r") as file:
           j = int(file.readline())
           data = list(map(int, file.readline().split()))
    if "I" in text:

    # input from keyboard
    j = int(input())
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
    for v, j in swaps:
        print(v, j)


if __name__ == "__main__":
    main()
