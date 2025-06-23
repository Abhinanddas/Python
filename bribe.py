def minimumBribes(q):
    # index =1
    # bribes =0
    # q = [i-1 for i in q]
    # for x in q:
        
    #     if (x - index) > 2:
    #         print("Too Chaotic")
    #         return
        
    #     for j in range(index-1):
    #         if q[j] > x:
    #             bribes +=1
    #     index +=1
    
    # print(bribes)
    
    bribes = 0
    q = [i-1 for i in q]
    print(q)
    for i, o in enumerate(q):
        cur = i

        if o - cur > 2:
            print("Too chaotic")
            return
        
        print(q[max(o - 1, 0):i])
        for k in q[max(o - 1, 0):i]:
            if k > o:
                bribes += 1

    print(bribes)
        
    
        
minimumBribes([4,1,2,3]) #too
minimumBribes([2,1,5,3,4])#3
minimumBribes([2, 5, 1, 3, 4])#too
minimumBribes([5, 1, 2, 3, 7, 8, 6, 4])#too
minimumBribes([1, 2, 5, 3, 7, 8, 6, 4])#7

