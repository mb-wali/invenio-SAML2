# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 TUGRAZ.
#



"""Shibboleth Authenticator"""

from __future__ import absolute_import, print_function

from .ext import ShibbolethAuthenticator
from .version import __version__

__all__ = (__version__, 'ShibbolethAuthenticator',)
