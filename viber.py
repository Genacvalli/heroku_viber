# # from viberbot import Api
# # from viberbot.api.bot_configuration import BotConfiguration
# # from viberbot.api.messages import TextMessage

# # auth_token = "50a753ee3227e3f2-e915355bb9bdb270-30545f3fd86c6b73"
# # bot_configuration = BotConfiguration(
# #     name='Smm plus',
# #     avatar='https://dl-media.viber.com/1/share/2/long/vibes/icon/image/0x0/9697/a28c32e2c9fd78bfc6e2c4a4094b07039f88596a589b5ae5e7aa7bb59e719697.jpg',
# #     auth_token=auth_token
# # )
# # viber = Api(bot_configuration)
# # receiver_id = 'receiver_user_id'
# # message = TextMessage(text='Hello, World!')
# # viber.send_messages(receiver_id, [message])

import requests

auth_token = "50a753ee3227e3f2-e915355bb9bdb270-30545f3fd86c6b73"

phone_number = "380990230507"

url = "https://chatapi.viber.com/pa/get_online"

headers = {"Content-Type": "application/json",
           "X-Viber-Auth-Token": auth_token}

data = {"id": phone_number}

response = requests.post(url, headers=headers, json=data)
print(response.text)
if response.status_code == 200:
    data = response.json()
    subscribed = data['status'] == 0
    print("User {} is{} subscribed to Viber".format(phone_number, "" if subscribed else " not"))
else:
    print("Error checking Viber subscription status: {}".format(response.text))


# from viberbot import Api
# from viberbot.api.bot_configuration import BotConfiguration
# from viberbot.api.messages import (
#     TextMessage,
#     ContactMessage,
#     PictureMessage,
#     VideoMessage
# )
# from viberbot.api.messages.data_types.contact import Contact

# bot_configuration = BotConfiguration(
# 	name='Smm plus',
# 	avatar='https://dl-media.viber.com/1/share/2/long/vibes/icon/image/0x0/9697/a28c32e2c9fd78bfc6e2c4a4094b07039f88596a589b5ae5e7aa7bb59e719697.jpg',
# 	auth_token='50a753ee3227e3f2-e915355bb9bdb270-30545f3fd86c6b73'
# )
# viber = Api(bot_configuration)

# if not viber.verify_signature(request.get_data(), request.headers.get('X-Viber-Content-Signature')):
#    return Response(status=403)

# # creation of text message
# text_message = TextMessage(text="sample text message!")

# # creation of contact message
# contact = Contact(name="Viber user", phone_number="380934855600")
# contact_message = ContactMessage(contact=contact)

# # creation of picture message
# picture_message = PictureMessage(text="Check this", media="http://site.com/img.jpg")

# # creation of video message
# video_message = VideoMessage(media="http://mediaserver.com/video.mp4", size=4324)
# @app.route('/', methods=['POST'])
# def incoming():
# 	viber_request = viber.parse_request(request.get_data())

# 	if isinstance(viber_request, ViberConversationStartedRequest) :
# 		viber.send_messages(viber_request.get_user().get_id(), [
# 			TextMessage(text="Welcome!")
# 		])

# 	return Response(status=200)