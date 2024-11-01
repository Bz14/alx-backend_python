#!/usr/bin/env python3
""" Generic utilities for github org client."""


import unittest
from typing import Mapping, Sequence
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """ Test access_nested_map function."""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)])
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence, expected: any) -> None:
        """ Test access_nested_map function."""
        self.assertEqual(access_nested_map(nested_map, path), expected)


if __name__ == "__main__":
    unittest.main()
