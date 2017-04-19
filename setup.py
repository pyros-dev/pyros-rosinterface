import setuptools


# Ref : https://packaging.python.org/single_source_version/#single-sourcing-the-version
with open('pyros_interfaces/ros/_version.py') as vf:
    exec(vf.read())


setuptools.setup(name='pyros_interfaces.ros',
    version=__version__,
    description='Pyros ROS interface to provide ROS introspection for non-ROS users.',
    url='http://github.com/asmodehn/pyros-rosinterface',
    author='AlexV',
    author_email='asmodehn@gmail.com',
    license='BSD',
    # TODO : enable namespace packages when supported properly with pip
    # packages=[
    #     'pyros.interfaces.ros',
    #     'pyros.interfaces.ros.api',
    #     'pyros.interfaces.ros.tests',
    #     'pyros.interfaces.ros.rostests',
    # ],
    packages=[
        'pyros_interfaces.ros',
        'pyros_interfaces.ros.api',
        'pyros_interfaces.ros.tests',
        'pyros_interfaces.ros.rostests',
    ],
    package_dir={
        #'pyros': 'src/pyros',
        #'pyros.interfaces.ros': 'src/pyros_interfaces_ros'  # pip is currently breaking this for editable packages -> changing structure
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
        'pyros-common>=0.4.0',
        'nose>=1.3.7',
        'mock==1.0.1',  # old mock to be compatible with trusty versions
    ],
    dependency_links=['git+https://github.com/asmodehn/pyros-common.git@namespace#egg=pyros-common'],
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
    namespace_packages=['pyros_interfaces']
)