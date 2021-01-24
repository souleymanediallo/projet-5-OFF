from app import App


def main():
    c = App()
    c.import_db()
    while True:
        c.scenario()


if __name__ == "__main__":
    main()

