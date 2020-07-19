# Non GUI

from instapy import InstaPy


class Instabot_automation(object):

    def __init__(self):
        self.session = InstaPy(username="d_code01", password="python3.8")
        self.subject = "cars"  # you can change the subject i just set it to cars

    def __repr__(self):
        self.login()

    def login(self):
        session = self.session
        session.login()
        session.set_quota_supervisor(enabled=True,
                                     sleep_after=["likes", "comments_d", "follows", "unfollows", "server_calls_h"],
                                     sleepyhead=True, stochastic_flow=True, notify_me=True,
                                     peak_likes_hourly=57,
                                     peak_likes_daily=585,
                                     peak_comments_hourly=21,
                                     peak_comments_daily=182,
                                     peak_follows_hourly=48,
                                     peak_follows_daily=None,
                                     peak_unfollows_hourly=35,
                                     peak_unfollows_daily=402,
                                     peak_server_calls_hourly=None,
                                     peak_server_calls_daily=4700)
        self.follow(session)

    def get_tags(self, subject):

        tags = []

        if subject == "cars":
            tags = ["#cars", "#benz", "#mercedes", "#Ferari", "#Automobile", "Porshe", "#Tesla"]
        if subject == "cloths":
            tags = ["#clothings", "#Offwhite", "#Palm Angels", "#Loius Vuitton"]
        if subject == "computer":
            tags = ["#computer", "#hardware", "#Apple", "#Microsoft"]
        if subject == "engineer":
            tags = ["#engineer"]
        if subject == "art":
            tags = ["#arts", "#creative art", "#mural paintings"]

        return tags

    def follow(self, session):

        tags = self.get_tags(self.subject)
        session.follow_by_tags(tags, amount=10)  # Follows the people that uses these hashtages on their posts
        session.set_do_like(True, percentage=70)

        session.set_user_interact(amount=3, percentage=32, randomize=True, media="Photo")
        session.follow_likers(tags, photos_grab_amount=2, follow_likers_per_photo=3, randomize=True,
                              sleep_delay=600, interact=True)
        session.unfollow_users(amount=20, nonFollowers=True, style="RANDOM", unfollow_after=72*60*60, sleep_delay=600)

        session.like_by_feed(amount=100, randomize=True, unfollow=True, interact=True)
        session.set_comments(['Nice!', "Awesome", "I like your stuff", "Cool!", "Great content: heart_eyes"],
                             media="Photo")
        session.set_do_comment(True, percentage=30)

        session.end()


if __name__ == "__main__":
    Instabot_automation().__repr__()