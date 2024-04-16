def bin_to_hexhelper(a):
    num = 0
    b = a[::-1]
    for i in range(0,len(b)):
        num+=pow(2,i)*int(b[i])
    return str(num)


def bintohex(a):  #a must be string and 32 bit in length
    c=""
    dict = {"1111":'f',"1110":"e","1101":"d","1100":"c","1011":"b","1010":"a"}
    for i in range(8):
        b = a[i*4:(i+1)*4]
        if b not in dict:
            c+=bin_to_hexhelper(b)
        else:
            c+=dict[b]
    return c

def unsigned_binary_to_dec(a): #a will be a string containing binary
    result=0
    for i in range(len(a)-1,-1):
        if(a[i]==1):
            result+=power(2,i)
    return result 
def make32bit(a):
    sign = a[0]
    extension = (32-len(a))*sign
    return(extension + a)

def DecToBin_signed(a_passed):
    a = abs(a_passed)
    signedbit="0"
    if(a_passed<0):
        signedbit = "1"
    st=""
    temp=a
    if(temp==0):
        return "0"
    while(temp!=0):
        st=st+str(temp%2)
        temp=temp//2
    st=st[::-1]
    return signedbit + st
def bin_todec(a): #Actually 2's complement binary
    ans = 0
    a_new = ""
    if(a[0]=="1"):
        a_new = two_complement(a)
        if(int(a_new[1:]) == 0):
            a_new = "1" + a_new
        b = a_new[::-1]
    else:
        b= a[::-1]
    for i in range(0,len(b) - 1):
        ans+=pow(2,i)*int(b[i])
    if b[len(b) - 1] == "0":
        return ans
    return -ans
def two_complement(a_passed):   #Dont use this for 2's complement finding just let it be in other functions
    a = a_passed[1:]
    if int(a[1:]) == 0:
        return "1" + a[1:]
    b = []
    for i in range(0,len(a)):
        if(a[i] == "0"):
            b.append("1")
        if(a[i] == "1"):
            b.append("0")
    j = len(a) - 1
    c=""
    while b[j] == "1":
        b[j] = "0"
        j-=1
    b[j] = "1"
    for i in range(0,len(b)):
        c=c+b[i]
    c="1" + c
    return c
def bitwise_xor(a,b):
    bin_a = DecToBin_signed(a)
    bin_b = DecToBin_signed(b)
    if(a<0):
        bin_a = two_complement(bin_a)
    if(b<0):
        bin_b = two_complement(bin_b)
    bin_a = make32bit(bin_a)
    bin_b = make32bit(bin_b)
    result = ""
    for i in range(0,len(bin_a)):
        if(bin_a[i] == bin_b[i]):
            result+="0"
        else:
            result+="1"
    return bin_todec(result)
def bitwise_or(a,b):
    bin_a = DecToBin_signed(a)
    bin_b = DecToBin_signed(b)
    if(a<0):
        bin_a = two_complement(bin_a)
    if(b<0):
        bin_b = two_complement(bin_b)
    bin_a = make32bit(bin_a)
    bin_b = make32bit(bin_b)
    result = ""
    for i in range(0, len(bin_a)):
        if bin_a[i] == "1" or bin_b[i] == "1":
            result+="1"
        else:
            result+="0"
    return bin_todec(result)
def rightshiftlogical(a,b):
    bin_a = DecToBin_signed(a)
    if(a<0):
        bin_a = two_complement(bin_a)
    bin_a = make32bit(bin_a)
    for i in range(0,b):
        bin_a = "0" + bin_a
    return(bin_todec(bin_a[:32]))
def overwritebin():
    bincode=open('C:\\Users\\ishit\\c,c++ dsa course\\bineq.txt','+w')
    bincode.close()
def readinst(pc):
    temp=assembly[pc]
    return temp
def ito2(n,b):
    mask= (1<<b)-1
    return"{:0{}b}".format(n & mask, b)
def dec(imm,str):
    if str=="s":
        return ((-1)**int(imm[0]) + int(imm[1:],2) - 2**(31*int(imm[0])))
    else:
        return (int(imm,2))

def writestatus(reg):
    a=open("C:\\Users\\ishit\\c,c++ dsa course\\bineq.txt","+a")
    cnt=1
    for i in reg.keys():
        
        if (cnt%5)==0:
            
            a.write('0b'+ito2(reg[i][1],32)+"\n")
        elif cnt==32:
            a.write('0b'+ito2(reg[i][1],32)+"\n")
        else:
            a.write('0b'+ito2(reg[i][1],32)+" ")
        cnt+=1
    a.close

        



fname='C:\\Users\\ishit\\c,c++ dsa course\\ascode.txt'
a=open(fname,'+a')
teller=a.tell()
a.close()
a=open(fname,'+r')
assembly=[]
while (True):
    k=a.readline().strip('\n')
    if a.tell()==teller:
        assembly.append(k)
        break
    if k.strip(' ')=='':
        continue 
    else: 
        assembly.append(k)
a.close()
print(assembly)
overwritebin()


