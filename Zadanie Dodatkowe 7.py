def sex(a):
    nl = len(a)
    if a[nl-1] == 'a' or a[nl-1] == 'A':
        return 'Kobieta'
    else:
        return 'Mezczyna'

names = ['Mikołaj','Dawid','Anna','Wiktoria','Krystian']

dict_names = {name: sex(name) for name in names }

sorted_names = dict(sorted(dict_names.items(), key = lambda x: x[1]))

print(sorted_names)

