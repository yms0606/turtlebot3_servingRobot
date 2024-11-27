// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from serving_interface:srv/Order.idl
// generated code does not contain a copyright notice

#ifndef SERVING_INTERFACE__SRV__DETAIL__ORDER__STRUCT_H_
#define SERVING_INTERFACE__SRV__DETAIL__ORDER__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'menu'
#include "rosidl_runtime_c/string.h"

/// Struct defined in srv/Order in the package serving_interface.
typedef struct serving_interface__srv__Order_Request
{
  uint8_t table_num;
  rosidl_runtime_c__String__Sequence menu;
  uint32_t total_price;
} serving_interface__srv__Order_Request;

// Struct for a sequence of serving_interface__srv__Order_Request.
typedef struct serving_interface__srv__Order_Request__Sequence
{
  serving_interface__srv__Order_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} serving_interface__srv__Order_Request__Sequence;


// Constants defined in the message

/// Struct defined in srv/Order in the package serving_interface.
typedef struct serving_interface__srv__Order_Response
{
  bool is_accept;
} serving_interface__srv__Order_Response;

// Struct for a sequence of serving_interface__srv__Order_Response.
typedef struct serving_interface__srv__Order_Response__Sequence
{
  serving_interface__srv__Order_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} serving_interface__srv__Order_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // SERVING_INTERFACE__SRV__DETAIL__ORDER__STRUCT_H_
