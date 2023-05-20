subnetmask = input('Sláðu inn subnetmaskann: ')
subnetmask = subnetmask.split('.')
wildcardmask = []
for x in subnetmask:
    wildcardmask.append(255-int(x))

print(wildcardmask)

wildcardmask = '.'.join(map(str, wildcardmask))

print(wildcardmask)
