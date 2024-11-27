// generated from rosidl_typesupport_cpp/resource/idl__type_support.cpp.em
// with input from serving_interface:srv/Order.idl
// generated code does not contain a copyright notice

#include "cstddef"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "serving_interface/srv/detail/order__struct.hpp"
#include "rosidl_typesupport_cpp/identifier.hpp"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_c/type_support_map.h"
#include "rosidl_typesupport_cpp/message_type_support_dispatch.hpp"
#include "rosidl_typesupport_cpp/visibility_control.h"
#include "rosidl_typesupport_interface/macros.h"

namespace serving_interface
{

namespace srv
{

namespace rosidl_typesupport_cpp
{

typedef struct _Order_Request_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _Order_Request_type_support_ids_t;

static const _Order_Request_type_support_ids_t _Order_Request_message_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_cpp",  // ::rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
    "rosidl_typesupport_introspection_cpp",  // ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  }
};

typedef struct _Order_Request_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _Order_Request_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _Order_Request_type_support_symbol_names_t _Order_Request_message_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, serving_interface, srv, Order_Request)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, serving_interface, srv, Order_Request)),
  }
};

typedef struct _Order_Request_type_support_data_t
{
  void * data[2];
} _Order_Request_type_support_data_t;

static _Order_Request_type_support_data_t _Order_Request_message_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _Order_Request_message_typesupport_map = {
  2,
  "serving_interface",
  &_Order_Request_message_typesupport_ids.typesupport_identifier[0],
  &_Order_Request_message_typesupport_symbol_names.symbol_name[0],
  &_Order_Request_message_typesupport_data.data[0],
};

static const rosidl_message_type_support_t Order_Request_message_type_support_handle = {
  ::rosidl_typesupport_cpp::typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_Order_Request_message_typesupport_map),
  ::rosidl_typesupport_cpp::get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_cpp

}  // namespace srv

}  // namespace serving_interface

namespace rosidl_typesupport_cpp
{

template<>
ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<serving_interface::srv::Order_Request>()
{
  return &::serving_interface::srv::rosidl_typesupport_cpp::Order_Request_message_type_support_handle;
}

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_cpp, serving_interface, srv, Order_Request)() {
  return get_message_type_support_handle<serving_interface::srv::Order_Request>();
}

#ifdef __cplusplus
}
#endif
}  // namespace rosidl_typesupport_cpp

// already included above
// #include "cstddef"
// already included above
// #include "rosidl_runtime_c/message_type_support_struct.h"
// already included above
// #include "serving_interface/srv/detail/order__struct.hpp"
// already included above
// #include "rosidl_typesupport_cpp/identifier.hpp"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support.hpp"
// already included above
// #include "rosidl_typesupport_c/type_support_map.h"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support_dispatch.hpp"
// already included above
// #include "rosidl_typesupport_cpp/visibility_control.h"
// already included above
// #include "rosidl_typesupport_interface/macros.h"

namespace serving_interface
{

namespace srv
{

namespace rosidl_typesupport_cpp
{

typedef struct _Order_Response_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _Order_Response_type_support_ids_t;

static const _Order_Response_type_support_ids_t _Order_Response_message_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_cpp",  // ::rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
    "rosidl_typesupport_introspection_cpp",  // ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  }
};

typedef struct _Order_Response_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _Order_Response_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _Order_Response_type_support_symbol_names_t _Order_Response_message_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, serving_interface, srv, Order_Response)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, serving_interface, srv, Order_Response)),
  }
};

typedef struct _Order_Response_type_support_data_t
{
  void * data[2];
} _Order_Response_type_support_data_t;

static _Order_Response_type_support_data_t _Order_Response_message_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _Order_Response_message_typesupport_map = {
  2,
  "serving_interface",
  &_Order_Response_message_typesupport_ids.typesupport_identifier[0],
  &_Order_Response_message_typesupport_symbol_names.symbol_name[0],
  &_Order_Response_message_typesupport_data.data[0],
};

static const rosidl_message_type_support_t Order_Response_message_type_support_handle = {
  ::rosidl_typesupport_cpp::typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_Order_Response_message_typesupport_map),
  ::rosidl_typesupport_cpp::get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_cpp

}  // namespace srv

}  // namespace serving_interface

namespace rosidl_typesupport_cpp
{

template<>
ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<serving_interface::srv::Order_Response>()
{
  return &::serving_interface::srv::rosidl_typesupport_cpp::Order_Response_message_type_support_handle;
}

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_cpp, serving_interface, srv, Order_Response)() {
  return get_message_type_support_handle<serving_interface::srv::Order_Response>();
}

#ifdef __cplusplus
}
#endif
}  // namespace rosidl_typesupport_cpp

// already included above
// #include "cstddef"
#include "rosidl_runtime_c/service_type_support_struct.h"
// already included above
// #include "serving_interface/srv/detail/order__struct.hpp"
// already included above
// #include "rosidl_typesupport_cpp/identifier.hpp"
#include "rosidl_typesupport_cpp/service_type_support.hpp"
// already included above
// #include "rosidl_typesupport_c/type_support_map.h"
#include "rosidl_typesupport_cpp/service_type_support_dispatch.hpp"
// already included above
// #include "rosidl_typesupport_cpp/visibility_control.h"
// already included above
// #include "rosidl_typesupport_interface/macros.h"

namespace serving_interface
{

namespace srv
{

namespace rosidl_typesupport_cpp
{

typedef struct _Order_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _Order_type_support_ids_t;

static const _Order_type_support_ids_t _Order_service_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_cpp",  // ::rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
    "rosidl_typesupport_introspection_cpp",  // ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  }
};

typedef struct _Order_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _Order_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _Order_type_support_symbol_names_t _Order_service_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, serving_interface, srv, Order)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, serving_interface, srv, Order)),
  }
};

typedef struct _Order_type_support_data_t
{
  void * data[2];
} _Order_type_support_data_t;

static _Order_type_support_data_t _Order_service_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _Order_service_typesupport_map = {
  2,
  "serving_interface",
  &_Order_service_typesupport_ids.typesupport_identifier[0],
  &_Order_service_typesupport_symbol_names.symbol_name[0],
  &_Order_service_typesupport_data.data[0],
};

static const rosidl_service_type_support_t Order_service_type_support_handle = {
  ::rosidl_typesupport_cpp::typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_Order_service_typesupport_map),
  ::rosidl_typesupport_cpp::get_service_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_cpp

}  // namespace srv

}  // namespace serving_interface

namespace rosidl_typesupport_cpp
{

template<>
ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_service_type_support_t *
get_service_type_support_handle<serving_interface::srv::Order>()
{
  return &::serving_interface::srv::rosidl_typesupport_cpp::Order_service_type_support_handle;
}

}  // namespace rosidl_typesupport_cpp
