from abc import ABC, abstractmethod

#Dekoratoriaus funkcija, skirta pridėti elgseną prieš ir po medicinos personalo veiksmų
def decorator(action):
    def wrapper(self, patient):
        print(f"{self.__class__.__name__} {self.name} is attending to {patient['name']}.")
        action(self, patient)
        print(f"{self.__class__.__name__} {self.name} is providing care to {patient['name']}.")
        return wrapper

#Abstrakti bazinė klasė medicinos personalui
class MedicalStaff(ABC):
    @abstractmethod
    def action(self, patient):
        pass

#Gydytojo klasė paveldima iš MedicalStaff
class Doctor(MedicalStaff):
    def __init__(self, name):
        self.name = name

    @decorator
    def action(self, patient):
        print(f"{self.__class__.__name__} {self.name} is examining {patient['name']}.")

#Slaugytojo klasė paveldima iš MedicalStaff
class Nurse(MedicalStaff):
    def __init__(self, name):
        self.name = name

    @decorator
    def action(self, patient):
        print(f"{self.__class__.__name__} {self.name} is attending to {patient['name']}.")

#Abstrakti bazinė klasė medicinos personalo dekoratoriams
class MedicalStaffDecorator(MedicalStaff, ABC):
    def __init__(self, medical_staff):
        self.medical_staff = medical_staff

    @abstractmethod
    def action(self, patient):
        pass

#HospitalManager klasė, atsakinga už gydytojų, slaugytojų ir pacientų valdymą
class HospitalManager:
    _instance = None #Singleton egzempliorius

#Singleton modelis: užtikrina, kad būtų sukurtas tik vienas egzempliorius
    def __new__(cls, filename='hospital_patients.txt'):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.filename = filename
            cls._instance.patients = []
            cls._instance.doctors = []
            cls._instance.nurses = []
            cls._instance.load_from_file()
        return cls._instance

#Duomenų įrašymo į failą metodas
    def save_to_file(self):
        try:
            with open(self.filename, 'w') as file:
                #Gydytojų, slaugytojų ir pacientų duomenų įrašymas į failą
                for staff in self.doctors:
                    file.write(f"Doctor,{staff}\n")
                for staff in self.nurses:
                    file.write(f"Nurse,{staff}\n")
                for patient in self.patients:
                    file.write(f"Patient,{patient['name']},{patient['sex']},{patient['age']},{patient['disease']}\n")
            print("Data saved successfully.")
        except Exception as e:
            print(f"Error occurred while saving data: {e}")

#Metodas įkelti duomenis iš failo
    def load_from_file(self):
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    data = line.strip().split(',')
                    if data[0] == 'Doctor':
                        self.doctors.append(data[1])
                    elif data[0] == 'Nurse':
                        self.nurses.append(data[1])
                    elif data[0] == 'Patient':
                        name, sex, age, disease = data[1:]
                        try:
                            age = int(age)
                        except ValueError:
                            continue
                        self.patients.append({'name': name, 'sex': sex, 'age': age, 'disease': disease})
        except FileNotFoundError:
            print(f"File {self.filename} not found.")
        except Exception as e:
            print(f"Error occurred while loading data: {e}")

#Metodas pridėti gydytoją
    def add_doctor(self, doctor):
        if isinstance(doctor, str) and doctor not in self.doctors:  #Patikrinimas, ar gydytojas nėra jau sąraše
            self.doctors.append(doctor)
            self.save_to_file()
            print(f"Doctor {doctor} added.")
        else:
            print("Invalid doctor or already exists.")

#Metodas pridėti slaugytoją
    def add_nurse(self, nurse):
        if isinstance(nurse, str) and nurse not in self.nurses:  # Patikriname, ar slaugytoja nėra jau sąraše
            self.nurses.append(nurse)
            self.save_to_file()
            print(f"Nurse {nurse} added.")
        else:
            print("Invalid nurse or already exists.")

#Metodas įtraukti pacientą
    def add_patient(self, patient):
        if isinstance(patient, dict) and 'name' in patient and 'sex' in patient and 'age' in patient and 'disease' in patient:
            self.patients.append(patient)
            self.save_to_file()
            print(f"Patient {patient['name']} added.")
        else:
            print("Invalid patient format.")

#Gydytojo pašalinimui skirtas metodas
    def remove_doctor(self, doctor_name):
        if doctor_name in self.doctors:
            self.doctors.remove(doctor_name)
            self.save_to_file()
            print(f"Doctor {doctor_name} removed.")
        else:
            print(f"Doctor {doctor_name} not found.")

#Slaugytojos pašalinimui skirtas metodas
    def remove_nurse(self, nurse_name):
        if nurse_name in self.nurses:
            self.nurses.remove(nurse_name)
            self.save_to_file()
            print(f"Nurse {nurse_name} removed.")
        else:
            print(f"Nurse {nurse_name} not found.")

#Paciento pašalinimui skirtas metodas
    def remove_patient(self, patient_name):
        for patient in self.patients:
            if patient['name'] == patient_name:
                self.patients.remove(patient)
                self.save_to_file()
                print(f"Patient {patient_name} removed.")
                break
        else:
            print(f"Patient {patient_name} not found.")

#Ligoninės klasė, atstovaujanti ligoninei
class Hospital:
    def __init__(self, name):
        self.name = name
        self.manager = HospitalManager()

#Duomenų įkėlimo iš failo metodas
    def load_from_file(self):
        self.manager.load_from_file()

#Paciento duomenų spausdinimo metodas
    def print_patients(self):
        for patient in self.manager.patients:
            print(f"Patient - {patient['name']}, {patient['sex']}, {patient['age']}, {patient['disease']} ")

#Medicinos personalo informacijos spausdinimo metodas
    def print_medical_staff(self):
        print("Doctors:")
        for doctor in self.manager.doctors:
            print(doctor)
        print("\nNurses:")
        for nurse in self.manager.nurses:
            print(nurse)

if __name__ == "__main__":
    hospital = Hospital("Test Hospital")
    hospital.load_from_file()

    while True:
        print("\nOptions:")
        print("1. Add Doctor")
        print("2. Remove Doctor")
        print("3. Add Nurse")
        print("4. Remove Nurse")
        print("5. Add Patient")
        print("6. Remove Patient")
        print("7. Print Medical Staff")
        print("8. Print Patients")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter doctor's name: ")
            hospital.manager.add_doctor(name)

        elif choice == '2':
            name = input("Enter doctor's name to remove: ")
            hospital.manager.remove_doctor(name)

        elif choice == '3':
            name = input("Enter nurse's name: ")
            hospital.manager.add_nurse(name)

        elif choice == '4':
            name = input("Enter nurse's name to remove: ")
            hospital.manager.remove_nurse(name)

        elif choice == '5':
            name = input("Enter patient's name: ")
            sex = input("Enter patient's sex: ")
            age = int(input("Enter patient's age: "))
            disease = input("Enter patient's disease: ")
            new_patient = {'name': name, 'sex': sex, 'age': age, 'disease': disease}
            hospital.manager.add_patient(new_patient)

        elif choice == '6':
            name = input("Enter patient's name to remove: ")
            hospital.manager.remove_patient(name)

        elif choice == '7':
            hospital.print_medical_staff()

        elif choice == '8':
            hospital.print_patients()

        elif choice == '9':
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please try again.")
