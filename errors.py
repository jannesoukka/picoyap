from flask import render_template

def render_error(message, suggestion_name=None, suggested_path=None):
    if suggestion_name and not suggested_path:
        suggested_path = "/" + suggestion_name
    return render_template("error.html", message=message, suggested_path=suggested_path, suggestion_name=suggestion_name)