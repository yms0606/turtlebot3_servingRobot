// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from serving_interface:srv/ServingStatus.idl
// generated code does not contain a copyright notice

#ifndef SERVING_INTERFACE__SRV__DETAIL__SERVING_STATUS__TRAITS_HPP_
#define SERVING_INTERFACE__SRV__DETAIL__SERVING_STATUS__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "serving_interface/srv/detail/serving_status__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace serving_interface
{

namespace srv
{

inline void to_flow_style_yaml(
  const ServingStatus_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: is_arrived
  {
    out << "is_arrived: ";
    rosidl_generator_traits::value_to_yaml(msg.is_arrived, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const ServingStatus_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: is_arrived
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "is_arrived: ";
    rosidl_generator_traits::value_to_yaml(msg.is_arrived, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const ServingStatus_Request & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace serving_interface

namespace rosidl_generator_traits
{

[[deprecated("use serving_interface::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const serving_interface::srv::ServingStatus_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  serving_interface::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use serving_interface::srv::to_yaml() instead")]]
inline std::string to_yaml(const serving_interface::srv::ServingStatus_Request & msg)
{
  return serving_interface::srv::to_yaml(msg);
}

template<>
inline const char * data_type<serving_interface::srv::ServingStatus_Request>()
{
  return "serving_interface::srv::ServingStatus_Request";
}

template<>
inline const char * name<serving_interface::srv::ServingStatus_Request>()
{
  return "serving_interface/srv/ServingStatus_Request";
}

template<>
struct has_fixed_size<serving_interface::srv::ServingStatus_Request>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<serving_interface::srv::ServingStatus_Request>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<serving_interface::srv::ServingStatus_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace serving_interface
{

namespace srv
{

inline void to_flow_style_yaml(
  const ServingStatus_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: get_back
  {
    out << "get_back: ";
    rosidl_generator_traits::value_to_yaml(msg.get_back, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const ServingStatus_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: get_back
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "get_back: ";
    rosidl_generator_traits::value_to_yaml(msg.get_back, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const ServingStatus_Response & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace serving_interface

namespace rosidl_generator_traits
{

[[deprecated("use serving_interface::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const serving_interface::srv::ServingStatus_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  serving_interface::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use serving_interface::srv::to_yaml() instead")]]
inline std::string to_yaml(const serving_interface::srv::ServingStatus_Response & msg)
{
  return serving_interface::srv::to_yaml(msg);
}

template<>
inline const char * data_type<serving_interface::srv::ServingStatus_Response>()
{
  return "serving_interface::srv::ServingStatus_Response";
}

template<>
inline const char * name<serving_interface::srv::ServingStatus_Response>()
{
  return "serving_interface/srv/ServingStatus_Response";
}

template<>
struct has_fixed_size<serving_interface::srv::ServingStatus_Response>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<serving_interface::srv::ServingStatus_Response>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<serving_interface::srv::ServingStatus_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<serving_interface::srv::ServingStatus>()
{
  return "serving_interface::srv::ServingStatus";
}

template<>
inline const char * name<serving_interface::srv::ServingStatus>()
{
  return "serving_interface/srv/ServingStatus";
}

template<>
struct has_fixed_size<serving_interface::srv::ServingStatus>
  : std::integral_constant<
    bool,
    has_fixed_size<serving_interface::srv::ServingStatus_Request>::value &&
    has_fixed_size<serving_interface::srv::ServingStatus_Response>::value
  >
{
};

template<>
struct has_bounded_size<serving_interface::srv::ServingStatus>
  : std::integral_constant<
    bool,
    has_bounded_size<serving_interface::srv::ServingStatus_Request>::value &&
    has_bounded_size<serving_interface::srv::ServingStatus_Response>::value
  >
{
};

template<>
struct is_service<serving_interface::srv::ServingStatus>
  : std::true_type
{
};

template<>
struct is_service_request<serving_interface::srv::ServingStatus_Request>
  : std::true_type
{
};

template<>
struct is_service_response<serving_interface::srv::ServingStatus_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // SERVING_INTERFACE__SRV__DETAIL__SERVING_STATUS__TRAITS_HPP_
