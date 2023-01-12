from project.hardware.hardware import Hardware
from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def __check_if_hardware_exist(hardware_name):
        for hardware in System._hardware:
            if hardware.name == hardware_name:
                return hardware

    @staticmethod
    def __check_if_software_exist(software_name):
        for software in System._software:
            if software.name == software_name:
                return software

    @staticmethod
    def register_power_hardware(name, capacity, memory):
        new_power_hardware = PowerHardware(name, capacity, memory)
        System._hardware.append(new_power_hardware)

    @staticmethod
    def register_heavy_hardware(name, capacity, memory):
        new_heavy_hardware = HeavyHardware(name, capacity, memory)
        System._hardware.append(new_heavy_hardware)

    @staticmethod
    def register_express_software(hardware_name, name, capacity_consumption, memory_consumption):
        hardware = System.__check_if_hardware_exist(hardware_name)

        if not hardware:
            return "Hardware does not exist"

        new_express_software = ExpressSoftware(name, capacity_consumption, memory_consumption)
        hardware.install(new_express_software)

        System._software.append(new_express_software)

    @staticmethod
    def register_light_software(hardware_name, name, capacity_consumption, memory_consumption):
        hardware = System.__check_if_hardware_exist(hardware_name)

        if not hardware:
            return "Hardware does not exist"

        new_light_software = LightSoftware(name, capacity_consumption, memory_consumption)
        hardware.install(new_light_software)

        System._software.append(new_light_software)

    @staticmethod
    def release_software_component(hardware_name, software_name):
        software = System.__check_if_software_exist(software_name)
        hardware = System.__check_if_hardware_exist(hardware_name)

        if software and hardware:
            hardware.uninstall(software)
            System._software.remove(software)
        else:
            return "Some of the components do not exist"

    @staticmethod
    def analyze():
        total_software_memory_consumed = sum([x.memory_consumption for x in System._software])
        total_software_capacity_consumed = sum([x.capacity_consumption for x in System._software])
        total_hardware_memory = sum([x.memory for x in System._hardware])
        total_hardware_capacity = sum([x.capacity for x in System._hardware])

        result = f"System Analysis\n" \
                 f"Hardware Components: {len(System._hardware)}\n" \
                 f"Software Components: {len(System._software)}\n" \
                 f"Total Operational Memory: {total_software_memory_consumed} / {total_hardware_memory}\n" \
                 f"Total Capacity Taken: {total_software_capacity_consumed} / {total_hardware_capacity}"
        return result

    @staticmethod
    def system_split():

        return '\n'.join(repr(x) for x in System._hardware)