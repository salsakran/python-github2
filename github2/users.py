from github2.core import BaseData, GithubCommand, Attribute, DateAttribute
import urllib
from repositories import Repository

class User(BaseData):
    id = Attribute("The user id")
    login = Attribute("The login username")
    name = Attribute("The users full name")
    company = Attribute("Name of the company the user is associated with")
    location = Attribute("Location of the user")
    email = Attribute("The users e-mail address")
    blog = Attribute("The users blog")
    following_count = Attribute("Number of other users the user is following")
    followers_count = Attribute("Number of users following this user")
    public_gist_count = Attribute(
                            "Number of active public gists owned by the user")
    public_repo_count = Attribute(
                        "Number of active repositories owned by the user")
    total_private_repo_count = Attribute("Number of private repositories")
    collaborators = Attribute("Number of collaborators")
    disk_usage = Attribute("Currently used disk space")
    owned_private_repo_count = Attribute("Number of privately owned repos")
    private_gist_count = Attribute(
        "Number of private gists owned by the user")
    plan = Attribute("Current active github plan")

    def is_authenticated(self):
        return self.plan is not None

    def __repr__(self):
        return "<User: %s>" % (self.login)


class Users(GithubCommand):
    domain = "users"

    def show(self, username):
        return self.get_value("", username, datatype=User)

    def followers(self, username):
        return self.make_request(username, "followers")

    def following(self, username):
        return self.make_request(username, "following")

    def follow(self, other_user):
        return self.make_request("follow", other_user)

    def unfollow(self, other_user):
        return self.make_request("unfollow", other_user)
    def repos(self, username):
        return self.make_request(username, "repos")
    def watching(self,username):
        return self.make_request(username, "watched")

class LegacySearch(GithubCommand):
    domain = 'legacy'
    def user(self, query,page=1):
        return self.get_values("user/search", urllib.quote_plus(query), filter="users", datatype=User)

    def user_by_email(self, query,page=1):
        return self.get_value("user/email", query, filter="user", datatype=User)
    def repo(self, query,page=1):
        return self.get_values("repos/search", urllib.quote_plus(query), filter="repositories", get_data = {'start_page':page})
