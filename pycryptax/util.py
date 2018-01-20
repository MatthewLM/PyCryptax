import datetime, copy

def dateFromString(s):
    try:
        return datetime.datetime.strptime(s, "%Y-%m-%d")
    except ValueError:
        return datetime.datetime.strptime(s, "%d %b %Y")

def getPrettyDate(d):
    return d.strftime("%d/%m/%Y")

def addToDictKey(d, k, v):

    if k in d:
        d[k] += v
    else:
        d[k] = copy.deepcopy(v)

