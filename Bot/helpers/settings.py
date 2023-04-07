from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from Bot.helpers import Variables

def generate_settings(vars: Variables):
    from_channel = vars.from_chat
    to_channel = vars.to_chat
    from_msg = vars.from_msg
    to_msg = vars.to_msg
    all = vars.all
    photo = vars.photo
    video = vars.video
    audio = vars.audio
    text = vars.text
    document = vars.document
    tag = vars.tag

    if from_msg == 0:
        from_msg = 'First'
    if to_msg == 0:
        to_msg = 'Last'
    if tag == 'copy':
        tag = 'Without Quote'
    else:
        tag = 'With Quote'
    if all:
        temp = \
        "TEXT       -       ✅\n" \
        "PHOTO      -       ✅\n" \
        "VIDEO      -       ✅\n" \
        "AUDIO      -       ✅\n" \
        "DOCUMENTS  -       ✅"
    else:
        temp = ''
        if text:
            temp += "TEXT       -       ✅"
        else:
            temp += "TEXT       -       ❌"
        if photo:
            temp += "\nPHOTO      -       ✅"
        else:
            temp += "\nPHOTO      -       ❌"
        if video:
            temp += "\nVIDEO      -       ✅"
        else:
            temp += "\nVIDEO      -       ❌"
        if audio:
            temp += "\nAUDIO      -       ✅"
        else:
            temp += "\nAUDIO      -       ❌"
        if document:
            temp += "\nDOCUMENTS  -       ✅"
        else:
            temp += "\nDOCUMENTS  -       ❌"

    text = f"""<b>Details:</b>
<code>From : {from_channel}</code>
<code>To   : {to_channel}</code>

<b>Settings:</b>
<code>From Msg  :   {from_msg}</code>
<code>To Msg    :   {to_msg}</code>

<code>FORWARD   :   {tag}</code>

<code>{temp}</code>"""
    return text


def generate_settings_btns(vars):
    from_msg = vars.from_msg
    to_msg = vars.to_msg
    all = vars.all
    photo = vars.photo
    video = vars.video
    audio = vars.audio
    text = vars.text
    document = vars.document
    tag = vars.tag

    btn = []

    if from_msg == 0:
        btn.append(
            [InlineKeyboardButton('From Msg : First',callback_data='toogle_settings|First')]
        )
    else:
        btn.append(
            [InlineKeyboardButton(f'From Msg : {from_msg}', callback_data='toogle_settings|First')]
        )
    if to_msg == 0:
        btn[0].append(
            InlineKeyboardButton('To Msg : Last',callback_data='toogle_settings|Last')
        )
    else:
        btn[0].append(
            InlineKeyboardButton(f'To Msg : {to_msg}', callback_data='toogle_settings|Last')
        )
    if tag == 'copy':
        btn.append(
            [InlineKeyboardButton('Forward : Without Quote', callback_data='toogle_settings|Tag')]
        )
    else:
        btn.append(
            [InlineKeyboardButton('Forward : With Quote', callback_data='toogle_settings|Tag')]
        )
    if all:
        btn.append(
            [
                InlineKeyboardButton('TEXT', callback_data='NoneBtn'),
                InlineKeyboardButton('✅', callback_data='toogle_settings|Text')
            ]
        )
        btn.append(
            [
                InlineKeyboardButton('PHOTO', callback_data='NoneBtn'),
                InlineKeyboardButton('✅', callback_data='toogle_settings|Photo')
            ]
        )
        btn.append(
            [
                InlineKeyboardButton('VIDEO', callback_data='NoneBtn'),
                InlineKeyboardButton('✅', callback_data='toogle_settings|Video')
            ]
        )
        btn.append(
            [
                InlineKeyboardButton('AUDIO', callback_data='NoneBtn'),
                InlineKeyboardButton('✅', callback_data='toogle_settings|Audio')
            ]
        )
        btn.append(
            [
                InlineKeyboardButton('DOCUMENT', callback_data='NoneBtn'),
                InlineKeyboardButton('✅', callback_data='toogle_settings|Docs')
            ]
        )
    else:
        if text:
            btn.append(
                [
                    InlineKeyboardButton('TEXT', callback_data='NoneBtn'),
                    InlineKeyboardButton('✅', callback_data='toogle_settings|Text')
                ]
            )
        else:
            btn.append(
                [
                    InlineKeyboardButton('TEXT', callback_data='NoneBtn'),
                    InlineKeyboardButton('❌', callback_data='toogle_settings|Text')
                ]
            )
        if photo:
            btn.append(
                [
                    InlineKeyboardButton('PHOTO', callback_data='NoneBtn'),
                    InlineKeyboardButton('✅', callback_data='toogle_settings|Photo')
                ]
            )
        else:
            btn.append(
                [
                    InlineKeyboardButton('PHOTO', callback_data='NoneBtn'),
                    InlineKeyboardButton('❌', callback_data='toogle_settings|Photo')
                ]
            )
        if video:
            btn.append(
                [
                    InlineKeyboardButton('VIDEO', callback_data='NoneBtn'),
                    InlineKeyboardButton('✅', callback_data='toogle_settings|Video')
                ]
            )
        else:
            btn.append(
                [
                    InlineKeyboardButton('VIDEO', callback_data='NoneBtn'),
                    InlineKeyboardButton('❌', callback_data='toogle_settings|Video')
                ]
            )
        if audio:
            btn.append(
                [
                    InlineKeyboardButton('AUDIO', callback_data='NoneBtn'),
                    InlineKeyboardButton('✅', callback_data='toogle_settings|Audio')
                ]
            )
        else:
            btn.append(
                [
                    InlineKeyboardButton('AUDIO', callback_data='NoneBtn'),
                    InlineKeyboardButton('❌', callback_data='toogle_settings|Audio')
                ]
            )
        if document:
            btn.append(
                [
                    InlineKeyboardButton('DOCUMENT', callback_data='NoneBtn'),
                    InlineKeyboardButton('✅', callback_data='toogle_settings|Docs')
                ]
            )
        else:
            btn.append(
                [
                    InlineKeyboardButton('DOCUMENT', callback_data='NoneBtn'),
                    InlineKeyboardButton('❌', callback_data='toogle_settings|Docs')
                ]
            )
    btn.append(
        [
            InlineKeyboardButton('ALL ✅', callback_data='toogle_settings|All'),
            InlineKeyboardButton('NONE ❌', callback_data='toogle_settings|None')
        ]
    )
    btn.append([InlineKeyboardButton(text='Back', callback_data='save_settings')])
    return InlineKeyboardMarkup(btn)

def all_checker(vars):
    photo = vars.photo
    video = vars.video
    audio = vars.audio
    text = vars.text
    document = vars.document

    if photo and video and audio and text and document:
        vars.all = True
    else:
        vars.all = False