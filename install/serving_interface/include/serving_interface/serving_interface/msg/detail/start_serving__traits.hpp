// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from serving_interface:msg/StartServing.idl
// generated code does not contain a copyright notice

#ifndef SERVING_INTERFACE__MSG__DETAIL__START_SERVING__TRAITS_HPP_
#define SERVING_INTERFACE__MSG__DETAIL__START_SERVING__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "serving_interface/msg/detail/start_serving__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace serving_interface
{

namespace msg
{

inline void to_flow_style_yaml(
  const StartServing & msg,
  std::ostream & out)
{
  out << "{";
  // member: is_started
  {
    out << "is_started: ";
    rosidl_generator_traits::value_to_yaml(msg.is_started, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const StartServing & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: is_started
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "is_started: ";
    rosidl_generator_traits::value_to_yaml(msg.is_started, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const StartServing & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace msg

}  // namespace serving_interface

namespace rosidl_generator_traits
{

[[deprecated("use serving_interface::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const serving_interface::msg::StartServing & msg,
  std::ostream & out, size_t indentation = 0)
{
  serving_interface::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use serving_interface::msg::to_yaml() instead")]]
inline std::string to_yaml(const serving_interface::msg::StartServing & msg)
{
  return serving_interface::msg::to_yaml(msg);
}

template<>
inline const char * data_type<serving_interface::msg::StartServing>()
{
  return "serving_interface::msg::StartServing";
}

template<>
inline const char * name<serving_interface::msg::StartServing>()
{
  return "serving_interface/msg/StartServing";
}

template<>
struct has_fixed_size<serving_interface::msg::StartServing>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<serving_interface::msg::StartServing>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<serving_interface::msg::StartServing>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // SERVING_INTERFACE__MSG__DETAIL__START_SERVING__TRAITS_HPP_
