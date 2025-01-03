# Copyright (C) 2024 Warren Usui, MIT License
from json import dumps
from itertools import chain

pentsol = (lambda t: dict((lambda b: (list(map(lambda a: [a, list(chain.from_iterable(
    list(map(lambda z: (lambda f: (lambda x: f(lambda v: x(x)(v)))(lambda x: f(
    lambda v: x(x)(v))))(lambda f: (lambda q: (list(chain.from_iterable(list(map(
    lambda h: (lambda g: (['\n'.join(list(map(lambda a: ''.join(a), g)))] if
    len(g[0]) == 10 or ((lambda b:  True if b[len(b) // 2].count('X') != 3 else
    (lambda a: list(chain.from_iterable(a['o'])).count('Y') <= list(chain.from_iterable(
    a['d'])).count('Y'))({'o': b[0: len(b) // 2], 'd': b[len(b) // 2 + 1:]}))(
    (list(zip(*g)) if len(g[0]) % 2 == 1 else g))) else []) if list(chain.from_iterable(
    g)).count('-') == 0 else f(g) if (lambda f: (lambda x: f(lambda v: x(x)(v)))
    (lambda x: f(lambda v: x(x)(v))))(lambda f: (lambda i: (lambda b: ((lambda a:
    b if list(chain.from_iterable(a)).count('#') == b else f(a))(list(map(lambda c:
    list(map(lambda b: i[b[0]][b[1]] if i[b[0]][b[1]] != '-' else '#' if ((b[0] > 0 and
    i[b[0] - 1][b[1]] == '#') or (b[1] > 0 and i[b[0]][b[1] - 1] == '#') or
    (b[0] < len(i) - 1 and i[b[0] + 1][b[1]] == '#') or (b[1] < len(i[0]) - 1 and
    i[b[0]][b[1] + 1] == '#')) else '-', map(lambda a: [c, a], range(0, len(i[0]))))),
    range(0, len(i)))))))(list(chain.from_iterable(i)).count('#'))))(list(map(
    lambda b: list(map(lambda a: ('#' if [b[0], a[0]] in [(lambda b: (lambda a:
    [a % len(b), a // len(b)]) (list(chain.from_iterable(zip(*b))).index('-'))(g))]
    and g[b[0]][a[0]] == '-' else g[b[0]][a[0]]), enumerate(b[1]))), enumerate(g)))) % 5
    == 0 and len(g[0]) == 10 or ((lambda b:  True if b[len(b) // 2].count('X') != 3
    else (lambda a: list(chain.from_iterable(a['o'])).count('Y') <=
    list(chain.from_iterable(a['d'])).count('Y'))({'o': b[0: len(b) // 2], 'd':
    b[len(b) // 2 + 1:]}))((list(zip(*g)) if len(g[0]) % 2 == 1 else g))) else [])(list
    (map(lambda b: list(map(lambda a: (t[4][h]['h'] if [b[0], a[0]] in (lambda b:
    (list(map(lambda a: [b['k'][0] + a[0], b['k'][1] + a[1]], b['h']['a'])) +
    [(lambda a: [b['k'][0] + a[0], b['k'][1] + a[1]])(b['h']['e'])])) ({'h': t[4][h],
    'k': (lambda b: (lambda a: [a % len(b), a // len(b)]) (list(chain.from_iterable(
    zip(*b))).index('-')))(q)}) and q[b[0]][a[0]] == '-' else q[b[0]][a[0]]), enumerate(
    b[1]))), enumerate(q)))), filter(lambda a: not t[4][a]['h'] in list(
    chain.from_iterable(q)), ((lambda f: (lambda x: f(lambda v: x(x)(v)))(lambda x:
    f(lambda v: x(x)(v))))(lambda f: (lambda i: (lambda c: (c if i['j'] == 4 else
    f({'j': i['j'] + 1, 'c': c, 'k': (lambda b: (lambda a: [a % len(b), a // len(b)])
    (list(chain.from_iterable(zip(*b))).index('-')))(i['l']), 'l': i['l']})))(list(
    map(lambda a: a[0], filter(lambda a: False if a[1]['p'] not in i['c'] else not
    ((lambda b: (lambda a: (True if a[0] >= len(b['l']) or a[1] >= len(b['l'][0]) or
    a[0] < 0 or a[1] < 0 or b['l'][a[0]][a[1]] != '-' else False)) ([b['k'][0] +
    b['e'][0], b['k'][1] + b['e'][1]]))({'k': i['k'], 'e': a[1]['e'], 'l': i['l']})),
    enumerate(t[i['j']])))))))({'j': 1, 'c': [0], 'k': (lambda b: (lambda a: [a % len(b),
    a // len(b)]) (list(chain.from_iterable(zip(*b))).index('-')))(q), 'l': q}))))))))))(
    z), b[a]))))], b.keys()))))((lambda e: dict(list(map(lambda d: [f"{d['f']}x{d['i']}",
    list(chain.from_iterable(map(lambda c: list(map(lambda b: list(map(lambda a: ['-'] *
    (b + 1) + ['X'] + ['-'] * (d['i'] - b - 2) if a in [c, c + 2] else ['-'] * b + ['X']
    * 3 + ['-'] * (d['i'] - b - 3) if a == c + 1 else ['-'] * d['i'], range(0, d['f']))),
    range(d['m'][c],(7 - d['f']) * 2 + d['f'] // 3))), range(0, len(d['m'])))))], e)) ))(
    list(map(lambda a: {'f': a, 'i': 60 // a, 'm': range(1, 1 - (a - 1) // 2, -1), 'n':
    (7 - a) * 2 + a // 3}, range(3, 7)))))))((lambda a: a[0:4] + [(lambda a: list(map(
    lambda a: {'e': a['e'], 'a': a['a'], 'p': a['p'], 'h': (lambda a: {55: 'P', 87: 'V',
    118: 'W', 535: 'L', 563: 'Y', 566: 'N', 1047: 'U', 1125: 'T', 1126: 'F', 1140:
    'Z', 3110: 'X', 66067: 'I'}[min((lambda g: chain.from_iterable(list(map(lambda e:
    list(map(lambda d: (lambda c: sum(map(lambda a: 2 ** a, map(lambda a: (lambda b:
    b * (b - 1) + b + a[0])(abs(a[0]) + abs(a[1])), c))))((lambda c: (lambda b: list(
    map(lambda a: [a[0], a[1] - b], c)))(min(list(map(lambda a: a[1], c)))))((lambda c:
    (lambda b: list(map(lambda a: [a[0] - b, a[1]], c)))(min(list(map(lambda a: a[0],
    c)))))(list(map(lambda a: [a[0] * e[0], a[1] * e[1]], d))))), [g, list(map(lambda a:
    [a[1], a[0]], g))])), [[1, 1], [1, -1], [-1, 1], [-1, -1]])))) (a['a'] + [a['e']]))])
    (a)}, a)))(a[4])])((lambda d: list(map(lambda c: list(map(lambda a: (lambda b: dict(
    a[1]) | {'b': b[a[0]]})(list(map(lambda b: list(map(lambda a: a['p'],
    d[c + 1])).index(b), range(0, d[c + 1][-1]['p'] + 1)))), enumerate(d[c]))), range(0,
    4))) + [d[-1][:]])((lambda f: (lambda x: f(lambda v: x(x)(v)))(lambda x: f(lambda v:
    x(x)(v))))(lambda f: (lambda d: d if len(d) >= 5 else f(d + [(lambda c: (lambda b:
    list(map(lambda a: a[0], filter(lambda a: a[1], b))))((lambda b: (lambda a:
    zip(c, a))(list(map(lambda a: b[a] not in b[0:a], range(0, len(b))))))(list(map(
    lambda a: (lambda a: sum(map(lambda a: 2 ** a, map(lambda a: (lambda b: b * (b - 1)
    + b + a[0])(abs(a[0]) + abs(a[1])), a))))(a['a'] + [a['e']]), c)))))(list(
    chain.from_iterable(map(lambda b: map(lambda a: {'e': a, 'a': (lambda a: a['a'] +
    [a['e']])(d[-1][b[0]]), 'p': b[0]}, b[1]), list(enumerate(list(map(lambda a: filter(
    ((lambda a: (lambda b: [] if b ==  a[1]['e'] or b in a[1]['a'] else list(filter(
    (lambda a: abs(a[0] - b[0]) + abs(a[1] - b[1]) == 1), [a[1]['e']] + a[1]['a'])))))(
    a), (lambda b: map(lambda a: (lambda a: [a['q'] - a['g'], a['g'] - abs(a['q'] -
    a['g'])])((lambda b: list(filter(lambda a: a['q'] > 0, map(lambda a: {'g':a + 1,
    'q': b - a * (a +1)}, range(0, 4))))[-1])(a)), range((lambda a: (a + 1) * (a + 2))(
    len(b[1]['a'])), 0, -1)))(a)), enumerate(d[-1])))))))))]))) ([[{'e': [0, 0], 'a': [],
    'p':-1}]]))))

with open("obf_pentominos.json", "w", encoding="utf-8") as outfile:
    outfile.write(dumps(pentsol, indent=4))
