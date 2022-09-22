import statistics
from robot.api.deco import *


@keyword(name="Get Mean")
def get_mean(data):
    return round(statistics.mean(data), 3)


@keyword(name="Get Stdev")
def get_stdev(data):
    return round(statistics.stdev(data), 3)