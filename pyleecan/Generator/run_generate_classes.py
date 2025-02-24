# -*- coding: utf-8 -*-
import sys
from os.path import dirname, abspath, normpath, join, realpath
from os import listdir, remove, system
import json
from datetime import datetime


begin = len(normpath(abspath(join(dirname(__file__), "../.."))))
end = len(normpath(abspath(join(dirname(__file__), ".."))))
MAIN_DIR = dirname(realpath(__file__))

package_name = MAIN_DIR[begin + 1 : end]

# Add the directory to the python path
sys.path.append(MAIN_DIR[:begin])

exec(
    "from "
    + package_name
    + ".Generator.ClassGenerator.class_generator import generate_class"
)
exec("from " + package_name + ".Generator.read_fct import read_all")
exec("from " + package_name + ".definitions import MAIN_DIR, DOC_DIR, INT_DIR")


# List of the main packages (to sort the classes)
PACKAGE_LIST = ["Geometry", "Machine", "Material", "Slot", "Import"]


def generate_code(root_path, gen_dict=None):
    """Generate pyleecan Classes code according to doc in root_path

    Parameters
    ----------
    root_path : str
        Path to the main folder of Pyleecan
    gen_dict : dict
        Generation dictionary (contains all the csv data)
    Returns
    -------
    None
    """
    CLASS_DIR = join(root_path, "Classes")
    FUNC_DIR = join(root_path, "Functions")
    DOC_DIR = join(root_path, "Generator", "ClassesRef")
    print("Reading classes csv in: " + DOC_DIR)
    print("Saving generated files in: " + CLASS_DIR)

    path = __file__[__file__.index(package_name) :]
    path = path.replace("\\", "/")

    # Deleting all the previous class
    print("Deleting old class files...")
    for file_name in listdir(CLASS_DIR):
        if file_name[0] != "_":
            remove(join(CLASS_DIR, file_name))

    # A file to import every classes quickly
    import_file = open(join(CLASS_DIR, "import_all.py"), "w")
    import_file.write("# -*- coding: utf-8 -*-\n\n")
    import_file.write('"""File generated by generate_code() - \n')
    import_file.write('WARNING! All changes made in this file will be lost!\n"""\n\n')

    # A file to select the constructor according to a string
    load_file = open(join(FUNC_DIR, "load_switch.py"), "w")
    load_file.write("# -*- coding: utf-8 -*-\n")
    load_file.write('"""File generated by generate_code() - \n')
    load_file.write('WARNING! All changes made in this file will be lost!\n"""\n\n')

    load_file.write("from ..Classes.import_all import *\n\n")
    load_file.write("load_switch = {\n")

    # Read all the csv files
    if gen_dict is None:
        gen_dict = read_all(DOC_DIR)

    # Generate all the class files (sorted to remove "commit noise")
    for class_name, _ in iter(sorted(list(gen_dict.items()))):
        import_file.write(
            "from ..Classes." + class_name + " import " + class_name + "\n"
        )
        load_file.write('    "' + class_name + '": ' + class_name + ",\n")
        print("Generation of " + class_name + " class")
        generate_class(gen_dict, class_name, CLASS_DIR)
    import_file.close()
    load_file.write("}\n")
    load_file.close()

    print("Generation of load_switch.py")
    print("Generation of import_all.py")

    # Save gen_dict
    class_dict_file = join(CLASS_DIR, "Class_Dict.json")
    with open(class_dict_file, "w") as json_file:
        json.dump(gen_dict, json_file, sort_keys=True, indent=4, separators=(",", ": "))


if __name__ == "__main__":
    gen_dict = read_all(DOC_DIR, is_internal=False, in_path=INT_DIR)
    generate_code(MAIN_DIR, gen_dict)
    # Run black
    try:
        import black

        system('"{}" -m black .'.format(sys.executable))
        if black.__version__.split(".")[0] != "20":
            print("\n############################################")
            print(
                "WARNING: The official version of black for pyleecan is 20, please update your black version"
            )
            print("############################################\n")
    except ImportError:
        print("/!\\ Please install and run black (version 20) /!\\")
    now = datetime.now()
    print("End at: ", now.strftime("%H:%M:%S"))
