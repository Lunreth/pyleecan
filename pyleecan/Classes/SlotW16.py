# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Slot/SlotW16.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Slot/SlotW16
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
from .Slot import Slot

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Slot.SlotW16._comp_point_coordinate import _comp_point_coordinate
except ImportError as error:
    _comp_point_coordinate = error

try:
    from ..Methods.Slot.SlotW16.build_geometry import build_geometry
except ImportError as error:
    build_geometry = error

try:
    from ..Methods.Slot.SlotW16.get_surface_active import get_surface_active
except ImportError as error:
    get_surface_active = error

try:
    from ..Methods.Slot.SlotW16.check import check
except ImportError as error:
    check = error

try:
    from ..Methods.Slot.SlotW16.comp_angle_opening import comp_angle_opening
except ImportError as error:
    comp_angle_opening = error

try:
    from ..Methods.Slot.SlotW16.comp_height import comp_height
except ImportError as error:
    comp_height = error

try:
    from ..Methods.Slot.SlotW16.comp_height_active import comp_height_active
except ImportError as error:
    comp_height_active = error

try:
    from ..Methods.Slot.SlotW16.comp_surface import comp_surface
except ImportError as error:
    comp_surface = error

try:
    from ..Methods.Slot.SlotW16.plot_schematics import plot_schematics
except ImportError as error:
    plot_schematics = error


from ._check import InitUnKnowClassError


