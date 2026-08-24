import sqlite3
from pathlib import Path
from datetime import datetime

# ─── SQLite Database ──────────────────────────────────────────────────────────
DB_PATH = Path(__file__).parent.parent / "transcriptions.db"

def init_db():
    """Create database and table if they don't exist."""
    conn = sqlite3.connect(DB_PATH)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS transcriptions (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            filename    TEXT,
            language    TEXT,
            model       TEXT,
            text        TEXT,
            word_count  INTEGER,
            created_at  TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_transcription(filename, language, model, text):
    """Persist a transcription to SQLite."""
    conn = sqlite3.connect(DB_PATH)
    word_count = len(text.split())
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conn.execute(
        "INSERT INTO transcriptions (filename, language, model, text, word_count, created_at) VALUES (?, ?, ?, ?, ?, ?)",
        (filename, language, model, text, word_count, created_at)
    )
    conn.commit()
    conn.close()

def load_history(limit=30):
    """Load recent transcriptions from SQLite."""
    conn = sqlite3.connect(DB_PATH)
    rows = conn.execute(
        "SELECT id, filename, language, model, text, word_count, created_at FROM transcriptions ORDER BY id DESC LIMIT ?",
        (limit,)
    ).fetchall()
    conn.close()
    return rows

def delete_transcription(row_id):
    """Delete a transcription by id."""
    conn = sqlite3.connect(DB_PATH)
    conn.execute("DELETE FROM transcriptions WHERE id = ?", (row_id,))
    conn.commit()
    conn.close()

def clear_all_history():
    """Delete all transcriptions."""
    conn = sqlite3.connect(DB_PATH)
    conn.execute("DELETE FROM transcriptions")
    conn.commit()
    conn.close()

# Initialize when imported
init_db()
