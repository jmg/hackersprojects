import time
from math import floor
from collections import OrderedDict
from datetime import datetime


def get_time_since(date):

    tokens = OrderedDict()
    tokens[31536000] = 'year'
    tokens[2592000] = 'month'
    tokens[86400] = 'day'
    tokens[3600] = 'hour'
    tokens[60] = 'minute'
    tokens[1] = 'second'

    time_since = int(time.mktime(datetime.utcnow().timetuple()) - time.mktime(date.timetuple()))

    for seconds, token in tokens.iteritems():

        if time_since < seconds:
            continue

        units = int(floor(time_since / seconds))
        end = 's' if units > 1 else ''
        return "%s %s%s ago" % (units, token, end)

    return "Just Now";
