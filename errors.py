from flask import flash, render_template
import re

limits = {}
limits["username"] = {}
limits["username"]["lenmax"] = 32
limits["username"]["lenmin"] = 2
limits["username"]["regex"] = "^[\w._\-]{2,32}$"
limits["password"] = {}
limits["password"]["lenmax"] = 5000
limits["password"]["lenmin"] = 8
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

verbose_limits = {}
verbose_limits["username"] = {}
verbose_limits["username"]["range"] = "The username must be in the range of " \
                                      + f"{limits['username']['lenmin']}–{limits['username']['lenmax']} characters."
verbose_limits["username"]["regex"] = "Each character in the username must be of any of the following types: " \
                                      "lowercase or uppercase alphanumeric (a–z, A–Z, 0–9), a full stop (.), an underscore (_), or a hyphen-minus (-)."
verbose_limits["username"]["unique"] = "The username must be unique."
verbose_limits["password"] = {}
verbose_limits["password"]["range"] = "The password must be in the range of " \
                                      + f"{limits['password']['lenmin']}–{limits['password']['lenmax']} characters."
verbose_limits["femtoyap_topic"] = {}
verbose_limits["femtoyap_topic"]["range"] = "The topic of the femtoyap must be in the range of " \
                                            + f"{limits['femtoyap_topic']['lenmin']}–{limits['femtoyap_topic']['lenmax']} characters."
verbose_limits["femtoyap_topic"]["regex"] = "Each character in the topic of the femtoyap must be of any of the following types: " \
                                            "lowercase alphanumeric (a–z, 0–9), an underscore (_), or a hyphen-minus (-)"
verbose_limits["femtoyap_topic"]["unique"] = "The topic of the femtoyap must be unique."
verbose_limits["attoyap_title"] = {}
verbose_limits["attoyap_title"]["range"] = "The title of the attoyap must be in the range of " \
                                            + f"{limits['attoyap_title']['lenmin']}–{limits['attoyap_title']['lenmax']} characters."
verbose_limits["zeptoyap_content"] = {}
verbose_limits["zeptoyap_content"]["range"] = "The zeptoyap must be in the range of " \
                                              + f"{limits['zeptoyap_content']['lenmin']}–{limits['zeptoyap_content']['lenmax']} characters."

error_msgs = {}
error_msgs["username"] = {}
error_msgs["username"]["exist"] = "The username does not exist!"
error_msgs["username"]["lenmax"] = f"The username is too long, over {limits['username']['lenmax']} characters!"
error_msgs["username"]["lenmin"] = f"The username is too short, less than {limits['username']['lenmin']} characters!"
error_msgs["username"]["regex"] = "The username has invalid character(s)!" 
error_msgs["username"]["unique"] = "The username is already taken!"
error_msgs["password"] = {}
error_msgs["password"]["lenmax"] = f"The password is too long, over {limits['password']['lenmax']} characters!"
error_msgs["password"]["lenmin"] = f"The password is too short, less than {limits['password']['lenmin']} characters!"
error_msgs["password"]["match"] = "The password inputs do not match!"
error_msgs["password"]["wrong"] = "The password is incorrect!"
error_msgs["femtoyap_topic"] = {}
error_msgs["femtoyap_topic"]["lenmax"] = f"The femtoyap topic name is too long, over {limits['femtoyap_topic']['lenmax']} characters!"
error_msgs["femtoyap_topic"]["lenmin"] = f"The femtoyap topic name is too short, less than {limits['femtoyap_topic']['lenmin']} characters!"
error_msgs["femtoyap_topic"]["regex"] = "The femtoyap topic name has invalid character(s)!"
error_msgs["femtoyap_topic"]["unique"] = "The femtoyap topic name is already taken!"
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

def get_restrictions(restriction_target):
    return [restriction for restriction in verbose_limits[restriction_target].values()]

def render_error(message, suggestion_name=None, suggested_path=None):
    if suggestion_name and not suggested_path:
        suggested_path = "/" + suggestion_name
    return render_template("error.html", message=message, suggested_path=suggested_path, suggestion_name=suggestion_name)