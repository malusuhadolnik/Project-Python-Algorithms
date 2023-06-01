from collections import Counter


def study_schedule(permanence_period, target_time):
    rangeList = []
    for time_preriod in permanence_period:
        rangeList.extend(range(time_preriod[0], time_preriod[1]+1))
    counter = Counter(rangeList)
    # print(counter[target_time])
    return counter[target_time]
    raise NotImplementedError
