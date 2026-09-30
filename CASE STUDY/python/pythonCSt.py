# 1. Store the following machine information: Machine ID, Machine Name, Temperature, Rotational Speed, Torque, and Tool Wear.

import csv
import os

class ts:
    def __init__(self):
        self.machine_id = []
        self.machine_name = []
        self.temperature = []
        self.rotational_speed = []
        self.torque = []
        self.tool_wear = []
        self.power = []
    
# 2. Create a function to calculate machine power: Power = Torque × Rotational Speed.
    def machine_power(self, Torque, Rotational_Speed):
        power = Torque * Rotational_Speed
        return power

    def add_machine_info(self):

        Machine_ID = int(input("Enter the Machine ID: "))
        Machine_Name = input("Enter the Machine Name: ")
        Temperature = int(input("Enter the Temperature: "))
        Rotational_Speed = int(input("Enter the Rotational Speed: "))
        Torque = int(input("Enter the Torque: "))
        Tool_Wear = int(input("Enter the Tool Wear: "))

        # Store data in lists
        self.machine_id.append(Machine_ID)
        self.machine_name.append(Machine_Name)
        self.temperature.append(Temperature)
        self.rotational_speed.append(Rotational_Speed)
        self.torque.append(Torque)
        self.tool_wear.append(Tool_Wear)

        # Calculate power
        power = self.machine_power(Torque, Rotational_Speed)
        self.power.append(power)

    def machine_info(self):

        print("Machine ID:", self.machine_id)
        print("Machine Name:", self.machine_name)
        print("Temperature:", self.temperature)
        print("Rotational Speed:", self.rotational_speed)
        print("Torque:", self.torque)
        print("Tool Wear:", self.tool_wear)
        print("Power:", self.power)

    def create_csv(self):
        if not self.machine_id:
            print("no data in machine")
            return 
        headers = ["machine_id",
                    "machine_name",
                    "temperature",
                    "rotational_speed",
                    "torque",
                    "tool_wear"]

        with open("CASE STUDY/python/machine.csv",mode = "a",newline ="")as file:
            writer = csv.writer(file)
            # writer.writerow(headers)
            for i in range(len(self.machine_id)):
                writer.writerow([
                    self.machine_id[i],
                    self.machine_name[i],
                    self.temperature[i],
                    self.rotational_speed[i],
                    self.torque[i],
                    self.tool_wear[i],
                    self.power[i]
                ])
# 3. Create a function to check machine status:

# • Temperature > 80 and Tool Wear > 100 → Maintenance Required        

    def machine_status(self):
        if self.temperature >80 and self.tool_wear >100:
            print("Machine is in Maintenance")
            return
        else:
            print("Machine is not in Maintenance")

# • Temperature > 80 → High Temperature

    def high_temperature(self):
        if self.temperature > 80:
            print("High Temperature")
            return
        else:
            print("normal temperature")

# • Tool Wear > 100 → High Tool Wear • Otherwise → Normal

    def high_tool_wear(self):
        if self.tool_wear >100:
            print("High Tool Wear")
            return
        else:
            print("normal tool wear")


# machine = ts()

# machine.add_machine_info()
# # machine.machine_info()
# machine.create_csv()

"""
# 4. Create a class Machine with a constructor, machine attributes, a method to display machine information, a method to check machine status, and a method to calculate machine power.

class Machine(ts):
    def display(self,machine_id,machine_name,temperature,power):
        self.machine_id = machine_id
        self.machine_name = machine_name
        self.temperature = temperature
        self.power = power

m = Machine()
m.display(103,"asdasd",80,100)
"""
"""
# 5. Save the machine report into machine_report.txt.

class txt(ts):
    def create_txt(self):
        if not self.machine_id:
            print("no data in machine")
            return

        if not os.path.exists("CASE STUDY/python/machine_report.txt"):
            with open("CASE STUDY/python/machine_report.txt",mode = "a",newline ="")as file:
                writer = csv.writer(file)
                for i in range(len(self.machine_id)):
                    writer.writerow([
                        self.machine_id[i],
                        self.machine_name[i],
                        self.temperature[i],
                        self.rotational_speed[i],
                        self.torque[i],
                        self.tool_wear[i],
                        self.power[i]
                    ])

tx = txt()
tx.create_txt()
"""
# 6. Read and display the saved report.

with open("CASE STUDY/python/machine.csv",mode = "r",newline ="")as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

















