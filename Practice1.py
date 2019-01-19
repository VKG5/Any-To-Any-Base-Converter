def Base_To_Decimal(strr,base):

    n1, n2 = strr.split('.')
    i, sum1 = (len(n1) - 1), 0

    ## INTEGER PART
    for n in n1:
        n = int(check_val(n))
        sum1 += n * (base**i)
        i-=1

    ## FRACTIONAL PART  
    j = 1
    sum2 = 0
    for i in n2:
        sum2 += int(check_val(i))*(base**(-j))
        j+=1

    sum = sum1 + sum2
    
    return str(sum)

def Decimal_To_Base(number, base, places):

    n1, n2 = number.split('.')

    print(n1, n2)

    ## INTEGER PART
    sum1 = ""
    while(int(n1)):
        temp = int(n1)%base
##        if(temp == 0):
##            sum1 = 1
        sum1 = str(temp) + sum1
        n1 = int(n1)//base

    print(sum1)
    #print(str2)

    ## FRACTIONAL PART
    n2 = '0.' + n2
    num1 = 0
    #print(n2)

    i = places
    while(i):
        temp = float(n2) * base
        num1 = num1*10 + int(temp)        

        n2 = float(temp) - int(temp)
        #print(n2)

        i-=1

    num, sum = '.' + str(num1), ""  

    sum += sum1 + num
    print(sum)

    return sum



# Main Body
def check_val(n):
    if( n >= '0' and n <= '9'):
        return int(n)
    if( n >= 'A' and n <= 'F'):
        return int((ord(n) - ord('A')) + 10)
    if( n == '.'):
        return 0 

strr = input("Enter a number: ")
base = int(input("Enter the base of the number: "))
base2 = int(input("Enter the base to which you want to convert: "))
places = int(input("Enter the number of places you want after decimal: "))

if('.' not in strr):
    strr += '.0'
    
for i in strr:
    if(int(check_val(i)) >= base):
        print("Invalid Number!")
        exit()

ans1 = Base_To_Decimal(strr,base)
print("Base to Decimal: ", ans1)
print("Decimal to Base: ", Decimal_To_Base(ans1, base2, places))


