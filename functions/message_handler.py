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

import random
from telegram.ext import MessageHandler, Filters

PARSE_MODE = 'MarkdownV2'


def bot_print(update, text):
    """向聊天窗口发消息"""
    try:
        text = text.replace('-', '\-').replace('.', '\.').replace('!', '\!').replace('=', '\=')
        update.message.reply_text(text, parse_mode=PARSE_MODE)
    except:
        text += '\n' + '-'*10 + '\nMarkdown解析失败, 显示原始文本'
        update.message.reply_text(text)


def bot_print_replace_all(text):
    """(暂时不用)将所有符号转义输出"""
    res = text.replace('_', '\_').replace('*', '\*').replace('[', '\[').replace(']', '\]').replace('(', '\(').replace(')', '\)').replace('~', '\~').replace('`', '\`').replace(
        '>', '\>').replace('#', '\#').replace('+', '\+').replace('-', '\-').replace('=', '\=').replace('|', '\|').replace('{', '\{').replace('}', '\}').replace('.', '\.').replace('!', '\!')
    print(res)


def echo(update, context):
    """复读机"""
    bot_print(update, update.message.text)


def answer(update, context):
    """人工智障回答问题"""
    message = update.message.text

    dic = {
        # 从后往前, 标点>长词>短词的优先级替换, 不可乱序
        '？': '',
        '?': '',
        '好吗': '',
        '好嘛': '',
        '吗': '',
        '嘛': '',
        '马': '',
        '么': '',
    }

    is_query = False
    for word in dic:
        pos = message.find(word)
        if (pos != -1) and (len(message) - pos - len(word) == 0):
            message = message.replace(word, dic[word])
            is_query = True

    if is_query:
        ans = random.randint(0, 1)
        if ans:
            message = random.choice(
                ['好,', '好的,', '好呀,', '好呀!', '可以鸭,']) + message
        else:
            message = random.choice(['不行', '不可以', '拒绝'])

        bot_print(update, message)
    else:
        return


def init_message(dp):
    # on noncommand i.e message - echo the message on Telegram
    # dp.add_handler(MessageHandler(Filters.text, echo))
    dp.add_handler(MessageHandler(Filters.text, answer))
    # pass
