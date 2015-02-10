from functools import partial
from .features import hog, igo, dsift

sparse_hog = partial(hog, mode='sparse')
double_igo = partial(igo, double_angles=True)
sparse_hog.__name__ = 'sparse_hog'
sparse_hog.__doc__ = hog.__doc__
double_igo.__name__ = 'double_igo'
double_igo.__doc__ = igo.__doc__

fast_dsift = partial(dsift, fast=True, window_size=5, geometry=(1, 1, 8))
fast_dsift.__name__ = 'fast_dsift'
