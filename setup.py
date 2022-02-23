#  Copyright (c) 2022. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.
from distutils.core import setup
import string
setup(
    name='Strings',
    version=string.__version__,
    author=string.__name__,
    url='www.example.com',
    license='LICENSE',
    packages=['mydates'],
    description='An example of building Python package.',
    install_requires=[
        # 'python>=3.6.0',
        # 'pandas>=0.10.0'
    ]
)