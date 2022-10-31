import pytest
from linked_list import LinkedList


def test_linked_list_constructor():
    ll = LinkedList(8)
    assert ll.head == ll.tail
    assert ll.head.value == 8 == ll.tail.value
    assert ll.length == 1


@pytest.fixture
def ll() -> LinkedList:
    return LinkedList(100)


@pytest.mark.parametrize(
    "values",
    [([8]), ([1, 2]), ([77, 1.0, 0.99, -1.72])],
)
def test_append(values, ll: LinkedList):
    [ll.append(value) for value in values]

    assert ll.length == int(1 + len(values))
    assert ll.head.value == 100
    assert ll.tail.value == values[-1]


def test_append_to_empty_list(ll: LinkedList):
    ll.pop()
    assert ll.length == 0

    ll.append(101)

    assert ll.length == 1
    assert ll.head.value == 101 == ll.tail.value


@pytest.mark.parametrize(
    "values_to_append, length", [([1, 27, 8698, 0.23], 4), (None, 0), ([1, 2], 2)]
)
def test_pop(ll: LinkedList, values_to_append, length):
    if values_to_append:
        [ll.append(value) for value in values_to_append]
    ll.pop()
    assert ll.length == length


def test_pop_from_empty_list(ll: LinkedList):
    ll.length = 0
    with pytest.raises(ValueError):
        ll.pop()


@pytest.mark.parametrize(
    "values_to_append, expected_value",
    [([1, 27, 8698, 0.23], 8698), (None, None), ([1, 2], 1)],
)
def test_penultimate_node(ll: LinkedList, values_to_append, expected_value):
    if values_to_append:
        [ll.append(value) for value in values_to_append]

    if expected_value:
        assert ll.penultimate_node.value == expected_value
    else:
        assert ll.penultimate_node is None


def test_prepend_when_one_node_in_list(ll: LinkedList):
    ll.prepend(12)

    assert ll.length == 2
    assert ll.head.value == 12
    assert ll.tail.value == 100  # the default from fixture


def test_prepend_with_many_nodes_in_the_list(ll: LinkedList):
    assert ll.length == 1
    [ll.append(value) for value in [1, 2, 3, 4, 5]]

    ll.prepend(12)
    ll.prepend(13)

    assert ll.length == 8
    assert ll.head.value == 13
    assert ll.head.next.value == 12
    assert ll.tail.value == 5


def test_prepend_when_list_empty(ll: LinkedList):
    ll.pop()

    ll.prepend(12)

    assert ll.head == ll.tail
    assert ll.head.value == 12 == ll.tail.value


def test_pop_first_when_one_node_in_list(ll: LinkedList):
    ll.pop_first()
    assert ll.length == 0
    assert ll.head is None is ll.tail


def test_pop_first_list_empty(ll: LinkedList):
    ll.length = 0
    with pytest.raises(ValueError):
        ll.pop_first()


@pytest.mark.parametrize("pop_times", [1, 2, 3, 4, 5])
def test_pop_first(ll: LinkedList, pop_times):
    [ll.append(value) for value in [1, 2, 3, 4, 5]]
    for _ in range(pop_times):
        ll.pop_first()

    expected_value = pop_times  # the head value before popping is 100
    assert ll.head.value == expected_value
