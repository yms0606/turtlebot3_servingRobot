// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from serving_interface:msg/StartServing.idl
// generated code does not contain a copyright notice
#include "serving_interface/msg/detail/start_serving__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


bool
serving_interface__msg__StartServing__init(serving_interface__msg__StartServing * msg)
{
  if (!msg) {
    return false;
  }
  // is_started
  return true;
}

void
serving_interface__msg__StartServing__fini(serving_interface__msg__StartServing * msg)
{
  if (!msg) {
    return;
  }
  // is_started
}

bool
serving_interface__msg__StartServing__are_equal(const serving_interface__msg__StartServing * lhs, const serving_interface__msg__StartServing * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // is_started
  if (lhs->is_started != rhs->is_started) {
    return false;
  }
  return true;
}

bool
serving_interface__msg__StartServing__copy(
  const serving_interface__msg__StartServing * input,
  serving_interface__msg__StartServing * output)
{
  if (!input || !output) {
    return false;
  }
  // is_started
  output->is_started = input->is_started;
  return true;
}

serving_interface__msg__StartServing *
serving_interface__msg__StartServing__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  serving_interface__msg__StartServing * msg = (serving_interface__msg__StartServing *)allocator.allocate(sizeof(serving_interface__msg__StartServing), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(serving_interface__msg__StartServing));
  bool success = serving_interface__msg__StartServing__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
serving_interface__msg__StartServing__destroy(serving_interface__msg__StartServing * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    serving_interface__msg__StartServing__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
serving_interface__msg__StartServing__Sequence__init(serving_interface__msg__StartServing__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  serving_interface__msg__StartServing * data = NULL;

  if (size) {
    data = (serving_interface__msg__StartServing *)allocator.zero_allocate(size, sizeof(serving_interface__msg__StartServing), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = serving_interface__msg__StartServing__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        serving_interface__msg__StartServing__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
serving_interface__msg__StartServing__Sequence__fini(serving_interface__msg__StartServing__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      serving_interface__msg__StartServing__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

serving_interface__msg__StartServing__Sequence *
serving_interface__msg__StartServing__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  serving_interface__msg__StartServing__Sequence * array = (serving_interface__msg__StartServing__Sequence *)allocator.allocate(sizeof(serving_interface__msg__StartServing__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = serving_interface__msg__StartServing__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
serving_interface__msg__StartServing__Sequence__destroy(serving_interface__msg__StartServing__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    serving_interface__msg__StartServing__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
serving_interface__msg__StartServing__Sequence__are_equal(const serving_interface__msg__StartServing__Sequence * lhs, const serving_interface__msg__StartServing__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!serving_interface__msg__StartServing__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
serving_interface__msg__StartServing__Sequence__copy(
  const serving_interface__msg__StartServing__Sequence * input,
  serving_interface__msg__StartServing__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(serving_interface__msg__StartServing);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    serving_interface__msg__StartServing * data =
      (serving_interface__msg__StartServing *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!serving_interface__msg__StartServing__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          serving_interface__msg__StartServing__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!serving_interface__msg__StartServing__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
