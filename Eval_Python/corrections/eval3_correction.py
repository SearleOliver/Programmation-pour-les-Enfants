## ── Fonctions utilitaires fournies (eval1) ────────────────────────
def ajouter(a, b):
    return a + b

def multiplier(a, b):
    return a * b
## ──────────────────────────────────────────────────────────────────

def somme_a(n):
    sum = 0
    for i in range(1,n+1):
        sum+=i
    return sum    
        
        
def somme_paire_a(n):
    sum = 0
    for i in range(1,n+1):
        if i%2==0:
            sum+=i
    return sum


def somme_liste(lst):
    sum = 0
    for e in lst:
        sum+=e
    return sum

def nombre_occurrences(lst, val):
    count = 0
    for e in lst:
        if e == val:
            count+=1
    return count

def max_liste(lst):
    max = lst[0]
    for e in lst:
        if e>max:
            max = e
    return max

def countdown(n):
    while (n>=0):
        print (n)
        n-=1

def somme_while(n):
    sum=0
    while (n>0):
        sum+=n
        n-=1
    return sum

def factorielle(n):
    fact=1
    while (n>0):
        fact*=n
        n-=1
    return fact

def fizzbuzz(n):
    result = []
    for i in range(1, n+1):
        div3 = i % 3 == 0
        div5 = i % 5 == 0
        if div3 and div5:
            result.append("FizzBuzz")
        elif div3:
            result.append("Fizz")
        elif div5:
            result.append("Buzz")
        else:
            result.append(i)
    return result