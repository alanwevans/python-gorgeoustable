# Python Gorgeous Tables

A subclass of https://github.com/dprince/python-prettytable with more advanced column formatting.

I found that I wanted more flexibility in formatting fields in a PrettyTable.  Looking at the source
it all boiled down to basically `_format_value`.  So I added a new property `custom_format` and
associated param in the `__init__` function.

This is by no means a fully fleshed out addition, I just wanted to get something together.

## Prerequisites

* [python-prettytable](https://github.com/dprince/python-prettytable) (available in most distros)

## Usage

Use just like PrettyTable, just add a `custom_format` parameter to `PrettyTable(custom_format=...)`
or manipulate `obj.custom_format`.  This is simply a hash whose keys are field names and values
are either strings suitable for `str.format()` or callables.

## Example


```python
import humanize
from gorgeoustable import GorgeousTable

g = GorgeousTable(
    field_names=['color', 'percentage', 'size', 'last','cost'],
    custom_format={'percentage': '{0:.1%}',
        'size': humanize.naturalsize,
        'last': humanize.naturaltime,
        'cost': lambda x: '{0:2.2f} Gg'.format(x/125),
	}
    )
g.add_row(['red', 0.011, 100000, 400, 19 * 3.14])
g.add_row(['blue', 0.3333, 2232323232323, 3453, 12 * 2.72])

print g
print '  * Gg conversion data: http://microgorillagrams.com/'
```

Gives something like:

```
+-------+------------+----------+----------------+---------+
| color | percentage |   size   |      last      |   cost  |
+-------+------------+----------+----------------+---------+
|  red  |    1.1%    | 100.0 kB | 6 minutes ago  | 0.48 Gg |
|  blue |   33.3%    |  2.2 TB  | 57 minutes ago | 0.26 Gg |
+-------+------------+----------+----------------+---------+
  * Gg conversion data: http://microgorillagrams.com/
```

## Contributing

Please use github.com [issues](https://github.com/alanwevans/python-gorgeoustable/issues) or [pull-request](https://github.com/alanwevans/python-gorgeoustable/pull/new/master).
