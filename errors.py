from flask import flash, render_template
import re

limits = {}
limits["username"] = {}
limits["username"]["lenmax"] = 32
limits["username"]["lenmin"] = 2
limits["username"]["regex"] = "^[\w._\-]{2,32}$"
limits["femtoyap_topic"] = {}
limits["femtoyap_topic"]["lenmax"] = 32
limits["femtoyap_topic"]["lenmin"] = 1
limits["femtoyap_topic"]["regex"] = "^[a-z0-9_\-]{1,32}$"
limits["attoyap_title"] = {}
limits["attoyap_title"]["lenmax"] = 100
limits["attoyap_title"]["lenmin"] = 1
limits["zeptoyap_content"] = {}
limits["zeptoyap_content"]["lenmax"] = 5000
limits["zeptoyap_content"]["lenmin"] = 1

error_msgs = {}
error_msgs["username"] = {}
error_msgs["username"]["lenmax"] = f"The username is too long, over {limits['username']['lenmax']} characters!"
error_msgs["username"]["lenmin"] = f"The username is too short, less than {limits['username']['lenmin']} characters!"
error_msgs["username"]["regex"] = "The username has invalid character(s)!"
error_msgs["username"]["taken"] = "The username is already taken!"
error_msgs["femtoyap_topic"] = {}
error_msgs["femtoyap_topic"]["lenmax"] = f"The femtoyap topic name is too long, over {limits['femtoyap_topic']['lenmax']} characters!"
error_msgs["femtoyap_topic"]["lenmin"] = f"The femtoyap topic name is too short, less than {limits['femtoyap_topic']['lenmin']} characters!"
error_msgs["femtoyap_topic"]["regex"] = "The femtoyap topic name has invalid character(s)!"
error_msgs["femtoyap_topic"]["taken"] = "The femtoyap topic name is already taken!"
error_msgs["attoyap_title"] = {}
error_msgs["attoyap_title"]["lenmax"] = f"The attoyap title is too long, over {limits['attoyap_title']['lenmax']} characters!"
error_msgs["attoyap_title"]["lenmin"] = f"The attoyap title is too short, less than {limits['attoyap_title']['lenmin']} characters!"
error_msgs["zeptoyap_content"] = {}
error_msgs["zeptoyap_content"]["lenmax"] = f"The zeptoyap is too long, over {limits['zeptoyap_content']['lenmax']} characters!"
error_msgs["zeptoyap_content"]["lenmin"] = f"The zeptoyap is too short, less than {limits['zeptoyap_content']['lenmin']} characters!"

def check_errors(restriction_target, sample):
    has_errors = False
    for limit in limits[restriction_target].keys():
        if limit == "lenmax":
            if limits[restriction_target][limit] < len(sample):
                has_errors = True
                flash(error_msgs[restriction_target][limit], "error")
        if limit == "lenmin":
            if limits[restriction_target][limit] > len(sample):
                has_errors = True
                flash(error_msgs[restriction_target][limit], "error")
        if limit == "regex":
            if not re.search(limits[restriction_target][limit], sample):
                has_errors = True
                flash(error_msgs[restriction_target][limit], "error")
    return has_errors

def render_error(message, suggestion_name=None, suggested_path=None):
    if suggestion_name and not suggested_path:
        suggested_path = "/" + suggestion_name
    return render_template("error.html", message=message, suggested_path=suggested_path, suggestion_name=suggestion_name)