def introduce_frecuency(a4=440):
    flag = True
    while flag:
        a4 = int(input("Introduce A4 hz (440 normaly): "))
        if type(a4) == int:
            flag = False
            return a4
        else:  # type(a4) != int or type(a4) == float:
            print("Only numbers!")


a4 = introduce_frecuency()

# The first A
a0 = a4 / 16

# The 12 piano notes
notes = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]

# Array of piano notes
piano = [[0 for y in range(12)] for x in range(10)]

# Put the frecuency in the notes
for x in range(len(piano)):
    for y in range(len(piano[x])):
        hz_distance = pow(2, y / 12)
        # rounded
        piano[x][y] = round(
            ((pow(2, x) * (a0)) * (hz_distance)), 5)
        # without rounded
        # piano[x][y] = (pow(2, x) * (a0)) * (hz_distance)

        if y == 0:
            print(f"{x}{notes[int(y)]}: {piano[x][int(y)]} hz")
        if y == 1:
            print(f"{x}{notes[int(y)]}: {piano[x][int(y)]} hz")
        if y == 2:
            print(f"{x}{notes[int(y)]}: {piano[x][int(y)]} hz")
        if y == 3:
            print(f"{x}{notes[int(y)]}: {piano[x][int(y)]} hz")
        if y == 4:
            print(f"{x}{notes[int(y)]}: {piano[x][int(y)]} hz")
        if y == 5:
            print(f"{x}{notes[int(y)]}: {piano[x][int(y)]} hz")
        if y == 6:
            print(f"{x}{notes[int(y)]}: {piano[x][int(y)]} hz")
        if y == 7:
            print(f"{x}{notes[int(y)]}: {piano[x][int(y)]} hz")
        if y == 8:
            print(f"{x}{notes[int(y)]}: {piano[x][int(y)]} hz")
        if y == 9:
            print(f"{x}{notes[int(y)]}: {piano[x][int(y)]} hz")
        if y == 10:
            print(f"{x}{notes[int(y)]}: {piano[x][int(y)]} hz")
        if y == 11:
            print(f"{x}{notes[int(y)]}: {piano[x][int(y)]} hz")
        if y == 12:
            print(f"{x}{notes[int(y)]}: {piano[x][int(y)]} hz")