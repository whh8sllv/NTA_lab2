import time
import sympy


def brute_force_DL(a, b, m):
    for x in range(2, m):
        if (a ** x) % m == b:
            return x
        
def get_short_canonical_form(num):
    canonical_form = sympy.factorint(num)
    p_list = list(canonical_form.keys())
    l_list = list(canonical_form.values())
    return p_list, l_list

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
                if res in r_list:
                    ind = r_list.index(res)
                    coefs.append(j_list[ind])
                else:
                    coefs = [1, 1]

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

def solve_system(y, mod):
    product = 1
    for i in mod:
        product *= i
    x = 0
    for j in range(len(y)):
        sup = product // mod[j]
        add = y[j] * sup * get_inverse(sup, mod[j])
        x += add
    return (x % product)


def main_SPH(alpha, beta, n):
    p_list, l_list = get_short_canonical_form(n)
    tabs = create_table(p_list, alpha, n)
    x = find_x_i(alpha, beta, p_list, l_list, n, tabs)
    y, mod = get_equations_system(x)
    res = solve_system(y, mod)
    return res

def time_check_brute_force(data):
    avg_time = []
    for i in data:
        alpha = i[0]
        beta = i[1]
        module = i[2]
        start = time.time()
        res = brute_force_DL(alpha, beta, module)
        alpha = 0
        beta = 0
        module = 0
        n = 0
        end = time.time()
        final_time = end - start
        avg_time.append(final_time)
    return (sum(avg_time) / len(avg_time))

alpha = int(input('alpha = '))
beta = int(input('beta = '))
module = int(input('module = '))
n = module-1

print()
dl1 = main_SPH(alpha, beta, n)
print(f'SPH: x = {dl1}')

# dl2 = brute_force_DL(alpha, beta, module)
# print(f'Brute Force: x = {dl2}')

# type 1, p = 2
test_data1_2 = [[15, 38, 47], [33, 9, 37], [8, 18, 41], [9, 9, 41], [56, 11, 97]]

# type 1, p = 3
test_data_1_3 = [[135, 340, 673], [798, 165, 911], [121, 79, 397], [258, 255, 409], [179, 644, 947]]

# type 1, p = 4
test_data_1_4 = [[7274, 7009, 9323], [3677, 4075, 4831], [1560, 1288, 4201], [551, 4063, 5237], [2909, 2480, 3163]]

# type 1, p = 5
test_data_1_5 = [[18077, 24936, 32561], [43376, 33221, 47881], [97910, 4172, 98809], [758, 12714, 20759], [4724, 3507, 21701]]

# type 1, p = 6
test_data_1_6 = [[581615, 22175, 676523], [110408, 331390, 523297], [65498, 63231, 225829], [169985, 502035, 917353], [244104, 62378, 307511]]

# type 1, p = 7
test_data_1_7 = [[8853595, 2370269, 9720521], [2070250, 930817, 8549773], [4129808, 964455, 4632403], [965027, 1983753, 2217349], [464951, 648646, 2888953]]

# type 2, p = 2
test_data_2_2 = [[8, 30, 83], [56, 27, 83], [48, 68, 83], [55, 73, 83], [35, 24, 83]]

# type 2, p = 3
test_data_2_3 = [[306, 187, 797], [130, 535, 557], [104, 137, 719], [592, 573, 719], [211, 443, 787]]

# type 2, p = 4
test_data_2_4 = [[4558, 1142, 5879], [3779, 2726, 3989], [4376, 4000, 6173], [2786, 2129, 3517], [549, 1347, 4283]]

# type 2, p = 5
test_data_2_5 = [[7031, 905, 27143], [31731, 76912, 95153], [25753, 43213, 56779], [56917, 36311, 98221], [59589, 39777, 89963]]

# type 2, p = 6
test_data_2_6 = [[176134, 245987, 271163], [153637, 67760, 161831], [663895, 823297, 880661], [81442, 74067, 348709], [170827, 236218, 708457]]

# res = time_check_brute_force(test_data_1_3)
# print(res)

# start = time.time()
# res = main_SPH(348, 621, 990)
# print(res)
# end = time.time()
# final = end - start
# print(final)
