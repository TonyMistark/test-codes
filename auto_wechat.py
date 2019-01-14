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
    return get_reply_data(url).get("text", "不懂你在说啥？")


if __name__ == "__main__":
    itchat.auto_login()
    friends = itchat.get_friends(update=True)[0:]
    print("friends-->", friends[0])
    name = {}
    nickname = []
    user = []
    females = []
    males = []
    unknown = []
    sex = set()
    for i in range(len(friends)):
        nickname.append(friends[i]["NickName"])
        user.append(friends[i]["UserName"])
        print(friends[i]["UserName"], friends[i]["Sex"])
        if friends[i]["Sex"] == 0:
            females.append(friends[i]["NickName"])
        elif friends[i]["UserName"] == 1:
            males.append(friends[i]["NickName"])
        else:
            unknown.append(friends[i]["NickName"])
    print("==============>females:\n", females)
    print("==============>males:\n", males)
    print("==============>unknown:\n", unknown)
    print(
        "男：",
        len(males),
        len(males) / len(friends),
        "女: ",
        len(females),
        len(females) / len(friends),
        "未知：",
        len(unknown),
        len(unknown) / len(friends),
    )
    print(sex)
    for i in range(len(friends)):
        name[nickname[i]] = user[i]

    # itchat.run()
