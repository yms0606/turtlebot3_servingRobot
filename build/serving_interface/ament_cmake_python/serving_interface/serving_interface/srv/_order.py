# generated from rosidl_generator_py/resource/_idl.py.em
# with input from serving_interface:srv/Order.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_Order_Request(type):
    """Metaclass of message 'Order_Request'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('serving_interface')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'serving_interface.srv.Order_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__order__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__order__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__order__request
            cls._TYPE_SUPPORT = module.type_support_msg__srv__order__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__order__request

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class Order_Request(metaclass=Metaclass_Order_Request):
    """Message class 'Order_Request'."""

    __slots__ = [
        '_table_num',
        '_menu',
        '_total_price',
    ]

    _fields_and_field_types = {
        'table_num': 'uint8',
        'menu': 'sequence<string>',
        'total_price': 'uint32',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.UnboundedString()),  # noqa: E501
        rosidl_parser.definition.BasicType('uint32'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.table_num = kwargs.get('table_num', int())
        self.menu = kwargs.get('menu', [])
        self.total_price = kwargs.get('total_price', int())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.table_num != other.table_num:
            return False
        if self.menu != other.menu:
            return False
        if self.total_price != other.total_price:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def table_num(self):
        """Message field 'table_num'."""
        return self._table_num

    @table_num.setter
    def table_num(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'table_num' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'table_num' field must be an unsigned integer in [0, 255]"
        self._table_num = value

    @builtins.property
    def menu(self):
        """Message field 'menu'."""
        return self._menu

    @menu.setter
    def menu(self, value):
        if __debug__:
            from collections.abc import Sequence
            from collections.abc import Set
            from collections import UserList
            from collections import UserString
            assert \
                ((isinstance(value, Sequence) or
                  isinstance(value, Set) or
                  isinstance(value, UserList)) and
                 not isinstance(value, str) and
                 not isinstance(value, UserString) and
                 all(isinstance(v, str) for v in value) and
                 True), \
                "The 'menu' field must be a set or sequence and each value of type 'str'"
        self._menu = value

    @builtins.property
    def total_price(self):
        """Message field 'total_price'."""
        return self._total_price

    @total_price.setter
    def total_price(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'total_price' field must be of type 'int'"
            assert value >= 0 and value < 4294967296, \
                "The 'total_price' field must be an unsigned integer in [0, 4294967295]"
        self._total_price = value


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_Order_Response(type):
    """Metaclass of message 'Order_Response'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('serving_interface')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'serving_interface.srv.Order_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__order__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__order__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__order__response
            cls._TYPE_SUPPORT = module.type_support_msg__srv__order__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__order__response

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class Order_Response(metaclass=Metaclass_Order_Response):
    """Message class 'Order_Response'."""

    __slots__ = [
        '_is_accept',
    ]

    _fields_and_field_types = {
        'is_accept': 'boolean',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.is_accept = kwargs.get('is_accept', bool())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.is_accept != other.is_accept:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def is_accept(self):
        """Message field 'is_accept'."""
        return self._is_accept

    @is_accept.setter
    def is_accept(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'is_accept' field must be of type 'bool'"
        self._is_accept = value


class Metaclass_Order(type):
    """Metaclass of service 'Order'."""

    _TYPE_SUPPORT = None

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('serving_interface')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'serving_interface.srv.Order')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__srv__order

            from serving_interface.srv import _order
            if _order.Metaclass_Order_Request._TYPE_SUPPORT is None:
                _order.Metaclass_Order_Request.__import_type_support__()
            if _order.Metaclass_Order_Response._TYPE_SUPPORT is None:
                _order.Metaclass_Order_Response.__import_type_support__()


class Order(metaclass=Metaclass_Order):
    from serving_interface.srv._order import Order_Request as Request
    from serving_interface.srv._order import Order_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')
