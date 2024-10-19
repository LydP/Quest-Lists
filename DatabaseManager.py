from PySide6 import QtSql


# TODO error handling
class DatabaseManager:
    def __init__(self):
        self.database = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.database.setDatabaseName('database/quest_lists_data.sqlite3')
        self.database.setConnectOptions('QSQLITE_ENABLE_REGEXP') # enable the use of regex

        self.database.open()

        self.query = QtSql.QSqlQuery()

    def count_quests(self, title):
        # TODO need to test this when database has some stuff in it
        """
        Creates a nested dictionary that organizes quest categories and their corresponding total number of quests
        and number of completed quests for a specified game and its DLCs.

        :param title: the game's title as a string
        :return: A dictionary of the form
        {Game:
            {Category:
                (quests completed, quest count)
            },
        DLC:
            {Category:
                (quests completed, quest count)
            }
        }
        """
        # query database for quest categories, any DLCs associated with the game, and the number of quests per category
        self.query.prepare("""
        SELECT
            qc.category_name,
            CASE
                WHEN DLCs.DLC_ID IS NULL THEN :game_title
                ELSE DLC_name
            END AS DLC_name,
            CASE
                WHEN DLCs.DLC_ID IS NULL THEN COUNT(q.quest_ID)
                ELSE COUNT(DLCq.quest_ID)
            END AS quest_counts,
            CASE
                WHEN DLCs.DLC_ID IS NULL THEN SUM(q.completion_state)
                ELSE SUM(DLCq.completion_state)
            END AS quests_completed
        FROM Quests q
            INNER JOIN Games g ON g.game_ID = q.game_ID
            INNER JOIN DLCs ON DLCs.game_ID = g.game_ID
            INNER JOIN QuestCategories qc ON qc.category_ID = q.category_ID
            INNER JOIN DLCQuests DLCq ON DLCq.DLC_ID = DLCs.DLC_ID
                AND DLCq.category_ID = qc.category_ID
        WHERE g.game_title = :game_title
        GROUP BY DLC_name, category_name
        """)
        self.query.bindValue(':game_title', title)
        self.query.exec()

        # store quest counts in nested dictionary
        quest_counts = {}
        while self.query.next():
            category_name = self.query.value(0)
            dlc_name = self.query.value(1)
            quest_count = self.query.value(2)
            quests_completed = self.query.value(3)

            if dlc_name not in quest_counts:
                quest_counts[dlc_name] = {}

            quest_counts[dlc_name][category_name] = (quests_completed, quest_count)

        return quest_counts

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
        primary_key: int
            The newly added game's primary key from the table
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

        primary_key = self.query.lastInsertId()

        return placeholder_title, placeholder_icon, primary_key

    def rename_game(self, old_name, new_name):
        """
        Change the game_title for a specified game in the Games table.

        :param old_name: The game's current name, as it exists in the database
        :param new_name: The game's new name, as defined by the user
        :return: None
        """
        self.query.prepare("""
        UPDATE Games
        SET game_title = :new_name
        WHERE game_title = :old_name
        """)
        self.query.bindValue(':old_name', old_name)
        self.query.bindValue(':new_name', new_name)
        self.query.exec()

    def get_all_games(self):
        """
        Queries the Games table for the game title, the path to its cover image, and its primary key and places
        them in a list of tuples.

        :return: A list of tuples containing the game titles, the paths to game icon images, and the game primary keys:
        [('Game Title', '/path/to/cover.jpg', game_id)]
        """
        self.query.prepare("""
        SELECT 
            game_ID,
            game_title,
            game_cover_path
        FROM Games
        ORDER BY game_title       
        """)
        self.query.exec()

        games_icons = []
        while self.query.next():
            games_icons.append((self.query.value(1), self.query.value(2), self.query.value(0)))

        return games_icons

    def close_database(self):
        """
        Closes the connection to the SQLite database

        :return: None
        """
        self.database.close()
