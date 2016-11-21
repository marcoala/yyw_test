def mean(*argv):
    """Calculate the average of the given numbers

    Usage:
    avg = mean(4,4,6,6)
    print(avg)
        5
    """
    return float(sum(argv)) / max(len(argv), 1)
