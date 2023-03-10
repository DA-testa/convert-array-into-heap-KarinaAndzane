# python3


def build_heap(data):
    
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    swaps = []
    for i in range(len(data)-1,- 1,-1):
        while i!=0:
            if data[i]<data[int((i-1)/2)]:
                data[i],data[int((i-1)/2)]=data[int((i-1)/2)],data[i]
                swaps.append((int((i-1)/2), i))
         
            i = int((i-1)/2)
           
    return swaps



def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
    mode = input()
    if "I" in mode:
    # input from keyboard
         n = int(input())
         data = list(map(int, input().split()))
    elif "F" in mode:
        filename=input()
        if 'a' not in filename:
            
            with open ("./tests/"+filename, mode ='r') as fails:
                n=int(fails.readline())
                data=(list(map(int,fails.readline().split())))
    else:
        print("error")
                    
    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
  
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i,j in swaps:
        print(i,j)


if __name__ == "__main__":
    main()
