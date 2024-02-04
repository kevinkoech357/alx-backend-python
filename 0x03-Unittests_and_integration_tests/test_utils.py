#!/usr/bin/env python3

"""
Testing access_nested_map func.
"""


from utils import access_nested_map, get_json
from parameterized import parameterized
import unittest
from unittest.mock import patch, Mock


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


class TestGetJson(unittest.TestCase):
    """
    Test class for the get_json function.
    """

    @patch("utils.requests.get")
    @parameterized.expand(
        [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]
    )
    def test_get_json(self, test_url, test_payload):
        """
        Test that get_json returns the expected
        result with mocked requests.get.
        """
        # Create a mock response object
        mock_response = Mock()
        mock_response.json.return_value = test_payload

        # Mock the requests.get method to return the mock response
        with patch("utils.requests.get",
                   return_value=mock_response) as mock_get:
            result = get_json(test_url)

        # Test that the mocked get method was called exactly once
        mock_get.assert_called_once_with(test_url)

        # Test that the output of get_json is equal to test_payload.
        self.assertEqual(result, test_payload)
