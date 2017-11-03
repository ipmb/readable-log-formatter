from __future__ import unicode_literals
import logging

# built-in attributes on LogRecord. Used to determine what is passed in `extras`
RESERVED_ATTRS = (
        'args', 'asctime', 'created', 'exc_info', 'exc_text', 'filename',
        'funcName', 'levelname', 'levelno', 'lineno', 'module',
        'msecs', 'message', 'msg', 'name', 'pathname', 'process',
        'processName', 'relativeCreated', 'stack_info', 'thread', 'threadName')


# from Fabric to colorize output
def _color(code):
    def inner(text, bold=False):
        c = code
        if bold:
            c = "1;%s" % c
        return "\033[%sm%s\033[0m" % (c, text)
    return inner


red = _color('31')
green = _color('32')
yellow = _color('33')
blue = _color('34')
white = _color('37')


# from python-json-logger
def _find_extras(record):
    extras = {}
    for key, value in record.__dict__.items():
        # this allows to have numeric keys
        starts_under = not (hasattr(key, "startswith") and key.startswith('_'))
        if key not in RESERVED_ATTRS and starts_under:
            extras[key] = value
    return extras


def _color_log_level(text, levelno):
    if levelno >= logging.ERROR:
        return red(text)
    elif levelno == logging.WARNING:
        return yellow(text)
    elif levelno <= logging.DEBUG:
        return blue(text)
    return white(text)


class ReadableFormatter(logging.Formatter):
    """
    This is meant for local development where "human" readable logs are
    important and "machine" readability is not.

    Usage in logging.config.dictConfig::

        'formatters': {
            'readable': {
                'class': 'readable_log_formatter.ReadableFormatter',
            },
        },
        'handlers': {
            'default': {
                'class': 'logging.StreamHandler',
                'formatter': 'readable',
            },
        }
    """
    separator = '$'
    indent = 8
    fmt = ('%(levelname){}s{} %(name)s in %(funcName)s (line:%(lineno)s)\n'
           '%(message)s%(readableExtras)s')

    def __init__(self, *args, **kwargs):
        # force format
        fmt = self.fmt.format(self.indent, self.separator)
        # replace fmt if supplied as arg instead kwargs
        if args and 'fmt' not in kwargs:
            args = (fmt,) + args[1:]
        else:
            kwargs['fmt'] = fmt
        super(ReadableFormatter, self).__init__(*args, **kwargs)

    def format(self, record):
        # extract extras from record
        record.readableExtras = '\n'.join(['{}: {}'.format(white(k), v)
                                           for k, v
                                           in _find_extras(record).items()])
        if record.readableExtras:
            record.readableExtras = '\n' + record.readableExtras
        # Color output
        out = super(ReadableFormatter, self).format(record)
        if record.exc_text:
            out = out.replace(record.exc_text, green(record.exc_text))
        lines = out.splitlines(True)
        level, code_info = lines[0].split(self.separator, 1)
        name, details = code_info.lstrip().split(' ', 1)
        first_line = ' '.join([_color_log_level(level, record.levelno),
                               white(name, bold=True),
                               white(details)])
        lines = [first_line] + lines[1:]
        # indent after first line
        return (' ' * (self.indent + 1)).join(lines)