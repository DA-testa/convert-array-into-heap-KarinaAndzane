# python3


def build_heap(data):
    swaps = []
    count = 0 
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    array = [0]
    for i in (data):
        array.append(i)

    for i in range(len(data)-1,-1,-1):
        
        swap(i,node)
         # swaps.append((data[i], data[int(i/2)]))
    return swaps,count

def swap(i,node):
    while i!=1:
        node=i
        if data[i]<data[int(i/2)]:
            data[i]=data[int(i/2)]
            data[int(i/2)]=node
            count=count+1
            swaps.append((data[i], data[int(i/2)]))
    return swap(int(i/2),node)

def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
    mode = input()
    if "I" in mode:
    # input from keyboard
         n = int(input())
         data = list(map(int, input().split()))
            
    if "F" in mode:
        filename=input()
        with open ("./test/"+filename, mode ='r') as fails:
            n=int(fails.readline())
            data=(list(map(int,fails.readline().split())))
                    
    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # print(len(swaps))
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
