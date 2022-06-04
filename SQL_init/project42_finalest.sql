-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `mydb`;
CREATE SCHEMA `mydb`;
USE `mydb`;

-- -----------------------------------------------------
-- Table `mydb`.`organizations`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`organizations` (
  `org_ID` INT NOT NULL,
  `org_name` VARCHAR(45) NOT NULL,
  `org_acronym` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`org_ID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`researchers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`researchers` (
  `researcher_ID` INT NOT NULL,
  `first_name` VARCHAR(45) NOT NULL,
  `last_name` VARCHAR(45) NOT NULL,
  `gender` VARCHAR(50) NOT NULL,
  `birth_date` DATE NOT NULL,
  `org_ID` INT NOT NULL,
  `employment_starting_date` DATE NOT NULL,
  PRIMARY KEY (`researcher_ID`),
  INDEX `fk_researchers_organizations1_idx` (`org_ID`),
  CONSTRAINT `fk_researchers_organizations1`
    FOREIGN KEY (`org_ID`)
    REFERENCES `mydb`.`organizations` (`org_ID`)
    ON DELETE cascade
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`HFRI_department`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`HFRI_department` (
  `HFRI_department_ID` INT NOT NULL,
  `HFRI_department_name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`HFRI_department_ID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`financial_programme`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`financial_programme` (
  `programme_ID` INT NOT NULL,
  `HFRI_department_ID` INT NOT NULL,
  PRIMARY KEY (`programme_ID`),
  INDEX `fk_financial_programme_HFRI_department1_idx` (`HFRI_department_ID`),
  CONSTRAINT `fk_financial_programme_HFRI_department1`
    FOREIGN KEY (`HFRI_department_ID`)
    REFERENCES `mydb`.`HFRI_department` (`HFRI_department_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`HFRI_executives`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`HFRI_executives` (
  `executive_ID` INT NOT NULL,
  `executive_first_name` VARCHAR(45) NOT NULL,
  `executive_last_name` VARCHAR(45) NOT NULL,
  `HFRI_department_ID` INT NOT NULL,
  PRIMARY KEY (`executive_ID`),
  INDEX `fk_HFRI_executives_HFRI_department1_idx` (`HFRI_department_ID`),
  CONSTRAINT `fk_HFRI_executives_HFRI_department1`
    FOREIGN KEY (`HFRI_department_ID`)
    REFERENCES `mydb`.`HFRI_department` (`HFRI_department_ID`)
    ON DELETE cascade
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`projects`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`projects` (
  `project_ID` INT NOT NULL,
  `project_title` VARCHAR(8000) NOT NULL,
  `project_starting_date` DATE NOT NULL,
  `project_summary` VARCHAR(8000) NOT NULL,
  `project_due_date` DATE NOT NULL,
  `supervisor_executive_ID` INT NOT NULL,
  `supervisor_researcher_ID` INT NOT NULL,
  `org_ID` INT NOT NULL,
  `capital` INT NOT NULL,
  `programme_ID` INT NOT NULL,
  PRIMARY KEY (`project_ID`),
  INDEX `fk_projects_researchers_idx` (`supervisor_researcher_ID`),
  INDEX `fk_projects_financial_programme1_idx` (`programme_ID`),
  INDEX `fk_projects_HFRI_executives1_idx` (`supervisor_executive_ID`),
  INDEX `fk_projects_organizations1_idx` (`org_ID`),
  CONSTRAINT `fk_projects_researchers`
    FOREIGN KEY (`supervisor_researcher_ID`)
    REFERENCES `mydb`.`researchers` (`researcher_ID`)
    ON DELETE no action
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_projects_financial_programme1`
    FOREIGN KEY (`programme_ID`)
    REFERENCES `mydb`.`financial_programme` (`programme_ID`)
    ON DELETE cascade
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_projects_HFRI_executives1`
    FOREIGN KEY (`supervisor_executive_ID`)
    REFERENCES `mydb`.`HFRI_executives` (`executive_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_projects_organizations1`
    FOREIGN KEY (`org_ID`)
    REFERENCES `mydb`.`organizations` (`org_ID`)
    ON DELETE cascade 
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`organization_address`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`organization_address` (
  `org_ID` INT NOT NULL,
  `street` VARCHAR(80) NOT NULL,
  `st_number` INT NOT NULL,
  `ZIP_code` INT NOT NULL,
  `city` VARCHAR(80) NOT NULL,
  PRIMARY KEY (`org_ID`, `street`, `st_number`, `ZIP_code`, `city`),
  INDEX `fk_organization_address_organizations1_idx` (`org_ID`),
  CONSTRAINT `fk_organization_address_organizations1`
    FOREIGN KEY (`org_ID`)
    REFERENCES `mydb`.`organizations` (`org_ID`)
    ON DELETE cascade
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`organization_telephone`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`organization_telephone` (
  `org_ID` INT NOT NULL,
  `telephone` VARCHAR(40) NOT NULL,
  PRIMARY KEY (`org_ID`, `telephone`),
  INDEX `fk_organization_telephone_organizations1_idx` (`org_ID`),
  CONSTRAINT `fk_organization_telephone_organizations1`
    FOREIGN KEY (`org_ID`)
    REFERENCES `mydb`.`organizations` (`org_ID`)
    ON DELETE cascade
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`company`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`company` (
  `company_ID` INT NOT NULL,
  `capital` INT NOT NULL,
  `org_ID` INT NOT NULL,
  PRIMARY KEY (`company_ID`, `org_ID`),
  INDEX `fk_company_organizations1_idx` (`org_ID`),
  CONSTRAINT `fk_company_organizations1`
    FOREIGN KEY (`org_ID`)
    REFERENCES `mydb`.`organizations` (`org_ID`)
    ON DELETE cascade
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`university`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`university` (
  `university_ID` INT NOT NULL,
  `ministry_budget` INT NOT NULL,
  `org_ID` INT NOT NULL,
  PRIMARY KEY (`university_ID`, `org_ID`),
  INDEX `fk_university_organizations1_idx` (`org_ID`),
  CONSTRAINT `fk_university_organizations1`
    FOREIGN KEY (`org_ID`)
    REFERENCES `mydb`.`organizations` (`org_ID`)
    ON DELETE cascade
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`research_center`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`research_center` (
  `research_center_ID` INT NOT NULL,
  `ministry_budget` INT NOT NULL,
  `private_budget` INT NOT NULL,
  `org_ID` INT NOT NULL,
  PRIMARY KEY (`research_center_ID`, `org_ID`),
  INDEX `fk_research_center_organizations1_idx` (`org_ID`),
  CONSTRAINT `fk_research_center_organizations1`
    FOREIGN KEY (`org_ID`)
    REFERENCES `mydb`.`organizations` (`org_ID`)
    ON DELETE cascade
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`final_product`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`final_product` (
  `product_ID` INT NOT NULL,
  `product_title` VARCHAR(8000) NOT NULL,
  `project_ID` INT NOT NULL,
  `product_summary` VARCHAR(8000),
  `product_due_date` DATE NOT NULL,
  PRIMARY KEY (`product_ID`, `project_ID`),
  INDEX `fk_final_product_projects1_idx` (`project_ID`),
  CONSTRAINT `fk_final_product_projects1`
    FOREIGN KEY (`project_ID`)
    REFERENCES `mydb`.`projects` (`project_ID`)
    ON DELETE cascade
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`scientific_field`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`scientific_field` (
  `scientific_field_name` VARCHAR(80) NOT NULL,
  PRIMARY KEY (`scientific_field_name`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`belongs_to`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`belongs_to` (
  `scientific_field` VARCHAR(80) NOT NULL,
  `project_ID` INT NOT NULL,
  PRIMARY KEY (`scientific_field`, `project_ID`),
  INDEX `fk_belongs_to_projects1_idx` (`project_ID`),
  CONSTRAINT `fk_belongs_to_scientific_field1`
    FOREIGN KEY (`scientific_field`)
    REFERENCES `mydb`.`scientific_field` (`scientific_field_name`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_belongs_to_projects1`
    FOREIGN KEY (`project_ID`)
    REFERENCES `mydb`.`projects` (`project_ID`)
    ON DELETE cascade
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`works`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`works` (
  `researcher_ID` INT NOT NULL,
  `project_ID` INT NOT NULL,
  PRIMARY KEY (`researcher_ID`, `project_ID`),
  INDEX `fk_works_projects1_idx` (`project_ID`),
  CONSTRAINT `fk_works_researchers1`
    FOREIGN KEY (`researcher_ID`)
    REFERENCES `mydb`.`researchers` (`researcher_ID`)
    ON DELETE no action
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_works_projects1`
    FOREIGN KEY (`project_ID`)
    REFERENCES `mydb`.`projects` (`project_ID`)
    ON DELETE cascade
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`evaluate`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`evaluate` (
  `researcher_ID` INT NOT NULL,
  `project_ID` INT NOT NULL,
  `grade` VARCHAR(45) NOT NULL,
  `evaluation_date` DATE NOT NULL,
  PRIMARY KEY (`researcher_ID`, `project_ID`),
  INDEX `fk_evaluate_projects1_idx` (`project_ID`),
  CONSTRAINT `fk_evaluate_researchers1`
    FOREIGN KEY (`researcher_ID`)
    REFERENCES `mydb`.`researchers` (`researcher_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_evaluate_projects1`
    FOREIGN KEY (`project_ID`)
    REFERENCES `mydb`.`projects` (`project_ID`)
    ON DELETE cascade
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
