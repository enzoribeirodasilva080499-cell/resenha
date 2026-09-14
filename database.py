import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "data" / "resenha.db"
DB_PATH.parent.mkdir(exist_ok=True)

db = sqlite3.connect(DB_PATH, check_same_thread=False)
db.row_factory = sqlite3.Row

def init_db():
    db.executescript("""
    CREATE TABLE IF NOT EXISTS users(
        guild_id INTEGER, user_id INTEGER,
        xp INTEGER DEFAULT 0, level INTEGER DEFAULT 0,
        coins INTEGER DEFAULT 0, daily INTEGER DEFAULT 0,
        PRIMARY KEY(guild_id,user_id)
    );
    CREATE TABLE IF NOT EXISTS warnings(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        guild_id INTEGER, user_id INTEGER, moderator_id INTEGER,
        reason TEXT, created_at INTEGER
    );
    CREATE TABLE IF NOT EXISTS config(
        guild_id INTEGER PRIMARY KEY,
        welcome_channel INTEGER,
        leave_channel INTEGER,
        log_channel INTEGER
    );
    """)
    db.commit()

def ensure_user(guild_id, user_id):
    db.execute("INSERT OR IGNORE INTO users(guild_id,user_id) VALUES(?,?)",
               (guild_id,user_id))
    db.commit()

def user(guild_id, user_id):
    ensure_user(guild_id,user_id)
    return db.execute("SELECT * FROM users WHERE guild_id=? AND user_id=?",
                      (guild_id,user_id)).fetchone()
