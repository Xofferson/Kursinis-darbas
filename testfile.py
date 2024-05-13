import unittest
from coursework import Doctor, Nurse, HospitalManager, Hospital
class Test_Hospital(unittest.TestCase):
    def setUp(self):
        self.hospital = Hospital("Test Hospital")

    def test_add_doctor(self):
        new_doctor = "Dr. Kazys"
        self.hospital.manager.add_doctor(new_doctor)
        self.assertIn(new_doctor, self.hospital.manager.doctors)

    def test_remove_doctor(self):
        doctor_to_remove = "Dr. Kazys"
        self.hospital.manager.doctors.append(doctor_to_remove)
        self.hospital.manager.save_to_file
        self.hospital.manager.doctors.remove(doctor_to_remove)
        self.hospital.manager.save_to_file()
        self.assertNotIn(doctor_to_remove, self.hospital.manager.doctors)

    def test_add_nurse(self):
        new_nurse = "Nurse Evelina"
        self.hospital.manager.add_nurse(new_nurse)
        self.assertIn(new_nurse, self.hospital.manager.nurses)

    def test_remove_nurse(self):
        nurse_to_remove = "Nurse Evelina"
        self.hospital.manager.nurses.append(nurse_to_remove)
        self.hospital.manager.save_to_file()  
        self.hospital.manager.nurses.remove(nurse_to_remove)
        self.hospital.manager.save_to_file()
        self.assertNotIn(nurse_to_remove, self.hospital.manager.nurses)

    def test_add_patient(self):
        new_patient = {'name': 'Paulius', 'sex': 'Male', 'age': 28, 'disease': 'Bronchitis'}
        self.hospital.manager.add_patient(new_patient)
        self.assertIn(new_patient, self.hospital.manager.patients)

    def test_remove_patient(self):
        patient_to_remove = {'name': 'Paulius', 'sex': 'Male', 'age': 28, 'disease': 'Bronchitis'}
        self.hospital.manager.patients.append(patient_to_remove)
        self.hospital.manager.remove_patient(patient_to_remove['name'])
        self.assertNotIn(patient_to_remove, self.hospital.manager.patients)

if __name__ == "__main__":
    unittest.main()

