#!/usr/bin/env python
# encoding: utf-8

import itchat


@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    return msg.text


if __name__ == "__main__":
    itchat.auto_login()
    itchat.run()
