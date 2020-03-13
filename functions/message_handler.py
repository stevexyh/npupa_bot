#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
* File Name    : message_handler.py
* Description  : Handle user's messages
* Create Time  : 2020-03-13 12:15:41
* Version      : 1.0
* Author       : Steve X
* GitHub       : https://github.com/Steve-Xyh
'''


from telegram.ext import MessageHandler, Filters

PARSE_MODE = 'MarkdownV2'


def bot_print(update, text):
    """向聊天窗口发消息"""
    try:
        text = text.replace('-', '\-').replace('.', '\.').replace('!', '\!')
        update.message.reply_text(text, parse_mode=PARSE_MODE)
    except:
        text += '\n' + '-'*10 + '\nMarkdown解析失败, 显示原始文本'
        update.message.reply_text(text)


def echo(update, context):
    """Echo the user message."""
    bot_print(update, update.message.text)


def init_message(dp):
    # on noncommand i.e message - echo the message on Telegram
    # dp.add_handler(MessageHandler(Filters.text, echo))
    pass
