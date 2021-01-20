## The Count

> Do you know why they call me the Count? Because I love to count! Ah-hah-hah!

A Discord bot that lets your users count as high as they want!

- Select a specific channel The Count will run in this channel only
- Easy to set up!

## How to run

#### Dependencies

```
pip3 install -r requirements.txt
```

#### dotenv

Create a `.env` file in the root folder to allow the bot to grab your Discord token. Note that this is not
your `CLIENT SECRET`, but your `BOT TOKEN`.

```
# .env
DISCORD_TOKEN=<YOUR_TOKEN>
```

#### Run

In the root folder

```sh
git clone https://github.com/r-incremental-games/TheCount
cd TheCount
python src/main.py
```

Or use the optional arguments. You can view all of them with

```sh
python src/main.py --help
```

## Usage

```
!set <x>    Sets the highest number to x
!reset      Sets the highest number to 0
!stats      Prints the stats of the top x users
!save       Save the progress to the disk
```