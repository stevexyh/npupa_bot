#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
* File Name    : check_new_member.py
* Description  : Handle new group members by questions
* Create Time  : 2020-03-13 12:15:25
* Version      : 1.1
* Author       : Steve X
* GitHub       : https://github.com/Steve-Xyh
'''


import random
from telegram.ext import Updater, Filters
from telegram.ext import CommandHandler, CallbackQueryHandler, MessageHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ChatPermissions
from functions import token as tk
from functions.message_handler import bot_print
############################### Keyboards ############################################


def start(update, context):
    '''触发问题菜单'''

    message = '入群检测'
    keyboard = [[InlineKeyboardButton('开始验证', callback_data='main')]]

    restrict_user(update, context)

    update.message.reply_text(
        text=message,
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


def restrict_user(update, context):
    '''禁言用户'''
    bot = context.bot
    target_user = update.message.new_chat_members[0]

    permission = ChatPermissions(
        can_send_messages=False,
        can_send_media_messages=False,
        can_send_polls=False,
        can_send_other_messages=False,
        can_add_web_page_previews=False,
        can_change_info=False,
        can_invite_users=False,
        can_pin_messages=False,
    )

    bot.restrict_chat_member(
        chat_id=update.message.chat_id,
        user_id=target_user.id,
        permissions=permission
    )

    bot_print(
        update,
        '已禁言用户【' + str(target_user.full_name) + '】'
    )


def revoke_restrict_user(update, context):
    '''解除禁言'''
    query = update.callback_query
    bot = context.bot
    target_user = query.message.reply_to_message.new_chat_members[0]

    permission = ChatPermissions(
        can_send_messages=True,
        can_send_media_messages=True,
        can_send_polls=True,
        can_send_other_messages=True,
        can_add_web_page_previews=True,
    )

    bot.restrict_chat_member(
        chat_id=query.message.chat_id,
        user_id=target_user.id,
        permissions=permission
    )

    bot_print(
        query,
        '已将用户【' + str(target_user.full_name) + '】解除禁言'
    )


def main_menu(update, context):
    '''主菜单'''
    query=update.callback_query
    bot=context.bot

    message='萌新请选择一个验证问题'
    question_list=random.sample(['q1', 'q2', 'q3'], 3)

    keyboard=[[InlineKeyboardButton('问题1', callback_data = question_list[0])],
                [InlineKeyboardButton('问题2', callback_data=question_list[1])],
                [InlineKeyboardButton('问题3', callback_data=question_list[2])]]

    keyboard = InlineKeyboardMarkup(keyboard)

    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=message,
        reply_markup=keyboard
    )

    return message, keyboard


def question_1(update, context):
    '''乘法检测'''
    query = update.callback_query
    bot = context.bot

    a = random.randint(0, 10)
    b = random.randint(0, 10)
    c = random.randint(0, 10)

    message = f'{a} * {b} = ?'
    ans_list = random.sample([a*c, a*b, b*c], 3)

    keyboard = [
        [InlineKeyboardButton(
            str(ans_list[0]),
            callback_data='true' if ans_list[0] == a*b else 'false'
        )],
        [InlineKeyboardButton(
            str(ans_list[1]),
            callback_data='true' if ans_list[1] == a*b else 'false'
        )],
        [InlineKeyboardButton(
            str(ans_list[2]),
            callback_data='true' if ans_list[2] == a*b else 'false'
        )],
        [InlineKeyboardButton(
            '换一个问题',
            callback_data='main'
        )],
    ]

    keyboard = InlineKeyboardMarkup(keyboard)

    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=message,
        reply_markup=keyboard
    )

    return message, keyboard


def question_2(update, context):
    '''加法检测'''
    query = update.callback_query
    bot = context.bot

    a = random.randint(0, 100)
    b = random.randint(0, 100)
    c = random.randint(0, 100)

    message = f'{a} + {b} = ?'
    ans_list = random.sample([a+c, a+b, b+c], 3)

    keyboard = [
        [InlineKeyboardButton(
            str(ans_list[0]),
            callback_data='true' if ans_list[0] == a+b else 'false'
        )],
        [InlineKeyboardButton(
            str(ans_list[1]),
            callback_data='true' if ans_list[1] == a+b else 'false'
        )],
        [InlineKeyboardButton(
            str(ans_list[2]),
            callback_data='true' if ans_list[2] == a+b else 'false'
        )],
        [InlineKeyboardButton(
            '换一个问题',
            callback_data='main'
        )],
    ]

    keyboard = InlineKeyboardMarkup(keyboard)

    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=message,
        reply_markup=keyboard
    )

    return message, keyboard


def question_3(update, context):
    '''玄学问题'''
    query = update.callback_query
    bot = context.bot

    message = '跑得最快的人是谁'
    ans = '香港记者'
    ans_list = random.sample([ans, '波尔特', '西方记者'], 3)

    keyboard = [
        [InlineKeyboardButton(
            str(ans_list[0]),
            callback_data='true' if ans_list[0] == ans else 'false'
        )],
        [InlineKeyboardButton(
            str(ans_list[1]),
            callback_data='true' if ans_list[1] == ans else 'false'
        )],
        [InlineKeyboardButton(
            str(ans_list[2]),
            callback_data='true' if ans_list[2] == ans else 'false'
        )],
        [InlineKeyboardButton(
            '换一个问题',
            callback_data='main'
        )],
    ]

    keyboard = InlineKeyboardMarkup(keyboard)

    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=message,
        reply_markup=keyboard
    )

    return message, keyboard


############################# Handlers #########################################

def true_handler(update, context):
    query = update.callback_query
    bot = context.bot

    message = '回答正确, 检测通过'
    keyboard = InlineKeyboardMarkup([])

    revoke_restrict_user(update, context)

    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=message,
        reply_markup=keyboard
    )


def false_handler(update, context):
    query = update.callback_query
    bot = context.bot

    message = '回答错误, 准备领取飞机票一张'
    keyboard = InlineKeyboardMarkup([])

    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=message,
        reply_markup=keyboard
    )


def init_app(dp):
    dp.add_handler(MessageHandler(
        Filters.status_update.new_chat_members, start))
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CallbackQueryHandler(main_menu, pattern='main'))
    dp.add_handler(CallbackQueryHandler(true_handler, pattern='true'))
    dp.add_handler(CallbackQueryHandler(false_handler, pattern='false'))
    dp.add_handler(CallbackQueryHandler(question_1, pattern='q1'))
    dp.add_handler(CallbackQueryHandler(question_2, pattern='q2'))
    dp.add_handler(CallbackQueryHandler(question_3, pattern='q3'))


################################################################################
if __name__ == "__main__":
    tk.TOKEN_FILE = '../token'
    PROXY = True if input('是否使用代理?[0]否, [1*]是\n') in ('', '1') else False
    PROXY_CONFIG = {'proxy_url': 'socks5://127.0.0.1:1081/'}

    updater = Updater(
        token=tk.get_token(),
        use_context=True,
        request_kwargs=PROXY_CONFIG if PROXY else None
    )

    # Get the dispatcher to register handlers
    dp = updater.dispatcher
    init_app(dp)

    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()
