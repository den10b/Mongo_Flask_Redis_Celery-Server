import flask

from . import app
from .models import Message


@app.route('/post', methods=['POST'])
def sendMessage():
    username = flask.request.values.get('user')  # Your form's
    message = flask.request.values.get('message')  # input names
    # db.session.add(Message(name=username, message=message))
    # db.session.commit()
    Message(name=username,message=message).save()
    return "200"


@app.route('/get', methods=['GET'])
def getChat():
    msg = ""
    for obj in Message.objects():
        msg+=str(obj.name+": "+obj.message+'\n')
    return msg

