import modules.database as database
import modules.app_yaml as app_yaml
import modules.stock_app as app

def main():

    app.heading()
    app.build_database()

if __name__ == "__main__":
    main()
