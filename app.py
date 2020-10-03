#!flask/bin/python
from flask import Flask, jsonify, abort, request, make_response, url_for
from scraper_profile import get_profile_data
from scraper_post import get_post_data

app = Flask(__name__, static_url_path="")


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/api/u/<username>', methods=['GET'])
def get_data_username(username):
    return jsonify(get_profile_data(username))


@app.route('/api/p/<post>', methods=['GET'])
def get_data_post(post):
    return jsonify(get_post_data(f"https://www.instagram.com/p/{post}"))


if __name__ == '__main__':
    app.run(debug=True)
