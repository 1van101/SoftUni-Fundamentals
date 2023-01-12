from project.software.software import Software


class Hardware:
    def __init__(self, name, hardware_type, capacity, memory):
        self.name = name
        self.hardware_type = hardware_type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []

    def install(self, software: Software):
        if all([self.capacity >= software.capacity_consumption, self.memory >= software.memory_consumption]):
            self.software_components.append(software)
        else:
            raise Exception("Software cannot be installed")

    def uninstall(self, software: Software):
        self.software_components.remove(software)

    def __repr__(self):
        total_memory_of_software_components = sum(x.memory_consumption for x in self.software_components)
        total_capacity_of_software_components = sum(x.capacity_consumption for x in self.software_components)

        names_of_software_components = "None" if not self.software_components else ', '.join(
            x.name for x in self.software_components)
        return f"Hardware Component - {self.name}\n" \
               f"Express Software Components: {len([x for x in self.software_components if x.software_type == 'Express'])}\n" \
               f"Light Software Components: {len([x for x in self.software_components if x.software_type == 'Light'])}\n" \
               f"Memory Usage: {total_memory_of_software_components} / {self.memory}\n" \
               f"Capacity Usage: {total_capacity_of_software_components} / {self.capacity}\n" \
               f"Type: {self.hardware_type}\n" \
               f"Software Components: {names_of_software_components}"
