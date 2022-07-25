def create_youtube_video(title, description,):
	youtubevideo={"title":title, "description":description,"likes":0, "dislikes":0, "comments":{}}
	return youtubevideo

def like(youtubevideo):
	if "likes" in youtubevideo:
		youtubevideo["likes"]+=1
	return create_youtube_video
def dislike(youtubevideo):
	if "dislikes" in youtubevideo:
		youtubevideo["dislikes"]+=1
	return create_youtube_video
def add_comment(comment_text,youtubevideo,username):
	youtubevideo["comments"][username]=comment_text
	return youtubevideo
x=create_youtube_video("thisistitle", "thisisdesc")
like(x)
dislike(x)
add_comment("hi", x,"hello")
for i in range(1,495):
	like(x)
print(x)



