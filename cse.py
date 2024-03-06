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
        return("0010111")
    return "error"

x = input()
y = opcode(x)

print(y)