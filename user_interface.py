from main import biomedRecords

from inspect import getmembers, isfunction

options = getmembers(biomedRecords, isfunction)
options = [options[opt][0] for opt, _ in enumerate(options)]

print('\t\t\tPlease an option below:')

for i in range(1, len(options)-1, 2):
    print(f'\t\t\t{options[i]}, {options[i+1]}')


choice = input('\t\t\t')