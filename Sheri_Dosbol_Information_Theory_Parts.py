from termcolor import colored # to make the console colorful. does not affect to parts
import random # library which help to work with random. Used in part 5


# to create and enter text in a file
def file_text():
    Text = input('Input some text: ')

    file = open("Text.txt", "w")
    file.write(Text)
    print('\n')


# this function solve probability. we just created this function to avoid writing the same code multiple times
def pprobability(variant, text):
    print('count: %i' % variant)
    all_len = len(text)
    print('All length = ' + str(all_len))
    probability = float(variant / all_len)
    return str(probability)


# Part 1: Calculate probabilities
def calculate():
    try:    #ordinnary try-except which open a file
        rt = open('Text.txt').read()
        rt
    except IOError:
        print('File %s not found. First you need to create a file!' % colored('Text.txt', 'red'))
        print('\n')
    while True:
        print(colored('[1]. Calculate all UPPERCASE letters', 'green'))
        print(colored('[2]. Calculate all lowercase letters', 'green'))
        print(colored('[3]. Calculate all numbers letters', 'green'))
        print(colored('[4]. Calculate all punctuations', 'green'))
        print(colored('[5]. Calculate all ' ' letters', 'green'))
        print(colored('[6]. Calculate one character', 'green'))
        print(colored('[0]. Exit', 'green'))
        x = int(input(colored('Choose one: ', 'blue')))

        if x == 1:  # Calculate Probability for all UPPERCASE letters
            ch_count = 0
            for u in rt:
                if u.isupper(): #
                    ch_count += 1
            print('P(UPPERCASE) = ' + pprobability(ch_count, rt) )


        elif x == 2:    # Calculate Probability for all lowercase letters
            ch_count = 0
            for l in rt:
                if l.islower():
                    ch_count += 1

            print('P(lower) = ' + pprobability(ch_count, rt))


        elif x == 3:    # Calculate Probability for all numbers letters
            ch_count = 0
            for n in rt:
                if n.isnumeric():
                    ch_count += 1

            print('P(numeric) = ' + pprobability(ch_count, rt))


        elif x == 4:    # Calculate Probability for all punctuations letters
            punctuation_and_simbols = ['.', ',', '!','@','#','$','%','^','&','*','(',')','_','+','/','*','?','>','<','~','`','"',"'",':',';','{','}','[',']']
            ch_count = 0
            for p in rt:
                for pas in punctuation_and_simbols:
                    if p in pas:
                        ch_count += 1

            print('P(punctuation marks) = ' + pprobability(ch_count, rt) )


        elif x == 5:    # Calculate Probability for all ' '(space) letters
            ch_count = 0
            for p in rt:
                if p.isspace():
                    ch_count += 1

            print('P(space) = ' + pprobability(ch_count, rt) )


        elif x == 6:    # Calculate Probability for all one character letters
            character = input('Enter character: ').lower()
            ch_count = rt.lower().count(character)

            print('P(%s) = ' %character + pprobability(ch_count, rt))

        elif x == 0:
            break
        else:
            print('You made wrong choice. Select one of the option! ')


# Part 2 : algorithm Shannon-Fano
def ShF():
    try:    #ordinnary try-except which open a file
        sf = open('Text.txt').read().lower()
        sf
    except IOError:
        print('File %s not found. First you need to create a file!' % colored('Text.txt', 'red'))
        print('\n')

    all_len = len(sf)
    proba ={}

    for s in sf: # Calculate Probability all characters
        v="%.3f"%(sf.count(s)/all_len)
        proba[s]=float(v)

    proba_values = sorted(proba.values(), reverse=True) # Sorted all probabilities in descending order
    sort_by_value = {}

    for i in proba_values:
        for k in proba.keys():
            if proba[k] == i:
                sort_by_value[k]=proba[k] # fill in dict sort_by_value

    print(sort_by_value)
    f_keys = list(sort_by_value.keys()) # create a new list which have all keys
    f_values = list(sort_by_value.values()) # create a new list which have all values

    s_values = []
    y=0
    s_len = len(f_values)

    #Shannon-Fano algorithm
    for x in range(s_len):
        if y == x:
            if x == s_len-1:
                val = '0' * y
            else:
                val='0'*y + '1'
            s_values.append(val) # fill in s_values. val is 1 or 0
        y +=1

    Shannon ={}

    for s in range(s_len):
        Shannon[f_keys[s]]=s_values[s] # fill in dict Shannon, take the key from f_keys list , take the value from s_values
    print('Result of Shannon-Fano algorithm: ')
    print(Shannon)

    word =''
    for s in sf:
        for x in Shannon.keys():
            if s == x:
                word+=Shannon[x]

    print(word)

# save on file
    with open('Text2.txt','w') as chiper:
        chiper.write(word +'\n') # first paragraph is cipher code
        for key,val in Shannon.items():
            chiper.write('{}:{}\n'.format(key,val)) # 2 and next paragraphs is key and val

    print('\n')


# Part 3: Decoding Shannon-Fano
def ShF_decode(cipher=''): # this function work with attribute and without attribute
    try:    #ordinnary try-except which open a file
        d = {}
        x=0
        with open('Text2.txt') as sf:
            for i in sf.readlines():
                if x == 0: # take first paragraph for cipher
                    if cipher=='':
                        cipher=i.strip()
                else: # take key and value from next parahgraphs
                    key, val = i.strip('\n').split(':') # remove \n - sign of new paragraph , then split :
                    d[key] = val # before : are keys, after : are values
                x+=1 # use for iterate paragraphs

    except IOError:
        print('File %s not found. First you need to create a file!' % colored('Text2.txt', 'red'))
        print('\n')


    print(d)
    print(cipher)


    word =''
    code=''
    for w in cipher: # this cycle decoded Shannon
        code+=w # after each check, a new cipher element is added
        for q in d.keys():
            if code==d[q]: # check key
                word+=q
                code=''

    print(word)


