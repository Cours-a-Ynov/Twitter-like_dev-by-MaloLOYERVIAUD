from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)
tweet = []
with open('tweet.json', 'r') as reader:
    tweet = json.loads(reader.read())

@app.route('/')
def home():
    with open('tweet.json', 'r') as reader:
        tweet = json.loads(reader.read())
    return render_template('twitter.html', twitter=tweet)

@app.route('/post', methods=['POST'])
def add():
    dico = {}
    dico["nom"] = request.form['nom']
    dico["msg"] = request.form['msg']
    tweet.append(dico)
    open('tweet.json', 'w').close()
    file = open("tweet.json", "a")
    file.write(json.dumps(tweet, indent=2))
    file.close()
    return redirect(url_for('home'))

@app.route('/tweetwow')
def wow():
    return render_template('tweetwow.html')

@app.route('/', methods=['GET'])
def cb():
    Like = "Like" + str(var.get())
    label.config(text=Like)

    root = Tk()

    var = IntVar()
    L = Radiobutton(root, text="Like", variable=var, value=1, command=sel)
    L.pack()

    label = Label(root)
    label.pack()
    root.mainloop()

@app.route('/response', methods=['POST'])
def rep():
    dico = {}
    dico["nomrsp"] = request.form['nomrsp']
    dico["rsp"] = request.form['rsp']
    tweet.append(dico)
    open('tweet.json', 'w').close()
    file = open("tweet.json", "a")
    file.write(json.dumps(tweet, indent=2))
    file.close()
    return redirect(url_for('home'))

@app.route('/tweetrsp')
def rsp():
    return render_template('tweetrsp.html')
