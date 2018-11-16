#!/usr/bin/env python
# encoding: utf-8

import itchat
import requests
import json


def get_reply_data(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return json.loads(r.text)
    except:
        return {}


@itchat.msg_register(["Text", "Map", "Card", "Note", "Sharing", "Picture"])
def text_reply(msg):
    url = (
        "http://www.tuling123.com/openapi/api?key=9dd33d6c10694a34b3de086e1d1c9603&info=%s"
        % msg["Text"]
    )
    response_msg = get_reply_data(url).get("text", "不懂你在说啥？")
    print(
        "%s: %s"
        % (
            msg["User"].get("RemarkName") or msg["User"].get("NickName", "someone"),
            msg.get("Text", ""),
        )
    )
    print("reply: %s" % response_msg)
    return response_msg


if __name__ == "__main__":
    itchat.auto_login()
    friends = itchat.get_friends(update=True)[0:]
    name = {}
    nickname = []
    user = []
    for i in range(len(friends)):
        nickname.append(friends[i]["NickName"])
        user.append(friends[i]["UserName"])
    for i in range(len(friends)):
        name[nickname[i]] = user[i]
    itchat.run()
