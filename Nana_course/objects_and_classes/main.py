from user import User
from post import Post

user_one = User("b.yushenkov@gmail.com", "Boris Yushenkov", "pwd_b", "Data Engineer")
user_one.get_user_info()

user_one.change_title("Lazy Boy")
user_one.get_user_info()

new_post = Post("secret message", user_one.name)
new_post.get_post_info()