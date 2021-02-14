a=input('Enter a number:')
b,f1,f2,f3=int(a),'','',''
ll=[]
try:
    for i in range(len(a)):
        e=len(a)-i-1
        l=['I','X','C','M','_X','_C','_M','_M']
        l2=['V','L','D','_V','_L','_D','']
        r=['','I','II','III','IV','V','VI','VII','VIII','IX']
        g=r[int(a[i])]
        if int(a[0])>3 and e>=6:l[-1]=4
        f1=g.replace('X',l[e+1])
        f2=f1.replace('I',l[e])
        f3=f2.replace('V',l2[e])
        ll.append(f3)
    print(''.join(ll))
except:
    print('invalid integer')
