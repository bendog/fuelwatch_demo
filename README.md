# fuel watch workshop demo code

Some demo examples of python code from the 2020 fuel watch workshop night 1

## requirements

```pip install requests feedparser```

to run app.py you will also need flask

```pip install flask```

## files

### get_feed.py

this file retrieves the RSS feed and outputs the content to `output.json`.
if output.json exists, it will read that version rather than fetch the content again.
I mostly added this feature so i could test the code whilst i was offline on a plane.

### fuelwatch.py

this file will output the conent to a very simple html table, using string substitution

to run this script type `python fuelwatch.py`

then check the file `output.html`

### jinjary.py

this file will do the same thing, but rather than pure python, it uses the jinja2 templating library, to insert the 'context' into a html template

to run this script type `python jinjary.py`

then check the file `output.html`

### app.py

this file uses the same jinja2 template, but will run a flask web app to server them.

to run flask type
`python -m flask run`

then go to <http://127.0.0.1:5000> in your web browser