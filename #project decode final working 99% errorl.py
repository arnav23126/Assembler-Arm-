import string
import numpy as np

def overwritebin():
    bincode=open('C:\\Users\\ishit\\c,c++ dsa course\\bineq.txt','+w')
    bincode.close()

def readinst(pc):
    temp=assembly[pc]
    return temp

def the_ultimate_label_dealer_2point0(wlh):
    dictlabels=dict()
    for i in wlh:
        if ':' in i[0]:
            labelname=''
            for j in i[0]:
                if(j!=':'):
                    labelname+=j
                else:
                    break
            dictlabels[labelname]=wlh.index(i)*4
            del i[0]
    
    for i in wlh:
        for j in dictlabels.keys():
            if j in i:
                ind=wlh.index(i)
                i[len(i)-1]=i[len(i)-1].replace(j,str(dictlabels[j]-(ind*4)))
            else:
                continue
    return wlh
        
def writebin(bineq,cnt):
    n=""
    if cnt>len(assembly)-1:
        n=""
    else:
        n="\n"
    bincode=open('C:\\Users\\ishit\\c,c++ dsa course\\bineq.txt','+a')
    for i in bineq:
        bincode.write(str(i))
    bincode.write(n)
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
        return [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,1]
    elif instype in I_type1:
        return [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1]
    elif instype in I_type2:
        return [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,1]
    elif instype in I_type3:
        return [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,1,1]
    elif instype in S_type:
        return [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,1]
    elif instype in B_type:
        return [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1,1]
    elif instype in U_type1:
        return [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,1,1]
    elif instype in U_type2:
        return [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,1]
    elif instype in J_type:
        return [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,1,1,1]
    elif instype == "rst":
        return [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,1,0]
    elif instype == "mul":
        return [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,1,0]
    elif instype == "halt":
        return [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,1,0,1]
    elif instype == "rvrs":
        return [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,1,1,1]
    else:
        return [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]

def funct3(x):
    lx0 = ["add","sub","addi","beq","jalr"]
    lx1 = ["sll","bne"]
    lx2 = ["slt","lw","sw"]
    lx3 = ["sltu","sltiu"]
    lx4 = ["xor","blt"]
    lx5 = ["srl","bge"]
    lx6 = ["or","bltu"]
    lx7 = ["and","bgeu"]
    if x in lx0:
        return [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif x in lx1:
        return [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0]
    elif x in lx2:
        return [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif x in lx3:
        return [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0]
    elif x in lx4:
        return [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif x in lx5:
        return [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0]
    elif x in lx6:
        return [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif x in lx7:
        return [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0]
    else:
        return [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

def funct7(x):
    lx1 = ["sub"]
    if x in lx1:
        return [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    else:
        return [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

def rs2(x):
    if x=="zero":
        return [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif x=="ra":
        return [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif x=="sp":
        return [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif x=="gp":
        return [0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif x=="tp":
        return [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif x=="t0":
        return [0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif x=="t1":
        return [0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif x=="t2":
        return [0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif x=="s0" or x=="fp":
        return [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif x=="s1":
        return [0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif x=="a0":
        return [0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif x=="a1":
        return [0,0,0,0,0,0,0,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif x=="a2":
        return [0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif x=="a3":
        return [0,0,0,0,0,0,0,0,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif x=="a4":
        return [0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif x=="a5":
        return [0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif x=="a6":
        return [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif x=="a7":
        return [0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif x=="s2":
        return [0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif x=="s3":
        return [0,0,0,0,0,0,0,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif x=="s4":
        return [0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif x=="s5":
        return [0,0,0,0,0,0,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif x=="s6":
        return [0,0,0,0,0,0,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif x=="s7":
        return [0,0,0,0,0,0,0,1,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif x=="s8":
        return [0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif x=="s9":
        return [0,0,0,0,0,0,0,1,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif x=="s10":
        return [0,0,0,0,0,0,0,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif x=="s11":
        return [0,0,0,0,0,0,0,1,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif x=="t3":
        return [0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif x=="t4":
        return [0,0,0,0,0,0,0,1,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif x=="t5":
        return [0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif x=="t6":
        return [0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    else:
        return [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]

def rs1(x):
    if x=="zero":
        return [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif x=="ra":
        return [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif x=="sp":
        return [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif x=="gp":
        return [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif x=="tp":
        return [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif x=="t0":
        return [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif x=="t1":
        return [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif x=="t2":
        return [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif x=="s0" or x=="fp":
        return [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif x=="s1":
        return [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif x=="a0":
        return [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif x=="a1":
        return [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif x=="a2":
        return [0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif x=="a3":
        return [0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif x=="a4":
        return [0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif x=="a5":
        return [0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif x=="a6":
        return [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif x=="a7":
        return [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif x=="s2":
        return [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif x=="s3":
        return [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif x=="s4":
        return [0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif x=="s5":
        return [0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif x=="s6":
        return [0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif x=="s7":
        return [0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif x=="s8":
        return [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif x=="s9":
        return [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif x=="s10":
        return [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif x=="s11":
        return [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif x=="t3":
        return [0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif x=="t4":
        return [0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif x=="t5":
        return [0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif x=="t6":
        return [0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    else:
        return [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]

def rd(x):
    if x=="zero":
        return [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif x=="ra":
        return [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0]
    elif x=="sp":
        return [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0]
    elif x=="gp":
        return [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0]
    elif x=="tp":
        return [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0]
    elif x=="t0":
        return [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0]
    elif x=="t1":
        return [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0]
    elif x=="t2":
        return [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0]
    elif x=="s0" or x=="fp":
        return [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0]
    elif x=="s1":
        return [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0]
    elif x=="a0":
        return [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0]
    elif x=="a1":
        return [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,0,0,0,0,0,0]
    elif x=="a2":
        return [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0]
    elif x=="a3":
        return [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,0,0,0,0,0,0,0]
    elif x=="a4":
        return [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0]
    elif x=="a5":
        return [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0]
    elif x=="a6":
        return [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0]
    elif x=="a7":
        return [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0]
    elif x=="s2":
        return [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0]
    elif x=="s3":
        return [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,1,0,0,0,0,0,0,0]
    elif x=="s4":
        return [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0]
    elif x=="s5":
        return [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,0,0,0,0,0,0]
    elif x=="s6":
        return [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,0,0,0,0,0,0,0]
    elif x=="s7":
        return [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,1,0,0,0,0,0,0,0]
    elif x=="s8":
        return [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0]
    elif x=="s9":
        return [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,0,0,0,0,0,0,0]
    elif x=="s10":
        return [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,0,0,0,0,0,0,0,0]
    elif x=="s11":
        return [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,1,0,0,0,0,0,0,0]
    elif x=="t3":
        return [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0]
    elif x=="t4":
        return [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,1,0,0,0,0,0,0,0]
    elif x=="t5":
        return [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0]
    elif x=="t6":
        return [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0]
    else:
        return [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]


def flip(a):
    if(a=="0"):
        return "1"
    elif(a=="1"):
        return "0"
def Cmp2(a):
    t="0"+a
    s=''
    flag=0
    if(int(t)==0):
        r=0
    else:
        r=t.rindex("1")
    for i in range(len(t)-1,-1,-1):
        if(i>=r):
            s=t[i]+s
        else:
            s=flip(t[i])+s
    return s    
def DecToBin(a):
    st=""
    temp=a
    if(temp==0):
        return "0"
    while(temp!=0):
        st=st+str(temp%2)
        temp=temp//2
    st=st[::-1]
    return st
def imm(num,ty):
    if(ty in ["jalr","lw","addi","sltiu"]):
        num=int(num)
        Orig=num
        num=abs(num)
        t=DecToBin(num)
        p="1"+11*"0"
        if Orig<0 and t==p:
            return [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        if len(t)>=12:
            return [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
        if Orig<0 : 
            t=Cmp2(t)
        elif Orig>0 :
            t="0"+t
        size=len(t)
        y=12-size
        if t[0]=="0":
            t="0"*y+t
        elif(t[0]=="1"):
            t="1"*y+t
        return [int(t[0]),int(t[1]),int(t[2]),int(t[3]),int(t[4]),int(t[5]),int(t[6]),int(t[7]),int(t[8]),int(t[9]),int(t[10]),int(t[11]),0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif(ty in ["beq","bne","blt","bge","bltu","bgeu"]):
        num=int(num)
        Orig=num
        num=abs(num)
        t=DecToBin(num)
        p="1"+"0"*12
        if(Orig<0 and t==p):
            return [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        if(len(t)>=13):
            return [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
        if(Orig<0):
            t=Cmp2(t)
        elif(Orig>0):
            t="0"+t
        size=len(t)
        y=13-size
        if(t[0]=="0"):
            t=y*"0"+t
            t=t[0:13]
            y=t[0]+t[2:8]
            z=t[8:12]+t[1]
        elif(t[0]=="1"):
            t=y*"1"+t
            t=t[0:13]
            y=t[0]+t[2:8]
            z=t[8:12]+t[1]
        t=y+z
        return [int(t[0]),int(t[1]),int(t[2]),int(t[3]),int(t[4]),int(t[5]),int(t[6]),0,0,0,0,0,0,0,0,0,0,0,0,0,int(t[7]),int(t[8]),int(t[9]),int(t[10]),int(t[11]),0,0,0,0,0,0,0]
    elif(ty in ["lui","auipc"]):
        num=int(num)
        Orig=num;
        num=abs(num)
        t=DecToBin(num)
        p="1"+"0"*31
        if(Orig<0 and t==p):
            return [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        if(len(t)>=32):
            return [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
        if(Orig<0):
            t=Cmp2(t)
        elif(Orig>0):
            t="0"+t
        size=len(t)
        y=32-size
        if(t[0]=="0"):
            t=y*"0"+t
        else:
            t=y*"1"+t
        return [int(t[0]),int(t[1]),int(t[2]),int(t[3]),int(t[4]),int(t[5]),int(t[6]),int(t[7]),int(t[8]),int(t[9]),int(t[10]),int(t[11]),int(t[12]),int(t[13]),int(t[14]),int(t[15]),int(t[16]),int(t[17]),int(t[18]),int(t[19]),0,0,0,0,0,0,0,0,0,0,0,0]
    elif(ty in ["sw","sb","sh","sd"]):
        num=int(num)
        Orig=num
        num=abs(num)
        t=DecToBin(num)
        p="1"+"0"*11
        if(Orig<0 and t==p):
            return [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        if(len(t)>=12):
            return [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
        if(Orig<0):
            t=Cmp2(t)
        elif(Orig>0):
            t="0"+t
        size=len(t)
        y=12-size
        if(t[0]=="0"):
            t=y*"0"+t
        else:
            t=y*"1"+t
        return [int(t[0]),int(t[1]),int(t[2]),int(t[3]),int(t[4]),int(t[5]),int(t[6]),0,0,0,0,0,0,0,0,0,0,0,0,0,int(t[7]),int(t[8]),int(t[9]),int(t[10]),int(t[11]),0,0,0,0,0,0,0]
    elif(ty in ["jal"]):
        num=int(num)
        Orig=num
        num=abs(num)
        t=DecToBin(num)
        p="1"+21*"0"
        if(Orig<0 and t==p):
            return [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        if(len(t)>=21):
            return [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
        if(Orig<0):
            t=Cmp2(t)
        elif(Orig>0):
            t="0"+t
        size=len(t)
        y=21-size
        if(t[0]=="0"):
            t=y*"0"+t
        else:
            t=y*"1"+t
        t=t[0:21];
        t=t[0]+t[10:20]+t[9]+t[1:9]
        return [int(t[0]),int(t[1]),int(t[2]),int(t[3]),int(t[4]),int(t[5]),int(t[6]),int(t[7]),int(t[8]),int(t[9]),int(t[10]),int(t[11]),int(t[12]),int(t[13]),int(t[14]),int(t[15]),int(t[16]),int(t[17]),int(t[18]),int(t[19]),0,0,0,0,0,0,0,0,0,0,0,0]     
    else:
        return[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

fname='C:\\Users\\ishit\\c,c++ dsa course\\ascode.txt'
a=open(fname,'+a')
teller=a.tell()
a.close()
a=open(fname,'+r')
assembly=[]
while (True):
    k=a.readline().strip('\n').lstrip()
    if a.tell()==teller:
        assembly.append([k.split(" ")[0]]+ k.split(" ")[1].split(","))
        break
    if k.strip(' ')=='':
        continue 
    else: 
        if "(" in k and ")" in k:
            k=[k.split(" ")[0]]+ k.split(" ")[1].split(",")
            t=k[len(k)-1]
            t=t.replace("("," ")
            t=t.replace(")"," ")
            t=t.split()
            k=k[:len(k)-1] + [t[1]] + [t[0]]
        elif ":" in k:
            k=k.split(" ")[0:2]+ k.split(" ")[2].split(",")
        else:
            k=[k.split(" ")[0]]+ k.split(" ")[1].split(",")
        assembly.append(k)
a.close()
print(assembly)
assembly=the_ultimate_label_dealer_2point0(assembly)
print(assembly)
overwritebin()

count=0

while(count!=len(assembly)):
    inst=readinst(count)
    count+=1
    opco=opcode(inst[0])
    funct_3=funct3(inst[0])
    funct_7=funct7(inst[0])
    immediate=imm(inst[len(inst)-1],inst[0])
    bineq= np.array(opco) + np.array(funct_3) + np.array(funct_7) + np.array(immediate)
    print(inst)
    print(bineq)

    if ["beq","zero","zero","0"] not in assembly :
        writebin('Missing Virtual Halt',count)
        print('Missing Virtual Halt')
        break
    
    if inst[0] in ["add","sub","sll","slt","sltu","xor","srl","or","and"]:
        try:
            bineq=np.array(bineq)+np.array(rs1(inst[2])) + np.array(rs2(inst[3])) + np.array(rd(inst[1])) 
            writebin(bineq,count)
        except Exception:
            print('Invalid Instruction')
            break
    
    if inst[0] in ["addi","sltiu"]:
        try:
            bineq=np.array(bineq) + np.array(rs1(inst[2])) + np.array(rd(inst[1]))
            print(bineq)
            writebin(bineq,count)
        except Exception:
            print('Invalid Instruction')
            break

    if inst[0] in ["lw"]:
        try:
            bineq=np.array(bineq) + np.array(rs1(inst[2])) + np.array(rd(inst[1]))
            writebin(bineq,count)
        except Exception:
            print('Invalid Instruction')
            break
    
    if inst[0] in ["jalr"]:
        try:
            bineq=np.array(bineq)+np.array(rs1(inst[2])) + np.array(rd(inst[1]))
            writebin(bineq,count)
        except Exception:
            print('Invalid Instruction')
            break
    
    if inst[0] in ["sw","sb","sh","sd"]:
        try:
            bineq=np.array(bineq)+np.array(rs1(inst[2])) + np.array(rs2(inst[1])) 
            writebin(bineq,count)
        except Exception:
            print('Invalid Instruction')
            break

    if inst[0] in ["beq","bne","blt","bge","bltu","bgeu"] and inst!=['beq',"zero","zero","0"]:
        try:    
            bineq=np.array(bineq)+np.array(rs1(inst[1])) + np.array(rs2(inst[2])) 
            writebin(bineq,count)
        except Exception:
            print('Invalid Instruction')
            break
    
    if inst[0] in ["jal","lui","auipc"]:
        try:
            bineq=np.array(bineq) + np.array(rd(inst[1]))
            writebin(bineq,count)
        except Exception:
            print('Invalid Instruction')
            break

    if  inst==['beq',"zero","zero","0"]:
        try:
            bineq=np.array(bineq)+np.array(rs1(inst[1])) + np.array(rs2(inst[2]))
            writebin(bineq,count)
        except Exception:
            print('Invalid Instruction')
            break       
    
    elif inst==["beq","zero","zero","0"] and count!=(len(assembly)):
         writebin('Invalid Virtual Halt',count)
         break
    if -1 in bineq:
        print("Invalid Instruction")
        break