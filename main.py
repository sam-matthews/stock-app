import modules.database as database
import yaml

def main():
    # Read JSON Contents from file.
    mylist=database.demo_load_from_json()
    print(mylist)

    # Get Dictionary
    mydict=mylist[0]
    print(mydict.get("create_table"))
    # Open database connection.
    connection = database.connection()

    # Create table based on syntax from JSON File.
    with connection:
        connection.execute(mydict.get("create_table"))

def run_yaml():

    with open("config.yaml", "r") as file:
        config = yaml.safe_load(file)

    # Access the data
    print("app_name: " + config["app_name"])
    print("version:  " + str(config["version"]))  

    table_name=config["sql"]["table_name"]
    table_sql=config["sql"]["table_sql"]
    drop_table="DROP TABLE " + table_name
    create_table=table_sql
    
    connection = database.connection()
    with connection:
        connection.execute(drop_table)
        connection.execute(create_table)


if __name__ == "__main__":
    # main()
    run_yaml()
