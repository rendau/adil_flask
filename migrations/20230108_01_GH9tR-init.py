"""
init
"""

from yoyo import step

__depends__ = {}

steps = [
    step(
        """
            CREATE TABLE IF NOT EXISTS book (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT not null default '',
                author TEXT not null default '',
                year INTEGER not null
            );
        """,
        "DROP TABLE if exists book",
    )
]
