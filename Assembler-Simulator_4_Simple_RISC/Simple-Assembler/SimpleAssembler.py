
opcode = {
      "add":'10000',
      "sub":'10001',
      "mov":'10010',
      "movr":"10011",
      "ld":'10100',
      "st":'10101',
      "mul":'10110',
      "div":'10111',
      "rs":'11000',
      "ls":'11001',
      "xor":'11010',
      "or":'11011',
      "and":'11100',
      "not":'11101',
      "cmp":'11110',
      "jmp":'11111',
      "jlt":'01100',
      "jgt":'01101',
      "je":'01111',
      "hlt":'01010'}


reg = {'R0':'000',
       'R1':'001',
       'R2':'010',
       'R3':'011',
       'R4':'100',
       'R5':'101',
       'R6':'110',
       'FLAGS':'111'}

reserved = ["add","sub","mul","div","jmp","jgt","jlt","je","cmp","ld","R0","R1","R2","R3","R4","R5","R6","FLAGS","var","st","not","xor","or","and","ls","rs","mov","hlt"]

#var_name = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_abcdefghijklmnopqrstuvwxyz"

var_mem = {}

output = []

def checkerror(x):
    def halt_present(x):
        if len(x)<256 and x[len(x)-1][0][0]!="hlt":
            print("Halt not present at last at line "+str(x[i][1]))
            exit()


    def halt_count(x):
        c=0
        l=[]
        for i in x.keys():
            if(x[i][0][0]=='hlt'):
                c+=1
                l.append(x[i][1])
        if(c>1):
            print("more than one hlt present at line number",end=" " )
            for a in l:
                print(a+" ",end="")
            exit()
        
    def variable_not_assigned(x):
        if x[0]!= "var":
            print("Variables not assigned.")

        else:
            print("Correct")

    reserved = ["add","sub","mul","div","jmp","jgt","jlt","je","cmp","ld","R0","R1","R2","R3","R4","R5","R6","FLAGS","var","st","not","xor","or","and","ls","rs","mov","hlt"]

    def typos(x):
        for i in x.keys():
            if x[i][0][0] not in reserved:
                print(x[i][0][0])
                print("Typographic error at line "+str(x[i][1]))
                exit()
    def label_var(x):
        st=['jgt','jlt','jmp','je']
        vt=['ld','st']
        for i in x.keys():
            if x[i][0][0] in st and x[i][0][1] not in label:
                print("undefined label")
                exit()
            elif x[i][0][0] in vt and x[i][0][2] not in var_store:
                print("undefined variable")
                exit()
            # elif x[0][1]!='FLAGS':
            #     print("Illegal memory address at line "+str(x[1]))
            #     exit()

    def reg_number(x):
        all_reg = ["R0","R1","R2","R3","R4","R5","R6"]
        for i in x.keys():
            if x[i][0][0] not in all_reg:
                print("Only registers allowed")
                exit()

    def reg_only(x):
        reserved = ["add","sub","mul","div","cmp","R0","R1","R2","R3","R4","R5","R6","not","xor","or","and","mov","hlt"]
        for i in x.keys():
            if x[i][0][0] not in reserved:
                print("Only registers are allowed h")
                exit()



    def checkA(x):
            if(len(x[0])!=4):
                print("wrong instruction at line"+str(x[1]))
                exit()
            elif(x[0][1]=="FLAGS"):
                print("Illegal use of flags at line "+str(x[1]))
                exit()
            elif(x[0][1] not in reg.keys() or x[0][2] not in reg.keys() or x[0][3] not in reg.keys() ):
                print("Typo in instruction at line "+str(x[1]))
                exit()
    def checkm(x):
        if len(x[0])!=3:
            print("Wrong Syntax a this line "+str(x[1]))
            exit()
        elif(x[0][2]=='FLAGS'):
            print("illegal use of flags "+str(x[1]))
            exit()
        elif(x[0][2][0:1]=='R'):
            if(x[0][2] not in reg.keys()):
                print("Invalid register name at line "+str(x[1]))
                exit()
        elif(x[0][2][0:1]=='$'):
            if (int(x[0][2][1:],10)<0 and int(x[0][2][1:],10)>255):
                print("Invalid immidiete in line "+str(x[1]))
                exit()
    def checkBlr(x):
        if(len(x[0]!=3)):
            print("Wrong Syntax at line "+str(x[1]))
            exit()
        elif(x[0][1]=='FLAGS' or x[0][2]=='FLAGS'):
            print("illegal use of flags register at line"+str(x[1]))
            exit()
        elif(x[0][1] not in reg.keys()):
            print(" Typographical error in line "+str(x[1]))
            exit()
    def checkD(x):
        if(len(x[0])!=3):
            print("wrong syntax at line "+str(x[1]))
            exit()
        elif x[0][1] not in reg.keys():
            print('typographical error at line '+str(x[1]))
            exit()
        elif x[0][0]=='ld' and x[0][1]=='FLAGS':
            print("Illegal use of flag register at line "+str(x[1]))
            exit()
        elif x[0][2] not in var_store.keys():
            print("Undefined variables at line "+str(x[1]))
            exit()
    def checkC(x):
        if len(x[0])!=3:
            print("Invalid syntax at line "+str(x[1]))
            exit()
        if x[0][0]=='not' and x[0][1]=='FLAGS':
            print("illegal use of flag register "+str(x[1]))
            exit()
        elif( x[0][2] not in reg.keys() or x[0][1] not in reg.keys()):
            print("typograhical error at line "+str(x[1]))
            exit()
    ta=['add','sub','mul','xor','or','and']
    tc=['div','not','cmp']
    tlr=['ls','rs']

    for i in x.keys():
        if(x[i][0][0] in ta):
            checkA(x[i])
        elif(x[i][0][0]=='ld' or x[i][0][0]=='st'):
            #print(x[i])
            checkD(x[i])
        elif(x[i][0][0]=='mov'):
            checkm(x[i])
        elif(x[i][0][0] in tc):
            checkC(x[i])
        elif(x[i][0][0] in tlr):
            checkBlr(x[i])
    
        


            


    halt_count(x)
    halt_present(x)
    label_var(x)
    typos(x)
    #reg_number(x)
    #reg_only(x)
        






