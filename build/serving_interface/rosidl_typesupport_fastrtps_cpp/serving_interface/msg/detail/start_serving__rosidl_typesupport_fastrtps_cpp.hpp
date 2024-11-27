// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__rosidl_typesupport_fastrtps_cpp.hpp.em
// with input from serving_interface:msg/StartServing.idl
// generated code does not contain a copyright notice

#ifndef SERVING_INTERFACE__MSG__DETAIL__START_SERVING__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_
#define SERVING_INTERFACE__MSG__DETAIL__START_SERVING__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_

#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_interface/macros.h"
#include "serving_interface/msg/rosidl_typesupport_fastrtps_cpp__visibility_control.h"
#include "serving_interface/msg/detail/start_serving__struct.hpp"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

#include "fastcdr/Cdr.h"

namespace serving_interface
{

namespace msg
{

namespace typesupport_fastrtps_cpp
{

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_serving_interface
cdr_serialize(
  const serving_interface::msg::StartServing & ros_message,
  eprosima::fastcdr::Cdr & cdr);

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_serving_interface
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  serving_interface::msg::StartServing & ros_message);

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_serving_interface
get_serialized_size(
  const serving_interface::msg::StartServing & ros_message,
  size_t current_alignment);

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_serving_interface
max_serialized_size_StartServing(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment);

}  // namespace typesupport_fastrtps_cpp

}  // namespace msg

}  // namespace serving_interface

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_serving_interface
const rosidl_message_type_support_t *
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, serving_interface, msg, StartServing)();

#ifdef __cplusplus
}
#endif

#endif  // SERVING_INTERFACE__MSG__DETAIL__START_SERVING__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_
