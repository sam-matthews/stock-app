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

    print("Starting yaml function")
    with open("config.yaml", "r") as file:
        config = yaml.safe_load(file)

    # Access the data
    print("app_name: " + config["app_name"])  # Output: MyApp
    print("theme: " + config["settings"]["theme"])  # Output: dark
    print("sql: "   + config["sql"])  # Output: sql

    sql=config["sql"]
    print("SQL from variable: " + sql)

    connection = database.connection()
    with connection:
        connection.execute(sql)


if __name__ == "__main__":
    # main()
    run_yaml()
