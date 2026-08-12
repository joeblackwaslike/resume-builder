from datetime import datetime
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit


def parse_common(names, data):
    return {f: data.get(f, "") for f in names.split()}


def format_date(value, fmt="%m/%Y"):
    parts = value.split("-")
    if len(parts) == 2:
        parts.append("01")

    dt = datetime.fromisoformat("-".join(parts))
    return dt.strftime(fmt)


def add_section_items(obj, item_processor):
    if isinstance(obj, (list, tuple)):
        return [item_processor(i) for i in obj]
    elif isinstance(obj, dict):
        return item_processor(obj)


def parse_year(date):
    date = datetime.fromisoformat(date).date()
    return str(date.year)


def stringify_sequence(sequence):
    if not sequence:
        return ""
    if isinstance(sequence, str):
        return sequence
    elif isinstance(sequence, (list, tuple, set)):
        return ", ".join(sequence)


def format_date_range(start, end, fmt="%m/%Y"):
    if not start or not end:
        return ""
    start = format_date(start, fmt)
    end = format_date(end, fmt)
    if start == end:
        return start
    return f"{start} -- {end}"


def clean_url(url):
    if not url:
        return url
    parts = urlsplit(url)
    return urlunsplit((parts.scheme, parts.netloc, parts.path, "", ""))


def add_utm_params(url, **params):
    if not url:
        return url
    parts = urlsplit(url)
    query = dict(parse_qsl(parts.query))
    query.update({k: v for k, v in params.items() if v})
    return urlunsplit((parts.scheme, parts.netloc, parts.path, urlencode(query), parts.fragment))


def build_utm_campaign(meta):
    return "-".join(str(p) for p in (meta.get("version"), meta.get("role"), meta.get("patch")) if p)


def add_items(obj, items):
    if not items:
        return obj
    if isinstance(items, str):
        obj.add_item(items)
    if isinstance(items, (tuple, list)):
        for item in items:
            obj.add_item(item)
    return obj
