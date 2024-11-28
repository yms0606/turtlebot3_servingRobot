// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from serving_interface:srv/Order.idl
// generated code does not contain a copyright notice

#ifndef SERVING_INTERFACE__SRV__DETAIL__ORDER__TRAITS_HPP_
#define SERVING_INTERFACE__SRV__DETAIL__ORDER__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "serving_interface/srv/detail/order__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace serving_interface
{

namespace srv
{

inline void to_flow_style_yaml(
  const Order_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: table_num
  {
    out << "table_num: ";
    rosidl_generator_traits::value_to_yaml(msg.table_num, out);
    out << ", ";
  }

  // member: menu
  {
    if (msg.menu.size() == 0) {
      out << "menu: []";
    } else {
      out << "menu: [";
      size_t pending_items = msg.menu.size();
      for (auto item : msg.menu) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: total_price
  {
    out << "total_price: ";
    rosidl_generator_traits::value_to_yaml(msg.total_price, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Order_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: table_num
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "table_num: ";
    rosidl_generator_traits::value_to_yaml(msg.table_num, out);
    out << "\n";
  }

  // member: menu
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.menu.size() == 0) {
      out << "menu: []\n";
    } else {
      out << "menu:\n";
      for (auto item : msg.menu) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }

  // member: total_price
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "total_price: ";
    rosidl_generator_traits::value_to_yaml(msg.total_price, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Order_Request & msg, bool use_flow_style = false)
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
  const serving_interface::srv::Order_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  serving_interface::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use serving_interface::srv::to_yaml() instead")]]
inline std::string to_yaml(const serving_interface::srv::Order_Request & msg)
{
  return serving_interface::srv::to_yaml(msg);
}

template<>
inline const char * data_type<serving_interface::srv::Order_Request>()
{
  return "serving_interface::srv::Order_Request";
}

template<>
inline const char * name<serving_interface::srv::Order_Request>()
{
  return "serving_interface/srv/Order_Request";
}

template<>
struct has_fixed_size<serving_interface::srv::Order_Request>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<serving_interface::srv::Order_Request>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<serving_interface::srv::Order_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace serving_interface
{

namespace srv
{

inline void to_flow_style_yaml(
  const Order_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: is_accept
  {
    out << "is_accept: ";
    rosidl_generator_traits::value_to_yaml(msg.is_accept, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Order_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: is_accept
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "is_accept: ";
    rosidl_generator_traits::value_to_yaml(msg.is_accept, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Order_Response & msg, bool use_flow_style = false)
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
  const serving_interface::srv::Order_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  serving_interface::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use serving_interface::srv::to_yaml() instead")]]
inline std::string to_yaml(const serving_interface::srv::Order_Response & msg)
{
  return serving_interface::srv::to_yaml(msg);
}

template<>
inline const char * data_type<serving_interface::srv::Order_Response>()
{
  return "serving_interface::srv::Order_Response";
}

template<>
inline const char * name<serving_interface::srv::Order_Response>()
{
  return "serving_interface/srv/Order_Response";
}

template<>
struct has_fixed_size<serving_interface::srv::Order_Response>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<serving_interface::srv::Order_Response>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<serving_interface::srv::Order_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<serving_interface::srv::Order>()
{
  return "serving_interface::srv::Order";
}

template<>
inline const char * name<serving_interface::srv::Order>()
{
  return "serving_interface/srv/Order";
}

template<>
struct has_fixed_size<serving_interface::srv::Order>
  : std::integral_constant<
    bool,
    has_fixed_size<serving_interface::srv::Order_Request>::value &&
    has_fixed_size<serving_interface::srv::Order_Response>::value
  >
{
};

template<>
struct has_bounded_size<serving_interface::srv::Order>
  : std::integral_constant<
    bool,
    has_bounded_size<serving_interface::srv::Order_Request>::value &&
    has_bounded_size<serving_interface::srv::Order_Response>::value
  >
{
};

template<>
struct is_service<serving_interface::srv::Order>
  : std::true_type
{
};

template<>
struct is_service_request<serving_interface::srv::Order_Request>
  : std::true_type
{
};

template<>
struct is_service_response<serving_interface::srv::Order_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // SERVING_INTERFACE__SRV__DETAIL__ORDER__TRAITS_HPP_
