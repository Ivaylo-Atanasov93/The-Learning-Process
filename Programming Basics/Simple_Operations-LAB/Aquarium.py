length = float(input('Enter the length of the aquarium: '))
width = float(input('Enter the width of the aquarium: '))
height = float(input('Enter the height of the aquarium: '))
usedVolume = float(input('Enter the percentage of the used volume: ')) * 0.01

volume = length * width * height
volumeInLiters = volume * 0.001

freeVolume = volumeInLiters * (1 - usedVolume)

print(f'{freeVolume:.3f}')