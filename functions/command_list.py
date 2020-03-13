#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
* File Name    : command_list.py
* Description  : Handle all the commands
* Create Time  : 2020-03-13 12:14:23
* Version      : 1.0
* Author       : Steve X
* GitHub       : https://github.com/Steve-Xyh
'''


from telegram.ext import CommandHandler
from .message_handler import bot_print

commands = '''
*技能表*
--------------------
*
/help - 技能表
/ying - 嘤
/meow - 喵
/poem - 念诗
/secret - 告诉你一个秘密
*
'''

# Define a few command handlers. These usually take the two arguments update and context.


def start(update, context):
    """Send a message when the command /start is issued."""
    bot_print(update, 'Hi!')


def help_list(update, context):
    """Send a message when the command /help is issued."""
    bot_print(update, commands)


def ying(update, context):
    """Send a message when the command /ying is issued."""
    bot_print(update, '嘤嘤嘤, 这里是小嘤')


def meow(update, context):
    """Send a message when the command /meow is issued."""
    bot_print(update, '喵喵喵=￣ω￣=')


def poem(update, context):
    """Send a message when the command /poem is issued."""
    bot_print(update, '苟利国家生死以, 岂因祸福避趋之 Θ..Θ')


def secret(update, context):
    """Send a message when the command /secret is issued."""
    bot_print(update, '黄哲臭猪🐷')


def bot_print_replace_all(text):
    """(暂时不用)将所有符号转义输出"""
    res = text.replace('_', '\_').replace('*', '\*').replace('[', '\[').replace(']', '\]').replace('(', '\(').replace(')', '\)').replace('~', '\~').replace('`', '\`').replace(
        '>', '\>').replace('#', '\#').replace('+', '\+').replace('-', '\-').replace('=', '\=').replace('|', '\|').replace('{', '\{').replace('}', '\}').replace('.', '\.').replace('!', '\!')
    print(res)


def init_command(dp):
    # on different commands - answer in Telegram
    # dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_list))
    dp.add_handler(CommandHandler("ying", ying))
    dp.add_handler(CommandHandler("meow", meow))
    dp.add_handler(CommandHandler("poem", poem))
    dp.add_handler(CommandHandler("secret", secret))


if __name__ == "__main__":
    print(start.__doc__)
    bot_print_replace_all(commands)