def convert(t):
    binary = bin(t).replace('0b', '')
    b = binary[::-1]
    while len(b) < 8:
        b = b + '0'
    binary = b[::-1]
    return binary

def add(x):
    addd = "1000000"
    addd = addd + reg[x[1]]
    addd = addd + reg[x[2]]
    addd = addd + reg[x[3]]
    return addd

def sub(x):
    sb = "1000100"
    sb = sb + reg[x[1]]
    sb = sb + reg[x[2]]
    sb = sb + reg[x[3]]
    return sb

def move_imm(x):
    #print(x)
    mov = "10010"
    mov = mov+reg[x[1]]
    mov = mov+convert(int(x[2][1:]))
    return mov

def move_reg(x):
    pt = "1001100000"
    pt = pt+ reg[x[1]]
    pt = pt+ reg[x[2]]
    return pt

def load(x):
    ld = "10100"
    ld = ld + reg[x[1]]
    ld = ld + var_store[x[2]]
    return ld

def store1(x):
    st = "10101"
    st = st + reg[x[1]]
    st = st + var_store[x[2]]
    return st

def mul(x):
    m = "1011000"
    m = m + reg[x[1]]
    m = m + reg[x[2]]
    m = m + reg[x[3]]
    return m

def div(x):
    d = "1011100000"
    d = d + reg[x[1]]
    d= d + reg[x[2]]
    return d

def right_shift(x):
    rs = "11000"
    rs = rs + reg[x[1]]  
    rs = rs + convert(int(x[2][1:]))
    return rs

def left_shift(x):
    ls = "11001"
    ls = ls + reg[x[1]]
    ls = ls + convert(int(x[2][1:]))
    return ls

def xor(x):
    z = "1101000"
    z = z + reg[x[1]]
    z = z + reg[x[2]]
    z = z + reg[x[3]]
    return z

def or_op(x):
    s = "1101100"
    s = s + reg[x[1]]
    s = s + reg[x[2]]
    s = s + reg[x[3]]
    return s

def and_op(x):
    a = "1110000"
    a = a + reg[x[1]]
    a = a + reg[x[2]]
    a = a + reg[x[3]]
    return a

def not_op(x):
    n = "1110100000"
    n = n + reg[x[1]]
    n = n + reg[x[2]]
    return n

def compare(x):
    cp = "1111000000"
    cp = cp+ reg[x[1]]
    cp = cp + reg[x[2]]
    return cp

label = {}

# uncoditional jump
def jump_1(x):
    jp = "11111000"
    jp = jp + label[x[1]]
    return jp

