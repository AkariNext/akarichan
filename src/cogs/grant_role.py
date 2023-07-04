import disnake
from disnake.ext import commands
from disnake.ext.commands import Cog, Bot
from injector import NoInject, inject

from src.di.container import di_container
from src.shared.config import akarichan_config
from src.shared.interfaces.usecases.grant_role.link_grant_role import LinkGrantRoleUsecaseABC
from src.shared.interfaces.usecases.grant_role.register_message_grant_role import RegisterMessageGrantRoleUsecaseABC

class Confirm(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=10.0)
        self.value: bool | None = None

    # When the confirm button is pressed, set the inner value to `True` and
    # stop the View from listening to more input.
    # We also send the user an ephemeral message that we're confirming their choice.
    @disnake.ui.button(label="Confirm", style=disnake.ButtonStyle.green)
    async def confirm(self, button: disnake.ui.Button, inter: disnake.MessageInteraction):
        await inter.response.send_message("Confirming...", ephemeral=True)
        self.value = True
        self.stop()

    # This one is similar to the confirmation button except sets the inner value to `False`.
    @disnake.ui.button(label="Cancel", style=disnake.ButtonStyle.grey)
    async def cancel(self, button: disnake.ui.Button, inter: disnake.MessageInteraction):
        await inter.response.send_message("Cancelling...", ephemeral=True)
        self.value = False
        self.stop()

class GrantRoleCog(Cog):
    @inject
    def __init__(
        self, bot: NoInject[Bot],
        link_grant_role_usecase: LinkGrantRoleUsecaseABC,
        register_message_grant_role_usecase: RegisterMessageGrantRoleUsecaseABC
    ) -> None:
        self.bot: Bot = bot
        self.link_grant_role_usecase: LinkGrantRoleUsecaseABC = link_grant_role_usecase
        self.register_message_grant_role_usecase: RegisterMessageGrantRoleUsecaseABC = register_message_grant_role_usecase

    @commands.slash_command(name='role', description='ロールに関するコマンド', guild_ids=akarichan_config.guild_ids)
    async def role(self, inter: disnake.CommandInteraction):
        pass
    
    @role.sub_command(name='link', description='リアクションとロールを紐づけします')
    async def link_reaction_to_role(self, inter: disnake.CommandInteraction, emoji: disnake.Emoji, role: disnake.Role, message: disnake.Message):
        if inter.guild_id is None:
            raise Exception('ギルドのIdが無い(おそらくDM?)')
        await self.link_grant_role_usecase.handle({'emoji_id': emoji.id, 'guild_id': inter.guild_id, 'role_id': role.id})
        
        embed=disnake.Embed(title="成功", description="絵文字とロールの関連付けに成功", color=0x8bc34c)

        await inter.response.send_message(embed=embed)

    @commands.message_command(name='Set', guild_ids=akarichan_config.guild_ids)
    async def set_message(self, inter: disnake.MessageCommandInteraction, message: disnake.Message):
        await self.register_message_grant_role_usecase.handle({'message_id': message.id})
        embed=disnake.Embed(title="成功", description="メッセージをロール登録用として登録しました", color=0x8bc34c)

        await inter.target.reply(embed=embed)
        

def setup(bot: Bot):
    bot.add_cog(di_container.create_object(GrantRoleCog, {'bot': bot}))
