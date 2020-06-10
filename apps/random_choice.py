#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
* File Name    : random_choice.py
* Description  :
* Create Time  : 2020-03-22 16:26:29
* Version      : 1.0
* Author       : Steve X
* GitHub       : https://github.com/Steve-Xyh
'''

import random
from telegram import ReplyKeyboardMarkup
from telegram.ext import CommandHandler, MessageHandler, ConversationHandler
from telegram.ext import Filters, Updater
from functions.message_handler import bot_print

CHOOSING, TYPING_REPLY, CHANGE_NUMBER = range(3)
choice_num = 1

reply_keyboard = [
    ['更改选择数量【默认1】'],
    ['输入选项'],
    ['结束输入']
]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)


def dic_to_str(user_data):
    facts = list()

    for key, value in user_data.items():
        facts.append('{} - {}'.format(key, value))

    return "\n".join(facts).join(['\n', '\n'])


def change_number_info(update, context):
    '''更改选择数量提示'''
    message = '想让小嘤帮你选出几个选项?'
    bot_print(update, message)

    return CHANGE_NUMBER


def number_edit(update, context):
    '''更改选择数量'''
    dic = {
        '零': '0',
        '一': '1',
        '二': '2',
        '两': '2',
        '三': '3',
        '仨': '3',
        '四': '4',
        '五': '5',
        '六': '6',
        '七': '7',
        '八': '8',
        '九': '9',
        '十': '10',
        '个': '',
    }

    text = update.message.text
    for num in dic:
        text = text.replace(num, dic[num])

    global choice_num
    choice_num = int(text)

    update.message.reply_text(
        f'好的, 小嘤会帮你选出{choice_num}个选项',
        reply_markup=markup
    )

    return CHOOSING


def start_random(update, context):
    '''开始入口'''
    update.message.reply_text(
        '选择恐惧症又犯了? 那让小嘤来帮你选择吧😏',
        reply_markup=markup
    )

    global choice_num
    choice_num = 1

    return CHOOSING


def input_options(update, context):
    '''输入选项'''
    message = '告诉小嘤你的选项吧, \n格式: 选项1,选项2,...'
    bot_print(update, message)

    return TYPING_REPLY


def received_options(update, context):
    '''显示所有选项'''
    user_data = context.user_data
    text = update.message.text.replace('，', ',')

    user_data['option_list'] = {}
    options = text.split(',')
    idx = 1
    for opt in options:
        user_data['option_list'][idx] = opt.strip()
        idx += 1

    update.message.reply_text(
        '你的选项:\n{}'.format(dic_to_str(user_data['option_list'])),
        reply_markup=markup
    )

    return CHOOSING


def done(update, context):
    '''结束输入, 开始选择'''
    global choice_num
    user_data = context.user_data
    try:
        choice_list = random.sample(
            list(user_data['option_list'].values()),
            choice_num
        )
        choices = '】\n【'.join(choice_list)
    except:
        bot_print(update, '你似乎还没输入选项, 小嘤可不笨噢')
        return ConversationHandler.END

    message = f'经过深思熟虑, 小嘤建议选择:\n\n【{choices}】'
    bot_print(update, message)

    user_data.clear()
    return ConversationHandler.END


def init_app(dp):
    '''初始化应用'''
    # Add conversation handler with the states CHOOSING, TYPING_CHOICE and TYPING_REPLY
    conv_handler = ConversationHandler(
        entry_points=[
            CommandHandler('random', start_random),
            MessageHandler(Filters.regex('.*什么*'), start_random),
            MessageHandler(Filters.regex('.*哪个*'), start_random),
            MessageHandler(Filters.regex('.*哪里*'), start_random),
            MessageHandler(Filters.regex('.*要不要*'), start_random),
        ],

        states={
            CHOOSING: [
                MessageHandler(
                    Filters.regex('^(更改选择数量【默认1】)$'),
                    change_number_info
                ),
                MessageHandler(
                    Filters.regex('^输入选项$'),
                    input_options
                )
            ],

            CHANGE_NUMBER: [MessageHandler(Filters.text, number_edit)],

            TYPING_REPLY: [MessageHandler(Filters.text, received_options), ],
        },

        fallbacks=[MessageHandler(Filters.regex('^结束输入$'), done)]
    )

    dp.add_handler(conv_handler)
    dp.add_handler(CommandHandler('random', start_random))


if __name__ == "__main__":
    PROXY = True
    PROXY_CONFIG = {'proxy_url': 'socks5://127.0.0.1:1081/'}

    updater = Updater(
        token=':',
        use_context=True,
        request_kwargs=PROXY_CONFIG if PROXY else None
    )

    print(f'Use PROXY:\t {PROXY_CONFIG}')
    dp = updater.dispatcher
    init_app(dp)

    updater.start_polling()
    updater.idle()
