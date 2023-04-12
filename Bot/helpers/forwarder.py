from pyrogram.enums import MessageMediaType
from Bot.helpers import Variables
from Bot import CodeXBotz


async def copy_forward(to_chat, msg, tag):
    if tag == 'copy':
        await msg.copy(to_chat)
    else:
        await msg.forward(to_chat)

async def forward(bot: CodeXBotz,user_id: int):
    vars = Variables(user_id)
    from_chat = vars.from_chat
    from_msg = vars.from_msg
    to_chat = vars.to_chat
    to_msg = vars.to_msg
    tag = vars.tag
    all = vars.all
    photo = vars.photo
    video = vars.video
    audio = vars.audio
    text = vars.text
    document = vars.document

    last = vars.last_msg

    if last:
        from_msg = last + 1
    elif not from_msg:
        from_msg = 1

    if not to_msg:
        msg = await bot.send_message(chat_id=from_chat,text=".")
        to_msg = msg.id
        await msg.delete()

    for msg_id in range(from_msg,to_msg):
        msg = await bot.get_messages(chat_id=from_chat,message_ids=msg_id)
        if msg.empty or msg.service:
            continue
        if all:
            await copy_forward(to_chat, msg, tag)
        elif photo and msg.media == MessageMediaType.PHOTO:
            await copy_forward(to_chat, msg, tag)
        elif video and msg.media == MessageMediaType.VIDEO:
            await copy_forward(to_chat, msg, tag)
        elif audio and msg.media == MessageMediaType.AUDIO:
            await copy_forward(to_chat, msg, tag)
        elif document and msg.media == MessageMediaType.DOCUMENT:
            await copy_forward(to_chat, msg, tag)
        elif text and not msg.media:
            await copy_forward(to_chat, msg, tag)

        vars.last_msg = msg.id

    vars.reset_all()
    await bot.send_message(chat_id=user_id,text="Forwarding Completed")