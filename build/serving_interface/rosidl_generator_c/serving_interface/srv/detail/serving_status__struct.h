// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from serving_interface:srv/ServingStatus.idl
// generated code does not contain a copyright notice

#ifndef SERVING_INTERFACE__SRV__DETAIL__SERVING_STATUS__STRUCT_H_
#define SERVING_INTERFACE__SRV__DETAIL__SERVING_STATUS__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in srv/ServingStatus in the package serving_interface.
typedef struct serving_interface__srv__ServingStatus_Request
{
  bool is_arrived;
} serving_interface__srv__ServingStatus_Request;

// Struct for a sequence of serving_interface__srv__ServingStatus_Request.
typedef struct serving_interface__srv__ServingStatus_Request__Sequence
{
  serving_interface__srv__ServingStatus_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} serving_interface__srv__ServingStatus_Request__Sequence;


// Constants defined in the message

/// Struct defined in srv/ServingStatus in the package serving_interface.
typedef struct serving_interface__srv__ServingStatus_Response
{
  bool get_back;
} serving_interface__srv__ServingStatus_Response;

// Struct for a sequence of serving_interface__srv__ServingStatus_Response.
typedef struct serving_interface__srv__ServingStatus_Response__Sequence
{
  serving_interface__srv__ServingStatus_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} serving_interface__srv__ServingStatus_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // SERVING_INTERFACE__SRV__DETAIL__SERVING_STATUS__STRUCT_H_
