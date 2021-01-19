import argparse
import os

from dotenv import load_dotenv

from TheCount import TheCount
from InputParser import InputParser


def main():
    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')

    assert (TOKEN is not None)
    parser = argparse.ArgumentParser(
        description=
        """
    The Count
    A Discord bot that allows you to count! AH AH AH!
        """,
        formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument("--send-opening-message", type=InputParser.string_to_boolean, nargs='?',
                        const=True, default=True,
                        help="Whether or not The Count should open with a greeting")
    parser.add_argument("--channel", default="counting",
                        help="The channel The Count will operate in"),
    parser.add_argument("--save-interval", default=10, type=InputParser.string_to_int,
                        help="The Count will save its progress after n messages")

    args = parser.parse_args()

    bot = TheCount(
        send_opening_message=args.send_opening_message,
        target_channel_name=args.channel,
        save_interval=args.save_interval,
    )

    bot.start(TOKEN)


if __name__ == '__main__':
    main()
