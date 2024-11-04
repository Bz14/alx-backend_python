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

    @patch('client.get_json')
    def test_public_repos(self, mock_json):
        """Test TestGithubOrgClient.test_public_repos
        return the correct value
        """
        payloads = [{"name": "google"}, {"name": "Twitter"}]
        mock_json.return_value = payloads

        with patch('client.GithubOrgClient._public_repos_url') as mock_public:
            mock_public.return_value = "hey there!"
            test_class = GithubOrgClient('test')
            result = test_class.public_repos()

            expected = [p["name"] for p in payloads]
            self.assertEqual(result, expected)

            mock_json.called_with_once()
            mock_public.called_with_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """ TestGithubOrgClient.has_license method """
        test_org = GithubOrgClient('google')
        self.assertEqual(test_org.has_license(repo, license_key), expected)
