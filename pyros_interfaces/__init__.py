# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

# this is a namespace package
import pkg_resources
pkg_resources.declare_namespace(__name__)

# It seems this strategy doesnt work with ROS generated message classes...
# import pkgutil
# __path__ = pkgutil.extend_path(__path__, __name__)