# Part 4: Hamming algorithm
def Hamming():
    try:    #ordinnary try-except which open a file
        cipher =''
        with open('Text2.txt') as sf:
            for i in sf.readlines():
                cipher=i.strip() #take a resoult of Part 2
                break

    except IOError:
        print('File %s not found. First you need to create a file!' % colored('Text2.txt', 'red'))
        print('\n')

# if the length of the cipher is not divisible by 4 without remainder, then the required number of 0s is added to the end of the cipher
    if len(cipher)%4!=0:
        n=4-len(cipher)%4
        for i in range(n):
            cipher+='0'

    code=''
    x=0

    # here we separate every 4 elements of the cipher with ' '(space)
    for c in cipher:
        if x%4==0 and x>0:
           code+=' '
        code += c
        x+=1

    print(code)

    z=1
    blocks=[]
    n=1

    # in this cycle we convert 4 digit code to (4,7) Hamming code
    for h in code:
        if h==' ':
            z=0
        else:
            if z==4:
                i1=int(code[n-4])
                i2=int(code[n-3])
                i3=int(code[n-2])
                i4=int(code[n-1])
                # find r1, r2, r3 bits
                r1=str(i1 ^ i2 ^ i3)
                r2=str(i2 ^ i3 ^ i4)
                r3=str(i1 ^ i2 ^ i4)
                # Hamming (4,7) block
                block=str(i1)+str(i2)+str(i3)+str(i4)+r1+r2+r3
                print(block)
                blocks.append(block) # collect all block to one code
        z+=1
        n+=1

    print(blocks)
    return blocks


# Part 5: Hamming error
def error_Hamming():
    blocks = Hamming()
    error_blocks=[]

    print('******************************************')

    # in this cycle we add one artificial error
    for a in blocks:
        i = random.randint(0,7) # define random bit
        v=0
        e_block = ''
        # here we change our randomly selected bit to an error value
        for b in a:
            if v == i:
                if b =='0':
                    b ='1'
                else:
                    b='0'
            v += 1
            e_block+=b
        error_blocks.append(e_block)
        continue

    print(error_blocks)
    return error_blocks


# Part 6: decoding Hamming code
def decode_Hamming():
    # dictionary with Error syndrom and error bit
    decoding_table={'000':'No error', '001':'r3', '010':'r2', '011':'i4', '100':'r1', '101':'i1', '110':'i3', '111':'i2'}
    blocks=error_Hamming()
    correct_block=[]
    cr_block={}
    for block in blocks:
        cr_block['i1'] = int(block[0])
        cr_block['i2'] = int(block[1])
        cr_block['i3'] = int(block[2])
        cr_block['i4'] = int(block[3])
        cr_block['r1'] = int(block[4])
        cr_block['r2'] = int(block[5])
        cr_block['r3'] = int(block[6])
        s1=cr_block['r1'] ^ cr_block['i1'] ^ cr_block['i2'] ^ cr_block['i3']
        s2=cr_block['r2'] ^ cr_block['i2'] ^ cr_block['i3'] ^ cr_block['i4']
        s3=cr_block['r3'] ^ cr_block['i1'] ^ cr_block['i2'] ^ cr_block['i4']
        s=str(s1)+str(s2)+str(s3) # error syndrom
        print('For {0} block Error bit is {1} '.format(block, decoding_table[s]))

        # in this cycle we find error bit and fix it
        for cb in cr_block.keys():
            if decoding_table[s]==cb:
                if cr_block[cb]==0:
                    cr_block[cb]=1
                else:
                    cr_block[cb]=0

        # correct block
        c_block=str(cr_block['i1'])+str(cr_block['i2'])+str(cr_block['i3'])+str(cr_block['i4'])+str(cr_block['r1'])+str(cr_block['r2'])+str(cr_block['r3'])
        correct_block.append(c_block)
    print(correct_block)

    code=''
    # here, just deleted the last 3 bits for each block. We did this in order to get 4-digit Shannon-Fano blocks
    for cb in correct_block:
        z=0
        for c in cb:
            if z<4:
                code+=c
            z+=1

    print(code)
    # sent this code to the Shannon-Fano decoder
    ShF_decode(code)


# a regular menu based on prints and conditions
while True:
    print(colored('[1]. Create File or Edit Text','green'))
    print(colored('[2]. *Part 1* Calculate','green'))
    print(colored('[3]. *Part 2* Shannon-Fano encoding','green'))
    print(colored('[4]. *Part 3* Shannon-Fano decoding','green'))
    print(colored('[5]. *Part 4* Hamming','green'))
    print(colored('[6]. *Part 5* Hamming error','green'))
    print(colored('[7]. *Part 6* Hamming decode','green'))
    print(colored('[0]. Exit','green'))
    x = int(input(colored('Choose one: ','blue')))
    if x == 1:
        file_text()
    elif x == 2:
        calculate()
    elif x == 3:
        ShF()
    elif x == 4:
        ShF_decode()
    elif x == 5:
        Hamming()
    elif x == 6:
        error_Hamming()
    elif x == 7:
        decode_Hamming()
    elif x == 0:
        break
    else:
        print ('You made wrong choice. Select one of the option! ')







