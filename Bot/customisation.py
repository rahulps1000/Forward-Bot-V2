from pyrogram import __version__ as pyrogram_version
from pyropatch import __version__ as pyropatch_version
from pyrogram.types import InlineKeyboardButton

# Start Message
start_text = "<b>Hello {mention}\n\nI am a  Bot, </b>"

# Help Message
help_text = "<b>❔ How to use this Bot</b>\n\n🔷 \n\n⭕"

# About Message
about_text = "<b>ABOUT ME\n\n" \
             "○ Creator : <a href='https://t.me/Lalettan_Bakthan'>Lalettan Bakthan</a>\n" \
             "○ Support : <a href='https://t.me/CodeXBotzSupport'>CodeXBotz Support</a>\n" \
             "○ Language : <a href='https://www.python.org/'>Python 3</a>\n" \
             f"○ Library : <a href='https://github.com/pyrogram/pyrogram'>Pyrogram Asyncio {pyrogram_version}</a>\n" \
             f"○ Add-on : <a href='https://github.com/rahulps1000/pyropatch'>Pyropatch {pyropatch_version}</a>\n" \
             "○ Channel : <a href='https://t.me/CodeXBotz'>Code 𝕏 Botz</a></b>"

# Already Forwarding Message
already_forwarding_text = "<b>Bot is Already Forwarding files. Please Try after It is Completed.</b>"

# Start Message Keyboard
start_keyboard = [
    [
        InlineKeyboardButton(text='🤔 Help', callback_data="help"),
        InlineKeyboardButton(text='🤖 About', callback_data="about")
    ],
    [
        InlineKeyboardButton(text='Close 🔒', callback_data="close")
    ]
]

# Help Message Keyboard
help_keyboard = [
    [
        InlineKeyboardButton(text='🤖 About', callback_data='about'),
        InlineKeyboardButton(text='Close 🔒', callback_data='close')
    ]
]

# About Message Keyboard
about_keyboard = [
    [
        InlineKeyboardButton(text='🤔 Help', callback_data='help'),
        InlineKeyboardButton(text='Close 🔒', callback_data='close')
    ]
]