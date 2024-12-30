import modules.stock_json as stock_json
import pprint
import modules.database as database

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

if __name__ == "__main__":
    main()
