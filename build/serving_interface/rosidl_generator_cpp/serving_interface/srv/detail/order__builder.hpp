// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from serving_interface:srv/Order.idl
// generated code does not contain a copyright notice

#ifndef SERVING_INTERFACE__SRV__DETAIL__ORDER__BUILDER_HPP_
#define SERVING_INTERFACE__SRV__DETAIL__ORDER__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "serving_interface/srv/detail/order__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace serving_interface
{

namespace srv
{

namespace builder
{

class Init_Order_Request_total_price
{
public:
  explicit Init_Order_Request_total_price(::serving_interface::srv::Order_Request & msg)
  : msg_(msg)
  {}
  ::serving_interface::srv::Order_Request total_price(::serving_interface::srv::Order_Request::_total_price_type arg)
  {
    msg_.total_price = std::move(arg);
    return std::move(msg_);
  }

private:
  ::serving_interface::srv::Order_Request msg_;
};

class Init_Order_Request_menu
{
public:
  explicit Init_Order_Request_menu(::serving_interface::srv::Order_Request & msg)
  : msg_(msg)
  {}
  Init_Order_Request_total_price menu(::serving_interface::srv::Order_Request::_menu_type arg)
  {
    msg_.menu = std::move(arg);
    return Init_Order_Request_total_price(msg_);
  }

private:
  ::serving_interface::srv::Order_Request msg_;
};

class Init_Order_Request_table_num
{
public:
  Init_Order_Request_table_num()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Order_Request_menu table_num(::serving_interface::srv::Order_Request::_table_num_type arg)
  {
    msg_.table_num = std::move(arg);
    return Init_Order_Request_menu(msg_);
  }

private:
  ::serving_interface::srv::Order_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::serving_interface::srv::Order_Request>()
{
  return serving_interface::srv::builder::Init_Order_Request_table_num();
}

}  // namespace serving_interface


namespace serving_interface
{

namespace srv
{

namespace builder
{

class Init_Order_Response_is_accept
{
public:
  Init_Order_Response_is_accept()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::serving_interface::srv::Order_Response is_accept(::serving_interface::srv::Order_Response::_is_accept_type arg)
  {
    msg_.is_accept = std::move(arg);
    return std::move(msg_);
  }

private:
  ::serving_interface::srv::Order_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::serving_interface::srv::Order_Response>()
{
  return serving_interface::srv::builder::Init_Order_Response_is_accept();
}

}  // namespace serving_interface

#endif  // SERVING_INTERFACE__SRV__DETAIL__ORDER__BUILDER_HPP_
