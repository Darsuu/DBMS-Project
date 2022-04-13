#stores all the routes the user can go to
from flask import Blueprint, flash, render_template, request

import sqlite3 as sql
import random

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template("home.html")

@views.route('/addPatient')
def addPatient():
    return render_template("addPatient.html")

@views.route('/patientTable')
def patientTable():
    conn = sql.connect("hospital.db")
    conn.row_factory = sql.Row
    cur = conn.cursor()
    cur.execute("""DROP VIEW IF EXISTS PATIENT_VIEW""")
    pat_view = """ CREATE VIEW PATIENT_VIEW AS SELECT * FROM PATIENT;"""
    cur.execute(pat_view)
    cur.execute("Select * from PATIENT_VIEW")
    rows = cur.fetchall()

    return render_template("patientTable.html", rows = rows)

@views.route('/doctorTable')
def doctorTable():
    conn = sql.connect("hospital.db")
    conn.row_factory = sql.Row
    cur = conn.cursor()
    cur.execute("begin")
    cur.execute("""DROP VIEW IF EXISTS DOCTOR_VIEW""")
    doc_view = """ CREATE VIEW DOCTOR_VIEW AS SELECT * FROM DOCTOR;"""
    cur.execute(doc_view)
    cur.execute("Select * from DOCTOR_VIEW")

    rows = cur.fetchall()
    return render_template("doctorTable.html", rows = rows)

@views.route('/views.addrec', methods = ['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        try:
            error = False
            name = request.form.get('Patient_Name')
            pno = request.form.get('Patient_PhoneNo')
            with sql.connect("hospital.db") as conn:
                cur = conn.cursor()
                cur.execute("Select * from DOCTOR;")
                records = cur.fetchall()
                found = False
                
                if(len(pno)!=10):
                    error = True
                    flash("Phone Number should be 10 digits long", category= "error")
                    conn.close()

                for row in records:
                    if(row[3]<5): # EACH DOCTOR CAN HAVE MAXIMUM OF 5 PATIENTS
                        found = True
                        cur.execute("begin")
                        try:
                            cur.execute("UPDATE DOCTOR SET PatNo = ? where ID = ?", (row[3]+1, row[1]))
                            cur.execute("INSERT INTO PATIENT(Name, PhoneNo) VALUES(?, ?)", (name, pno))
                            cur.execute("commit")
                        except Exception as e:
                            cur.execute("rollback")
                            error = True
                            flash(e)
                            break
                        cur.execute("SELECT * FROM PATIENT ORDER BY ID DESC LIMIT 1")
                        id = cur.fetchone()
                        rnd = random.randrange(0,6)
                        symptoms = ["Cough", "Fever", "Headache", "Runny Nose", "Rashes", "Cold", "Vomitting"]
                        cur.execute("INSERT INTO PATIENTAPPOINTMENTS(PatID, DocID, Symptoms) VALUES (?, ?, ?)", (id[1], row[1] , symptoms[rnd]))
                        flash("You have been assigned a Doctor", category = "success")
                        break

                if(found == False):
                    flash(" No Doctors available", category = "error")
                conn.commit()

        except:
            conn.rollback()

        finally:
            conn.close()
            if(error):
                return render_template("addPatient.html")
            return render_template("home.html")

@views.route('/appointmentTable')
def appointmentTable():
    conn = sql.connect("hospital.db")
    conn.row_factory = sql.Row
    cur = conn.cursor()
    cur.execute("""DROP VIEW IF EXISTS APPOINTMENT_VIEW""")
    pat_view = """ CREATE VIEW APPOINTMENT_VIEW AS SELECT * FROM PATIENTAPPOINTMENTS;"""
    cur.execute(pat_view)
    cur.execute("Select * from APPOINTMENT_VIEW")
    rows = cur.fetchall()

    return render_template("appointmentTable.html", rows = rows)

def getRandom():
    return