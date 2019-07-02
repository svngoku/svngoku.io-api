# api for blogs
from flask import Flask
from flask_restful import abort,Api, Resource

app = Flask(__name__)
api = Api(app)

BLOGS = {
    'blog1' : {'title': "hello", 'resume': "hello WORLD"}
}

def abort_if_blog(blog_id):
    if blog_id not in BLOGS:
        abort(404, message="blog {} doesn't exist".format(blog_id))


Api.add_resource()