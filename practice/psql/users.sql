-----主キーはid INTEGER PRIMARY KEY AUTOINCREMENT,これにする
--ここにおいてデータベースの編集するにはまずpracticeディレクトリに移動する必要がある
-- その後、psqlを起動する
-- そこでsqlite3 app.dbこのコマンドを実行する
-- するとsqliteのプロンプトが表示されるので、そこでSQL文を実行する
-- 例えば、CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT, nameなどなど

CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
