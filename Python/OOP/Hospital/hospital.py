class Patient(object):

    def __init__(self, id, name, bed = None):
        self.id = id
        self.name = name
        self.bed = bed
    
class Hospital(object):

    def __init__(self, patients, name, capacity, beds = {}):

        self.patients = patients
        self.name = name
        self.capacity = capacity
        self.beds = beds
        for i in range(0, capacity):
            self.beds[i] = None

    def admit(self, patient):
        if len(self.patients) >= self.capacity:
            print "Hospital is at max capacity, sorry."
        else:
            for i in self.beds:
                if self.beds[i] == None:
                    patient.bed = i
                    self.patients.append(patient)
                    self.beds[i] = "occupied"
                    break
        return self
    
    def discharge(self, patient):
        for i in self.beds:
            if patient.bed == i:
                self.beds[i] = None
                patient.bed = None
                self.patients.remove(self.patients[i])
                break
        return self

    def display(self):
        print "Name:", self.name
        print "Capacity:", self.capacity
        for patient in self.patients:
            print "Patient:", patient.bed, patient.name
        print self.beds

patient0 = Patient(1, "john")

patient1 = Patient(2, "jim")

patient2 = Patient(3, "tim")
patient3 = Patient(4, "phil")
patient4 = Patient(5, "nick")
patient5 = Patient(6, "eric")
patient6 = Patient(7, "zack")
patient7 = Patient(8, "jane")
patient8 = Patient(9, "sarah")
patient9 = Patient(10, "tom")

hospital = Hospital([], "Sacred Heart", 10)
hospital.admit(patient0)
hospital.admit(patient1)
hospital.display()
hospital.discharge(patient0)
hospital.display()

hospital.admit(patient2)
hospital.admit(patient3)
hospital.admit(patient4)
hospital.admit(patient5)
hospital.admit(patient6)
hospital.admit(patient7)
hospital.admit(patient8)
hospital.admit(patient9)
hospital.display()
hospital.discharge(patient4)
hospital.display()
hospital.admit(patient8)
hospital.admit(patient9)
hospital.admit(patient8)
hospital.admit(patient9)