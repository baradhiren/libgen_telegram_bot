import json
import requests
import time
import urllib
import libgenapi
import FileInteractions

TOKEN = "560217157:AAGjIgiP8ZxAH3Bx8fJoYYW42MOBemTkE1w"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)
FileObj = FileInteractions.FileInteractions()
LIBGENOBJ = libgenapi.Libgenapi(FileObj.readmirrors())


def get_url(url):
    response = requests.get(url)
    content = response.content.decode('utf8')
    return content


def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js


def get_updates(offset=None):
    url = URL + "getupdates?timeout=100"
    if offset:
        url += "&offset={}".format(offset)
    js = get_json_from_url(url)
    return js


def get_last_chat_id_and_text(updates):
    num_updates = len(updates['result'])
    last_update = num_updates - 1
    text = updates['result'][last_update]['message']['text']
    chat_id = updates['result'][last_update]['message']['chat']['id']
    return text, chat_id


def send_message(text, chat_id):
    text = urllib.parse.quote_plus(text)
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    get_url(url)


def get_last_update_id(updates):
    update_ids = []
    for update in updates["result"]:
        update_ids.append(int(update["update_id"]))
    return max(update_ids)


def echo_all(updates):
    for update in updates["result"]:
        try:
            text = update["message"]["text"]
            chat = update["message"]["chat"]["id"]
            result = LIBGENOBJ.search(text)
            if result:
                for book in result:
                    bookresult = manage_book(book)
                    send_message(bookresult, chat)
            else:
                send_message("No books found by {} name.".format(text), chat)
        except Exception as e:
            print(e)


def manage_book(book):
    result_string = ''
    result_string += "Author: "
    if book['author'] is not None:
        result_string += book['author'] + '\n'
    result_string += "Title: "
    if book['title'] is not None:
        result_string += book['title'] + '\n'
    result_string += "Language: "
    if book['language'] is not None:
        result_string += book['language'] + '\n'
    result_string += "Extension: "
    if book['extension'] is not None:
        result_string += book['extension'] + '\n'
    result_string += "Edition: "
    if book['edition'] is not None:
        result_string += book['edition'] + '\n'
    result_string += "ISBN: "
    if book['isbn'] is not None:
        for isbn in book['isbn']:
            result_string += isbn + '\n'
    result_string += "Publisher: "
    if book['publisher'] is not None:
        result_string += book['publisher'] + '\n'
    result_string += "Series: "
    if book['series'] is not None:
        result_string += book['series'] + '\n'
    result_string += "Year: "
    if book['year'] is not None:
        result_string += book['year'] + '\n'
    result_string += "Pages: "
    if book['pages'] is not None:
        result_string += book['pages'] + '\n'
    result_string += "Size: "
    if book['size'] is not None:
        result_string += book['size'] + '\n'
    result_string += "Mirrors: "
    if book['mirrors'] is not None:
        for mirror in book['mirrors']:
            result_string += mirror + '\n'
    else:
        result_string += "No Mirrors found."

    return result_string


def main():
    last_update_id = None
    while True:
        updates = get_updates(last_update_id)
        if len(updates["result"]) > 0:
            last_update_id = get_last_update_id(updates) + 1
            echo_all(updates)
        time.sleep(0.5)


if __name__ == '__main__':
    main()
