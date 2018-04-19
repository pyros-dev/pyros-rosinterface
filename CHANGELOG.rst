^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package pyros_interfaces_ros
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

0.4.1 (2018-04-19)
------------------
* adjusting package version
* Merge pull request `#10 <https://github.com/pyros-dev/pyros-rosinterface/issues/10>`_ from pyros-dev/pyros_common_5
  adating pyros exceptionsto recent pyros_common.exception base class.
* fixing super call
* now exposing __version_\_ as usually done
* bumping packages version
* reviewing rosinstall file for this package.
* Adapting Pyros Exceptions to new format
* adating pyros exceptionsto recent pyros_common.exception base class.
* Merge pull request `#8 <https://github.com/pyros-dev/pyros-rosinterface/issues/8>`_ from pyros-dev/improved_logging
  now logging config values
* Merge pull request `#7 <https://github.com/pyros-dev/pyros-rosinterface/issues/7>`_ from cehberlin/master
  Fixed missing forwards that are used by rostful
* fixed broken manifest loading in message_conversion and safe api
* Fixed missing ServiceException forwarding
* now logging config values
* Merge pull request `#6 <https://github.com/pyros-dev/pyros-rosinterface/issues/6>`_ from asmodehn/namespace
  Namespace
* filling up readme
* adding setup.py commands to make release easier...
* adding main module and launch file to be able to launch pyros node by itself.
* removing the debug print of sys.path
* now exposing PyrosROS class from the package.
* Contributors: AlexV, Christopher Hrabia, alexv

0.4.0 (2017-04-24)
------------------
* comments
* changing pyros_interfaces_ros import name
* fixing pyros_interfaces_common import name
* fixing path to version module.
* dropping our idea of namespace packages since we cannot easily make a working ROS deb pkg out of it.
* activating dependency retrieval (from dependency link) until pyros-common with namespace is released as deb.
* using dependency links to get in progress namespace package pyros_interfaces directly from git.
* enforcing usage of pkg-resources, not pkgutil, for namespace packages.
  moved importe of common out of try catch.
* reorganizing to nest everything under pyros_interfaces namespace
* WIP reviewing how to handle config...
* adding pyros_test as test dependency.
* adding pyros_utils as dependency.
  cleaning some imports.
* switching to use shadow fixed ros repositories
* fixed tests, version number and dependency to pyros_common
* restructuring to simplify things...
* fixing imports for new pyros structure
* adding dependency on catkin_pip
* fixing tests paths
* setting cmakelists and package.xml
* gathering and restructuring ros dependent part of pyros
* adding project files
* moving rosinstall files to proper directory
* Merge branch 'master' into HEAD
* Initial commit
* moving mock interface outside of ROS, to not depend on ROS for mocks.
* small file rename to match new name from pub and sub.
* Merge branch 'pub_sub' of https://github.com/asmodehn/pyros into socket_safety
  Conflicts:
  pyros/rosinterface/param_if_pool.py
  pyros/rosinterface/topic.py
* fixing node interface after pub/sub mixup. simplified stringpub and string sub tests.
* fixing tests filenames. cleanup debug prints.
* fixing cross logic between pubs ans subs.
* improving subscriber / publisher inter interfacing... added timeout to connect a pub/sub.
* now properly inverting (publisher_if is subscriber and vice versa)
* fixing broken update loop of ros_interface.
* skipping failing rosinterface test for now. passing fine independently, more investigation needed...
* separating pubs and subs. needs pyros_test 0.0.6 for tests.
* moving all ros api calls into subpackage to make patching easier.
  cleaned up imports
* first version of rospy safe API
* improving travis build to test with cache as well...
  change version_eq to version_gte since buidfarm doesnt handle version_eq properly (yet?).
* moving mockinterface into rosinterface.mock since design follows ROS concepts.
  fixed all tests.
  bumped pyros minor version to 0.3.0 because of all the changes...
* merged testRosInterfaceNoCache and testRosInterfaceCache. fixed all issues.
* fixed tests without cache
* basic usecase now working again with cache. needs lots of cleanup...
* continuing changes in rosinterface, splitting service, topics and params interface pools
  now rosinterface tests all passing
* splitting baseinterface to simplify things. fixed mockinterface and tests.
* various cleanups
* improved profiling script.
* comments
* fixing bwcompat issues.
  dropping shutdown behavior fix for now.
* improved management of interface topics and reference counting.
  still broken for multiprocess because shutdown is not working properly.
* fixing params and services removal with cache diff input.
  improved topics interface creation and cleanup.
* speeding up topic interfacing
* fixed logic for removing transients on difference update.
  now forwarding exception if param type not found
  small test improvements.
* fixing param behavior in ros_interface and added unit tests.
* improving first dynamic ROS import to ros_interface. improved logging.
  some test clean up since we use python testing framework now.
* now fails with explanation if ConnectionCacheProxy not available in rocon_python_comms.
* importing pyros_setup only when imports from ros_interface failed.
* improved main init to import dependencies from python or from ROS packages.
  fixed check for unicode strings.
  started implementing CATKIN_PIP_NO_DEPS for testing.
  reviewing dependencies version.
* moved some dependencies out of pyros_setup, to not require pyros_setup if using ROS environment as usual.
* Merge branch 'indigo-devel' of https://github.com/asmodehn/pyros into config_refactor
  Conflicts:
  pyros/rosinterface/ros_interface.py
* fixing tests
* fixed check for early topic detection and stabilize cache diff optimization.
* reviewing how we use zmp nodes and improving tests... WIP
* fix adding available services.
  improved logging.
  Conflicts:
  pyros/baseinterface/baseinterface.py
  pyros/rosinterface/ros_interface.py
* fixed checking for available transients. now doesnt have to be a dict, just an iterable.
  Conflicts:
  pyros/rosinterface/ros_interface.py
* removed useless None in get(smthg, None)
* added interface cache tests to run by default.
  reverted debug long timeouts.
* finished manual merging of connection_cache_diff_callback.
  fixed all RosInterfaceCache tests, but code really need refactoring...
* starting manual merge of connection_cache_diff_callback branch
* fixes for connection cache with diff optimisation.
  added pubsub wait for confirm from cache, but deleted pubsub report deleted before confirmation from cache.
  Not sure if it is the right choice, but extra care is needed when deleting...
* fix tests for RosInterface especially with cache (but no diff optim)
* adding yujin underlay as we need it for connectioncache message format.
* fixing path to current workspace
* fixing various minor python issues
* Merge branch 'indigo-devel' of https://github.com/asmodehn/pyros into config_refactor
  Conflicts:
  package.xml
  pyros/pyros_client.py
* removed duplicated import
* moved pyros and zmp sources, otherwise pyros was not find through egg link.
* Contributors: AlexV, alexv
