# from distutils.core import setup
# from catkin_pkg.python_setup import generate_distutils_setup
#
# # ROS PACKAGING
# # using distutils : https://docs.python.org/2/distutils
# # fetch values from package.xml
# setup_args = generate_distutils_setup(
#     packages=[
#         'pyros',
#         'pyros.ros',
#         'pyros.ros.api',
#         'pyros.ros.tests',
#         'pyros.ros.rostests',
#     ],
#     package_dir={
#         'pyros': 'src/pyros',
#     }
# )
# setup(**setup_args)


import setuptools


# Ref : https://packaging.python.org/single_source_version/#single-sourcing-the-version
with open('src/pyros_ns/interfaces/ros/_version.py') as vf:
    exec(vf.read())


setuptools.setup(name='pyros.ros',
    version=__version__,
    description='Pyros ROS interface to provide ROS introspection for non-ROS users.',
    url='http://github.com/asmodehn/pyros-ros',
    author='AlexV',
    author_email='asmodehn@gmail.com',
    license='BSD',
    # TODO : enable namespace packages when supported properly with pip
    # packages=[
    #     'pyros.tests',
    #     'pyros.interfaces.ros',
    #     'pyros.interfaces.ros.api',
    #     'pyros.interfaces.ros.tests',
    #     'pyros.interfaces.ros.rostests',
    # ],
    packages=[
        'pyros_tests',
        'pyros_interfaces_ros',
        'pyros_interfaces_ros.api',
        'pyros_interfaces_ros.tests',
        'pyros_interfaces_ros.rostests',
    ],
    package_dir={
        #'pyros': 'src/pyros',
        'pyros_tests': 'src/pyros_tests',
        'pyros_interfaces_ros': 'src/pyros_interfaces_ros'
    },
    # entry_points={
    #     'console_scripts': [
    #         'pyros = pyros.__main__:nosemain'
    #     ]
    # },
    # this is better than using package data ( since behavior is a bit different from distutils... )
    include_package_data=True,  # use MANIFEST.in during install.
    install_requires=[
        'tblib',  # this might not always install six (latest version does not)
        'six',
        'pyzmq',
        'pyzmp>=0.0.14',  # lets match the requirement in package.xml (greater than)
        'pyros_setup>=0.1.5',  # Careful : pyros-setup < 0.0.8 might already be installed as a deb in /opt/ros/indigo/lib/python2.7/dist-packages/
        'pyros_config>=0.1.4',
        'nose>=1.3.7',
        'mock==1.0.1',  # old mock to be compatible with trusty versions
    ],
    # Reference for optional dependencies : http://stackoverflow.com/questions/4796936/does-pip-handle-extras-requires-from-setuptools-distribute-based-sources
    test_suite="nose.collector",
    tests_require=["nose"],
    # cmdclass={
    #     'rosdevelop': RosDevelopCommand,
    #     'prepare_release': PrepareReleaseCommand,
    #     'publish': PublishCommand,
    #     'rospublish': ROSPublishCommand,
    # },
    zip_safe=False,  # TODO testing...
    # namespace_packages=['pyros', 'pyros.interfaces']
)