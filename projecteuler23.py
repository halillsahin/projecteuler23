def toplam_bölenler(n):
    bölenler = [1]
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            bölenler.append(i)
            if i != n // i:
                bölenler.append(n // i)
    return sum(bölenler)

fazlasayıar = []
for i in range(12, 28123):
    if toplam_bölenler(i) > i:
        fazlasayıar.append(i)

çiftler = set()
for i in range(len(fazlasayıar)):
    for j in range(i, len(fazlasayıar)):
        çift = fazlasayıar[i] + fazlasayıar[j]
        if çift <= 28123:
            çiftler.add(çift)
toplam_fazlasayılar = list(filter(lambda x: x not in çiftler, range(1, 28124)))






print(sum(toplam_fazlasayılar))
