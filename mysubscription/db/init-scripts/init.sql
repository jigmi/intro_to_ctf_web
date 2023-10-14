CREATE TABLE IF NOT EXISTS emails (
    email VARCHAR(50),
    date_joined VARCHAR(50),
    subscription_period VARCHAR(50),
    subscription_type VARCHAR(50),
    subscription_method VARCHAR(50)
);

USE mysql;
CREATE TABLE IF NOT EXISTS flag (
    flags VARCHAR(50)
);

INSERT INTO flag (flags) VALUES ('SECSOC{1l0v3uN10n1nJ3C710n}');

CREATE USER 'jig'@'%' IDENTIFIED BY 'ushouldntbehere';

GRANT SELECT ON *.* TO 'jig'@'%' IDENTIFIED BY 'ushouldntbehere';

FLUSH PRIVILEGES;