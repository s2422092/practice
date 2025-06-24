-- users テーブルが存在する場合は削除
DROP TABLE IF EXISTS users;

-- ユーザー情報を格納するテーブルを作成
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);