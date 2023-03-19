# python3
def parallel_processing(n, m, data):
    output = []
    thread = [0]*n
    time = 0
    i = 0
    j = 0

    while j < len(data):
        for i in range (len(thread)):
            if thread[i] == 0 :
                thread[i] = data[j]-1
                output.append([i, time])
                if j < len(data):
                    j += 1
            else:
                thread[i] -= 1
        time += 1

    return output
# def define_heap(data, n, i, swaps):
#     smallest = i
#     leftChild = 2*i+1
#     rightChild = 2*i+2

#     if leftChild < n and data[leftChild] < data[smallest]:
#         smallest = leftChild
#     if rightChild < n and data[rightChild] < data[smallest]:
#         smallest = rightChild

#     if smallest != i:
#         data[i], data[smallest] = data[smallest], data[i]
#         swaps.append((i, smallest))
#         define_heap(data, n, smallest, swaps)
    
# def build_heap(data):
#     swaps = []
#    n = len(data)
#     i = n // 2-1
#     while i>= 0:
#         define_heap(data, n, i, swaps)
#         i = i-1

           
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)


#     return swaps


def main():
      n = 0
    m = 0

    #i = input()# file or input
    i = "i"
    if "i" in i.lower() :
        n,m = map(int, input().split())
        data = list(map(int, input().split()))

    elif "f" in i.lower() :
        name = input()
        #name = "./test/" + name
        if "a" not in name:
            with open(name, mode = 'r' ,  encoding = "utf8") as fail:
                n,m = map(int, fail.readline().split())
                data = list(map(int, fail.readline().split()))
        else :
            return
                
    else :
        return

#     text = input()
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
#     if "F" in text:
#            text = input()
#     if "F" in text:
#         filename = input()
#         if "a" not in filename:
#             path = "./tests/" + filename
#             with open(path, "r") as file:
#                 n = int(file.readline())
#                 data = list(map(int, file.readline().split()))
#     if "I" in text:

    # input from keyboard
#        n = int(input())
#         data = list(map(int, input().split()))

    # checks if lenght of data is the same as the said lenght
#     assert len(data) == j

#     # calls function to assess the data 
#     # and give back all swaps
#     swaps = build_heap(data)

#     # TODO: output how many swaps were made, 
#     # this number should be less than 4n (less than 4*len(data))
  result = parallel_processing(n,m,data)

#     # output all swaps
#     print(len(swaps))
#     for i, j in swaps:
#         print(i, j)
 for i, j in result :
        print(i,j)


if __name__ == "__main__":
    main()
