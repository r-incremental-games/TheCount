from random import choice

import discord
from discord.ext import commands

from InputParser import InputParser
from Stats import Stats
from SaveLoad import SaveLoad


class TheCount(object):

    def __init__(self,
                 send_opening_message=True,
                 target_channel_name="counting",
                 save_interval=10
                 ):
        self.client = commands.Bot(command_prefix="!")
        self.target_channel_name = target_channel_name
        self.channel = None
        self.stats = Stats()
        self.next_number = 1
        self.save_interval = save_interval

        self.load()

        @self.client.event
        async def on_ready():
            print(f'{self.client.user} has connected to Discord!')
            self.channel = self.get_counting_channel()
            assert self.channel is not None
            await self.update_discord_activity()
            if send_opening_message:
                await self.channel.send(
                    self.get_random_opening_message() + " The next number is " + str(self.next_number))

        @self.client.event
        async def on_message(message):
            if message.channel.name != self.channel.name:
                return
            if message.author == self.client.user:
                return

            text = message.content + " "

            target_prefix = str(self.next_number) + " "
            if not text.startswith(target_prefix):
                await self.client.process_commands(message)
                await message.delete()
                return

            self.next_number += 1

            await self.update_discord_activity()

            user = message.author
            self.stats.increment_user(user.name)

            if self.next_number % self.save_interval == 0:
                self.save()

        @self.client.command()
        async def set(ctx, arg):
            """ADMIN ONLY: Set the next_number manually"""
            if not ctx.message.author.guild_permissions.administrator:
                return
            if InputParser.is_int(arg):
                num = int(arg)
                self.next_number = num + 1
                await self.update_discord_activity()
                await ctx.send("Highest number is set to " + str(num))

        @self.client.command()
        async def reset(ctx):
            """ADMIN ONLY: Reset the next_number back to 0"""
            if not ctx.message.author.guild_permissions.administrator:
                return
            self.next_number = 0
            self.stats.reset()
            await self.update_discord_activity()
            await ctx.send("Restarted!")

        @self.client.command()
        async def save(ctx):
            """ADMIN ONLY: Save the progress to the disk"""
            if not ctx.message.author.guild_permissions.administrator:
                return
            self.save()
            await ctx.send("Saved successfully!")

        @self.client.command()
        async def stats(ctx):
            """Send a message with the stats in the channel"""
            high_scores = self.stats.get_high_scores()
            res = ""
            for h in high_scores:
                res += h[0] + "\t" + str(h[1]) + "\n"
            await ctx.send(res)

    def start(self, token):
        self.client.run(token)

    def save(self):
        print("Saving... ", end=' ')
        SaveLoad.save_stats_dict(self.stats.dict)
        SaveLoad.save_highest_number(self.next_number - 1)
        print("Success")

    def load(self):
        print("Loading... ", end=' ')
        self.stats.dict = SaveLoad.get_stats_dict()
        self.next_number = SaveLoad.get_highest_number() + 1

        print("Success")

    def get_counting_channel(self):
        """Search the list of channels for one that is named 'counting' (case-insensitive)"""
        for c in self.client.get_all_channels():
            if c.name.lower() == self.target_channel_name:
                return c
        return None

    def get_random_opening_message(self):
        messages = [
            "AH AH AH!",
            "Do you know why they call me the Count? Because I love to count! Ah-hah-hah!",
            "Ah-hah-hah! Can you make it up to 34969?",
            "One guess, Two guesses, THREE!"
        ]
        return choice(messages)

    async def update_discord_activity(self):
        await self.client.change_presence(
            status=discord.Status.idle,
            activity=discord.Game("count to " + str(self.next_number))
        )
