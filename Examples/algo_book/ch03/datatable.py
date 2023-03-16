from contextlib import contextmanager
from output import visualize

SKIP = '*'

class DataTable:
    def __init__(self, widths, labels, output=True, decimals=3):
        assert len(widths) == len(labels)
        self.output = output
        self.labels = labels
        self.widths = widths
        self.fmt = ''
        self.entry_fmt = ''
        self.values = {}
        self.num_rows = 0
        self.row_index = {}
        symbol = ',d'
        for idx, width in enumerate(widths):
            self.fmt += '{{0[{}]:>{}}}\t'.format(idx, width)
            self.entry_fmt += '{{0[{}]:>{}{}}}\t'.format(idx, width, symbol)
            symbol = '.{}f'.format(decimals)
        if output:
            print(self.fmt.format(labels))

    def set_output(self, status):
        """Turn on/off output status for row() method calls."""
        self.output = status

    def format(self, field, fmt):
        """
        Change the format of this entry from 'f' into the given format.
        Defect: If change first column to 'f', then decimals length is ignored.
        """
        idx = self.labels.index(field)
        if idx < 0:
            raise ValueError('{} is not a valid field'.format(field))

        # {0[IDX]:>FORMAT}
        target = '{{0[{}]:>'.format(idx)
        where = self.entry_fmt.index(target)
        rest = self.entry_fmt.find('}', where)
        prefix = self.entry_fmt[:where + len(target)]
        suffix = self.entry_fmt[rest:]
        self.entry_fmt = prefix + str(self.widths[idx]) + fmt + suffix

    def row(self, row):
        """
        Helper method to load up an entire row of values.
        If any values are SKIP then must eliminate without throwing off the formatting of output
        """
        if self.output:
            formats = self.entry_fmt.split('\t')

            if SKIP in row:
                new_formats = []
                for fmt, val, width in zip(formats, row, self.widths):
                    if val == SKIP:
                        new_formats.append('{}:>{}s}}'.format(fmt.split(':')[0], width))
                    else:
                        new_formats.append(fmt)
                formats = new_formats

            if len(row) == len(self.labels):
                print('\t'.join(formats).format(row))
            else:
                # assume partial rows are left-justified... WILL BE REPLACED WITH SKIP...
                print('\t'.join(formats[:len(row)]).format(row))

        if not row[0] in self.values:
            self.values[row[0]] = {}
            self.row_index[self.num_rows] = row[0]
            self.num_rows += 1

        # replace all values
        for idx in range(1, len(row)):
            self.values[row[0]][self.labels[idx]] = row[idx]

    def header(self, column):
        """Return the header for the row."""
        return self.labels[column]

    def entry(self, row, column):
        """If row and column belongs to value, return entry."""
        if row in self.values:
            vals = self.values[row]
            if column in vals:
                return vals[column]
        return None

    def column(self, column):
        """Return array of values in given column. Eliminate 'SKIP' and remaining."""
        cols = []
        for row in range(self.num_rows):
            label = self.row_index[row]
            vals = self.values[label]

            if column in vals:
                cols.append(vals[column])
            elif column == self.labels[0]:  # might be row label
                cols.append(label)

        # SKIP ALL remaining values...
        if SKIP in cols:
            idx = cols.index(SKIP)
            cols = cols[:idx]

        return cols


def process(table, chapter, number, description, create_image=True, xaxis='Problem instance size',
            yaxis='Time (in seconds)'):
    """Process Table by printing label/Description and visualizing table."""
    label = '{} {}-{}'.format(number.args[0].element(), chapter, number.args[0])
    print('{}. {}'.format(label, description))
    if create_image:
        visualize(table, description, label, xaxis=xaxis, yaxis=yaxis)
    print()


def caption(chapter, number):
    """
    Return string for 'element chapter-number. description'.
    number is either a TableNum or a FigureNum.
    """
    return '{} {}-{}'.format(number.args[0].element(), chapter, number.args[0])


def comma(n):
    """Return string for integer n with commas at thousands, i.e., '2,345,217'."""
    return '{:,}'.format(n)

