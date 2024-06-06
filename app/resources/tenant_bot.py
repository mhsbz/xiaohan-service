import botpy
from ..configs import app_config
from botpy.message import Message


class TenantBotClient(botpy.Client):
    async def on_at_message_create(self, message: Message):
        await message.reply(content=f"机器人{self.robot.name}收到你的@消息了: {message.content}")


intents = botpy.Intents(public_guild_messages=True)
client = TenantBotClient(intents=intents)
print(app_config.app_id)
print(app_config.app_secret)
client.run(appid=app_config.app_id,secret=app_config.app_secret)
