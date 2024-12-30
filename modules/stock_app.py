# This module is used to store the main functions which get called.

import modules.app_yaml as app_yaml
import modules.database as db

def heading():
    config = app_yaml.open_yaml("config.yaml")

    print("app_name: " + config["app_name"])
    print("version:  " + str(config["version"]))
    print("=====================================")

def build_database():

    # Open yaml and grab some SQL to run.
    config = app_yaml.open_yaml("config.yaml")
    create_table=config["sql"]["table_sql"]
    drop_table="DROP TABLE " + config["sql"]["table_name"]

    # Open DB Connection.
    connection = db.connection()
    with connection:
        connection.execute(drop_table)
        connection.execute(create_table)