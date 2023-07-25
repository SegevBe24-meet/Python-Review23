def create_youtube_video(title, description):
   video = {"Title":title,"Description":description,"likes":0,"dislikes":0,"comments":{},"hashtag":}
   hash1 = 
   return video

def like(video):
    if "likes" in video:
        video["likes"] += 1
    return video

def dislikes(video):
    if "dislikes" in video:
        video["dislikes"] +=1
    return video

def add_comment(video,username,comment_text):
    actions = {username:comment_text}
    video["comments"] = actions
    return video["comments"]


yt_video = create_youtube_video("Taylor Swift-seven","song from the album folklore ,2021")
for i in range(495):
    like(yt_video)
add_comment(yt_video,"Taylor Swift","omg best song everrrrrrrr <333333")

print(yt_video)

