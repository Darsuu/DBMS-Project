# Hospital Management System

## System Requirement Specification

1. *Purpose of this document* : The purpose of this document is to describe the problem statement and the solution that we have come up with. We have to create a hospital management system to manage the day-to-day operations of a hospital like registration of patients, booking appointments, managing doctor schedules etc.

2. *Scope of this document* : The main objective of this system is to provide appointment booking services to patients of a hospital, keeping in mind doctor schedules. An added functionality is providing every patient with not only their medical history, but also the diagnosis and associated medication prescribed by the doctor.

3. *Overview* : The problem statement presented to us is that hospitals interact with a lot of people in a day and there are various activities involved in day to day operations of hospitals, for example booking of appointments, managing doctor schedules, managing patient diagnoses, managing medical histories of patients, reports etc. Therefore, it is imperative to have a highly efficient DBMS to manage patient and doctor data. The DBMS has various constraints, for example, a doctor can only have 5 appointments a day. We have also created a front-end which will make it easier for patients to register themselves and apply for appointments. The DBMS will be programmed using MySQL, the backend using Flask and the frontend using HTML, CSS and Bootstrap.

## General Description 

### Objective of User
- To manage the day to day operations of hospitals
- Booking appointments
- Accessing Medical History
- Viewing diagnosis and prescribed medication

### System Requirements
- SQLite
- HTML
- CSS
- Flask(Python)
- Bootstrap

### Functional Requirements
1.	The system allows patients to view available slots in doctor schedules.
2.	It allows patients to book appointments and reschedule them, if necessary, and provide vital information like symptoms experienced.
3.	It should assign a doctor who is available and also prevents appointments from clashing.
4.	Doctors should be able access and update patients’ medical records.
5.	Doctors should be able to provide diagnosis and prescribe the associated medication.

### Data Requirements
For the proper functioning of the system, we require 4 tables namely - Patient, Doctor, PatientAppointments, AccessMedicalRecord.
Data must be inputted according to the constraints which have been programmed into the description of the tables.
All the tables have been normalized to 3NF.

## Entity-Relationship Diagram

![ER diagram](https://user-images.githubusercontent.com/81075125/178330462-e4c1911d-0f97-4b88-b8c1-f345554a7825.JPG)

## Relational Schema Design - Normalized

![ER Normalised](https://user-images.githubusercontent.com/81075125/178330806-5c226773-dade-44be-aa9b-2b5bfbad35a7.JPG)


## Data Normalization

1NF : All Attributes are Atomic.
2NF : No Partial Dependency.
3NF : Absence of any Transitive Dependency.
1.	Patient :
R = (PatId, PatName, PatPhone)
FDs:
PatID → PatName
PatID →  PatPhone

2.	Doctor :
R = (DocID, DocName,DocDept,AppNo)
FDs:
DocID → DocName
DocID →  DocDept
DocID → AppNo
 
2.	AccessMedicalRecord:
R = (PatId,Date&Time,DocID, Ailments, Medication, Diagnosis,)
FDs:
(PatId,Date&Time)→  Ailments
(PatId,Date&Time)→Medication
(PatId,Date&Time)→  Diagnosis

(PatID,Date&Time) serve as a composite primary key. The same patient can come more than once in a day hence we must also use Date & Time as a part of the PK
 
4.	PatientsAttendAppointments:
R = (PatId,DocID, Symptoms)
FDs:
(PatId,DocID) →  Symptoms

### List of Tables
1. Doctor
2. Patient
3. PatientAppointments
4. AccessMedicalRecord

### Additional Components
We have enforced a number of constraints and properties to ensure proper functioning of the system, for example, atomicity has been ensured by use of rollbacks and commits.

## Group Members & Contribution
Darshan Abhaykumar - 2020A7PS1214P

Nidhish Parekh - 2020A7PS0986P

