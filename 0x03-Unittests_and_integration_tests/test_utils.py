#!/usr/bin/env python3
""" Generic utilities for github org client."""


import unittest
from typing import Mapping, Sequence
from parameterized import parameterized
from unittest.mock import patch, MagicMock
from utils import access_nested_map, get_json


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

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence, expected:
                                         any) -> None:
        """ Test access_nested_map function."""
        with self.assertRaises(expected):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """ Test get_json function."""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})])
    @patch('requests.get')
    def test_get_json(self, test_url: str, test_payload: dict,
                      mock_get: MagicMock) -> None:
        """ Test get_json function."""
        mock_get.return_value.json.return_value = test_payload
        self.assertEqual(get_json(test_url), test_payload)
        mock_get.assert_called_once_with(test_url)


if __name__ == "__main__":
    unittest.main()
