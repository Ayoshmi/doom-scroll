def individual_check(time):
    if time > 180:
        return "AGGRESSIVE"
    elif time > 40:
        return "GENTLE"
    else:
        return "SAFE"


def cumulative_check(total_time, open_count):

    if total_time > 240:
        return "AGGRESSIVE"

    elif total_time > 100 or open_count > 4:
        return "GENTLE"

    else:
        return "SAFE"