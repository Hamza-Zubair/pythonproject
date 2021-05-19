def makeweeklist(r1, wlist): 
    if (r1 == wlist): 
        return r1 
    else: 
        # Create empty list 
        res = [] 
        # loop to append successors to list until r2 is reached. 
        while(r1 < wlist+1 ): 
            res.append(r1) 
            r1 += 1
        return res 
# Driver Code 
r1, wlist = 1, 52
a= []
a = makeweeklist(r1, wlist)
print (a)