from main import biomedRecords

from inspect import getmembers, isfunction

options = getmembers(biomedRecords, isfunction)
options = [options[opt][0] for opt, _ in enumerate(options)]

for i in range(1, len(options)-1, 2):
    print(f'\t\t\t{options[i]}, {options[i+1]}')


choice = input('\t\tPlease choose one of the inputs above: \n\t\t\t')