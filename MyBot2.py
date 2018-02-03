import vk_api
import time

vk = vk_api.VkApi(token='69dc6fb58b768b8ec923cd0e0af553b5b0e574ec1853fe13e278da0780a6510771b92bd924ed0d8d6736f')
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
        if response['items'][0]['body'] == 'привет':
            write_msg(item['user_id'], 'И тебе Привет!\n Давай сыграем!\n Нажми 1, если хочешь играть. \nНажми 2 если не хочешь')
        elif response['items'][0]['body'] == '1':
            write_msg(item['user_id'], 'Не лает, не кусает,\n а в дом не пускает?')
        elif response['items'][0]['body'] == 'замок':
            write_msg(item['user_id'], 'Правильно!\n Зимой и летом одним цветом.')
        elif response['items'][0]['body'] == 'елка':
            write_msg(item['user_id'], 'Правильно!\n На лугу живет скрипач,\n Носит фрак и ходит вскачь.')
        elif response['items'][0]['body'] == 'кузнечик':
            write_msg(item['user_id'], 'Правильно!\n Под водой живёт народ, \nХодит задом наперёд')
        elif response['items'][0]['body'] == 'раки':
            write_msg(item['user_id'], 'Правильно!\n Ты угадал все загадки, Поздравляю!')
        elif response['items'][0]['body'] == '2':
            write_msg(item['user_id'], 'Ладно :c \nЕсли захочешь поиграть, напиши 1')
        else:
            write_msg(item['user_id'], 'Не правильно.\n Напиши 1 или 2 что бы сыграть :3')

    time.sleep(1)