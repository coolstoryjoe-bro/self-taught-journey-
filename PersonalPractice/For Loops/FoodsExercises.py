video_games = ["becastles", "valorant", "league of legends", "minecraft", "xenoblade", "xenoblade 2", "stardew valley"]
print(video_games[:3])
print(video_games[2:5])
print(video_games[-3:])

my_anime = ["violet evergarden", "rainbow days", "astra lost in space", "princess principle", "overly cautious hero",
         "land of the lustrious", "clannad", "cardcaptor"]
audreys_anime = my_anime[:]

my_anime.append("legend of the shield hero")
audreys_anime.append("haikyu")

for me_anime in my_anime:
    print(f"{me_anime.title()} is a really good anime!")

for her_anime in audreys_anime:
    print(f"{her_anime.title()}, she really liked this anime!")


