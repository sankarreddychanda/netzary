def prime_sum(x):
    sum = 0
    for i in range(2, x):
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            sum = sum+i
            for k in range(2,sum):
                if sum%k==0:
                    break
            else:
                if sum < x:
                    print('prime sum',sum)
prime_sum(1000)










