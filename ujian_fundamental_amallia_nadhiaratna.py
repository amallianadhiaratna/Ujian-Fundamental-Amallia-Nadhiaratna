# ## Nomor 1
def calculate_years(principal,interest,tax,desired):
    year = 0
    while principal < desired :
        principal=principal+(principal*interest)-tax*(principal*interest)
        year += 1
    return year
print(calculate_years(1000.00,0.05,0.18,1100.00))
print(calculate_years(1200.00,0.17,0.05,2000.00))
print(calculate_years(1500.00,0.07,0.6,5000.00))


# Nomor 2
def expandedForm(num):
    if num>=10 and num<=99:
        print(str((num//10)*10)+'+'+str(num%10))
    elif num>=100 and num<=999:
        print(str((num//100)*100)+'+'+str((num%100)//10*10)+'+'+str(num%10))
    elif num>=1000 and num<=9999:
        print(str((num//1000)*1000)+'+'+str((num%1000)//100*100)+'+'+str((num%100)//10*10)+'+'+str(num%10))
    elif num>=10000 and num<=99999:
        print(str((num//10000)*10000)+'+'+str((num%1000)//100*100)+'+'+str((num%100)//10*10)+'+'+str(num%10))    
expandedForm(12)
expandedForm(42)
expandedForm(70304)

###coretan
# y=[]
# x=[]
# num=70304
# if num>=10 and num<=99:
#     x.append(str((num//10)*10))
#     x.append(str(num%10))
# elif num>=100 and num<=999:
#     x.append(str((num//100)*100))
#     x.append(str(((num%100)//10*10))
#     x.append(str(num%10))
# elif num>=1000 and num<=9999:
#     x.append(str((num//1000)*1000))
#     x.append(str((num%1000)//100*100))
#     x.append(str((num%100)//10*10))
#     x.append(str(num%10))
# elif num>=10000 and num<=99999:
#     x.append(str((num//10000)*10000))
#     x.append(str((num%10000)//1000*1000))
#     x.append(str((num%1000)//100*100))
#     x.append(str((num%100)//10*10))
#     x.append(str(num%10))
# for i in x:
#     if x[i]==0:
#         y.append(x[i])
# print(y)
# print(x)    

## Nomor 3
def tower_builder1(n_floors, blocksize):
    w,h=blocksize
    z=''
    for i in range(n_floors):
        for j in range (0,11):
            if j<=3 or j>=w*h:
                z+='  '
            else:
                z+=' *'
        z+='\n'
    for i in range(n_floors):
        for j in range (0,11):
            if j<=3-w or j>=(w**h):
                z+='  '
            else:
                z+=' *'
        z+='\n'
    for i in range(n_floors):
        for j in range (0,11):
            if j<=3-2*w or j>=10:
                z+='  '
            else:
                z+=' *'
        z+='\n'
    print(z)
tower_builder1(3,(2,3))

def tower_builder2(n_floors, blocksize):
    z= ''
    for i in range (n_floors+1):
        for j in range (0, 23):
            if j >= 10-i and j <= 11+i:
                z += ' *'
            else: 
                z += '  '    
        z += '\n'
    print (z)     

tower_builder2(6,(2,1))

