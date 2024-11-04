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

    def test_public_repos_url(self):
        """ TestGithubOrgClient._public_repos_url method """
        test_org = GithubOrgClient('google')
        with patch('client.GithubOrgClient.org') as mock:
            mock.return_value = {'repos_url': 'http://example.com'}
            self.assertEqual(test_org._public_repos_url, 'http://example.com')

    def test_public_repos(self):
        """ TestGithubOrgClient.public_repos method """
        test_org = GithubOrgClient('google')
        with patch('client.GithubOrgClient.repos_payload') as mock:
            mock.return_value = [{'name': 'repo1'}, {'name': 'repo2'}]
            self.assertEqual(test_org.public_repos(), ['repo1', 'repo2'])
            self.assertEqual(test_org.public_repos('MIT'), ['repo1', 'repo2'])
