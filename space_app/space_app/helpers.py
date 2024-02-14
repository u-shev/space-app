import os
from dotenv import load_dotenv
from posts.models import Post
import aiohttp


'''Taking api key from .env file'''
load_dotenv()
nasa_api = os.getenv('NASA_API')


'''Getting the posts list'''


async def get_posts_list():
    post_list = Post.objects.all().select_related('author')
    posts = [post async for post in post_list]
    return posts

'''Taking info and picture/video from nasa api, making different variables
for templates to show picture or video'''


async def get_data_from_api():
    async with aiohttp.ClientSession() as session:
        response = await session.get(
            f'https://api.nasa.gov/planetary/apod?api_key={nasa_api}')
        if response.status == 200:
            nasa_json = await response.json()
            nasa_info = nasa_json['explanation']
            if nasa_json['media_type'] == "image":
                nasa_picture = nasa_json['url']
                nasa_video = None
            elif nasa_json['media_type'] == "video":
                nasa_video = nasa_json['url']
                nasa_picture = None
            else:
                nasa_video = None
                nasa_picture = None
        else:
            nasa_info = "Some problems with Nasa API occured, so you see this picture"
            nasa_video = None
            nasa_picture = "https://apod.nasa.gov/apod/image/2402/RosetteCone_Bernard_5398.jpg"
        context = nasa_info, nasa_picture, nasa_video
        return context
