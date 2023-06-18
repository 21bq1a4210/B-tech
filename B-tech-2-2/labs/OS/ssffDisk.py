def ssffdiskschduling(tracks, head):
    seek_tim = 0
    while len(tracks)!=0:
        min_track = tracks[0]
        
        for j in range(len(tracks)):
            track_seek_tim = abs(tracks[j] -head)
            if min_track - head > track_seek_tim:
                min_track = tracks[j]
        seek_tim += abs(min_track)
        head = min_track
        tracks.remove(min_track)
    return seek_tim

if __name__ == "__main__":
    trc = [176, 79, 34, 60, 92, 11, 41, 114]
    head = 60
    seek_tim = ssffdiskschduling(trc, head)
    print(seek_tim)