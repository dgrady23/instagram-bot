#READ THIS
#THIS CODE SHOULD NOT BE RUN MORE THAN ONCE PER HOUR OR BOT MAY BE BANNED

from time import sleep
from instabot import Bot

my_bot = Bot()

my_bot.login(username="packston123", password="packston")

sleep(20)

my_bot.follow("bigdovv5765")
#1 account
#--- my_bot.follow_users(["","",""])
#multiple follows


#my_bot.upload_photo("", caption= "wow this worked very cool")

sleep(503333)

my_bot.send_message("blahblahblah")

sleep(60333333)

my_bot.like_user("bigdovv5765", amount=2, filtration=False)

sleep(80555535)

user_id = my_bot.get_user_id_from_username
media_id = my_bot.get_last_user_medias(user_id, 1)
my_bot.comment(media_id[0], "wow very cool")


sleep(100090)

my_bot.logout()
