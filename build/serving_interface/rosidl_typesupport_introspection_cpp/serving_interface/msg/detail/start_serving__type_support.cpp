// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from serving_interface:msg/StartServing.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "serving_interface/msg/detail/start_serving__struct.hpp"
#include "rosidl_typesupport_introspection_cpp/field_types.hpp"
#include "rosidl_typesupport_introspection_cpp/identifier.hpp"
#include "rosidl_typesupport_introspection_cpp/message_introspection.hpp"
#include "rosidl_typesupport_introspection_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_introspection_cpp/visibility_control.h"

namespace serving_interface
{

namespace msg
{

namespace rosidl_typesupport_introspection_cpp
{

void StartServing_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) serving_interface::msg::StartServing(_init);
}

void StartServing_fini_function(void * message_memory)
{
  auto typed_message = static_cast<serving_interface::msg::StartServing *>(message_memory);
  typed_message->~StartServing();
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember StartServing_message_member_array[1] = {
  {
    "is_started",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(serving_interface::msg::StartServing, is_started),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers StartServing_message_members = {
  "serving_interface::msg",  // message namespace
  "StartServing",  // message name
  1,  // number of fields
  sizeof(serving_interface::msg::StartServing),
  StartServing_message_member_array,  // message members
  StartServing_init_function,  // function to initialize message memory (memory has to be allocated)
  StartServing_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t StartServing_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &StartServing_message_members,
  get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace msg

}  // namespace serving_interface


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<serving_interface::msg::StartServing>()
{
  return &::serving_interface::msg::rosidl_typesupport_introspection_cpp::StartServing_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, serving_interface, msg, StartServing)() {
  return &::serving_interface::msg::rosidl_typesupport_introspection_cpp::StartServing_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif
