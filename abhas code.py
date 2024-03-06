def opcode(x):
    R_type = ["add","sub","sll","slt","sltu","xor","srl","or","and"]
    I_type1 = ["lw"]
    I_type2 = ["addi","sltiu"]
    I_type3= ["jalr"]
    S_type = ["sw"]
    B_type = ["beq","bne","blt","bge","bltu","bgeu"]
    U_type1 = ["lui"]
    U_type2 = ["auipc"]
    J_type = ["jal"]
    
    if x in R_type:
        return("0110011")
    if x in I_type1:
        return("0000011")
    if x in I_type2:
        return("0010011")
    if x in I_type3:
        return("1100111")
    if x in S_type:
        return("0100011")
    if x in B_type:
        return("1100011")
    if x in U_type1:
        return("0110111")
    if x in U_type2:
        return("0010111")
    if x in J_type:
        return("1101111")
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
    if x in lx1:
        return "001"
    if x in lx2:
        return "010"
    if x in lx3:
        return "011"
    if x in lx4:
        return "100"
    if x in lx5:
        return "101"
    if x in lx6:
        return "110"
    if x in lx7:
        return "111"
    if x in null:
        return ""
    return "error"
def funct7(x):
    lx0 = ["add","sll","slt","sltu","xor","srl","or","and"]
    lx1 = ["sub"]
    null = ["lw","addi","sltiu","jalr","sw","beq","bne","blt","bge","bltu","bgeu","lui","auipc","jal"]
    if x in lx0:
        return "0000000"
    if x in lx1:
        return "0100000"
    if x in null:
        return ""
    return "error"
x = input()
opcodebin = opcode(x)
funct3bin = funct3(x)
funct7bin = funct7(x)
print(opcodebin,funct3bin,funct7bin)