def jump_ifless(x):
    jt = "01100000"
    jt = jt + label[x[1]]
    return jt

def jump_ifgreater(x):
    jg = "01101000"
    jg = jg + label[x[1]]
    return jg

def jump_ifequal(x):
    jq = "01111000"
    jq = jq + label[x[1]]
    return jq

def halt(x):
    return "0101000000000000"

def main(Input):
    if (Input[0][0] in opcode.keys()):
        if (Input[0][0] == "add"):
                output.append(add(Input[0]))
        elif (Input[0][0] == "sub"):
            output.append(sub(Input[0]))
        elif (Input[0][0] =='mov'):
            if (Input[0][2] in reg.keys()):
                output.append(move_reg(Input[0]))
            else:
                output.append(move_imm(Input[0]))
        elif (Input[0][0] == "ld"):
                output.append(load(Input[0]))
        elif (Input[0][0] == "st"):
                output.append(store1(Input[0]))
        elif (Input[0][0] == "mul"):
                output.append(mul(Input[0]))
        elif (Input[0][0] == "div"):
                output.append(div(Input[0]))
        elif (Input[0][0] == "rs"):
                output.append(right_shift(Input[0]))
        elif (Input[0][0] == "ls"):
                output.append(left_shift(Input[0]))
        elif (Input[0][0] == "xor"):
                output.append(xor(Input[0]))
        elif (Input[0][0] == "or"):
                output.append(or_op(Input[0]))
        elif (Input[0][0] == "and"):
                output.append(and_op(Input[0]))
        elif (Input[0][0] == "not"):
                output.append(not_op(Input[0]))
        elif (Input[0][0] == "cmp"):
                output.append(compare(Input[0]))
        elif (Input[0][0] == "jmp"):
                output.append(jump_1(Input[0]))
        elif (Input[0][0] == "jlt"):
                output.append(jump_ifless(Input[0]))
        elif (Input[0][0] == "jgt"):
                output.append(jump_ifgreater(Input[0]))
        elif (Input[0][0] == "je"):
                output.append(jump_ifequal(Input[0]))
        elif (Input[0][0] == "hlt"):
            output.append(halt(Input[0]))
    else:
        pass

count = 0
store = {}
while True:
    try:
        Input = input()
        Input = Input.strip()
        if (Input!= ""):
            if (Input.split()[0] != "hlt" and (len(Input.split()) == 1)):
                print("The instruction is not valid at line no." + str(count+1))
                exit()
            store[count] = [Input.split(), count]
            count = count + 1
    except EOFError:
        break

var_store = {}
# print(store)
for i in store.keys():
    if (store[i][0][0] == "var"):
        if (len(store[i][0]) == 1):
            print("The instruction is invalid at line no.:-" + str(store[i][1]))
            exit()
        # elif(store[i][0][1] in reserved):
        #     print("The Reserved words cannot be used as variable name at line no.:-" + str(store[i][1]))
        #     exit()
        # for j in store[i][0][1]:
        #     if(j not in var_name):
        #         print("The variable name is not valid at line no.:-" + str(store[i][1]))
        #         exit()
        var_store[store[i][0][1]] = 0
    elif (store[i][0][0][-1:] == ':'):
        if (store[i][0][0][:-1] in label):
            print("Both labels has same name hence invalid instruction at line no.:-" + str(store[i][1]))
            exit()
        # elif(store[i][0][0][:-1] in reserved):
        #     print("The Reserved words cannot be used as variable name at line no.:-" + str(store[i][1]))
        #     exit()
        # for j in store[i][0][0][:-1]:
        #     if(j not in var_name):
        #         print("The given instruction is not valid at line no.:-" + str(store[i][1]))
        #         exit()
        k = len(var_store)
        l = int(i)
        m = l-k
        label[store[i][0][0][:-1]] = convert(m)

        # to delete back the var as we don't want it
        del store[i][0][0]

j = 0
for i in var_store.keys():
    s = len(store)
    #v = len(var_name)
    v=len(var_store)
    f = s-v
    var_store[i] = convert(f + j)
    j = j+1

#check for errors
checkerror(store)



j = 0
a = len(var_store)
while ((a + j) in store.keys()):
    main(store[a + j])
    j = j + 1

for i in range(len(output)):
    print(output[i])
#print(len(output))

# filein=open("testcase.txt","rt")
# for s in filein:
#     str=""
#     for i in s:
        

