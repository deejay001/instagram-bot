from instapy import InstaPy
from tkinter import *
from tkinter import ttk
import tkinter.font as tkfont
from tkinter import scrolledtext

# Gui


class Instabot_automation(object):

    def __init__(self):
        self.username = Page1().username_t.get()
        self.password = Page1().password_t.get()

        username = self.username
        password = self.password

        self.session = InstaPy(username=username, password=password)

        self.a_type = Page2().account_type
        self.subject = Page2().subject_b.get()
        self.to_follow = Page2().follow_list.get(1)

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

    def get_tags(self):
        subject = self.subject

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
        to_follow = self.to_follow

        if to_follow:
            to_follow_l = to_follow.split(",")
            follow_list = []

            for i in range(len(to_follow_l)):
                to_follow_p = to_follow_l[i]
                follow_list.append(to_follow_p)

            num = len(follow_list)

            session.follow_by_list(follow_list, amount=num, sleep_delay=600, interact=False)

        tags = self.get_tags()
        session.follow_by_tags(tags, amount=10)
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


class Page(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)

    def show(self):
        self.lift()


class Page1(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        bg_color = "#435d54"
        header = tkfont.Font(family="Bahnschrift SemiBold", size=20)
        sub_heading = tkfont.Font(family="Sans Serif", size=20)

        canvas1 = Canvas(self, width=400, height=500, bg=bg_color)
        h_label = Label(canvas1, text="Instabot automator\n"
                                      "by D_code", font=header, background=bg_color)
        s_canvas1 = Canvas(canvas1, height=400, width=300, bg="#334b43", borderwidth=0.1, relief="sunken")

        canvas1.create_window(200, 40, window=h_label)
        canvas1.create_window(200, 280, window=s_canvas1)

        username_l = Label(s_canvas1, text="Username", font=sub_heading, bg="#334b43", fg="White")
        self.username_t = Entry(s_canvas1, width=20, bg="White", font=tkfont.Font(size=19))
        password_l = Label(s_canvas1, text="Password", font=sub_heading, bg="#334b43", fg="White")
        self.password_t = Entry(s_canvas1, width=20, bg="White", font=tkfont.Font(size=19))
        self.start_button = Button(s_canvas1, text="OK", width=15, font=tkfont.Font(size=10), height=2)

        s_canvas1.create_window(70, 30, window=username_l)
        s_canvas1.create_window(150, 80, window=self.username_t)
        s_canvas1.create_window(70, 150, window=password_l)
        s_canvas1.create_window(155, 200, window=self.password_t)
        s_canvas1.create_window(150, 350, window=self.start_button)

        canvas1.pack(side="top", fill="both", expand=True)


class Page2(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        button_font = tkfont.Font(family="RockWell", size=18)
        header_font = tkfont.Font(family="Bahnschrift SemiBold", size="20")
        sub_heading = tkfont.Font(family="Sans Serif", size=16)
        radio_font = tkfont.Font(family="RockWell", size=15)

        canvas2 = Canvas(self, width=400, height=500, bg="White")
        canvas2.pack(side="top", fill="both", expand=True)

        header_l = Label(canvas2, text="Options", font=header_font, bg="White")
        self.start_button = Button(canvas2, text="Start Bot", width=50, font=button_font, bg="dark Green")
        option_canvas = Canvas(canvas2, width=350, height=400, highlightbackground="dark green")

        canvas2.create_window(200, 480, window=self.start_button)
        canvas2.create_window(200, 15, window=header_l)
        canvas2.create_window(200, 250, window=option_canvas)

        type_l = Label(option_canvas, text="Account type", font=sub_heading)
        self.account_type = StringVar()
        account_type = self.account_type
        personal = Radiobutton(option_canvas, text="Personal", variable=account_type, value="personal", font=radio_font)
        business = Radiobutton(option_canvas, text="Business", variable=account_type, value="business", font=radio_font)

        subject_l = Label(option_canvas, text="Account subject:", font=sub_heading)
        subject_list = ["cars", "cloths", "computer", "engineer", "art"]
        self.subject_b = ttk.Combobox(option_canvas, width=10, values=subject_list)

        follow_l = Label(option_canvas, text="People you want to follow(optional)", font=tkfont.Font(size=12))
        self.follow_list = scrolledtext.ScrolledText(option_canvas, height=11, width=40, highlightbackground="Green")

        option_canvas.create_window(80, 25, window=type_l)
        option_canvas.create_window(80, 65, window=personal)
        option_canvas.create_window(200, 65, window=business)
        option_canvas.create_window(100, 130, window=subject_l)
        option_canvas.create_window(250, 130, window=self.subject_b)
        option_canvas.create_window(140, 180, window=follow_l)
        option_canvas.create_window(180, 300, window=self.follow_list)


class MainView(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)

        self.p1 = Page1(self)
        self.p2 = Page2(self)

        p1 = self.p1
        p2 = self.p2

        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        button1 = p1.start_button
        button2 = p2.start_button

        button1.configure(command=p2.lift)
        button2.configure(command=p1.lift)

        p1.show()


if __name__ == "__main__":
    root = Tk()
    root.title("Instabot Automation")
    root.geometry("400x500")
    root.resizable(width=False, height=False)

    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)

    root.mainloop()
