from collections import Counter


def study_schedule(permanence_period, target_time):
    if not permanence_period or not target_time:
        return None
    rangeList = []
    for time_preriod in permanence_period:
        try:
            rangeList.extend(range(time_preriod[0], time_preriod[1]+1))
        except TypeError:
            return None

    counter = Counter(rangeList)
    return counter[target_time]
    # raise NotImplementedError
