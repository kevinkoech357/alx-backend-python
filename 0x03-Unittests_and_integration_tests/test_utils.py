#!/usr/bin/env python3

"""
Testing access_nested_map func.
"""


from utils import access_nested_map
from parameterized import parameterized
import unittest


class TestAccessNestedMap(unittest.TestCase):
    """
    Test class for the access_nested_map function.
    """

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(self, nested_map, path, expected_result):
        """
        Test the access_nested_map function with different inputs.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand(
        [
            ({}, ("a",), "'a'"),
            ({"a": 1}, ("a", "b"), "'b'"),
        ]
    )
    def test_access_nested_map_exception(
        self, nested_map, path, expected_exception_msg
    ):
        """
        Test that access_nested_map raises a KeyError for specific inputs.
        """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)

        self.assertIn(expected_exception_msg, str(context.exception))