class SlotW16(Slot):

    VERSION = 1
    IS_SYMMETRICAL = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Slot.SlotW16._comp_point_coordinate
    if isinstance(_comp_point_coordinate, ImportError):
        _comp_point_coordinate = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotW16 method _comp_point_coordinate: "
                    + str(_comp_point_coordinate)
                )
            )
        )
    else:
        _comp_point_coordinate = _comp_point_coordinate
    # cf Methods.Slot.SlotW16.build_geometry
    if isinstance(build_geometry, ImportError):
        build_geometry = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotW16 method build_geometry: " + str(build_geometry)
                )
            )
        )
    else:
        build_geometry = build_geometry
    # cf Methods.Slot.SlotW16.get_surface_active
    if isinstance(get_surface_active, ImportError):
        get_surface_active = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotW16 method get_surface_active: "
                    + str(get_surface_active)
                )
            )
        )
    else:
        get_surface_active = get_surface_active
    # cf Methods.Slot.SlotW16.check
    if isinstance(check, ImportError):
        check = property(
            fget=lambda x: raise_(
                ImportError("Can't use SlotW16 method check: " + str(check))
            )
        )
    else:
        check = check
    # cf Methods.Slot.SlotW16.comp_angle_opening
    if isinstance(comp_angle_opening, ImportError):
        comp_angle_opening = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotW16 method comp_angle_opening: "
                    + str(comp_angle_opening)
                )
            )
        )
    else:
        comp_angle_opening = comp_angle_opening
    # cf Methods.Slot.SlotW16.comp_height
    if isinstance(comp_height, ImportError):
        comp_height = property(
            fget=lambda x: raise_(
                ImportError("Can't use SlotW16 method comp_height: " + str(comp_height))
            )
        )
    else:
        comp_height = comp_height
    # cf Methods.Slot.SlotW16.comp_height_active
    if isinstance(comp_height_active, ImportError):
        comp_height_active = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotW16 method comp_height_active: "
                    + str(comp_height_active)
                )
            )
        )
    else:
        comp_height_active = comp_height_active
    # cf Methods.Slot.SlotW16.comp_surface
    if isinstance(comp_surface, ImportError):
        comp_surface = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotW16 method comp_surface: " + str(comp_surface)
                )
            )
        )
    else:
        comp_surface = comp_surface
    # cf Methods.Slot.SlotW16.plot_schematics
    if isinstance(plot_schematics, ImportError):
        plot_schematics = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotW16 method plot_schematics: " + str(plot_schematics)
                )
            )
        )
    else:
        plot_schematics = plot_schematics
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        W0=0.0122,
        W3=0.0122,
        H0=0.001,
        H2=0.0122,
        R1=0.001,
        Zs=36,
        init_dict=None,
        init_str=None,
    ):
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
            if "W0" in list(init_dict.keys()):
                W0 = init_dict["W0"]
            if "W3" in list(init_dict.keys()):
                W3 = init_dict["W3"]
            if "H0" in list(init_dict.keys()):
                H0 = init_dict["H0"]
            if "H2" in list(init_dict.keys()):
                H2 = init_dict["H2"]
            if "R1" in list(init_dict.keys()):
                R1 = init_dict["R1"]
            if "Zs" in list(init_dict.keys()):
                Zs = init_dict["Zs"]
        # Set the properties (value check and convertion are done in setter)
        self.W0 = W0
        self.W3 = W3
        self.H0 = H0
        self.H2 = H2
        self.R1 = R1
        # Call Slot init
        super(SlotW16, self).__init__(Zs=Zs)
        # The class is frozen (in Slot init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        SlotW16_str = ""
        # Get the properties inherited from Slot
        SlotW16_str += super(SlotW16, self).__str__()
        SlotW16_str += "W0 = " + str(self.W0) + linesep
        SlotW16_str += "W3 = " + str(self.W3) + linesep
        SlotW16_str += "H0 = " + str(self.H0) + linesep
        SlotW16_str += "H2 = " + str(self.H2) + linesep
        SlotW16_str += "R1 = " + str(self.R1) + linesep
        return SlotW16_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Slot
        if not super(SlotW16, self).__eq__(other):
            return False
        if other.W0 != self.W0:
            return False
        if other.W3 != self.W3:
            return False
        if other.H0 != self.H0:
            return False
        if other.H2 != self.H2:
            return False
        if other.R1 != self.R1:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from Slot
        diff_list.extend(super(SlotW16, self).compare(other, name=name))
        if other._W0 != self._W0:
            diff_list.append(name + ".W0")
        if other._W3 != self._W3:
            diff_list.append(name + ".W3")
        if other._H0 != self._H0:
            diff_list.append(name + ".H0")
        if other._H2 != self._H2:
            diff_list.append(name + ".H2")
        if other._R1 != self._R1:
            diff_list.append(name + ".R1")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from Slot
        S += super(SlotW16, self).__sizeof__()
        S += getsizeof(self.W0)
        S += getsizeof(self.W3)
        S += getsizeof(self.H0)
        S += getsizeof(self.H2)
        S += getsizeof(self.R1)
        return S

    def as_dict(self, **kwargs):
        """
        Convert this object in a json serializable dict (can be use in __init__).
        Optional keyword input parameter is for internal use only
        and may prevent json serializability.
        """

        # Get the properties inherited from Slot
        SlotW16_dict = super(SlotW16, self).as_dict(**kwargs)
        SlotW16_dict["W0"] = self.W0
        SlotW16_dict["W3"] = self.W3
        SlotW16_dict["H0"] = self.H0
        SlotW16_dict["H2"] = self.H2
        SlotW16_dict["R1"] = self.R1
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        SlotW16_dict["__class__"] = "SlotW16"
        return SlotW16_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.W0 = None
        self.W3 = None
        self.H0 = None
        self.H2 = None
        self.R1 = None
        # Set to None the properties inherited from Slot
        super(SlotW16, self)._set_None()

    def _get_W0(self):
        """getter of W0"""
        return self._W0

    def _set_W0(self, value):
        """setter of W0"""
        check_var("W0", value, "float", Vmin=0)
        self._W0 = value

    W0 = property(
        fget=_get_W0,
        fset=_set_W0,
        doc=u"""Slot isthmus angular width.

        :Type: float
        :min: 0
        """,
    )

    def _get_W3(self):
        """getter of W3"""
        return self._W3

    def _set_W3(self, value):
        """setter of W3"""
        check_var("W3", value, "float", Vmin=0)
        self._W3 = value

    W3 = property(
        fget=_get_W3,
        fset=_set_W3,
        doc=u"""Tooth width

        :Type: float
        :min: 0
        """,
    )

    def _get_H0(self):
        """getter of H0"""
        return self._H0

    def _set_H0(self, value):
        """setter of H0"""
        check_var("H0", value, "float", Vmin=0)
        self._H0 = value

    H0 = property(
        fget=_get_H0,
        fset=_set_H0,
        doc=u"""Slot isthmus height.

        :Type: float
        :min: 0
        """,
    )

    def _get_H2(self):
        """getter of H2"""
        return self._H2

    def _set_H2(self, value):
        """setter of H2"""
        check_var("H2", value, "float", Vmin=0)
        self._H2 = value

    H2 = property(
        fget=_get_H2,
        fset=_set_H2,
        doc=u"""Slot height

        :Type: float
        :min: 0
        """,
    )

    def _get_R1(self):
        """getter of R1"""
        return self._R1

    def _set_R1(self, value):
        """setter of R1"""
        check_var("R1", value, "float", Vmin=0)
        self._R1 = value

    R1 = property(
        fget=_get_R1,
        fset=_set_R1,
        doc=u"""Top radius

        :Type: float
        :min: 0
        """,
    )
