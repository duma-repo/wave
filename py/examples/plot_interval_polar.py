# Plot / Interval / Polar
# No description available.
# ---
from synth import FakeCategoricalSeries
from telesync import Site, data, ui

site = Site()

page = site['/demo']

n = 24
f = FakeCategoricalSeries()
v = page.add('example', ui.plot_card(
    box='1 1 4 5',
    title='Interval, polar',
    data=data('product price', n),
    vis=ui.vis([ui.mark(coord='polar', mark='interval', x='=product', y='=price', y_min=0)])
))
v.data = [(c, x) for c, x, dx in [f.next() for _ in range(n)]]

page.sync()