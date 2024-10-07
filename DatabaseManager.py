from PySide6 import QtSql


# TODO error handling
class DatabaseManager:
    def __init__(self):
        self.database = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.database.setDatabaseName('database/quest_lists_data.sqlite3')
        self.database.setConnectOptions('QSQLITE_ENABLE_REGEXP') # enable the use of regex

        self.database.open()

        self.query = QtSql.QSqlQuery()

    def add_new_game(self):
        """
        Adds a new placeholder title and icon path to the Games table. The placeholder title will be 'New Game' or
        'New Game <n>', where <n> is the next available integer in the sequence of existing game titles. If 'New
        Game' already exists, the next available title will be 'New Game 1', 'New Game 2', and so on. The method
        ensures that any gaps in the sequence are filled (e.g., if 'New Game 2' and 'New Game 4' exist, the next title
        will be 'New Game 3').

        :return:
        placeholder_title: str
            The placeholder title added to the database
        placeholder_icon: str
            The path to the placeholder icon added to the database
        """
        placeholder_title = 'New Game'
        placeholder_icon = 'resources/test_img.jpg'

        # query iteration value of placeholder_title iteration from Games table (e.g. '<placeholder_title>' yields 0,
        # '<placeholder_title> 1' yields 1, etc.)
        self.query.prepare(r"""
        SELECT
            CASE
                WHEN SUBSTR(game_title, LENGTH(:game_title) + 2) = '' THEN 0
                ELSE CAST(SUBSTR(game_title, LENGTH(:game_title) + 2) AS INTEGER)                
            END
        FROM Games
        WHERE game_title REGEXP :game_title || '(\s[0-9]+)?$'
        """)
        self.query.bindValue(':game_title', placeholder_title)
        self.query.exec()

        # place iteration values in a list
        new_games = []
        # NB: next() always returns True at least once, even when the query returns nothing and the table from which it
        # is querying is empty
        while self.query.next():
            new_games.append(self.query.value(0))

        # find the largest number from a sequence of consecutive iteration values, increment, and append to
        # placeholder_title
        new_games = sorted(new_games)
        if new_games and (min(new_games) == 0):
            for i, n in enumerate(new_games):
                if i != n:
                    placeholder_title = f'{placeholder_title} {new_games[i - 1] + 1}'
                    break

            if (i == (len(new_games) - 1)) and (i == new_games[i]):
                placeholder_title = f'{placeholder_title} {i + 1}'

        # add placeholder_title and placeholder_icon to Games table
        self.query.prepare("""
        INSERT INTO Games (game_title, game_cover_path)
        VALUES (:game_title, :game_icon)
        """)
        self.query.bindValue(':game_title', placeholder_title)
        self.query.bindValue(':game_icon', placeholder_icon)
        self.query.exec()

        return placeholder_title, placeholder_icon

    def get_all_games(self):
        """
        Queries the Games table for the game title and the path to its cover image and places them in a list of tuples.

        :return: A list of tuples containing the game titles and the paths to game icon images:
        [('Game Title', '/path/to/cover.jpg')]
        """
        self.query.prepare("""
        SELECT 
            game_title,
            game_cover_path
        FROM Games            
        """)
        self.query.exec()

        games_icons = []
        while self.query.next():
            games_icons.append((self.query.value(0), self.query.value(1)))

        return games_icons

    def close_database(self):
        """
        Closes the connection to the SQLite database

        :return: None
        """
        self.database.close()
