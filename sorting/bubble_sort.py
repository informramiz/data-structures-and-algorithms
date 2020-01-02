"""
Problem-1: Sam records when they wake up every morning. Assuming Sam always wakes up in the same hour, use bubble sort
to sort by earliest to latest.
"""


def compare_default(l1, l2):
    return l1 <= l2


def bubble_sort(times, compare=compare_default):
    for i in range(len(times)):
        inversions = 0
        for j in range(len(times)-i-1):
            if not compare(times[j], times[j+1]):
                temp = times[j]
                times[j] = times[j+1]
                times[j+1] = temp
                inversions += 1
        if inversions == 0:
            # no inversions, it means array is sorted so no need to further traverse
            break


wakeup_times = [16, 49, 3, 12, 56, 49, 55, 22, 13, 46, 19, 55, 46, 13, 25, 56, 9, 48, 45]
bubble_sort(wakeup_times)
print("Pass" if (wakeup_times[0] == 3) else "Fail")

"""
Problem: Sam doesn't always go to sleep in the same hour. Given the following times Sam has gone to sleep, 
sort the times from latest to earliest.
"""
# Entries are (h, m) where h is the hour and m is the minute
sleep_times = [(24,13), (21,55), (23,20), (22,5), (24,23), (21,58), (24,3)]
bubble_sort(sleep_times, compare=lambda l1, l2: (l1[0] + l1[1]/60) > (l2[0] + l2[1]/60))
print ("Pass" if (sleep_times == [(24,23), (24,13), (24,3), (23,20), (22,5), (21,58), (21,55)]) else "Fail")