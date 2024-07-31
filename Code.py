import random

m = [1, 6, 6, 1]
a = [3, 4, 6, 7]

def combine(w1, w2):
    p = w1 / (w1 + w2)
    if random.random() < p:
        return 1
    else:
        return 2

def choose_best_warrior(army):
    s = -1
    i = -1
    for j in range(len(army)):
        if s < army[j]:
            s = army[j]
            i = j
    return [s, i]

w = 0
n = 10000
for _ in range(n):
    r = m.copy()
    s = a.copy()
    while r and s:
        w1 = choose_best_warrior(r)[0]
        i_a = random.randint(0, len(s) - 1)
        w2 = s[i_a]
        wi = combine(w1, w2)
        if wi == 1:
            s.remove(w2)
            r[choose_best_warrior(r)[1]] += w2
        else:
            r.remove(w1)
            s[i_a] += w1
    if r:
        w += 1

p = w / n
print("PART 1:   ")
print("Probability of winning the tournament:", p)

import random

m = [1, 6, 6, 1]
a = [3, 4, 6, 7]

def combine(w1, w2):
    p = w1 / (w1 + w2)
    if random.random() < p:
        return 1
    else:
        return 2

def choose_best_warrior(army):
    min_str = 100000
    idx = -1
    for i in range(len(army)):
        if min_str > army[i]:
            min_str = army[i]
            idx = i
    return [min_str, idx]

w = 0
n = 10000
for _ in range(n):
    r = m.copy()
    s = a.copy()
    while r and s:
        w1 = choose_best_warrior(r)[0]
        i_a = random.randint(0, len(s) - 1)
        w2 = s[i_a]
        wi = combine(w1, w2)
        if wi == 1:
            s.remove(w2)
            r[choose_best_warrior(r)[1]] += w2
        else:
            r.remove(w1)
            s[i_a] += w1
    if r:
        w += 1

p = w / n
print("PART 2:   ")
print("Probability of winning the tournament:", p)

print("PART 3:   ")
print("TotalStrength = IntialStrength+ (Sum of gains in all battles)")
print()
print("Alice picks a warrior with strength x and you pick a warrior with strength y: Expected Gain will be::")
print("Gain = (y/x+y)*x + (x/x+y)*-y = 0")
print()
print("Therefore every match is fair(i.e. 0 expected gain)")

import random

m = [1, 6, 6, 1]
a = [3, 4, 6, 7]

def combine(w1, w2):
    p = w1 / (w1 + w2)
    if random.random() < p:
        return 1
    else:
        return 2

w = 0
n = 10000
for _ in range(n):
    r = m.copy()
    s = a.copy()
    while r and s:
        r_idx = random.randint(0, len(r) - 1)
        w1 = r[r_idx]
        s_idx = random.randint(0, len(s) - 1)
        w2 = s[s_idx]
        win = combine(w1, w2)
        if win == 1:
            s.remove(w2)
            r[r_idx] += w2
        else:
            r.remove(w1)
            s[s_idx] += w1
    if r:
        w += 1

p = w / n

print("It wouldn't matter in which order we choose the warrior.")
print("Since net gain is zero each round.")
print("So any approach will be an optimal approach.")
print("Hence we have randomized the selection process.")
print()
print("Probability of winning the tournament:", p)
ppp=(1+6+6+1)/(1+6+6+1+3+4+6+7)
print("Theortitcal value is:  ",ppp)
print("Difference is" ,abs(ppp-p)," which is negligible.")
