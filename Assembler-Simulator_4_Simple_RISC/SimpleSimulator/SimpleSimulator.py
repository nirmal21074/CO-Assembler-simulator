import matplotlib.pyplot as plt

reg = {

    '000': 0,

    '001': 0,

    '010': 0,

    '011': 0,

    '100': 0,

    '101': 0,

    '110': 0,

    '111':'0'*16

}

flags={'V':0,'G':0,'L':0,'E':0}

memadd={}

for i in range(256):

    memadd[i]="0"*16



def binarytodecimal(x):


    return int(x,2)



def decimaltobinary16(n):

    binary = bin(n).replace('0b', '')

    b = binary[::-1]

    while len(b) < 16:

        b = b + '0'

    binary = b[::-1]

    return binary



def decimaltobinary8(n):

    binary = bin(n).replace('0b', '')

    b = binary[::-1]

    while len(b) < 8:

        b = b + '0'

    binary = b[::-1]

    return binary



def overflow(x):

    global reg

    while x >= (256**2):

        x = x - (256**2)

        reg['111']='0'*12+'1000'

    return x



# from sys import stdout

#fileout=open("out.txt","w")



def printer(i):

    global reg

    global opcode

    global flags

    if opcode!="11110":

        reg['111']='0'*16

        for x in flags:

            flags[x]=0
    #print(i)
    # print(type(reg['000']))
    # print(type(reg['001']))
    # print(type(reg['010']))
    # print(type(reg['011']))
    # print(type(reg['100']))
    # print(type(reg['101']))
    # print(type(reg['110']))   
    ##print(reg)
    print(decimaltobinary8(i)+" "+decimaltobinary16(reg['000'])+" "+decimaltobinary16(reg['001'])+" "+decimaltobinary16(reg['010'])+" "+decimaltobinary16(reg['011'])+" "+decimaltobinary16(reg['100'])+" "+decimaltobinary16(reg['101'])+" "+decimaltobinary16(reg['110'])+" "+reg['111'])

    #fileout.write(decimaltobinary8(i)+" "+decimaltobinary16(reg['000'])+" "+decimaltobinary16(reg['001'])+" "+decimaltobinary16(reg['010'])+" "+decimaltobinary16(reg['011'])+" "+decimaltobinary16(reg['100'])+" "+decimaltobinary16(reg['101'])+" "+decimaltobinary16(reg['110'])+" "+reg['111']+"\n")



type_a = ['10000', '10001', '10110', '11010', '11011', '11100']

type_b = ['10010', '11000', '11001']

type_c = ['10011', '10111', '11101', '11110']

type_d = ['10100', '10101']

type_e = ['11111', '01100', '01101', '01111']

type_f = ["01010"]



stmts=[]

def sub_checker(x):

    global reg

    if x<0:

        reg['111']='0'*12+'1'+'0'*3

        x=0

    return x



# filein = open("bin.txt", "r")

# j=0

# for x in filein:

#     x=x.strip()

#     memadd[j]=x

#     stmts.append(x)

#     j+=1

j=0

while True:

    try:

        x=input()

        x=x.strip()

        memadd[j]=x

        stmts.append(x)

        j+=1

    except EOFError:

        break

x_coo = []

y_coo = []

count = 0

i=0

while i<len(stmts):


    # print(i)
    # print(count)
    # print(stmts[i])
    x_coo.append(count)
    
    count+=1
    
    y_coo.append(i)
    
    n=stmts[i]

    opcode=n[:5]

    if opcode in type_a:

        reg1 = n[7:10]

        reg2 = n[10:13]

        reg3 = n[13:]

        if opcode == "10000":

            reg[reg3] = overflow(reg[reg1] + reg[reg2])

            printer(i)

        elif opcode == "10001":

            reg[reg3] = sub_checker(reg[reg1] - reg[reg2])

            printer(i)

        elif opcode == "10110":

            reg[reg3] = overflow(reg[reg1] * reg[reg2])

            printer(i)

        elif opcode == "11010":

            reg[reg3] = reg[reg1] ^ reg[reg2]

            printer(i)

        elif opcode == "11011":

            reg[reg3] = reg[reg1] | reg[reg2]

            printer(i)

        elif opcode == "11100":

            reg[reg3] = reg[reg1] & reg[reg2]

            printer(i)

    elif opcode in type_b:

        reg1 = n[5:8]

        imm = binarytodecimal(n[8:])

        if opcode == "10010":

            reg[reg1] = imm

            printer(i)

        elif opcode == "11000":

            reg[reg1] = reg[reg1] << imm

            printer(i)

        elif opcode == "11001":

            reg[reg1] = reg[reg1] >> imm

            printer(i)

    elif opcode in type_c:

        r0 = "000"

        r1 = "001"

        reg1 = n[10:13]

        reg2 = n[13:]

        if opcode == "10011":

            reg[reg2] = reg[reg1]

            printer(i)

        elif opcode == "10111":

            reg[r0] = reg[reg1]//reg[reg2]

            reg[r1] = reg[reg1]%reg[reg2]

            printer(i)

        elif opcode == "11101":

            # reg[reg2]!=reg[reg1]
            lam=decimaltobinary16(int(reg[reg1], 2))
            lam=lam.replace("0","2")
            lam=lam.replace("1","0")
            lam=lam.replace("2","1")
            reg[reg[reg2]] = lam

            printer(i)

        elif opcode=="11110":

            cm=reg[reg2]-reg[reg1]

            if cm<0:

                reg['111']="0000000000000010"

                flags['G']=1
                flags['L']=0
                flags['E']=0
                flags['V']=0
                printer(i)
                
            elif cm>0:

                reg['111']="0000000000000100"
                flags['G']=0
                flags['L']=1
                flags['E']=0
                flags['V']=0
                printer(i)

            elif cm==0:

                reg['111']="0000000000000001"
                flags['G']=0
                flags['L']=0
                flags['E']=1
                flags['V']=0
                printer(i)

    elif opcode in type_d:

        reg1 = n[5:8]

        mem_d = binarytodecimal(n[8:])

        if opcode == "10100":

            reg[reg1] = binarytodecimal (memadd[mem_d])

            printer(i)

        elif opcode == "10101":

            memadd[mem_d] = decimaltobinary16( reg[reg1])

            printer(i)

    

    elif opcode in type_e:

        mem_e = binarytodecimal(n[8:])

        if opcode == "11111":

            i = mem_e
            #printer(i)

        elif opcode == "01100" and flags['L']==1:
                i=mem_e
                #printer(i)

        elif opcode =="01101" and flags['G']==1:

            # if flags['G']==1:

                i=mem_e
                #printer(i)

        elif opcode =="01111" and flags['E']==1:


                i=mem_e
                #printer(i)

        printer(i)

    elif opcode in type_f:

        printer(i)

        break

    i+=1

#print(memadd)

for i in range(256):

    # fileout.write(memadd[i]+"\n")

    print(memadd[i])

plt.scatter(x_coo, y_coo)
plt.show()
