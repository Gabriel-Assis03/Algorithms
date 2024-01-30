def study_schedule(permanence_period, target_time):
    cont = 0
    if target_time is None:
        return None
    for per in permanence_period:
        if (not isinstance(per[0], int) or
                not isinstance(per[1], int)):
            return None
        if per[0] <= target_time <= per[1]:
            cont += 1
    return cont
