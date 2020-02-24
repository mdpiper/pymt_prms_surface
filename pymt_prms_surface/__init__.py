#! /usr/bin/env python

from .bmi import (PRMSSurface,
)

__all__ = ["PRMSSurface",
]

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
