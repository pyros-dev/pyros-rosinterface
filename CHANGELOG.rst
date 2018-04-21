Changelog
=========


0.4.2 (2018-04-21)
------------------
- Adding rosservice dependency. [AlexV]
- Fixing param getval/setval interface. [AlexV]
- Updating README. [AlexV]
- Changed travis config to not attempt to build packages. ros build farm
  will do it. [AlexV]


0.4.1 (2018-04-19)
------------------
- 0.4.1. [AlexV]
- Updating changelog. [AlexV]
- Adjusting package version. [AlexV]
- Merge pull request #10 from pyros-dev/pyros_common_5. [AlexV]

  adating pyros exceptionsto recent pyros_common.exception base class.
- Fixing super call. [AlexV]
- Now exposing __version__ as usually done. [AlexV]
- Bumping packages version. [AlexV]
- Reviewing rosinstall file for this package. [AlexV]
- Adapting Pyros Exceptions to new format. [AlexV]
- Adating pyros exceptionsto recent pyros_common.exception base class.
  [AlexV]
- Merge pull request #8 from pyros-dev/improved_logging. [AlexV]

  now logging config values
- Now logging config values. [alexv]
- Merge pull request #7 from cehberlin/master. [AlexV]

  Fixed missing forwards that are used by rostful
- Fixed broken manifest loading in message_conversion and safe api.
  [Christopher Hrabia]
- Fixed missing ServiceException forwarding. [Christopher Hrabia]
- Merge pull request #6 from asmodehn/namespace. [AlexV]

  Namespace
- Filling up readme. [AlexV]
- Adding setup.py commands to make release easier... [AlexV]
- Adding main module and launch file to be able to launch pyros node by
  itself. [AlexV]
- Removing the debug print of sys.path. [AlexV]
- Now exposing PyrosROS class from the package. [AlexV]


0.4.0 (2017-04-24)
------------------
- 0.4.0. [AlexV]
- Preparing for 0.4 release. [AlexV]
- Comments. [AlexV]
- Changing pyros_interfaces_ros import name. [AlexV]
- Fixing pyros_interfaces_common import name. [AlexV]
- Fixing path to version module. [AlexV]
- Dropping our idea of namespace packages since we cannot easily make a
  working ROS deb pkg out of it. [AlexV]
- Activating dependency retrieval (from dependency link) until pyros-
  common with namespace is released as deb. [AlexV]
- Using dependency links to get in progress namespace package
  pyros_interfaces directly from git. [AlexV]
- Enforcing usage of pkg-resources, not pkgutil, for namespace packages.
  moved importe of common out of try catch. [AlexV]
- Reorganizing to nest everything under pyros_interfaces namespace.
  [AlexV]
- WIP reviewing how to handle config... [alexv]
- Adding pyros_test as test dependency. [alexv]
- Adding pyros_utils as dependency. cleaning some imports. [alexv]
- Switching to use shadow fixed ros repositories. [alexv]
- Fixed tests, version number and dependency to pyros_common. [alexv]
- Restructuring to simplify things... [alexv]
- Fixing imports for new pyros structure. [alexv]
- Adding dependency on catkin_pip. [alexv]
- Fixing tests paths. [alexv]
- Setting cmakelists and package.xml. [alexv]
- Gathering and restructuring ros dependent part of pyros. [alexv]
- Adding project files. [alexv]
- Moving rosinstall files to proper directory. [alexv]
- Merge branch 'master' into HEAD. [alexv]
- Initial commit. [AlexV]
- Moving mock interface outside of ROS, to not depend on ROS for mocks.
  [alexv]
- Small file rename to match new name from pub and sub. [alexv]
- Merge branch 'pub_sub' of https://github.com/asmodehn/pyros into
  socket_safety. [alexv]

  Conflicts:
  	pyros/rosinterface/param_if_pool.py
  	pyros/rosinterface/topic.py
- Fixing node interface after pub/sub mixup. simplified stringpub and
  string sub tests. [alexv]
- Fixing tests filenames. cleanup debug prints. [alexv]
- Fixing cross logic between pubs ans subs. [alexv]
- Improving subscriber / publisher inter interfacing... added timeout to
  connect a pub/sub. [alexv]
- Now properly inverting (publisher_if is subscriber and vice versa)
  [alexv]
