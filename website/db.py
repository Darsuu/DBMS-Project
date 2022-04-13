from os import curdir
import sqlite3

conn = sqlite3.connect("hospital.db")
cur = conn.cursor()
conn.isolation_level = None

# ALL TABLE DROP QUERIES
cur.execute("begin")
try:
    cur.execute("""DROP TABLE IF EXISTS PATIENT""")
    cur.execute("""DROP TABLE IF EXISTS DOCTOR""")
    cur.execute("""DROP TABLE IF EXISTS PATIENTAPPOINTMENTS""")
    cur.execute("""DROP TABLE IF EXISTS MEDICALRECORD""")
    cur.execute("""DROP VIEW IF EXISTS PATIENT_VIEW""")
    cur.execute("""DROP VIEW IF EXISTS DOCTOR_VIEW""")
    cur.execute("""DROP VIEW IF EXISTS APPOINTMENT_VIEW""")
    cur.execute("commit")
except:
    cur.execute("rollback")

# ALL THE TABLE CREATION QUERIES
pat_table = """ CREATE TABLE PATIENT (
            Name VARCHAR(255) NOT NULL,
            ID INTEGER PRIMARY KEY,
            PhoneNo INT NOT NULL UNIQUE
        ); """

doc_table = """ CREATE TABLE DOCTOR (
            Name VARCHAR(255) NOT NULL,
            ID INTEGER PRIMARY KEY,
            Dept VARCHAR(255) NOT NULL,
            PatNo INTEGER DEFAULT 0 NOT NULL 
        );"""

patappt_table = """ CREATE TABLE PATIENTAPPOINTMENTS (
            PatID INTEGER,
            DocID INTEGER,
            Symptoms VARCHAR(255),
            FOREIGN KEY (PatID) references PATIENT(ID),
            FOREIGN KEY (DocID) references DOCTOR(ID),
            PRIMARY KEY (PatID, DocID)
        );""" 

medrec_table = """ CREATE TABLE MEDICALRECORD (
            PatID INTEGER,
            DocID INTEGER,
            Ailments VARCHAR(255),
            Medication VARCHAR(255),
            Diagnosis VARCHAR(255),
            Date TEXT,
            FOREIGN KEY (PatID) references PATIENT(ID),
            FOREIGN KEY (DocID) references DOCTOR(ID),
            PRIMARY KEY (PatID, DocID)
        );""" 

# ALL INSERTING VALUE QUERIES       
doc_val1 = """ INSERT INTO DOCTOR (Name, Dept) VALUES ('Mohan', 'Cardiology');"""
doc_val2 = """ INSERT INTO DOCTOR (Name, Dept) VALUES ('Suresh', 'Physiology');"""

# EXECUTING CREATION QUERIES
cur.execute("begin")
try:
    cur.execute(pat_table)
    cur.execute(doc_table)
    cur.execute(patappt_table)
    cur.execute(medrec_table)

# INSERTING VALUES INTO TABLE QUERIES
    cur.execute(doc_val1)
    cur.execute(doc_val2) # YOU CAN TEST THE TRANSACTION ATOMICITY PROPERTY BY GIVING A WRONG QUERY AND CHECKING IF TABLE EXISTS OR NOT
    cur.execute("commit")

except:
    cur.execute("rollback")

print("Opened Database successfully")

conn.close()