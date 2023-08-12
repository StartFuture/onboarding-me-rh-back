CREATE DATABASE IF NOT EXISTS onboarding_me DEFAULT CHARACTER SET utf8;
USE onboarding_me;


CREATE TABLE IF NOT EXISTS Company (
  id BIGINT AUTO_INCREMENT,
  company_name VARCHAR(255) NOT NULL,
  trading_name VARCHAR(255),
  logo BLOB,
  cnpj VARCHAR(14) NOT NULL UNIQUE,
  email VARCHAR(255) NOT NULL UNIQUE,
  company_password VARCHAR(255) NOT NULL,
  state_register VARCHAR(14),
  PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS Address (
  id BIGINT AUTO_INCREMENT,
  num VARCHAR(255) NOT NULL,
  complement VARCHAR(255),
  zipcode VARCHAR(8) NOT NULL,
  street VARCHAR(255) NOT NULL,
  district VARCHAR(255) NOT NULL,
  city VARCHAR(255) NOT NULL,
  state VARCHAR(255) NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS Employee (
  id BIGINT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  surname VARCHAR(255) NOT NULL,
  birthdate DATE NOT NULL,
  employee_role VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL UNIQUE,
  employee_password VARCHAR(255) NOT NULL,
  phone_number VARCHAR(14),
  cpf VARCHAR(11) NOT NULL UNIQUE,
  level_access ENUM('admin', 'manager', 'default') NOT NULL,
  company_id BIGINT NOT NULL,
  address_id BIGINT NOT NULL,
  FOREIGN KEY (company_id) REFERENCES Company (id),
  FOREIGN KEY (address_id) REFERENCES Address (id),
  PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS WelcomeKit (
  id BIGINT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  image BLOB,
  PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS WelcomeKitItem (
  id BIGINT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  image BLOB NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS WelcomeKit_WelcomeKitItem (
  id BIGINT AUTO_INCREMENT,
  welcome_kit_id BIGINT NOT NULL,
  item_id BIGINT NOT NULL,
  FOREIGN KEY (welcome_kit_id) REFERENCES WelcomeKit (id),
  FOREIGN KEY (item_id) REFERENCES WelcomeKitItem (id),
  PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS Tracking (
  id BIGINT AUTO_INCREMENT,
  tracking_code VARCHAR(255) NOT NULL UNIQUE,
  status ENUM('to_be_send','sended','delivered') NOT NULL,
  employee_id BIGINT NOT NULL,
  welcome_kit_id BIGINT NOT NULL,
  FOREIGN KEY (employee_id) REFERENCES Employee (id),
  FOREIGN KEY (welcome_kit_id) REFERENCES WelcomeKit (id),
  PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS Chat (
  id BIGINT AUTO_INCREMENT,
  company_id BIGINT,
  first_employee_id BIGINT NOT NULL,
  FOREIGN KEY (company_id) REFERENCES Company (id),
  FOREIGN KEY (first_employee_id) REFERENCES Employee (id),
  PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS Chat_Employee (
  id BIGINT AUTO_INCREMENT,
  chat_id BIGINT NOT NULL,
  second_employee_id BIGINT NOT NULL,
  FOREIGN KEY (chat_id) REFERENCES Chat (id),
  FOREIGN KEY (second_employee_id) REFERENCES Employee (id),
  PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS Message (
  id BIGINT AUTO_INCREMENT,
  user_to BIGINT NOT NULL,
  user_from BIGINT NOT NULL,
  message VARCHAR(255) NOT NULL,
  created_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  read_date TIMESTAMP,
  chat_id BIGINT NOT NULL,
  FOREIGN KEY (chat_id) REFERENCES Chat (id),
  PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS GamifiedJourney (
  id BIGINT AUTO_INCREMENT,
  welcome_video_link VARCHAR(255),
  company_id BIGINT NOT NULL,
  FOREIGN KEY (company_id) REFERENCES Company (id),
  PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS Game (
  id BIGINT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  gamified_journey_id BIGINT NOT NULL,
  FOREIGN KEY (gamified_journey_id) REFERENCES GamifiedJourney (id),
  PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS Medal (
  id BIGINT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  image BLOB NOT NULL,
  game_id BIGINT NOT NULL,
  FOREIGN KEY (game_id) REFERENCES Game (id),
  PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS Score (
  id BIGINT AUTO_INCREMENT,
  total_points INTEGER NOT NULL DEFAULT 0,
  last_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  employee_id BIGINT NOT NULL,
  FOREIGN KEY (employee_id) REFERENCES Employee (id),
  PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS Medal_Score (
  id BIGINT AUTO_INCREMENT,
  medal_id BIGINT NOT NULL,
  score_id BIGINT NOT NULL,
  FOREIGN KEY (medal_id) REFERENCES Medal (id),
  FOREIGN KEY (score_id) REFERENCES Score (id),
  PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS Quiz (
  id BIGINT AUTO_INCREMENT,
  link_video VARCHAR(255) NOT NULL,
  score INTEGER NOT NULL,
  title VARCHAR(255) NOT NULL,
  question VARCHAR(255) NOT NULL,
  quiz_type ENUM('culture','principle') NOT NULL,
  game_id BIGINT NOT NULL,
  FOREIGN KEY (game_id) REFERENCES Game (id),
  PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS Alternative (
  id BIGINT AUTO_INCREMENT,
  alternative_text VARCHAR(255) NOT NULL,
  is_answer TINYINT NOT NULL DEFAULT 0,
  quiz_id BIGINT NOT NULL,
  FOREIGN KEY (quiz_id) REFERENCES Quiz (id),
  PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS CategoryTool (
  id BIGINT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS Tool (
  id BIGINT AUTO_INCREMENT,
  link_download VARCHAR(255) NOT NULL,
  score INTEGER NOT NULL,
  name VARCHAR(255) NOT NULL,
  game_id BIGINT NOT NULL,
  category_id BIGINT NOT NULL,
  FOREIGN KEY (game_id) REFERENCES Game (id),
  FOREIGN KEY (category_id) REFERENCES CategoryTool (id),
  PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS Employee_Alternative (
  id BIGINT AUTO_INCREMENT,
  employee_id BIGINT NOT NULL,
  alternative_id BIGINT NOT NULL,
  FOREIGN KEY (employee_id) REFERENCES Employee (id),
  FOREIGN KEY (alternative_id) REFERENCES Alternative (id),
  PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS Employee_Tool (
  id BIGINT AUTO_INCREMENT,
  employee_id BIGINT NOT NULL,
  tool_id BIGINT NOT NULL,
  FOREIGN KEY (employee_id) REFERENCES Employee (id),
  FOREIGN KEY (tool_id) REFERENCES Tool (id),
  PRIMARY KEY (id)
);