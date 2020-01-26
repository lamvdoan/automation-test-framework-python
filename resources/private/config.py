import configparser
import os

"""
The path fetches the parent working directory and aggregates that with the secrets.ini file.
The config will read the section and the field name, which gets assigned to a variable.

Requirement:
1. Make sure the secrets.ini exist
2. The path of the file is correct
3. The PYTHONPATH is set up properly in your ~/.bash_profile
"""

config = configparser.ConfigParser()


def get_config_value(section, field):
    """
    Retrieve the values from the secrets.ini

    :param section: Section
    :param field: field
    :return: String value corresponding to the field
    """

    try:
        value = config.get(section, field)
        return value
    except configparser.NoOptionError:
        print("Missing Option: Section={}, Field={}.  Field does not exist in secrets.ini!".format(section, field))
    except configparser.NoSectionError:
        print("Missing Section: Section={}, Field={}.  Section does not exist in secrets.ini!".format(section, field))


# Returns e.g. /Users/Lam.Doan/Code/automation-test-framework-python/resources/private
private_directory_path = os.path.dirname(os.path.abspath(__file__))

# Returns e.g. /Users/Lam.Doan/Code/automation-test-framework-python/resources/private/secrets.ini
secrets_path = os.path.join(os.path.expandvars(private_directory_path), "secrets.ini")

try:
    config.read(secrets_path)
except Exception as e:
    print("Path: {}".format(secrets_path))
    print("Config Error: {}".format(e))
    print("Check the secrets.ini to make sure it has all the parameters that are listed in the secrets_template.ini")

#CONFIG
MOBILE_TYPE = get_config_value("mobile-config", "mobile_type")

# URL
FETCH_HOST = get_config_value("fetch-prod", "host")

# AUTOMATION CONFIGS
APPIUM_DRIVER_HOST = "http://localhost:4723/wd/hub"
CHROME_DRIVER_PATH = private_directory_path + "/../chromedriver/chromedriver"

