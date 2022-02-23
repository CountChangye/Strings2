#  Copyright (c) 2022. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.
import setuptools
import string
setuptools.setup(
    name='Strings',
    version=string.__version__,
    author=string.__name__,
    author_email='121116728@qq.com',
    url='https://github.com/CountChangye/Strings',
    packages=setuptools.find_packages(),
    license='LICENSE',
    description='对字符串的操作',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)