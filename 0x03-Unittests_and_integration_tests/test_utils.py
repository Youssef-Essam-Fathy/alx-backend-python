#!/usr/bin/env python3
"""
Unit tests for the access_nested_map function.
"""

import unittest
from unittest.mock import (
    patch,
    Mock
  )
from utils import (
    access_nested_map,
    get_json
  )
from parameterized import parameterized
from typing import (
    Mapping,
    Sequence,
    Any,
)


class TestAccessNestedMap(unittest.TestCase):
    """
    Test cases for the access_nested_map function.

    Args:
        unittest.TestCase: The base class for unit tests in Python.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Mapping, path: Sequence,
                               expected: Any):
        """
        Test access_nested_map with various nested maps and paths.

        Args:
            nested_map (Mapping): The nested map to access.
            path (Sequence): The sequence of keys to access the nested value.
            expected (Any): The expected value from the nested map.

        Asserts:
            The value accessed from the nested map matches the expected value.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
      ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence):
        """
      Test access_nested_map with various nested maps and paths.

      Args:
          nested_map (Mapping): The nested map to access.
          path (Sequence): The sequence of keys to access the nested value.
          expected (Any): The expected value from the nested map.

      Asserts:
          The exception message from the nested map matches the expected value.

        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """_summary_

  Args:
      unittest (_type_): _description_
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url: str,
                      test_payload: dict, requests_get: Any):
        """_summary_

      Args:
          url (str): _description_
        """
        mock_url = Mock()
        mock_url.json.return_value = test_payload
        requests_get.return_value = mock_url

        result = get_json(test_url)

        requests_get.assert_called_once_with(test_url)

        self.assertEqual(test_payload, result)


if __name__ == "__main__":
    unittest.main()
