// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from serving_interface:srv/ServingStatus.idl
// generated code does not contain a copyright notice

#ifndef SERVING_INTERFACE__SRV__DETAIL__SERVING_STATUS__STRUCT_HPP_
#define SERVING_INTERFACE__SRV__DETAIL__SERVING_STATUS__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__serving_interface__srv__ServingStatus_Request __attribute__((deprecated))
#else
# define DEPRECATED__serving_interface__srv__ServingStatus_Request __declspec(deprecated)
#endif

namespace serving_interface
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct ServingStatus_Request_
{
  using Type = ServingStatus_Request_<ContainerAllocator>;

  explicit ServingStatus_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->is_arrived = false;
    }
  }

  explicit ServingStatus_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->is_arrived = false;
    }
  }

  // field types and members
  using _is_arrived_type =
    bool;
  _is_arrived_type is_arrived;

  // setters for named parameter idiom
  Type & set__is_arrived(
    const bool & _arg)
  {
    this->is_arrived = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    serving_interface::srv::ServingStatus_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const serving_interface::srv::ServingStatus_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<serving_interface::srv::ServingStatus_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<serving_interface::srv::ServingStatus_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      serving_interface::srv::ServingStatus_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<serving_interface::srv::ServingStatus_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      serving_interface::srv::ServingStatus_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<serving_interface::srv::ServingStatus_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<serving_interface::srv::ServingStatus_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<serving_interface::srv::ServingStatus_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__serving_interface__srv__ServingStatus_Request
    std::shared_ptr<serving_interface::srv::ServingStatus_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__serving_interface__srv__ServingStatus_Request
    std::shared_ptr<serving_interface::srv::ServingStatus_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const ServingStatus_Request_ & other) const
  {
    if (this->is_arrived != other.is_arrived) {
      return false;
    }
    return true;
  }
  bool operator!=(const ServingStatus_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct ServingStatus_Request_

// alias to use template instance with default allocator
using ServingStatus_Request =
  serving_interface::srv::ServingStatus_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace serving_interface


#ifndef _WIN32
# define DEPRECATED__serving_interface__srv__ServingStatus_Response __attribute__((deprecated))
#else
# define DEPRECATED__serving_interface__srv__ServingStatus_Response __declspec(deprecated)
#endif

namespace serving_interface
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct ServingStatus_Response_
{
  using Type = ServingStatus_Response_<ContainerAllocator>;

  explicit ServingStatus_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->get_back = false;
    }
  }

  explicit ServingStatus_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->get_back = false;
    }
  }

  // field types and members
  using _get_back_type =
    bool;
  _get_back_type get_back;

  // setters for named parameter idiom
  Type & set__get_back(
    const bool & _arg)
  {
    this->get_back = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    serving_interface::srv::ServingStatus_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const serving_interface::srv::ServingStatus_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<serving_interface::srv::ServingStatus_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<serving_interface::srv::ServingStatus_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      serving_interface::srv::ServingStatus_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<serving_interface::srv::ServingStatus_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      serving_interface::srv::ServingStatus_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<serving_interface::srv::ServingStatus_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<serving_interface::srv::ServingStatus_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<serving_interface::srv::ServingStatus_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__serving_interface__srv__ServingStatus_Response
    std::shared_ptr<serving_interface::srv::ServingStatus_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__serving_interface__srv__ServingStatus_Response
    std::shared_ptr<serving_interface::srv::ServingStatus_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const ServingStatus_Response_ & other) const
  {
    if (this->get_back != other.get_back) {
      return false;
    }
    return true;
  }
  bool operator!=(const ServingStatus_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct ServingStatus_Response_

// alias to use template instance with default allocator
using ServingStatus_Response =
  serving_interface::srv::ServingStatus_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace serving_interface

namespace serving_interface
{

namespace srv
{

struct ServingStatus
{
  using Request = serving_interface::srv::ServingStatus_Request;
  using Response = serving_interface::srv::ServingStatus_Response;
};

}  // namespace srv

}  // namespace serving_interface

#endif  // SERVING_INTERFACE__SRV__DETAIL__SERVING_STATUS__STRUCT_HPP_
