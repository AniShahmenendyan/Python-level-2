from flask import Flask, request, render_template, redirect, url_for
import json
import os

app = Flask(__name__)


def read_posts():
    file_path = os.path.join(app.root_path, "data.json")
    with open(file_path) as json_file:
        data = json.load(json_file)
        return data


def get_posts(keyword=None):
    posts = read_posts()
    result = []
    if keyword:

        for post in posts:
            if (keyword.lower() in post['title'].lower()) or (keyword.lower() in post['description'].lower()):
                result.append(post)
    else:
        result = posts

    return result


def get_post_by_id(post_id):
    posts = read_posts()
    for post in posts:
        if post['post_id'] == post_id:
            return post
    return None


@app.route('/')
def home():
    return redirect(url_for('posts'))


@app.route('/post/<int:post_id>')
def post(post_id):
    post = get_post_by_id(post_id)
    return render_template('post.html', post=post)


@app.route('/posts')
def posts():
    keyword = ''
    if request.args.get('q'):
        keyword = request.args.get('q')

    posts = get_posts(keyword)
    return render_template('posts.html', posts=posts, keyword=keyword)

if __name__ == '__main__':
    app.run(debug=True)
