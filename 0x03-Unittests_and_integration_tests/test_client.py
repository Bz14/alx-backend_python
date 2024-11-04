#!/usr/bin/env python3
""" Test client module """
from client import GithubOrgClient
import unittest
from unittest.mock import patch, MagicMock
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """ TestGithubOrgClient class """

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json: MagicMock):
        """ TestGithubOrgClient.org method """
        test_org = GithubOrgClient(org_name)
        test_org.org()
        mock_get_json.called_with_once(test_org.ORG_URL.format(org=org_name))
