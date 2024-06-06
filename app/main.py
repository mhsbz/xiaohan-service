# -*- coding: utf-8 -*-
import os

import botpy
import requests
from botpy import logging
from botpy.ext.cog_yaml import read
from botpy.message import GroupMessage, Message

test_config = read(os.path.join(os.path.dirname(__file__), "config.yaml"))

log = logging.get_logger()

action_list = [
    "踏入仙途", "打坐", "我的修仙信息"
]


class MyClient(botpy.Client):
    async def on_ready(self):
        log.info(f"robot 「{self.robot.name}」 on_ready!")

    async def on_group_at_message_create(self, message: GroupMessage):
        content = message.content.strip().lstrip("/").rstrip("/")
        if content not in action_list:
            # 指令无效
            return
        response = requests.get(
            f'{test_config["service_host"]}member_id={message.author.member_openid}&action={message.content}')

        if response.status_code == 200:
            messageResult = await message.api.post_group_message(
                group_openid=message.group_openid,
                msg_id=message.id,
                content=response.text.strip('"'))
            log.info(messageResult)


if __name__ == "__main__":
    intents = botpy.Intents(public_messages=True)
    client = MyClient(intents=intents)
    client.run(appid=test_config["appid"], secret=test_config["secret"])
