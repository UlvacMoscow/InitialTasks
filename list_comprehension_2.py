names = ['anna', 'john', 'jenny', 'michael', 'alex']

"""

filter

"""
new_names = [x for x in names if x.startswith('j')]

print(new_names)

new_names_2 = []
for n in names:
    if n.startswith('a'):
        new_names_2.append(n)


print(new_names_2)
