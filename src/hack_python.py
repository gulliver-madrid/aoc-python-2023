from typing import (
    Any,
    Callable,
    Iterable,
    Iterator,
    Mapping,
    Sequence,
    TypeVar,
    Generic,
    overload,
)

T = TypeVar("T")
U = TypeVar("U")
V = TypeVar("V")


class G_List(Generic[T]):
    """Wrapper de iterable que permite usar metodos como map o filter"""

    data: Iterable[T] | None

    def __init__(self, data: Iterable[T]):
        self.data = iter(data)

    def map(self, f: Callable[[T], U]) -> "G_List[U]":
        assert self.data is not None
        data = self.data
        self.data = None
        return G_List(f(x) for x in data)

    def filter(self, f: Callable[[Any], Any]) -> "G_List[T]":
        assert self.data is not None
        data = self.data
        self.data = None
        return G_List(filter(f, data))

    def __iter__(self) -> Iterator[T]:
        assert self.data is not None
        data = self.data
        self.data = None
        return iter(data)

    def list(self) -> list[T]:
        return list(self)


class G_Dict(Generic[T, U]):
    """Wrapper de dict que permite usar metodos como map o filter"""

    data: dict[T, U] | None

    def __init__(self, data: dict[T, U]):
        self.data = data

    def map(self, f: Callable[[U], V]) -> "G_Dict[T, V]":
        assert self.data is not None
        return G_Dict({k: f(v) for k, v in self.data.items()})

    def filter(self, f: Callable[[U], Any]) -> "G_Dict[T, U]":
        assert self.data is not None
        return G_Dict({k: v for k, v in self.data.items() if f(v)})

    def dict(self) -> dict[T, U]:
        # nota: esto invalida el diccionario interno
        assert self.data is not None
        data = self.data
        self.data = None
        return data

    def __iter__(self) -> Iterator[tuple[T, U]]:
        # nota: esto invalida el diccionario interno
        assert self.data is not None
        data = self.data
        self.data = None
        return iter(data.items())

    def __eq__(self, other: object) -> bool:
        return isinstance(other, self.__class__) and self.data == other.data


@overload
def g(data: Mapping[T, U]) -> G_Dict[T, U]:
    ...


@overload
def g(data: Sequence[T] | Iterator[T]) -> G_List[T]:
    ...


def g(data: Sequence[T] | Iterator[T] | Mapping[T, U]) -> G_List[T] | G_Dict[T, U]:
    if isinstance(data, dict):
        return G_Dict(data)
    else:
        return G_List(data)
