import random

class User:
    def __init__(self, name):
        self.name = name
        self.post = []
        self.followers = 0
        self.comment=0
        self.likes=0

    def add_post(self, content):
        self.post.append(content)
        self.followers += random.randint(1, 15)
        self.comment += random.randint(1, 5)
        self.likes += random.randint(1, 50)

    def status(self):
        print(f"{self.name} has {len(self.post)} posts and {self.followers} followers")
        print(f"the posts got {self.likes} likes and {self.comment} comments")


name = input("Enter your username: ")
user = User(name)

while True:
    user_choice = input("do you want to post? (yes/no) ")
    if user_choice == "yes":
        content = input("write your post: ")
        user.add_post(content)
    else:
        break

user.status()
