import pytest
from data_structures.linked_list import LinkedList


def test_exists():
    assert LinkedList


# @pytest.mark.skip("TODO")
def test_instantiate():
    assert LinkedList()


# @pytest.mark.skip("TODO")
def test_empty_head():
    linked = LinkedList()
    assert linked.head is None


# @pytest.mark.skip("TODO")
def test_populated_head():
    linked = LinkedList()
    linked.insert("apple")
    assert linked.head.value == "apple"


# @pytest.mark.skip("TODO")
def test_to_string_empty():
    linked_list = LinkedList()

    assert str(linked_list) == "NULL"


# @pytest.mark.skip("TODO")
def test_to_string_single():
    linked_list = LinkedList()

    linked_list.insert("apple")

    assert str(linked_list) == "{ apple } -> NULL"


# @pytest.mark.skip("TODO")
def test_to_string_double():
    linked_list = LinkedList()

    linked_list.insert("apple")

    assert str(linked_list) == "{ apple } -> NULL"

    linked_list.insert("banana")

    assert str(linked_list) == "{ banana } -> { apple } -> NULL"


# @pytest.mark.skip("TODO")
def test_includes_true():
    linked_list = LinkedList()

    linked_list.insert("apple")

    linked_list.insert("banana")

    assert linked_list.includes("apple")


# @pytest.mark.skip("TODO")
def test_includes_false():
    linked_list = LinkedList()

    linked_list.insert("apple")

    linked_list.insert("banana")

    assert not linked_list.includes("cucumber")


def test_append_mango():
    linked_list = LinkedList()

    linked_list.insert("apple")

    linked_list.insert("banana")

    linked_list.append("mango")

    actual = str(linked_list)

    expected = "{ banana } -> { apple } -> { mango } -> NULL"

    assert actual == expected


def test_insert_before_middle_node():
    linked_list = LinkedList()

    linked_list.insert("apple")

    linked_list.insert("banana")

    linked_list.append("mango")

    linked_list.insert_before("apple", "orange")

    actual = str(linked_list)

    expected = "{ banana } -> { orange } -> { apple } -> { mango } -> NULL"

    assert actual == expected


def test_insert_after_middle_node():
    linked_list = LinkedList()

    linked_list.insert("apple")

    linked_list.insert("banana")

    linked_list.append("mango")

    linked_list.insert_before("apple", "orange")

    linked_list.insert_after("apple", "grapes")

    actual = str(linked_list)

    expected = "{ banana } -> { orange } -> { apple } -> { grapes } -> { mango } -> NULL"

    assert actual == expected


def test_insert_before_first_node():
    linked_list = LinkedList()

    linked_list.insert("apple")

    linked_list.insert_before("apple", "orange")

    actual = str(linked_list)

    expected = "{ orange } -> { apple } -> NULL"
