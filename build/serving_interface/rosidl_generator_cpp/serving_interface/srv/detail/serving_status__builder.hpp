// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from serving_interface:srv/ServingStatus.idl
// generated code does not contain a copyright notice

#ifndef SERVING_INTERFACE__SRV__DETAIL__SERVING_STATUS__BUILDER_HPP_
#define SERVING_INTERFACE__SRV__DETAIL__SERVING_STATUS__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "serving_interface/srv/detail/serving_status__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace serving_interface
{

namespace srv
{

namespace builder
{

class Init_ServingStatus_Request_is_arrived
{
public:
  Init_ServingStatus_Request_is_arrived()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::serving_interface::srv::ServingStatus_Request is_arrived(::serving_interface::srv::ServingStatus_Request::_is_arrived_type arg)
  {
    msg_.is_arrived = std::move(arg);
    return std::move(msg_);
  }

private:
  ::serving_interface::srv::ServingStatus_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::serving_interface::srv::ServingStatus_Request>()
{
  return serving_interface::srv::builder::Init_ServingStatus_Request_is_arrived();
}

}  // namespace serving_interface


namespace serving_interface
{

namespace srv
{

namespace builder
{

class Init_ServingStatus_Response_get_back
{
public:
  Init_ServingStatus_Response_get_back()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::serving_interface::srv::ServingStatus_Response get_back(::serving_interface::srv::ServingStatus_Response::_get_back_type arg)
  {
    msg_.get_back = std::move(arg);
    return std::move(msg_);
  }

private:
  ::serving_interface::srv::ServingStatus_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::serving_interface::srv::ServingStatus_Response>()
{
  return serving_interface::srv::builder::Init_ServingStatus_Response_get_back();
}

}  // namespace serving_interface

#endif  // SERVING_INTERFACE__SRV__DETAIL__SERVING_STATUS__BUILDER_HPP_
