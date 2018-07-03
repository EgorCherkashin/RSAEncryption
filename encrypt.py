import random


# ------------

def textconvert(message):
    output = []
    for character in message:
        number = ord(character)
        output.append(number)
    return (output)


def letter_encrypt(mess):
    p = 7  # Prime Number 1
    q = 19  # Prime Number 2
    n = p * q
    f = (p - 1) * (q - 1)
    print(f)
    e, d = random_onefactor()
    print("e: ", e, "\nd: ", d)
    m = textconvert(mess)
    final = []
    for x in m:
        encry = x ^ e
        c = encry % n
        final.append(c)
    return (final)


def encrypt(pk, message):
    print("Encrypting...")
    key, n = pk
    # cipher = [(ord(char) ** key) % n for char in message]
    l = []
    for x in message:
        m = ord(x) ** key
        out = m % n
        l.append(out)
    return l


def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in xrange(3, int(num ** 0.5) + 2, 2):
        if num % n == 0:
            return False
    return True


def generate_keypair(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randrange(1, phi)

    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    d = multiplicative_inverse(e, phi)
    return ((e, n), (d, n))


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def multiplicative_inverse(a, b):
    x = 0
    y = 1
    lx = 1
    ly = 0
    oa = a
    ob = b
    while b != 0:
        q = a // b
        (a, b) = (b, a % b)
        (x, lx) = ((lx - (q * x)), x)
        (y, ly) = ((ly - (q * y)), y)
    if lx < 0:
        lx += ob
    if ly < 0:
        ly += oa

    return lx


def conv(mess):
    l = []
    for x in mess:
        m = chr(x)
        l.append(m)
    return (l)


primes = [109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229,
          233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359,
          367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491,
          499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641,
          643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787,
          797]

prime1 = random.choice(primes)
prime2 = 0
while prime2 == 0:
    choice = random.choice(primes)
    if choice > prime1:
        prime2 = choice
    else:
        pass
public, private = generate_keypair(prime2, prime1)

if __name__ == '__main__':
    msg = encrypt(private, "Hello!")
    print(msg)
    print("".join(conv(msg)))
    print("Private key: ", public)
