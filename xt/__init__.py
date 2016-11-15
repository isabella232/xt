# xt
import re, json


def xvert(instream, delimiter):
    for inp in instream:
        yield parsetile(inp, delimiter)


def format_hash(x, y, z, delimiter):
    return "{1}{0}{2}{0}{3}".format(delimiter, z, x, y)


def parsetile(inp, delimiter='/'):
    if re.match(r'.*\d+[\-\/]\d+[\-\/]\d+.*', inp):
        z, x, y = [int(t) for t in re.findall(r'(^|[\/\s\-])(\d+)[\-\/](\d+)[\-\/](\d+)', inp)[-1][1:]]
        return json.dumps([x, y, z])

    elif re.match(r'\[\d+(\,\s|\,)\d+(\,\s|\,)\d+\]', inp):
        x, y, z = json.loads(inp)

        return format_hash(x, y, z, delimiter)

    else:
        raise ValueError('Could not parse tile')