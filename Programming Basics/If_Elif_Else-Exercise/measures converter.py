metrics = float(input())
inputMeasure = input()
outputMeasure = input()

if inputMeasure == 'mm':
    if outputMeasure == 'cm':
        print(f'{metrics / 10:.3f}')
    elif outputMeasure == 'm':
        print(f'{metrics / 1000:.3f}')

elif inputMeasure == 'cm':
    if outputMeasure == 'mm':
        print(f'{metrics * 10:.3f}')
    elif outputMeasure == 'm':
        print(f'{metrics / 100:.3f}')

elif inputMeasure == 'm':
    if outputMeasure == 'mm':
        print(f'{metrics * 1000:.3f}')
    elif outputMeasure == 'cm':
        print(f'{metrics * 100:.3f}')