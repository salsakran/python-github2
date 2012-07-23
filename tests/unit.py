# -*- coding: latin-1 -*-
import unittest

from github2.issues import Issue
from github2.client import Github


class ReprTests(unittest.TestCase):
    """__repr__ must return strings, not unicode objects."""

    def test_issue(self):
        """Issues can have non-ASCII characters in the title."""
        i = Issue(title = u'abcdé')
        self.assertEqual(str, type(repr(i)))


       
class UserAPI(unittest.TestCase):
    """
        test out the apis for users
    """
    def test_get(self):
        client = Github()
        res = client.users.show('defunkt')
        self.assertNotEqual(res, None)
    
    def test_serialize(self):
        client = Github()
        res = dict(client.users.show('defunkt'))
        self.assertNotEqual(res, None)

    def test_followers(self):
        client = Github()
        res = client.users.followers('defunkt')
        self.assertNotEqual(res, None)
        self.assertNotEqual(len(res), 0)
    def test_following(self):
        client = Github()
        res = client.users.following('defunkt')
        self.assertNotEqual(res, None)
        self.assertNotEqual(len(res), 0)
    def test_search_by_email(self):
        client = Github()
        res = client.search.user_by_email('chris@github.com')
        print res
        self.assertNotEqual(res, None)
    def test_search_by_name(self):
        client = Github()
        res = client.search.user('Wanstrath')
        print res
        self.assertNotEqual(res, None)


class RepoAPI(unittest.TestCase):
    """
        test apis for repos
    """
    def test_search(self):
        client = Github()
        res = client.search.repo('rails')
        self.assertNotEqual(res, None)

    def test_get(self):
        client = Github()
        res = client.repos.show('rails/rails')
        self.assertNotEqual(res, None)
    def test_languages(self):
        client = Github()
        res = client.repos.languages('rails/rails')
        self.assertNotEqual(res, None)
    def test_contributors(self):
        client = Github()
        res = client.repos.list_contributors('rails/rails')
        self.assertNotEqual(res, None)
    def test_user_repos(self):
        client = Github()
        res = client.users.repos('rails')
        self.assertNotEqual(res, None)
    def test_watching(self):
        client = Github()
        res = client.users.watching('defunkt')
        self.assertNotEqual(res, None)
