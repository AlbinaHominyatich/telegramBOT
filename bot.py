import requests
import random


url = "https://api.telegram.org/bot<токен>/"#не забудь свій токен!


def last_update(request):
    response = requests.get(request + 'getUpdates')
    response = response.json()
    results = response['result']
    total_updates = len(results) - 1
    return results[total_updates]


def get_chat_id(update):
    chat_id = update['message']['chat']['id']
    return chat_id


def get_message_text(update):
    message_text = update['message']['text']
    return message_text


def send_message(chat, text):
    params = {'chat_id': chat, 'text': text}
    response = requests.post(url + 'sendMessage', data=params)
    return response


def main():
    update_id = last_update(url)['update_id']
    while True:
        update = last_update(url)
        if update_id == update['update_id']:
            if get_message_text(update).lower() == 'привіт' or get_message_text(update).lower() == 'хай' or get_message_text(update).lower() == 'здоров!':
               send_message(get_chat_id(update), 'Вітаю!')
            elif get_message_text(update).lower() == 'кості':
               _1 = random.randint(1, 6)
               _2 = random.randint(1, 6)
               send_message(get_chat_id(update), 'У тебе ' + str(_1) + ' та ' + str(_2) + '!\nТвій результат ' + str(_1+_2) + '!')
            else:
                send_message(get_chat_id(update), 'Пробач, я не розумію тебе:(')
            update_id += 1


if __name__ == '__main__':
    main()
