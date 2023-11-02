"""Testing Points class."""

from lessons.CQ07.point import Point

my_point: Point = Point(4.0, 5.0)

print(my_point.scale_by(10))
print(my_point.scale(8))