// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from serving_interface:srv/ServingStatus.idl
// generated code does not contain a copyright notice
#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#include <Python.h>
#include <stdbool.h>
#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-function"
#endif
#include "numpy/ndarrayobject.h"
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif
#include "rosidl_runtime_c/visibility_control.h"
#include "serving_interface/srv/detail/serving_status__struct.h"
#include "serving_interface/srv/detail/serving_status__functions.h"


ROSIDL_GENERATOR_C_EXPORT
bool serving_interface__srv__serving_status__request__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[60];
    {
      char * class_name = NULL;
      char * module_name = NULL;
      {
        PyObject * class_attr = PyObject_GetAttrString(_pymsg, "__class__");
        if (class_attr) {
          PyObject * name_attr = PyObject_GetAttrString(class_attr, "__name__");
          if (name_attr) {
            class_name = (char *)PyUnicode_1BYTE_DATA(name_attr);
            Py_DECREF(name_attr);
          }
          PyObject * module_attr = PyObject_GetAttrString(class_attr, "__module__");
          if (module_attr) {
            module_name = (char *)PyUnicode_1BYTE_DATA(module_attr);
            Py_DECREF(module_attr);
          }
          Py_DECREF(class_attr);
        }
      }
      if (!class_name || !module_name) {
        return false;
      }
      snprintf(full_classname_dest, sizeof(full_classname_dest), "%s.%s", module_name, class_name);
    }
    assert(strncmp("serving_interface.srv._serving_status.ServingStatus_Request", full_classname_dest, 59) == 0);
  }
  serving_interface__srv__ServingStatus_Request * ros_message = _ros_message;
  {  // is_arrived
    PyObject * field = PyObject_GetAttrString(_pymsg, "is_arrived");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->is_arrived = (Py_True == field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * serving_interface__srv__serving_status__request__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of ServingStatus_Request */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("serving_interface.srv._serving_status");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "ServingStatus_Request");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  serving_interface__srv__ServingStatus_Request * ros_message = (serving_interface__srv__ServingStatus_Request *)raw_ros_message;
  {  // is_arrived
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->is_arrived ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "is_arrived", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}

#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
// already included above
// #include <Python.h>
// already included above
// #include <stdbool.h>
// already included above
// #include "numpy/ndarrayobject.h"
// already included above
// #include "rosidl_runtime_c/visibility_control.h"
// already included above
// #include "serving_interface/srv/detail/serving_status__struct.h"
// already included above
// #include "serving_interface/srv/detail/serving_status__functions.h"


ROSIDL_GENERATOR_C_EXPORT
bool serving_interface__srv__serving_status__response__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[61];
    {
      char * class_name = NULL;
      char * module_name = NULL;
      {
        PyObject * class_attr = PyObject_GetAttrString(_pymsg, "__class__");
        if (class_attr) {
          PyObject * name_attr = PyObject_GetAttrString(class_attr, "__name__");
          if (name_attr) {
            class_name = (char *)PyUnicode_1BYTE_DATA(name_attr);
            Py_DECREF(name_attr);
          }
          PyObject * module_attr = PyObject_GetAttrString(class_attr, "__module__");
          if (module_attr) {
            module_name = (char *)PyUnicode_1BYTE_DATA(module_attr);
            Py_DECREF(module_attr);
          }
          Py_DECREF(class_attr);
        }
      }
      if (!class_name || !module_name) {
        return false;
      }
      snprintf(full_classname_dest, sizeof(full_classname_dest), "%s.%s", module_name, class_name);
    }
    assert(strncmp("serving_interface.srv._serving_status.ServingStatus_Response", full_classname_dest, 60) == 0);
  }
  serving_interface__srv__ServingStatus_Response * ros_message = _ros_message;
  {  // get_back
    PyObject * field = PyObject_GetAttrString(_pymsg, "get_back");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->get_back = (Py_True == field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * serving_interface__srv__serving_status__response__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of ServingStatus_Response */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("serving_interface.srv._serving_status");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "ServingStatus_Response");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  serving_interface__srv__ServingStatus_Response * ros_message = (serving_interface__srv__ServingStatus_Response *)raw_ros_message;
  {  // get_back
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->get_back ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "get_back", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
