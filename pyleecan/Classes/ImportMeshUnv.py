# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Import/ImportMeshUnv.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Import/ImportMeshUnv
"""

from os import linesep
from sys import getsizeof
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ..Functions.copy import copy
from ..Functions.load import load_init_dict
from ..Functions.Load.import_class import import_class
from .Import import Import

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Import.ImportMeshUnv.get_data import get_data
except ImportError as error:
    get_data = error


from ._check import InitUnKnowClassError


class ImportMeshUnv(Import):
    """Import mesh data from an unv file"""

    VERSION = 1

    # cf Methods.Import.ImportMeshUnv.get_data
    if isinstance(get_data, ImportError):
        get_data = property(
            fget=lambda x: raise_(
                ImportError("Can't use ImportMeshUnv method get_data: " + str(get_data))
            )
        )
    else:
        get_data = get_data
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(self, file_path="", init_dict=None, init_str=None):
        """Constructor of the class. Can be use in three ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for pyleecan type, -1 will call the default constructor
        - __init__ (init_dict = d) d must be a dictionary with property names as keys
        - __init__ (init_str = s) s must be a string
        s is the file path to load

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_str is not None:  # Load from a file
            init_dict = load_init_dict(init_str)[1]
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "file_path" in list(init_dict.keys()):
                file_path = init_dict["file_path"]
        # Set the properties (value check and convertion are done in setter)
        self.file_path = file_path
        # Call Import init
        super(ImportMeshUnv, self).__init__()
        # The class is frozen (in Import init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        ImportMeshUnv_str = ""
        # Get the properties inherited from Import
        ImportMeshUnv_str += super(ImportMeshUnv, self).__str__()
        ImportMeshUnv_str += 'file_path = "' + str(self.file_path) + '"' + linesep
        return ImportMeshUnv_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Import
        if not super(ImportMeshUnv, self).__eq__(other):
            return False
        if other.file_path != self.file_path:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from Import
        diff_list.extend(super(ImportMeshUnv, self).compare(other, name=name))
        if other._file_path != self._file_path:
            diff_list.append(name + ".file_path")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from Import
        S += super(ImportMeshUnv, self).__sizeof__()
        S += getsizeof(self.file_path)
        return S

    def as_dict(self, **kwargs):
        """
        Convert this object in a json serializable dict (can be use in __init__).
        Optional keyword input parameter is for internal use only
        and may prevent json serializability.
        """

        # Get the properties inherited from Import
        ImportMeshUnv_dict = super(ImportMeshUnv, self).as_dict(**kwargs)
        ImportMeshUnv_dict["file_path"] = self.file_path
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        ImportMeshUnv_dict["__class__"] = "ImportMeshUnv"
        return ImportMeshUnv_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.file_path = None
        # Set to None the properties inherited from Import
        super(ImportMeshUnv, self)._set_None()

    def _get_file_path(self):
        """getter of file_path"""
        return self._file_path

    def _set_file_path(self, value):
        """setter of file_path"""
        check_var("file_path", value, "str")
        self._file_path = value

    file_path = property(
        fget=_get_file_path,
        fset=_set_file_path,
        doc=u"""Path of the file to load

        :Type: str
        """,
    )
