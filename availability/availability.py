c1 = [("9:00", '10:30'), ('12:00', "13:00"), ('16:00', "18:00")]
bounds1 = ('9:00', "20:00")
c2 = [("10:00", '11:30'), ('12:30', "14:30"),
      ('14:30', "15:00"), ("16:00", "17:00")]
bounds2 = ("10:00", "18:30")


def time2Int(timeStr):
    hourMinute = timeStr.split(":")
    return int(hourMinute[0]) * 100 + int(hourMinute[1])


def earlier(time1, time2):
    return (time2Int(time1) - time2Int(time2)) < 0


def getEarlier(time1, time2):
    if (earlier(time1, time2)):
        return time1
    else:
        return time2


def getLater(time1, time2):
    if (earlier(time1, time2)):
        return time2
    else:
        return time1


def equals(time1, time2):
    # print("Equals: " + str(time2Int(time1)) + " " + str(time2Int(time2)))
    return time2Int(time1) == time2Int(time2)


def GetOverlap(slot1, slot2):
    return (getLater(slot1[0], slot2[0]), getEarlier(slot1[1], slot2[1]))


def GetAvailabilities(schedule, bounds):
    availabilities = []
    avail_start = bounds[0]
    for meeting in schedule:
        if not equals(avail_start, meeting[0]):
            availabilities.append((avail_start, meeting[0]))
        avail_start = meeting[1]
    if not equals(avail_start, bounds[1]):
        availabilities.append((avail_start, bounds[1]))
    return availabilities


# get absolute bounds
bounds = GetOverlap(bounds1, bounds2)

# get availabilities rather than bookings
a1 = GetAvailabilities(c1, bounds)
a2 = GetAvailabilities(c2, bounds)

# Find overlapping spaces
p1 = 0
p2 = 0
avails = []
while p1 < len(a1) and p2 < len(a2):
    slot1 = a1[p1]
    slot2 = a2[p2]

    # If the end of one's slot is before the start of the other's slot, advance to next slot
    if earlier(slot1[1], slot2[0]):
        p1 += 1
        continue
    if earlier(slot2[1], slot1[0]):
        p2 += 1
        continue

    # Found overlap, start is later start and earlier end
    avails.append(GetOverlap(a1[p1], a2[p2]))

    # Advance whichever one ends first
    if earlier(slot1[1], slot2[1]):
        p1 += 1
    else:
        p2 += 1


print(a1)
print(a2)
print(avails)
