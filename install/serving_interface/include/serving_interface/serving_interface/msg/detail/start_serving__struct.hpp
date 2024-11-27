// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from serving_interface:msg/StartServing.idl
// generated code does not contain a copyright notice

#ifndef SERVING_INTERFACE__MSG__DETAIL__START_SERVING__STRUCT_HPP_
#define SERVING_INTERFACE__MSG__DETAIL__START_SERVING__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__serving_interface__msg__StartServing __attribute__((deprecated))
#else
# define DEPRECATED__serving_interface__msg__StartServing __declspec(deprecated)
#endif

namespace serving_interface
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct StartServing_
{
  using Type = StartServing_<ContainerAllocator>;

  explicit StartServing_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->is_started = false;
    }
  }

  explicit StartServing_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->is_started = false;
    }
  }

  // field types and members
  using _is_started_type =
    bool;
  _is_started_type is_started;

  // setters for named parameter idiom
  Type & set__is_started(
    const bool & _arg)
  {
    this->is_started = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    serving_interface::msg::StartServing_<ContainerAllocator> *;
  using ConstRawPtr =
    const serving_interface::msg::StartServing_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<serving_interface::msg::StartServing_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<serving_interface::msg::StartServing_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      serving_interface::msg::StartServing_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<serving_interface::msg::StartServing_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      serving_interface::msg::StartServing_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<serving_interface::msg::StartServing_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<serving_interface::msg::StartServing_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<serving_interface::msg::StartServing_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__serving_interface__msg__StartServing
    std::shared_ptr<serving_interface::msg::StartServing_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__serving_interface__msg__StartServing
    std::shared_ptr<serving_interface::msg::StartServing_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const StartServing_ & other) const
  {
    if (this->is_started != other.is_started) {
      return false;
    }
    return true;
  }
  bool operator!=(const StartServing_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct StartServing_

// alias to use template instance with default allocator
using StartServing =
  serving_interface::msg::StartServing_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace serving_interface

#endif  // SERVING_INTERFACE__MSG__DETAIL__START_SERVING__STRUCT_HPP_
