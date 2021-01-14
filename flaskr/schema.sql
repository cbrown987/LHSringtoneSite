DROP TABLE IF EXISTS files;
DROP TABLE IF EXISTS post;

CREATE TABLE files(
    name   TEXT NOT NULL ,
    username TEXT UNIQUE  NOT NULL,
    password TEXT NOT NULL
);
