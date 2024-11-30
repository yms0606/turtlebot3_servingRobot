from setuptools import find_packages, setup
import glob
import os

package_name = 'serving_node'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', glob.glob(os.path.join('launch', '*.launch.py'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='yms',
    maintainer_email='ymsix0622@gmail.com',
    description='serving robot package',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'order=serving_node.merge.order:main',
            'display=serving_node.merge.display:main',
            'robot=serving_node.merge.robot:main',
        ],
    },
)
