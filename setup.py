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
    author_email='121116728@qq.com',
    url='https://github.com/CountChangye/Strings',
    license='LICENSE',
    packages=['Strings'],
    description='对字符串的操作',
    install_requires=[
        # 'python>=3.6.0',
        # 'pandas>=0.10.0'
    ]
)