# simulator starting
registers = {
    '00000': ['zero',0], '00001': ["ra",0], '00010': ["sp",0], '00011': ["gp",0],  '00100': ["tp",0],
    '00101':[ "t0",0],'00110':[ "t1",0] , '00111':[ "t2",0], '01000':[ "s0",0],'01001':[ "s1",0],
    '01010':[ "a0",0], '01011':[ "a1",0],'01100':[ "a2",0] , '01101':[ "a3",0], '01110':[ "a4",0],
   '01111' :[ "a5",0], '10000':[ "a6",0],'10001':[ "a7",0] , '10010':[ "s2",0],'10011':[ "s3",0] ,
  '10100': [ "s4",0] , '10101':[ "s5",0],'10110':[ "s6",0] ,'10111':[ "s7",0] ,'11000':[ "s8",0] ,
   '11001':[ "s9",0] , '11010':["s10",0] ,'11011': ["s11",0] , '11100':[ "t3",0], '11101':[ "t4",0],
   '11110': [ "t5",0],'11111':[ "t6",0] 
}
memory={'00010000':0,
'00010004':0,
'00010008':0,
'0001000c':0,
'00010010':0,
'00010014':0,
'00010018':0,
'0001001c':0,
'00010020':0,
'00010024':0,
'00010028':0,
'0001002c':0,
'00010030':0,
'00010034':0,
'00010038':0,
'0001003c':0,
'00010040':0,
'00010044':0,
'00010048':0,
'0001004c':0,
'00010050':0,
'00010054':0,
'00010058':0,
'0001005c':0,
'00010060':0,
'00010064':0,
'00010068':0,
'0001006c':0,
'00010070':0,
'00010074':0,
'00010078':0,
'0001007c':0,
}
pc=0
pcflag=0
while(int(pc/4)!=len(assembly)):
    bineq=assembly[int(pc/4)]
    op=bineq[25:]
    d=bineq[20:25]
    rsrc1=bineq[12:17]
    rsrc2=bineq[7:12]
    f3=bineq[17:20]
    f7=bineq[:7]
    i_type_imm=bineq[0:12]
    if op=='0110011':
        if f3=='000' and f7 == '0000000':  #add
            registers[d][1] = registers[rsrc1][1] + registers[rsrc2][1]
            pc=pc+4
        elif f3 == '000' and f7 == '0100000': #sub
            registers[d][1] = registers[rsrc1][1] - registers[rsrc2][1]   #Before changing anything on this line contact harshit
            pc+=4
        elif f3 == '001': #sll  Harshit ot sure
            d=dec(ito2(registers[rsrc2][1],32)[27:],"u")
            a=ito2(registers[rsrc1][1],32)[:32-d] + "0"*d
            registers[d][1]=dec(a,"s")
            pc+=4
        elif f3 == '010':#slt
            if(registers[rsrc1][1] < registers[rsrc2][1]):    #Before changing anything on this line contact harshit
                registers[d][1] = 1
            else:
                registers[d][1] = 0
            pc+=4
        elif f3 == '011':  #sltu   Harshit not sure
            if(dec(ito2(registers[rsrc2][1],32),'u') < dec(ito2(registers[rsrc2][1],32),'u')): #need to change later with a signed to unsigned converter with abs
                registers[d][1] = 1
            else:
                registers[d][1] = 0
            pc+=4
        elif f3 == '100':   #xor
            registers[d][1]=bitwise_xor(registers[rsrc1][1],registers[rsrc2][1])
            pc+=4
        elif f3 =='101':    #srl
            b=registers[rsrc2][1]
            temp_in_sbinary=DecToBin_signed(b)
            temp_in_2_complement=make32bit(two_complement(temp_in_sbinary))
            lower_5_bits=temp_in_2_complement[-5:0:-1]
            lower_5_bits_in_dec=unsigned_binary_to_dec(lower_5_bits)
            registers[d][1]=rightshiftlogical(registers[rsrc1][1],lower_5_bits_in_dec)
            pc+=4
        elif f3 == '110':    #or
            registers[d][1]=bitwise_or(registers[rsrc1][1],registers[rsrc2][1])
            pc+=4
        elif f3 == '111':   #and
            registers[d][1]=bitwise_and(registers[rsrc1][1],registers[rsrc2][1])
            pc+=4
    if op=="000011":#lw
        imm_i_32_bit=make32bit(i_type_imm)
        number=bin_todec(imm_i_32_bit)
        location=registers[rsrc1]+number

    
    if op=="0010011":    #addi
        imm_i_32_bit=make32bit(i_type_imm)
        number=bin_todec(imm_i_32_bit)
        registers[d][1]=registers[rsrc1][1]+number
        
    if op == '1010110':
           registers[d][1] = registers[rsrc2][1]*registers[rsrc1][1]
           pc+=4
    elif op=='0110011':
        if f3=='011':
            if registers[d][0] < dec(f7+rsrc1,'s')+registers[rsrc2][1]:
                registers[d][0]=1
            else:
                registers[d][0]=0
            pc=pc+4
    elif op=='1100011':
        if f3=='000':
            if registers[rsrc1][1]==registers[rsrc2][1]:
                immb='11'
                pc=pc + dec(immb,'s')
            else:
                pc=pc+4
        elif f3=='001':
            if registers[rsrc1][1]!=registers[rsrc2][1]:
                immb='11'
                pc=pc + dec(immb,'s')
            else:
                pc=pc+4
        elif f3=='101':
            if registers[rsrc2][1]>=registers[rsrc1][1]:
                immb='11'
                pc=pc + dec(immb,'s')
            else:
                pc=pc+4
        elif f3=='100':
            if registers[rsrc2][1]<registers[rsrc1][1]:
                immb='11'
                pc=pc + dec(immb,'s')
            else:
                pc=pc+4
        elif f3=='110':
            if registers[rsrc2][1]<registers[rsrc1][1]:
                immb='11'
                pc=pc + dec(immb,'u')
            else:
                pc=pc+4
        else:
            if registers[rsrc2][1]>=registers[rsrc1][1]:
                immb='11'
                pc=pc + dec(immb,'u')
            else:
                pc=pc+4
    elif op=='1100111' :
        registers[rsrc2][1]=pc+4
        pc=pc + dec(f7,'u') +registers[rsrc1]
        if pc%2 != 0:
            pc=pc-1
    else:
        pass
    writestatus(registers)

