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
    "加入异世界修仙", "加入修仙界", "加入异世界", "术修", "剑修", "魔法", "剑士", "生成角色", "领取内测专属奖励", "",
    "修炼", "闭关", "签到", "战斗相关", "进入迷宫"
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
            resp = response.text.replace('"', '').replace(r'\n', '\n')

            messageResult = await message._api.post_group_message(
                group_openid=message.group_openid,
                msg_id=message.id,
                content=resp)
            log.info(messageResult)


if __name__ == "__main__":
    intents = botpy.Intents(public_messages=True)
    client = MyClient(intents=intents)
    client.run(appid=test_config["appid"], secret=test_config["secret"])
