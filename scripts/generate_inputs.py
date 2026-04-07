import random

alphabet = ['a','b','c']

def gen_file(name, n=25):
    values = {c: random.randint(1,10) for c in alphabet}
    A = ''.join(random.choice(alphabet) for _ in range(n))
    B = ''.join(random.choice(alphabet) for _ in range(n))

    with open(name, 'w') as f:
        f.write(str(len(alphabet)) + "\n")
        for c in alphabet:
            f.write(f"{c} {values[c]}\n")
        f.write(A + "\n")
        f.write(B + "\n")

for i in range(1,11):
    gen_file(f"input{i}.in")
