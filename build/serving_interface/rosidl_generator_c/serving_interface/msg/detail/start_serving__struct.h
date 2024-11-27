// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from serving_interface:msg/StartServing.idl
// generated code does not contain a copyright notice

#ifndef SERVING_INTERFACE__MSG__DETAIL__START_SERVING__STRUCT_H_
#define SERVING_INTERFACE__MSG__DETAIL__START_SERVING__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in msg/StartServing in the package serving_interface.
typedef struct serving_interface__msg__StartServing
{
  bool is_started;
} serving_interface__msg__StartServing;

// Struct for a sequence of serving_interface__msg__StartServing.
typedef struct serving_interface__msg__StartServing__Sequence
{
  serving_interface__msg__StartServing * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} serving_interface__msg__StartServing__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // SERVING_INTERFACE__MSG__DETAIL__START_SERVING__STRUCT_H_
