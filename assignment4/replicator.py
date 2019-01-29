def repeat_good(a):
    return '-'.join([str(a[b]*(b+1)).capitalize() for b in range(len(a))])
                   
print(repeat_good("abcd"))



def repeat_bad(a):
    r=''
    b=0
    while b < len(a):
        c = 0
        while c < b+1:
            if c == 0:
                r=r+a[b].upper()
            else:
                r=r+a[b].lower()
            c=c+1
        r=r+'-'
        b=b+1
    return r[:len(r)-1]

print(repeat_bad('abcd'))

                
               
                
                
                
             

           
          

