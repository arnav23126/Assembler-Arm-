#project decode
def overwritebin():
    bincode=open('bineq.txt','+w')
    bincode.close()

def readinst(pc):
    temp=assembly[pc]
    
    if '\n' in temp and len(temp)<7:
        global count
        count+=1
        return readinst(pc+1)
    else:
        return temp
        
def writebin(bineq):
    bincode=open('bineq.txt','+a')
    bincode.write(str(bineq))
    bincode.close()

def opcode(instype):
    R_type = ["add","sub","sll","slt","sltu","xor","srl","or","and"]
    I_type1 = ["lw"]
    I_type2 = ["addi","sltiu"]
    I_type3= ["jalr"]
    S_type = ["sw","sb","sh","sd"]
    B_type = ["beq","bne","blt","bge","bltu","bgeu"]
    U_type1 = ["lui"]
    U_type2 = ["auipc"]
    J_type = ["jal"]
    
    if instype in R_type:
        return("0110011")
    elif instype in I_type1:
        return("0000011")
    elif instype in I_type2:
        return("0010011")
    elif instype in I_type3:
        return("1100111")
    elif instype in S_type:
        return("0100011")
    elif instype in B_type:
        return("1100011")
    elif instype in U_type1:
        return("0110111")
    elif instype in U_type2:
        return("0010111")
    elif instype in J_type:
        return("1101111")
    else:
        return "error"

def funct3(x):
    lx0 = ["add","sub","addi","beq","jalr"]
    lx1 = ["sll","bne"]
    lx2 = ["slt","lw","sw"]
    lx3 = ["sltu","sltiu"]
    lx4 = ["xor","blt"]
    lx5 = ["srl","bge"]
    lx6 = ["or","bltu"]
    lx7 = ["and","bgeu"]
    null = ["lui","auipc","jal"]
    if x in lx0:
        return "000"
    elif x in lx1:
        return "001"
    elif x in lx2:
        return "010"
    elif x in lx3:
        return "011"
    elif x in lx4:
        return "100"
    elif x in lx5:
        return "101"
    elif x in lx6:
        return "110"
    elif x in lx7:
        return "111"
    elif x in null:
        return ""

def funct7(x):
    lx0 = ["add","sll","slt","sltu","xor","srl","or","and"]
    lx1 = ["sub"]
    null = ["lw","addi","sltiu","jalr","sw","beq","bne","blt","bge","bltu","bgeu","lui","auipc","jal"]
    if x in lx0:
        return "0000000"
    elif x in lx1:
        return "0100000"
    elif x in null:
        return ""

def register_code(x):
    if x=="zero":
        return "00000"
    elif x=="ra":
        return "00001"
    elif x=="sp":
        return "00010"
    elif x=="gp":
        return "00011"
    elif x=="tp":
        return "00100"
    elif x=="t0":
        return "00101"
    elif x=="t1":
        return "00110"
    elif x=="t2":
        return "00111"
    elif x=="s0" or x=="fp":
        return "01000"
    elif x=="s1":
        return "01001"
    elif x=="a0":
        return "01010"
    elif x=="a1":
        return "01011"
    elif x=="a2":
        return "01100"
    elif x=="a3":
        return "01101"
    elif x=="a4":
        return "01110"
    elif x=="a5":
        return "01111"
    elif x=="a6":
        return "10000"
    elif x=="a7":
        return "10001"
    elif x=="s2":
        return "10010"
    elif x=="s3":
        return "10011"
    elif x=="s4":
        return "10100"
    elif x=="s5":
        return "10101"
    elif x=="s6":
        return "10110"
    elif x=="s7":
        return "10111"
    elif x=="s8":
        return "11000"
    elif x=="s9":
        return "11001"
    elif x=="s10":
        return "11010"
    elif x=="s11":
        return "11011"
    elif x=="t3":
        return "11100"
    elif x=="t4":
        return "11101"
    elif x=="t5":
        return "11110"
    elif x=="t6":
        return "11111"
    else:
        return "error"

def flip(a):
    if(a=="0"):
        return "1";
    elif(a=="1"):
        return "0";

def Cmp2(a):
    t="0"+a;
    s='';
    flag=0;
    if(int(t)==0):
        r=0;
    else:
        r=t.rindex("1");
    for i in range(len(t)-1,-1,-1):
        if(i>=r):
            s=t[i]+s;
        else:
            s=flip(t[i])+s;
    return s;
   
def DecToBin(a):
    st="";
    temp=a;
    if(temp==0):
        return "0";
    while(temp!=0):
        st=st+str(temp%2);
        temp=temp//2;
    st=st[::-1];
    return st;

