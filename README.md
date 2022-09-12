![687474703a2f2f692e696d6775722e636f6d2f616f6144455a312e706e67](https://user-images.githubusercontent.com/65199318/189535125-6fc7a0bc-9787-4dda-86bb-4cbe3b448759.png)
# Darkest Dungeon Provision Autobuy Bot

This bot intends to autobuy provisions for your expedition every time the game shows "Provisions Screen"

PS.: since this bot uses pywin32 lib, this bot only works on Windows, it's easily adaptable to Linux, since only the click function uses this lib. (I'm planning to do this)

## About the project
Why make an autobuy provisions bot?

As a horror fan, I love Darkest Dungeon concept, mechanics and everything, but as a developer, I hate to repete choices/actions. So I decided to build this bot to buy provisions automatically, for each dungeon and it's length.

Python is also my favorite technology, and I'm recently doing some professional work using this tech stack and I'd like to share that experience with the community. I hope all of you enjoy this. As someone who always used community tools and mods, it's a pleasure to me to do something useful.

## Getting started

1 - You need to have Python installed.

2 - You just need to extract the files and install the requirements.txt dependencies.

    pip install -r requirements.txt

3 - Open the game and at settings, disable "Fullscreen" checkbox and at "Resolution" set your monitor resolution.

  <img width="749" alt="Darkest Dungeon Settings Menu" src="https://user-images.githubusercontent.com/65199318/189550530-a83c0d4b-c225-43b9-93cb-ab1eb1fb7f0b.png">

4 - Run the game with argument/parameter "-borderless" ()

5 - In the file "configs.py", change the field "GAME_SCREEN_RESOLUTION" to your game resolution
Then, just run the file "run.py" with administrator privilege.

    
## Future

* Add PyQT5 GUI