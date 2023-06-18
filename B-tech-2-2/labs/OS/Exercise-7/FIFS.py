def FIFS(sequence, head):
    seq1 = sequence[:]
    seq1.insert(0, head)
    seck_time = 0
    for i in range(len(seq1)):
        seck_time += abs(seq1[1] - seq1[i+1])
    return seck_time

if __name__ == "__main__":
    sequence = list(map(int,input("enter the sequence:").split()))
    head = int(input("Enter the current position of the head:"))
    seck_time = FIFS(sequence, head)
    print(f"The seck time using FIFS: {seck_time}")