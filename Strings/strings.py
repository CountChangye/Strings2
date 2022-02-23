#  Copyright (c) 2022. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.

__author__ = "CountChangye <121116728@qq.com>"
__version__ = "0.0.1"


class string(str):
    """ Python strings for humans """

    def len(self):
        return self.__len__()

    @property
    def length(self):
        return self.len()

    @property
    def size(self):
        return self.length

    def add(self, value):
        return self + string(value)


if __name__ == "__main__":
    s = string("Hello")
    x = s.add(", world")
    print(type(x))
