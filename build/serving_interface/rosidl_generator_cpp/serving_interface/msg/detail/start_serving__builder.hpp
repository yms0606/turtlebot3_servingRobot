// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from serving_interface:msg/StartServing.idl
// generated code does not contain a copyright notice

#ifndef SERVING_INTERFACE__MSG__DETAIL__START_SERVING__BUILDER_HPP_
#define SERVING_INTERFACE__MSG__DETAIL__START_SERVING__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "serving_interface/msg/detail/start_serving__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace serving_interface
{

namespace msg
{

namespace builder
{

class Init_StartServing_is_started
{
public:
  Init_StartServing_is_started()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::serving_interface::msg::StartServing is_started(::serving_interface::msg::StartServing::_is_started_type arg)
  {
    msg_.is_started = std::move(arg);
    return std::move(msg_);
  }

private:
  ::serving_interface::msg::StartServing msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::serving_interface::msg::StartServing>()
{
  return serving_interface::msg::builder::Init_StartServing_is_started();
}

}  // namespace serving_interface

#endif  // SERVING_INTERFACE__MSG__DETAIL__START_SERVING__BUILDER_HPP_
