
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
            return -1;
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
            return -1;
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
            return -1;
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
            return -1;
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
            return -1;
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
    
        
        
        
            
        
while True:
    o=input("enter the opcode");
    c=input("enter the immediate");
    y=imm(c,o);
    if(type(y)==str):
        print(y);
    elif(type(y)==tuple):
        print(y[0],y[1]);
    elif(type(y)==int):
        print("Error")
    print("Do you want to continue(y/n)");
    ch=input("enter the choice");
    if(ch=="n" or ch=="N"):
        break;
    
    
        
