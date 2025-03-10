from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello workddd'

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/')
def index(): pass

@app.route('/login')
def login(): pass

@app.route('/user/<username>')
def profile(username): pass

def asdf():
    with app.test_request_context():
        print url_for('index')
        print url_for('login')
        print url_for('login', next='/')
        print url_for('profile', username='John Doe')

if __name__ == '__main__' :
    app.debug = True
    app.run(host='0.0.0.0')

