#!/usr/bin/env python
'''Generic cdf/pdf/ccdf plotting functions.'''
import os

import matplotlib.pyplot as plt
import networkx as nx
import pylab


def plot(ptype, data, colors, axes, label, xscale, yscale,
         write_filepath = None, write = False, num_bins = None, ext = 'pdf'):

    fig = pylab.figure()
    lines = []
    datanames = []
        
    if ptype == 'cdf':
        index = 0
        for key, val in data.iteritems():
            x = sorted(val)
            y = [(float(i + 1) / len(x)) for i in range(len(x))]
            lines.append(pylab.plot(x, y, colors[index]))
            datanames.append(key)
            index += 1
#    elif ptype == 'ccdf':
#        x = sorted(data)
#        y = [1.0 - (float(i + 1) / len(x)) for i in range(len(x))]
#    elif ptype == 'pdf':
#        # bin data by value
#        hist = {}
#        data_max = max(data)
#        # use all bins if our data is integers
#        if data_max == int(data_max):
#            num_bins = data_max
#        else:
#            num_bins = 1000
#        for d in data:
#            bin = int((float(d) * num_bins) / float(data_max))
#            if bin not in hist:
#                hist[bin] = 1
#            else:
#                hist[bin] += 1
#
#        x = []
#        y = []
#        for i in range(num_bins + 1):
#            range_lo = float(i) / float(num_bins) * data_max
#            range_hi = float(i + 1) / float(num_bins) * data_max
#            y_val = (float(hist[i]) / len(data)) if i in hist else 0
#            x.append(range_lo)
#            y.append(y_val)
#
#            x.append(range_hi)
#            y.append(y_val)
#
#        # scale max Y
#        axes[3] = float(max(hist.values())) / len(data)
    else:
        raise Exception("invalid plot type")

    pylab.grid(True)
    pylab.xscale(xscale)
    pylab.yscale(yscale)
    pylab.axis(axes)
    pylab.xlabel("value")
    pylab.ylabel(ptype)
    pylab.title(label)
    pylab.legend(lines, datanames, loc = "lower right")
    if write:
        fig.savefig(write_filepath + '.' + ext)
    else:
        pylab.show()
