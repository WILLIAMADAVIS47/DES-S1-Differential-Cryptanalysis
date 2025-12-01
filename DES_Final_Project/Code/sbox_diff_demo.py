import random

S1 = [
    [14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],
    [0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],
    [4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],
    [15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]
]

def s1_box(x):
    b0 = x & 1
    b5 = (x >> 5) & 1
    row = (b5 << 1) | b0
    col = (x >> 1) & 0b1111
    return S1[row][col]

def run_diff(delta_in, num_trials):
    c = {}
    for _ in range(num_trials):
        x = random.randint(0,63)
        x2 = x ^ delta_in
        y1 = s1_box(x)
        y2 = s1_box(x2)
        d = y1 ^ y2
        c[d] = c.get(d,0) + 1
    return c

def key_filter(delta_in, target_delta_out, num_pairs=40):
    true_key = random.randint(0,63)
    pairs = []
    while len(pairs) < num_pairs:
        x1 = random.randint(0,63)
        x2 = x1 ^ delta_in
        y1 = s1_box(x1 ^ true_key)
        y2 = s1_box(x2 ^ true_key)
        if (y1 ^ y2) == target_delta_out:
            pairs.append((x1,x2))
    scores = [0]*64
    for x1,x2 in pairs:
        for k in range(64):
            y1 = s1_box(x1 ^ k)
            y2 = s1_box(x2 ^ k)
            if (y1 ^ y2) == target_delta_out:
                scores[k] += 1
    r = sorted(range(64), key=lambda k: scores[k], reverse=True)
    print("true key:", true_key, f"({true_key:06b})")
    print("top key candidates:")
    for k in r[:8]:
        print(k, f"({k:06b})", "score:", scores[k])
    print()

def main():
    delta_in = 0b000010
    num_trials = 20000
    c = run_diff(delta_in, num_trials)
    for d,count in sorted(c.items(), key=lambda p:p[1], reverse=True):
        print(d, count, count/num_trials)
    key_filter(delta_in, 12, num_pairs=80)


if __name__ == "__main__":
    main()
