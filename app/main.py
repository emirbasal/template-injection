from flask import Flask, escape, request, render_template, url_for, flash, redirect, render_template_string
from forms import RequestFeatureForm
from flask import Markup

app = Flask(__name__)

app.config['SECRET_KEY'] = 'FLAG{215528c368ea01d663cb1ace3edfe67a}'


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/request', methods=['GET', 'POST'])
def request_feature():
    form = RequestFeatureForm()
    if form.validate_on_submit():

        # I know. It's a bad idea. But there is no other option to make the site vulnerable
        template = '''
            <html>
                <head>
                    <meta charset="UTF-8">
                    <link rel="stylesheet" href="https://bootswatch.com/4/united/bootstrap.min.css">
                    <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='base.css')}}">
                    <title>Weihnachtsgebäck.com</title>
                </head>
                <body>
                    <div>
                        <nav class="navbar navbar-expand-lg navbar-dark bg-primary py-4">
                            <a class="navbar-brand" href="{{ url_for('home') }}" style="font-size: 25px">Weihnachtsgebäck.com</a>
                            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarColor01"
                                    aria-controls="navbarColor01" aria-expanded="false" aria-label="Toggle navigation">
                                <span class="navbar-toggler-icon"></span>
                            </button>

                            <div class="collapse navbar-collapse" id="navbarColor01">
                                <ul class="navbar-nav mr-auto">
                                    <li class="nav-item">
                                        <a class="nav-link disabled" href="#">Gingerbread</a>
                                    </li>
                                    <li class="nav-item">
                                        <a class="nav-link disabled" href="#">Christmas biscuit</a>
                                    </li>
                                </ul>
                                 <div class="navbar-nav">
                                     <a class="nav-link disabled" href="">About</a>
                                     <a class="nav-link active" href="{{ url_for('request_feature') }}">Request feature</a>
                                     <a class="nav-link disabled" href="">Login</a>
                                </div>
                            </div>
                        </nav>
                    </div>
                    <div class="container">
                        <div align="center" style="margin-top:15rem">
                            <h2>The feature "%s" was successfully submitted! Thank you!</h2>
                            <a href="{{ url_for('home') }}">
                                <button class="btn btn-info" type="submit">Back to homepage</button>
                            </a>
                        </div>
                    </div>
                    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
                    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
                    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
                </body>
            </html>''' % form.title.data

        return render_template_string(template)

    else:
        return render_template('featureRequest.html', form=form)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False, port=5000)
