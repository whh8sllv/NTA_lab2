def brute_force_DL(a, b, m):
    for x in range(2, m):
        if (a ** x) % m == b:
            return x
        
res = []
def get_canonical_form(num):
    if num == 1:
        return res
    for i in range(2, num+1):
        if num % i == 0:
            num = int(num/i)
            res.append(i)
            return get_canonical_form(num)

def get_short_canonical_form(arr):
    p = []
    l = []
    for i in arr:
        if i not in p:
            p.append(i)
            l.append(arr.count(i))
    return p, l

def extended_EA(a, b):
    u0, u1 = 1, 0
    v0, v1 = 0, 1
    r = a % b
    q = a // b
    while r != 0:
        u0, u1 = u1, (u0 - q * u1)
        v0, v1 = v1, (v0 - q * v1)
        a = b
        b = r
        r = a % b
        q = a // b
    return (b, u1, v1)

def get_inverse(a, mod):
    inverse_element = extended_EA(a, mod)[1] % mod
    return inverse_element

def create_table(p_list, alpha, n):
    table = {}
    for p_i in p_list:
        j_index = []
        r = []
        for j in range(0, p_i):
            r_j = (alpha ** ((n * j) // p_i)) % (n+1)
            j_index.append(j)
            r.append(r_j)
        table[p_i] = (j_index, r)
    return table


def find_x_i(alpha, beta, p_list, l_list, n, table):
    xi_dict = {}
    inverse_elemet = get_inverse(alpha, n+1)
    for i in range(len(p_list)):
        coefs = []
        j_list, r_list = table[p_list[i]]
        for _ in range(l_list[i]):
            if _ == 0:
                res = (beta ** (n//p_list[i])) % (n+1)
                ind = r_list.index(res)
                coefs.append(j_list[ind])
            else:
                alpha_pow = 0
                for m, k in enumerate(coefs):
                    alpha_pow += ((p_list[i] ** m ) * k)
                main_power = n // (p_list[i] ** (_ + 1))
                res = ((beta * (inverse_elemet ** alpha_pow)) ** main_power) % (n+1)
                ind = r_list.index(res)
                coefs.append(j_list[ind])
        xi_dict[p_list[i]] = coefs
    return xi_dict


def get_equations_system(coefs_dict):
    y = []
    mod = []
    p_list = [i for i in coefs_dict.keys()]
    coef_list = [i for i in coefs_dict.values()]
    for i in range(len(coef_list)):
        y_i = 0
        for m, j in enumerate(coef_list[i]):
            y_i += j * (p_list[i] ** m)
        module = p_list[i] ** len(coef_list[i])
        y_new = y_i % module
        y.append(y_new)
        mod.append(module)
    return y, mod


    
    


    


alpha = int(input('alpha = '))
beta = int(input('beta = '))
module = int(input('module = '))
n = module-1

# step 1: get canonical form of (module-1)

can_form = get_canonical_form(n)

p_list, l_list = get_short_canonical_form(can_form)

# step 2: tables for p_i

tabs = create_table(p_list, alpha, n)

#print(tabs)

# x

x = find_x_i(alpha, beta, p_list, l_list, n, tabs)

print(get_equations_system(x))

