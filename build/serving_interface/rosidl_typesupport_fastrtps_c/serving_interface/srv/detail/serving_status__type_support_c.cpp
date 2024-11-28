// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from serving_interface:srv/ServingStatus.idl
// generated code does not contain a copyright notice
#include "serving_interface/srv/detail/serving_status__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "serving_interface/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "serving_interface/srv/detail/serving_status__struct.h"
#include "serving_interface/srv/detail/serving_status__functions.h"
#include "fastcdr/Cdr.h"

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

// includes and forward declarations of message dependencies and their conversion functions

#if defined(__cplusplus)
extern "C"
{
#endif


// forward declare type support functions


using _ServingStatus_Request__ros_msg_type = serving_interface__srv__ServingStatus_Request;

static bool _ServingStatus_Request__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _ServingStatus_Request__ros_msg_type * ros_message = static_cast<const _ServingStatus_Request__ros_msg_type *>(untyped_ros_message);
  // Field name: is_arrived
  {
    cdr << (ros_message->is_arrived ? true : false);
  }

  return true;
}

static bool _ServingStatus_Request__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _ServingStatus_Request__ros_msg_type * ros_message = static_cast<_ServingStatus_Request__ros_msg_type *>(untyped_ros_message);
  // Field name: is_arrived
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message->is_arrived = tmp ? true : false;
  }

  return true;
}  // NOLINT(readability/fn_size)

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_serving_interface
size_t get_serialized_size_serving_interface__srv__ServingStatus_Request(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _ServingStatus_Request__ros_msg_type * ros_message = static_cast<const _ServingStatus_Request__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name is_arrived
  {
    size_t item_size = sizeof(ros_message->is_arrived);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

static uint32_t _ServingStatus_Request__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_serving_interface__srv__ServingStatus_Request(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_serving_interface
size_t max_serialized_size_serving_interface__srv__ServingStatus_Request(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  size_t last_member_size = 0;
  (void)last_member_size;
  (void)padding;
  (void)wchar_size;

  full_bounded = true;
  is_plain = true;

  // member: is_arrived
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }

  size_t ret_val = current_alignment - initial_alignment;
  if (is_plain) {
    // All members are plain, and type is not empty.
    // We still need to check that the in-memory alignment
    // is the same as the CDR mandated alignment.
    using DataType = serving_interface__srv__ServingStatus_Request;
    is_plain =
      (
      offsetof(DataType, is_arrived) +
      last_member_size
      ) == ret_val;
  }

  return ret_val;
}

static size_t _ServingStatus_Request__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_serving_interface__srv__ServingStatus_Request(
    full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}


static message_type_support_callbacks_t __callbacks_ServingStatus_Request = {
  "serving_interface::srv",
  "ServingStatus_Request",
  _ServingStatus_Request__cdr_serialize,
  _ServingStatus_Request__cdr_deserialize,
  _ServingStatus_Request__get_serialized_size,
  _ServingStatus_Request__max_serialized_size
};

static rosidl_message_type_support_t _ServingStatus_Request__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_ServingStatus_Request,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, serving_interface, srv, ServingStatus_Request)() {
  return &_ServingStatus_Request__type_support;
}

#if defined(__cplusplus)
}
#endif

// already included above
// #include <cassert>
// already included above
// #include <limits>
// already included above
// #include <string>
// already included above
// #include "rosidl_typesupport_fastrtps_c/identifier.h"
// already included above
// #include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
// already included above
// #include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
// already included above
// #include "serving_interface/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
// already included above
// #include "serving_interface/srv/detail/serving_status__struct.h"
// already included above
// #include "serving_interface/srv/detail/serving_status__functions.h"
// already included above
// #include "fastcdr/Cdr.h"

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

// includes and forward declarations of message dependencies and their conversion functions

#if defined(__cplusplus)
extern "C"
{
#endif


// forward declare type support functions


using _ServingStatus_Response__ros_msg_type = serving_interface__srv__ServingStatus_Response;

static bool _ServingStatus_Response__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _ServingStatus_Response__ros_msg_type * ros_message = static_cast<const _ServingStatus_Response__ros_msg_type *>(untyped_ros_message);
  // Field name: get_back
  {
    cdr << (ros_message->get_back ? true : false);
  }

  return true;
}

static bool _ServingStatus_Response__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _ServingStatus_Response__ros_msg_type * ros_message = static_cast<_ServingStatus_Response__ros_msg_type *>(untyped_ros_message);
  // Field name: get_back
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message->get_back = tmp ? true : false;
  }

  return true;
}  // NOLINT(readability/fn_size)

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_serving_interface
size_t get_serialized_size_serving_interface__srv__ServingStatus_Response(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _ServingStatus_Response__ros_msg_type * ros_message = static_cast<const _ServingStatus_Response__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name get_back
  {
    size_t item_size = sizeof(ros_message->get_back);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

static uint32_t _ServingStatus_Response__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_serving_interface__srv__ServingStatus_Response(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_serving_interface
size_t max_serialized_size_serving_interface__srv__ServingStatus_Response(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  size_t last_member_size = 0;
  (void)last_member_size;
  (void)padding;
  (void)wchar_size;

  full_bounded = true;
  is_plain = true;

  // member: get_back
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }

  size_t ret_val = current_alignment - initial_alignment;
  if (is_plain) {
    // All members are plain, and type is not empty.
    // We still need to check that the in-memory alignment
    // is the same as the CDR mandated alignment.
    using DataType = serving_interface__srv__ServingStatus_Response;
    is_plain =
      (
      offsetof(DataType, get_back) +
      last_member_size
      ) == ret_val;
  }

  return ret_val;
}

static size_t _ServingStatus_Response__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_serving_interface__srv__ServingStatus_Response(
    full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}


static message_type_support_callbacks_t __callbacks_ServingStatus_Response = {
  "serving_interface::srv",
  "ServingStatus_Response",
  _ServingStatus_Response__cdr_serialize,
  _ServingStatus_Response__cdr_deserialize,
  _ServingStatus_Response__get_serialized_size,
  _ServingStatus_Response__max_serialized_size
};

static rosidl_message_type_support_t _ServingStatus_Response__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_ServingStatus_Response,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, serving_interface, srv, ServingStatus_Response)() {
  return &_ServingStatus_Response__type_support;
}

#if defined(__cplusplus)
}
#endif

#include "rosidl_typesupport_fastrtps_cpp/service_type_support.h"
#include "rosidl_typesupport_cpp/service_type_support.hpp"
// already included above
// #include "rosidl_typesupport_fastrtps_c/identifier.h"
// already included above
// #include "serving_interface/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "serving_interface/srv/serving_status.h"

#if defined(__cplusplus)
extern "C"
{
#endif

static service_type_support_callbacks_t ServingStatus__callbacks = {
  "serving_interface::srv",
  "ServingStatus",
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, serving_interface, srv, ServingStatus_Request)(),
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, serving_interface, srv, ServingStatus_Response)(),
};

static rosidl_service_type_support_t ServingStatus__handle = {
  rosidl_typesupport_fastrtps_c__identifier,
  &ServingStatus__callbacks,
  get_service_typesupport_handle_function,
};

const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, serving_interface, srv, ServingStatus)() {
  return &ServingStatus__handle;
}

#if defined(__cplusplus)
}
#endif
