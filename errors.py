from flask import flash, render_template
import re
import users

# raw limit values for various targets
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

# limit values represented with readable text, with some database-related additions, like uniqueness (good for giving the end user readable instructions automatically when filling out forms)
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

# error messages. accounts for raw limit values, database-related restrictions as well as some other conditions not in verbose_limits (e.g. login status)
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
error_msgs["password_login"] = {}
error_msgs["password_login"]["wrong"] = "The password is incorrect!"
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
error_msgs["login_need"] = {}
error_msgs["login_need"]["base"] = "You are not logged in!"
error_msgs["login_need"]["create_attoyap"] = f"{error_msgs['login_need']['base']} You must be logged in to create attoyaps!"
error_msgs["login_need"]["create_zeptoyap"] = f"{error_msgs['login_need']['base']} You must be logged in to create zeptoyaps!"
error_msgs["login_need"]["logout"] = f"{error_msgs['login_need']['base']} You must be logged in to log out!"

succ_msgs = {} 
# value is a tuple if parameters (e.g. username) are needed. 
# The integers represent the order of the parameters. The parameters are given to the flash_succ function as a list.
succ_msgs["login"] = ("Successfully logged in as ", 0, ".")
succ_msgs["login_again"] = ("Successfully logged out and logged in. You are now logged in as ", 0, ".")
succ_msgs["logout"] = "Successfully logged out."
succ_msgs["signup"] = "Successfully created a new account."
succ_msgs["signup_again"] = ("Successfully logged out and created a new account. You are now logged in as ", 0, ".")

def check_errors(check_target, sample=None): 
    has_errors = False
    if check_target in error_msgs["login_need"].keys():
        # check_target needs the user to be logged in
        if not users.is_logged_in():
            has_errors = True
            flash_error("login_need", check_target)
    if check_target in limits.keys():
        # expected sample type: string
        # this block is for common restrictions, like lower and upper bounds for string length and regular expressions
        # if check_target has other restrictions, they are handled in another block
        for limit in limits[check_target].keys():
            if limit == "lenmax":
                if limits[check_target][limit] < len(sample):
                    has_errors = True
                    flash_error(check_target, limit)
            if limit == "lenmin":
                if limits[check_target][limit] > len(sample):
                    has_errors = True
                    flash_error(check_target, limit)
            if limit == "regex":
                if not re.search(limits[check_target][limit], sample):
                    has_errors = True
                    flash_error(check_target, limit)
    if check_target == "password":
        # expected sample type: 2-tuple: (password, password_again)
        if sample[1] != sample[0]:
            has_errors = True
            flash_error(check_target, "match")
    return has_errors

def flash_error(upper_key, lower_key):
    flash(error_msgs[upper_key][lower_key], "error")
    return

def flash_succ(action, parameters=None):
    base = succ_msgs[action]
    if parameters:
        # expected type of parameters: list
        temp = map(lambda base_part, params : params[base_part] if type(base_part) is int else base_part, base)
        base = "".join(list(temp))
    flash(base, "info")
    return

def get_restrictions(restriction_target):
    return [restriction for restriction in verbose_limits[restriction_target].values()]

def render_error(message, suggestion_name=None, suggested_path=None):
    if suggestion_name and not suggested_path:
        suggested_path = "/" + suggestion_name
    return render_template("error.html", message=message, suggested_path=suggested_path, suggestion_name=suggestion_name)