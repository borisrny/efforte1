from datetime import datetime, timedelta


def to_bool(val):
    if isinstance(val, bool):
        return val
    return val.lower() == 'true'


def fmt_date(dt):
    return dt.strftime('%m-%d-%Y')


def utc2local(utc):
    # epoch = time.mktime(utc.timetuple())
    # offset = datetime.fromtimestamp(epoch) - datetime.utcfromtimestamp(epoch)
    # return utc - offset
    offset = timedelta(hours=4)
    return utc - offset


def fmt_date_tm(dt):
    ldt = utc2local(dt)
    return ldt.strftime('%m/%d/%Y %H:%M')
    # return dt.strftime('%m/%d/%Y %H:%M')


def api_str2date(strd):
    fmt = '%b %d %Y'
    return datetime.strptime(strd[4:15], fmt)


def util_get_nulloverride(d, fld, dflt):
    ret = d.get(fld, dflt)
    return ret if ret is not None else dflt
