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
    














alpha = int(input('alpha = '))
beta = int(input('beta = '))
module = int(input('module = '))

brute_force_res = brute_force_DL(alpha, beta, module)
print()
print(f'x = {brute_force_res}')
print(f'{alpha}^{brute_force_res} = {beta} (mod {module})')

module_can = get_canonical_form(module-1)
print(module_can)