def MemoDP(memo, w, v, index, last):

    try:
        return memo[(index, last)]
    except:
        if index ==0:
            if w[index] <=last:
                return v[index]
            else:
                return 0

        without_l = MemoDP(memo, w, v, index -1, last)

        if w[index] > last:
            return without_l
        else:
            with_l =v[index] + MemoDP(memo, w, v, index - 1, last - w[index])

        maxvalue = max(with_l , without_l)

        memo[(index, last)] = maxvalue

        return maxvalue

w = [3,2,1,4,5]
v = [25,20,15,40,50]
memo = {}  #null
f = int(input("the knapsack capacity:"))
print ("the total value is: ", MemoDP(memo, w, v, len(w)-1, f))