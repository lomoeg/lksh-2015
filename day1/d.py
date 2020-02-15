s1 = input()
cards = list(map(int, s1.split()))

s2 = input()
position = list(map(int, s2.split()))
position.append(len(cards))

s = []
sfinal = []

st = 0

for x in position:
    fn = x
    s = cards[st:fn]
    s = s[::-1]
    st = fn
    sfinal += s

sfinal = sfinal[::-1]

print(*sfinal)