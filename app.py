from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

CONFESSIONS_FILE = "confessions.txt"

# Intro page
@app.route("/")
def intro():
    return render_template("intro.html")  # Fancy welcome page

# Writing page
@app.route("/write")
def home():
    return render_template("index.html")

# Save cfrom flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

CONFESSION_FILE = 'confession.txt'

@app.route('/')
def intro():
    return render_template('intro.html')

@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        confession = request.form.get('confession')
        if confession:
            with open(CONFESSION_FILE, 'a', encoding='utf-8') as f:
                f.write(confession.strip() + "\n")
        return redirect(url_for('feed'))
    return render_template('index.html')

@app.route('/feed')
def feed():
    try:
        with open(CONFESSION_FILE, 'r', encoding='utf-8') as f:
            confessions = f.readlines()
    except FileNotFoundError:
        confessions = []
    return render_template('feed.html', confessions=confessions)

if __name__ == '__main__':
    app.run(debug=True)
onfession
@app.route("/submit", methods=["POST"])
def submit():
    confession = request.form.get("confession", "").strip()
    
    if confession:  # Only save if not empty
        with open(CONFESSIONS_FILE, "a", encoding="utf-8") as f:
            f.write(confession + "\n")
    
    return redirect(url_for("feed"))

# Confession feed page
@app.route("/feed")
def feed():
    try:
        with open(CONFESSIONS_FILE, "r", encoding="utf-8") as f:
            confessions = [line.strip() for line in f if line.strip()]
        confessions.reverse()  # Newest first
    except FileNotFoundError:
        confessions = []

    return render_template("feed.html", confessions=confessions)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
