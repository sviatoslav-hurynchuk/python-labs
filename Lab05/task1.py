def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes(n, output_format):
    result = []
    for num in range(0, n):
        if is_prime(num):
            result.append(num)

    match output_format:
        case 'list':
            print(result)
        case 'column':
            for num in result:
                print(num)
        case 'count':
            print(len(result))
find_primes(10, 'list')
print('----')
find_primes(10, 'column')
print('----')
find_primes(10, 'count')