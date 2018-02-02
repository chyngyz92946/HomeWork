import vk_api
import time

vk = vk_api.VkApi(token='3881b2fa09a292b0e7ebcb2ade126f78f99768cbc3698aca4583fb12bd220628e99b6d61002bf2cc3e7b1')
vk._auth_token()

values = {'out': 0, 'count': 100, 'time_offset': 60}
response = vk.method('messages.get', values)


def write_msg(user_id, s):
    vk.method('messages.send', {'user_id': user_id, 'message': s})


while True:
    response = vk.method('messages.get', values)
    if response['items']:
        values['last_message_id'] = response['items'][0]['id']
    for item in response['items']:
        if response['items'][0]['body'] == 'Привет':
            write_msg(item['user_id'], 'И тебе Привет! Давай сыграем! Нажми 1, если хочешь играть. Нажми 2 если не хочешь')
        elif response['items'][0]['body'] == '1':
            write_msg(item['user_id'], 'Не лает, не кусает, а в дом не пускает?')
        elif response['items'][0]['body'] == '2':
            write_msg(item['user_id'], 'Ладно :c Если захочешь поиграть, напиши 1')
        else:
            write_msg(item['user_id'], 'Я тебя не понимаю. Напиши 1 или 2 :3')

    time.sleep(1)