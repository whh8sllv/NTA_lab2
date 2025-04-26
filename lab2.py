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



# alpha = int(input('alpha = '))
# beta = int(input('beta = '))
module = int(input('module = '))

# brute_force_res = brute_force_DL(alpha, beta, module)
# print()
# print(f'x = {brute_force_res}')
# print(f'{alpha}^{brute_force_res} = {beta} (mod {module})')

module_can = get_canonical_form(module)
print(f'{module} = {module_can}')

module_can_short = get_short_canonical_form(module_can)
print(f'Short form: {module} = {module_can_short}')


