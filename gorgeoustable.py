from prettytable import PrettyTable

# Author: Alan Evans <alanwevans@gmail.com>
#
# A subclass of https://github.com/dprince/python-prettytable
# with more advanced column formatting.
#
# This class just adds a 'custom_format' property and __init__ param.
# The param is a dictionary with field names as keys whose values are
# either format strings suitable for str.format or callables.
#

class GorgeousTable(PrettyTable):
    def __init__(self, *args, **kwargs):
        self.custom_format = kwargs.pop('custom_format', {})
        super(GorgeousTable, self).__init__(*args, **kwargs)

    def _format_value(self, field, value):
        fmt = self.custom_format.get(field, None)

        if isinstance(fmt, str):
            return self._unicode(fmt.format(value))
        elif callable(fmt):
            return self._unicode(fmt(value))
        else:
            return super(GorgeousTable, self)._format_value(field, value)
