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
