import modules.database as database
import modules.app_yaml as app_yaml
import modules.stock_app as app

def main():

    app.heading()
    # config = app_yaml.open_yaml("config.yaml")

    # Access the data
    #print("app_name: " + config["app_name"])
    #print("version:  " + str(config["version"]))

    # table_name=config["sql"]["table_name"]
    # table_sql=config["sql"]["table_sql"]
    # drop_table="DROP TABLE " + table_name
    # create_table=table_sql
    
    # connection = database.connection()
    # with connection:
    #     connection.execute(drop_table)
    #     connection.execute(create_table)

if __name__ == "__main__":
    main()
