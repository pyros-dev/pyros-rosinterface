#!/usr/bin/python
from __future__ import absolute_import, division, print_function

# All ways to run pyros ROS interface node and all Manager commands
# should be defined here for consistency

import os
import sys
import click
import errno

import pyros_interfaces_ros

# #importing current package if needed ( solving relative package import from __main__ problem )
# if __package__ is None:
#     sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
#     from rostful.server import Server
# else:
#     from .server import Server

import logging
from logging.handlers import RotatingFileHandler


#
# Arguments' default value is None here
# to use default values from config file if one is provided.
# If no config file is provided, internal defaults are used.
#
@click.command()
@click.option('subs', '--sub', default=None, multiple=True,)
@click.option('pubs', '--pub', default=None, multiple=True,)
@click.option('svcs', '--svc', default=None, multiple=True,)
@click.option('params', '--param', default=None, multiple=True,)  # this is the last possible config override, and has to be explicit.
@click.option('ros_args', '-r', '--ros-arg', multiple=True, default='')
def run(subs, pubs, svcs, params, ros_args):
    """
    Start rostful server.
    :param subs: a list of regex to determine which subscriber to listen on
    :param pubs: a list of regex to determine which publisher to inject in
    :param svcs: a list of regex to determine which services to expose
    :param params: a list of regex to determine which params to expose
    :param ros_args: the ros arguments (useful to absorb additional args when launched with roslaunch)
    """

    # Start Server with config passed as param
    rosnode = pyros_interfaces_ros.PyrosROS("pyros")

    # run the node
    # Note when we run the node without using the subprocess API, we need to pass the config directly...
    rosnode.run(
        publishers=list(pubs),
        subscribers=list(subs),
        services=list(svcs),
        params=list(params),
    )


if __name__ == '__main__':
    run()