def imm(num,ty):
    num=int(num);
    if(ty in ["0000011","0010011","1100111"]):
        Orig=num;
        num=abs(num);
        t=DecToBin(num);
        if(len(t)>=12):
            return '-1';
        if(Orig<0):
            t=Cmp2(t);
        elif(Orig>0):
            t="0"+t;
        size=len(t);
        y=12-size;
        if(t[0]=="0"):
            t="0"*y+t;
            return t;
        elif(t[0]=="1"):
            t="1"*y+t;
            return t;
    elif(ty in ["1100011"]):
        Orig=num;
        num=abs(num);
        t=DecToBin(num);
        if(len(t)>=13):
            return '-1';
        if(Orig<0):
            t=Cmp2(t);
        elif(Orig>0):
            t="0"+t;
        size=len(t);
        y=13-size;
        if(t[0]=="0"):
            t=y*"0"+t;
            t=t[0:13]
            y=t[0]+t[2:8];
            z=t[8:12]+t[1];
            return y,z;
        elif(t[0]=="1"):
            t=y*"1"+t;
            t=t[0:13];
            y=t[0]+t[2:8];
            z=t[8:12]+t[1];
            return y,z;
    elif(ty in ["0110111","0010111"]):
        Orig=num;
        num=abs(num);
        t=DecToBin(num);
        if(len(t)>=32):
            return '-1';
        if(Orig<0):
            t=Cmp2(t);
        elif(Orig>0):
            t="0"+t;
        size=len(t);
        y=32-size;
        if(t[0]=="0"):
            t=y*"0"+t;
        else:
            t=y*"1"+t;
        return t[:20];
    elif(ty in ["0100011"]):
        Orig=num;
        num=abs(num);
        t=DecToBin(num);
        if(len(t)>=12):
            return '-1';
        if(Orig<0):
            t=Cmp2(t);
        elif(Orig>0):
            t="0"+t;
        size=len(t);
        y=12-size;
        if(t[0]=="0"):
            t=y*"0"+t;
        else:
            t=y*"1"+t;
        return t[0:7],t[7:]
    elif(ty in ["1101111"]):
        Orig=num;
        num=abs(num);
        t=DecToBin(num);
        if(len(t)>=21):
            return '-1';
        if(Orig<0):
            t=Cmp2(t);
        elif(Orig>0):
            t="0"+t;
        size=len(t);
        y=21-size;
        if(t[0]=="0"):
            t=y*"0"+t;
        else:
            t=y*"1"+t;
        t=t[0:21];
        t=t[0]+t[10:20]+t[9]+t[1:9];
        return t;
      
fname=input('File Name: ')
ascode=open(fname,'+r')
assembly = ascode.readlines()
ascode.close()

overwritebin()

count=0

while(count!=len(assembly)):
    
    inst=readinst(count).split()
    count+=1
    
    inst=[inst[0]]+inst[1].split(',')
    opco=opcode(inst[0])
    #print(inst)
    if opco=='error':
        writebin('Invalid Instruction Name')
        break
    

    elif inst==["addi","x0","x0","0"]:
        pass

    elif opco=='0110011':
        bineq=funct7(inst[0])+register_code(inst[3])+register_code(inst[2])+ funct3(inst[0])+register_code(inst[1])+opco
        if 'error'in bineq:
            writebin('Invalid Register Name')
        else:
            writebin(bineq + '\n')
    
    elif opco in ["0010011"]:
        bineq=imm(inst[3],opco)+register_code(inst[2])+ funct3(inst[0])+register_code(inst[1])+opco
        if 'error'in bineq:
            writebin('Invalid Register Name')
        elif '-1'in bineq:
            writebin('Invalid Imm Value') 
        else:
            writebin(bineq + '\n')

    elif opco in ['1100111',"0000011"]:
        t=inst[2].split('(')
        bineq=imm(t[0],opco)+register_code(t[1].strip(')'))+ funct3(inst[0])+register_code(inst[1])+opco
        if 'error'in bineq:
            writebin('Invalid Register Name')
        elif '-1'in bineq:
            writebin('Invalid Imm Value')
        else:
            writebin(bineq + '\n')
    
    elif opco in ['0100011']:
        t=inst[2].split('(')
        x,y=imm(t[0],opco)
        bineq=x+register_code(inst[1])+register_code(t[1].strip(')'))+ funct3(inst[0])+y+opco
        if 'error'in bineq:
            writebin('Invalid Register Name')
        elif '-1'in bineq:
            writebin('Invalid Imm Value')
        else:
            writebin(bineq + '\n')

    elif opco in ["1100011"] and inst!=['beq',"zero","zero","0"]:
        x,y=imm(inst[3],opco)
        bineq=x+register_code(inst[2])+register_code(inst[1])+ funct3(inst[0])+y+opco
        if 'error'in bineq:
            writebin('Invalid Register Name')
        elif '-1'in bineq:
            writebin('Invalid Imm Value')
        else:
            writebin(bineq + '\n')
    
    elif opco in ["0110111","0010111","1101111"]:
        bineq=imm(inst[2],opco)+register_code(inst[1])+opco
        if 'error'in bineq:
            writebin('Invalid Register Name')
        elif '-1'in bineq:
            writebin('Invalid Imm Value') 
        else:
            writebin(bineq + '\n')

    elif opco in ["1100011"] and inst==['beq',"zero","zero","0"]:
        x,y=imm(inst[3],opco)
        bineq=x+register_code(inst[2])+register_code(inst[1])+ funct3(inst[0])+y+opco
        if 'error'in bineq:
            writebin('Invalid Register Name')
        elif '-1'in bineq:
            writebin('Invalid Imm Value')
        else:
            writebin(bineq)       

    elif inst==["beq","zero","zero","0"] and count==(len(assembly)):
        break
    
    elif inst!=["beq","zero","zero","0"] and count==(len(assembly)):
        writebin('Missing Virtual Halt')
        break
    
    elif inst==["beq","zero","zero","0"] and count!=(len(assembly)):
        writebin('Invalid Virtual Halt')
        break
