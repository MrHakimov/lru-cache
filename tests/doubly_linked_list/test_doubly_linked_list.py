import pytest

from lru_cache import DoublyLinkedList


@pytest.fixture
def init_list():
    return DoublyLinkedList()


def test_is_empty(init_list):
    assert init_list.is_empty()


def test_pop_left_on_empty_list(init_list):
    with pytest.raises(AssertionError):
        init_list.pop_left()


def test_pop_left_on_normal_list(init_list):
    init_list.put_right(1, 1)

    assert init_list.pop_left().value == 1
    assert init_list.is_empty()


def test_pop_right_on_empty_list(init_list):
    with pytest.raises(AssertionError):
        init_list.pop_right()


def test_pop_right_on_normal_list(init_list):
    init_list.put_right(1, 1)

    assert init_list.pop_right().value == 1
    assert init_list.is_empty()


def test_put_and_pops(init_list):
    init_list.put_right(1, 1)
    init_list.put_right(2, 2)
    init_list.put_right(3, 3)

    assert init_list.pop_left().value == 1
    assert init_list.pop_right().value == 3
    assert init_list.pop_right().value == 2

    with pytest.raises(AssertionError):
        init_list.pop_left()

    with pytest.raises(AssertionError):
        init_list.pop_right()

    assert init_list.is_empty()

    init_list.put_left(2, 2)
    init_list.put_right(3, 3)
    init_list.put_left(1, 1)

    assert init_list.pop_right().value == 3
    assert init_list.pop_right().value == 2
    assert init_list.pop_right().value == 1

    with pytest.raises(AssertionError):
        init_list.pop_left()

    with pytest.raises(AssertionError):
        init_list.pop_right()

    assert init_list.is_empty()