- Fixing broken update loop of ros_interface. [alexv]
- Skipping failing rosinterface test for now. passing fine
  independently, more investigation needed... [alexv]
- Separating pubs and subs. needs pyros_test 0.0.6 for tests. [alexv]
- Moving all ros api calls into subpackage to make patching easier.
  cleaned up imports. [AlexV]
- First version of rospy safe API. [AlexV]
- Improving travis build to test with cache as well... change version_eq
  to version_gte since buidfarm doesnt handle version_eq properly
  (yet?). [alexv]
- Moving mockinterface into rosinterface.mock since design follows ROS
  concepts. fixed all tests. bumped pyros minor version to 0.3.0 because
  of all the changes... [alexv]
- Merged testRosInterfaceNoCache and testRosInterfaceCache. fixed all
  issues. [alexv]
- Fixed tests without cache. [alexv]
- Basic usecase now working again with cache. needs lots of cleanup...
  [alexv]
- Continuing changes in rosinterface, splitting service, topics and
  params interface pools now rosinterface tests all passing. [alexv]
- Splitting baseinterface to simplify things. fixed mockinterface and
  tests. [alexv]
- Various cleanups. [alexv]
- Improved profiling script. [alexv]
- Comments. [alexv]
- Fixing bwcompat issues. dropping shutdown behavior fix for now.
  [alexv]
- Improved management of interface topics and reference counting. still
  broken for multiprocess because shutdown is not working properly.
  [alexv]
- Fixing params and services removal with cache diff input. improved
  topics interface creation and cleanup. [alexv]
- Speeding up topic interfacing. [alexv]
- Fixed logic for removing transients on difference update. now
  forwarding exception if param type not found small test improvements.
  [alexv]
- Fixing param behavior in ros_interface and added unit tests. [alexv]
- Improving first dynamic ROS import to ros_interface. improved logging.
  some test clean up since we use python testing framework now. [alexv]
- Now fails with explanation if ConnectionCacheProxy not available in
  rocon_python_comms. [alexv]
- Importing pyros_setup only when imports from ros_interface failed.
  [alexv]
- Improved main init to import dependencies from python or from ROS
  packages. fixed check for unicode strings. started implementing
  CATKIN_PIP_NO_DEPS for testing. reviewing dependencies version.
  [alexv]
- Moved some dependencies out of pyros_setup, to not require pyros_setup
  if using ROS environment as usual. [alexv]
- Merge branch 'indigo-devel' of https://github.com/asmodehn/pyros into
  config_refactor. [alexv]

  Conflicts:
  	pyros/rosinterface/ros_interface.py
- Fixing tests. [alexv]
- Fixed check for early topic detection and stabilize cache diff
  optimization. [alexv]
- Reviewing how we use zmp nodes and improving tests... WIP. [alexv]
- Fix adding available services. improved logging. [alexv]

  Conflicts:
  	pyros/baseinterface/baseinterface.py
  	pyros/rosinterface/ros_interface.py
- Fixed checking for available transients. now doesnt have to be a dict,
  just an iterable. [alexv]

  Conflicts:
  	pyros/rosinterface/ros_interface.py
- Removed useless None in get(smthg, None) [alexv]
- Added interface cache tests to run by default. reverted debug long
  timeouts. [alexv]
- Finished manual merging of connection_cache_diff_callback. fixed all
  RosInterfaceCache tests, but code really need refactoring... [alexv]
- Starting manual merge of connection_cache_diff_callback branch.
  [alexv]
- Fixes for connection cache with diff optimisation. added pubsub wait
  for confirm from cache, but deleted pubsub report deleted before
  confirmation from cache. Not sure if it is the right choice, but extra
  care is needed when deleting... [alexv]
- Fix tests for RosInterface especially with cache (but no diff optim)
  [alexv]
- Adding yujin underlay as we need it for connectioncache message
  format. [alexv]
- Fixing path to current workspace. [alexv]
- Fixing various minor python issues. [AlexV]
- Merge branch 'indigo-devel' of https://github.com/asmodehn/pyros into
  config_refactor. [AlexV]

  Conflicts:
  	package.xml
  	pyros/pyros_client.py
- Removed duplicated import. [AlexV]
- Moved pyros and zmp sources, otherwise pyros was not find through egg
  link. [alexv]


