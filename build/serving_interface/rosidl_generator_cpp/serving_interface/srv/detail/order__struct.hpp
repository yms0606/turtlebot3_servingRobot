// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from serving_interface:srv/Order.idl
// generated code does not contain a copyright notice

#ifndef SERVING_INTERFACE__SRV__DETAIL__ORDER__STRUCT_HPP_
#define SERVING_INTERFACE__SRV__DETAIL__ORDER__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__serving_interface__srv__Order_Request __attribute__((deprecated))
#else
# define DEPRECATED__serving_interface__srv__Order_Request __declspec(deprecated)
#endif

namespace serving_interface
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct Order_Request_
{
  using Type = Order_Request_<ContainerAllocator>;

  explicit Order_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->table_num = 0;
      this->total_price = 0ul;
    }
  }

  explicit Order_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->table_num = 0;
      this->total_price = 0ul;
    }
  }

  // field types and members
  using _table_num_type =
    uint8_t;
  _table_num_type table_num;
  using _menu_type =
    std::vector<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>>;
  _menu_type menu;
  using _total_price_type =
    uint32_t;
  _total_price_type total_price;

  // setters for named parameter idiom
  Type & set__table_num(
    const uint8_t & _arg)
  {
    this->table_num = _arg;
    return *this;
  }
  Type & set__menu(
    const std::vector<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>> & _arg)
  {
    this->menu = _arg;
    return *this;
  }
  Type & set__total_price(
    const uint32_t & _arg)
  {
    this->total_price = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    serving_interface::srv::Order_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const serving_interface::srv::Order_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<serving_interface::srv::Order_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<serving_interface::srv::Order_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      serving_interface::srv::Order_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<serving_interface::srv::Order_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      serving_interface::srv::Order_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<serving_interface::srv::Order_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<serving_interface::srv::Order_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<serving_interface::srv::Order_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__serving_interface__srv__Order_Request
    std::shared_ptr<serving_interface::srv::Order_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__serving_interface__srv__Order_Request
    std::shared_ptr<serving_interface::srv::Order_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Order_Request_ & other) const
  {
    if (this->table_num != other.table_num) {
      return false;
    }
    if (this->menu != other.menu) {
      return false;
    }
    if (this->total_price != other.total_price) {
      return false;
    }
    return true;
  }
  bool operator!=(const Order_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Order_Request_

// alias to use template instance with default allocator
using Order_Request =
  serving_interface::srv::Order_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace serving_interface


#ifndef _WIN32
# define DEPRECATED__serving_interface__srv__Order_Response __attribute__((deprecated))
#else
# define DEPRECATED__serving_interface__srv__Order_Response __declspec(deprecated)
#endif

namespace serving_interface
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct Order_Response_
{
  using Type = Order_Response_<ContainerAllocator>;

  explicit Order_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->is_accept = false;
    }
  }

  explicit Order_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->is_accept = false;
    }
  }

  // field types and members
  using _is_accept_type =
    bool;
  _is_accept_type is_accept;

  // setters for named parameter idiom
  Type & set__is_accept(
    const bool & _arg)
  {
    this->is_accept = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    serving_interface::srv::Order_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const serving_interface::srv::Order_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<serving_interface::srv::Order_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<serving_interface::srv::Order_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      serving_interface::srv::Order_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<serving_interface::srv::Order_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      serving_interface::srv::Order_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<serving_interface::srv::Order_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<serving_interface::srv::Order_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<serving_interface::srv::Order_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__serving_interface__srv__Order_Response
    std::shared_ptr<serving_interface::srv::Order_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__serving_interface__srv__Order_Response
    std::shared_ptr<serving_interface::srv::Order_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Order_Response_ & other) const
  {
    if (this->is_accept != other.is_accept) {
      return false;
    }
    return true;
  }
  bool operator!=(const Order_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Order_Response_

// alias to use template instance with default allocator
using Order_Response =
  serving_interface::srv::Order_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace serving_interface

namespace serving_interface
{

namespace srv
{

struct Order
{
  using Request = serving_interface::srv::Order_Request;
  using Response = serving_interface::srv::Order_Response;
};

}  // namespace srv

}  // namespace serving_interface

#endif  // SERVING_INTERFACE__SRV__DETAIL__ORDER__STRUCT_HPP_
