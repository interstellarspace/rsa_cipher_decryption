###############################Extended_Eucledian_Alg
def Extended_Eucledian_Alg(num, mod):
    qi_list = list()
    remainder_list = list()
    #i_list = list()
    gcd_for_inverse(num, mod, qi_list, remainder_list)
    #print(qi_list)
    #print(remainder_list)
    inv = calculate_inverse(qi_list)
    if inv < 0:
        inv = inv % mod
    if remainder_list[len(remainder_list)-2] == 1.0:
        return inv
    else:
        #print("Error: num '%' mod " + str(mod) + " has not multiplicative inverse")
        return( str(num) + " mod " + str(mod) + " has no multiplicative inverse.")
    
def gcd_for_inverse(a,b, qi_list, remainder_list):
    if b == 0:
        return a
    else:
        qi_list.append(math.trunc(a / b))
        remainder_list.append(a % b)
        return gcd_for_inverse(b, a % b, qi_list, remainder_list)

def calculate_inverse(qi_list):
    xjold = 0
    xjnew = 1
    #print(qi_list)
    for x in range(1,len(qi_list)-1):
        inv = xjold - (qi_list[x] * xjnew)
        xjold = xjnew
        xjnew = inv
    return inv

def print_array(array):
    for x in cipher:
        for w in x:
            sys.stdout.write(str(w) + "\t")
        sys.stdout.write("\n")

def gcd(x,y):
    if(y==0):
        return x
    else:
        return gcd(y,x%y)

def gen_primes(n):
    plist = list()
    for x in range(2,n):
        prime = True
        for y in range(2,x):
            if(gcd(x,y)!=1):
                prime = False
                break
        if(prime):
            plist.append(x)
    return plist


def prime_factorization(n):
    i = 2
    p_list = gen_primes(n)
    
    for x in p_list:
        if(n % x == 0):
            y = n / x
            try:
                p_list.index(y)
                return [x,y]
            except ValueError:
                break
    return [0,0]

def calc_plaintext(cipher,private_key, n, plain):
    for i in cipher:
        row = list()
        for j in i:
            row.append(int((j**private_key) % n))
        plain.append(row)
    
def convert_to_letters(plaintext):
    alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    s = ""
    
    for x in range(0,26):
        for y in range(0,26):
            for z in range(0,26):
                if(676*x+26*y+z == plaintext):
                    return alpha[x] + alpha[y] + alpha[z]
    raise NameError("Cannot invert the process: " + str(plaintext))

def convert_ciphers(plaintext):
    s = ""
    
    for x in plaintext:
        for y in x:
            s = s + convert_to_letters(y)
        s = s + "\n"
    
    return s
    
def decrypt_rsa(n,b):
    #Calculate factors of n
    x = prime_factorization(n)
    print("Prime factor: " + str(x))
    
    #Compute using totient function
    tot = (x[0]-1)*(x[1]-1)
    print("Totient: " + str(tot))
    
    #Private key
    private_key = Extended_Eucledian_Alg(b, tot)
    print("Private key: " + str(private_key))
    
    plain = list()
    calc_plaintext(cipher, private_key, n, plain)
    
    decryption = convert_ciphers(plain)
    print("\nDecryption:\n" + decryption)

cipher = ([12423,11524,7243,7459,14303,6127,10964,16399]
         ,[9792,13629,14407,18817,18830,13556,3159,16647]
         ,[5300,13951,81,8986,8007,13167,10022,17213]
         ,[2264,961,17459,4101,2999,14569,17183,15827]
         ,[12693,9553,18194,3830,2664,13998,12501,18873]
         ,[12161,13071,16900,7233,8270,17086,9792,14266]
         ,[13236,5300,13951,8850,12129,6091,18110,3332]
         ,[15061,12347,7817,7946,11675,13924,13892,18031]
         ,[2620,6276,8500,201,8850,11178,16477,10161]
         ,[3533,13842,7537,12259,18110,44,2364,15570]
         ,[3460,9886,8687,4481,11231,7547,11383,17910]
         ,[12867,13203,5102,4742,5053,15407,2976,9330]
         ,[12192,56,2471,15334,841,13995,17592,13297]
         ,[2430,9741,11675,424,6686,738,13874,8168]
         ,[7913,6246,14301,1144,9056,15967,7328,13203]
         ,[796,195,9872,16979,15404,14130,9105,2001]
         ,[9792,14251,1498,11296,1105,4502,16979,1105]
         ,[56,4118,11302,5988,3363,15827,6928,4191]
         ,[4277,10617,874,13211,11821,3090,18110,44]
         ,[2364,15570,3460,9886,9988,3798,1158,9872]
         ,[16979,15404,6127,9872,3652,14838,7437,2540]
         ,[1367,2512,14407,5053,1521,297,10935,17137]
         ,[2186,9433,13293,7555,13618,13000,6490,5310]
         ,[18676,4782,11374,446,4165,11634,3846,14611]
         ,[2364,6789,11634,4493,4063,4576,17955,7965]
         ,[11748,14616,11453,17666,925,56,4118,18031]
         ,[9522,14838,7437,3880,11476,8305,5102,2999]
         ,[18628,14326,9175,9061,650,18110,8720,15404]
         ,[2951,722,15334,841,15610,2443,11056,2186])

n = 18923
b = 1261
decrypt_rsa(n,b)