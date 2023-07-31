from flask import Flask

app = Flask(__name__)
SCORES_FILE_NAME = "Scores.txt"


@app.route('/')
def score_server():
    try:
        with open(SCORES_FILE_NAME, 'r') as file:
            score = file.read().strip()
        html = f'''
        <html>
            <head>
                <title>Scores Game</title>
            </head>
            <body>
                <h1>The score is <div id="score">{'SCORE'}</div></h1>
            </body>
        </html>
        '''
    except Exception as e:
        html = f'''
        <html>
            <head>
                <title>Scores Game</title>
            </head>
            <body>
                <h1><div id="score" style="color:red">{'Error'}</div></h1>
            </body>
        </html>
        '''
    return html


if __name__ == '__main__':
    app.run()
