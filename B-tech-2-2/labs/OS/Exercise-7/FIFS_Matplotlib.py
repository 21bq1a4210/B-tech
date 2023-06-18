from matplotlib import pyplot as plt


def FIFS(seq, start):
    temp = seq[:]
    temp.insert(0, start)
    plt.rcParams['xtick.bottom'] = plt.rcParams['xtick.labelbottom'] = True
    plt.rcParams['xtick.top'] = plt.rcParams['xtick.labeling'] = True
    size = len(temp)
    x = temp
    y = []
    headmovement = 0
    for i in range(0, size):
        y.append(-i)
        if i != size-1:
            headmovement = headmovement + abs(temp[i] - temp[i+1])
            string = 'Headmovement ='
if __name__ == "__main__":
    sequence = list(map(int, input("enter the sequence:").split()))
    head = int(input("Enter the current position of the head:"))
    seck_time = FIFS(sequence, head)
    print(f"The seck time using FIFS: {seck_time}")