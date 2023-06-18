def fifo(page_list, frame_size):
    page_faults = 0
    frame_list = []

    for page in page_list:
        if page not in frame_list:
            if len(frame_list) == frame_size:
                frame_list.pop(0)
            frame_list.append(page)
            page_faults += 1

    return page_faults

pages=list(map(int,input("enter the input:").split()))
cap=int(input("enter the capasity:"))
print(f"The no.of page faults are: {fifo(pages,cap)}")