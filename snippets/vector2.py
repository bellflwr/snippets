from __future__ import annotations

from math import acos, atan2, sqrt
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterator


class Vector2:
    __x: float
    __y: float

    __slots__ = "__x", "__y"

    def __init__(self, x: float, y: float):
        self.__x = x
        self.__y = y

    @property
    def x(self) -> float:
        return self.__x

    @property
    def y(self) -> float:
        return self.__y

    def is_zero(self) -> bool:
        return self.__x == 0 and self.__y == 0

    def square_magnitude(self) -> float:
        return self.__x * self.__x + self.__y * self.__y

    def magnitude(self) -> float:
        return sqrt(self.__x * self.__x + self.__y * self.__y)

    def normalized(self) -> Vector2:
        if self.is_zero():
            raise ValueError("Cannot normalize zero-vector.")

        return self / self.magnitude()

    def dot(self, other: Vector2) -> float:
        return self.__x * other.x + self.__y * other.y

    def cross(self, other: Vector2) -> float:
        return self.__x * other.y - self.__y * other.x

    def angle(self) -> float:
        """Angle of the vector in standard position."""

        if self.is_zero():
            raise ValueError("Cannot get angle of zero-vector.")

        return atan2(self.__y, self.__x)

    def angle_between(self, other: Vector2) -> float:
        """Smallest angle between two vectors."""

        if self.is_zero() or other.is_zero():
            raise ValueError("Cannot get angle of zero-vector.")

        return acos(self.dot(other) / (self.magnitude() * other.magnitude()))

    def distance(self, other: Vector2) -> float:
        return (other - self).magnitude()

    def updated(self, x: float | None = None, y: float | None = None) -> Vector2:
        new_x = self.__x if x is None else x
        new_y = self.__y if y is None else y

        return Vector2(new_x, new_y)

    def __repr__(self) -> str:
        return f"Vector2(x={self.__x}, y={self.__y})"

    def __str__(self) -> str:
        return self.__repr__()

    def __eq__(self, other: object) -> bool:
        match other:
            case Vector2():
                return self.__x == other.x and self.__y == other.y
            case _:
                raise TypeError(f'Vector2 cannot be compared to type "{type(other)}".')

    def __bool__(self) -> bool:
        return self.is_zero()

    def __len__(self) -> int:
        return 2

    def __hash__(self) -> tuple[float, float]:  # type: ignore[override]
        return (self.x, self.y)

    def __add__(self, other: object) -> Vector2:
        match other:
            case Vector2():
                return Vector2(self.__x + other.x, self.__y + other.y)
            case _:
                raise TypeError(f'Type "{type(other)}" cannot be added to Vector2.')

    def __sub__(self, other: object) -> Vector2:
        match other:
            case Vector2():
                return Vector2(self.__x - other.x, self.__y - other.y)
            case _:
                raise TypeError(
                    f'Type "{type(other)}" cannot be subtracted from Vector2.'
                )

    def __mul__(self, other: object) -> Vector2:
        match other:
            case float():
                return Vector2(self.__x * other, self.__y * other)
            case Vector2():
                raise TypeError(
                    "Vector products should be calculated "
                    "with the Vector2.dot() method."
                )
            case _:
                raise TypeError(
                    f'Vector2 cannot be multiplied by type "{type(other)}".'
                )

    def __truediv__(self, other: object) -> Vector2:
        match other:
            case float():
                return Vector2(self.__x / other, self.__y / other)
            case _:
                raise TypeError(f'Vector2 cannot be divided by type "{type(other)}".')

    def __neg__(self) -> Vector2:
        return Vector2(-self.__x, -self.__y)

    def __abs__(self) -> float:
        return self.magnitude()

    def __getitem__(self, idx: int) -> float:
        if idx == 0:
            return self.__x
        elif idx == 1:
            return self.__y
        else:
            raise IndexError(
                f"Vector2 only has indicies [0, 1] for attributes [x, y], not {idx}."
            )

    def __iter__(self) -> Iterator[float]:
        return iter((self.__x, self.__y))

    def __copy__(self) -> Vector2:
        return Vector2(self.__x, self.__y)
