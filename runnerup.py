if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()));
    print(sorted(list(set(arr)))[-2]);

    """last = max(arr);
    arr.remove(last);   
    if(max(arr)== last):
            last1= max(arr);
            arr.remove(last1)
            print(max(arr));
    else:
            print(max.arr);"""
   
    
