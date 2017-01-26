

def get_agg_window_in_min(hours):
    # returns aggregation time window depending on overall time period
    window_in_min = 1

    if hours > 4:
        window_in_min = 3
    if hours > 12:
        window_in_min = 5
    if hours > 24:
        window_in_min = 6
    if hours > 4 * 24:
        window_in_min = 10
    if hours > 7 * 24:
        window_in_min = 20
    if hours > 30 * 24:
        window_in_min = 60
    if hours > 3 * 30 * 24:
        window_in_min = 90
    return window_in_min