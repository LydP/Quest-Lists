from PySide6 import QtSql

# TODO error handling
class DatabaseManager:
    def __init__(self):
        self.database = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.database.setDatabaseName('database/quest_lists_data.sqlite3')
        self.database.setConnectOptions('QSQLITE_ENABLE_REGEXP') # enable the use of regex

        self.database.open()

        self.query = QtSql.QSqlQuery()

    def add_game(self):
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
        while self.query.next():
            new_games.append(self.query.value(0))

        # find the largest number from a series of consecutive iteration values, increment, and append to
        # placeholder_title
        new_games = sorted(new_games)
        if new_games and (min(new_games) == 0):
            for i, n in enumerate(new_games):
                if i != n:
                    placeholder_title = f'{placeholder_title} {new_games[i - 1] + 1}'
                    break

            if (i == (len(new_games) - 1)) and (i == new_games[i]):
                placeholder_title = f'{placeholder_title} {i + 1}'

        # add placeholder_title and icon to Games table
        self.query.prepare("""
        INSERT INTO Games (game_title, game_cover_path)
        VALUES (:game_title, :game_icon)
        """)
        self.query.bindValue(':game_title', placeholder_title)
        self.query.bindValue(':game_icon', placeholder_icon)
        self.query.exec()
