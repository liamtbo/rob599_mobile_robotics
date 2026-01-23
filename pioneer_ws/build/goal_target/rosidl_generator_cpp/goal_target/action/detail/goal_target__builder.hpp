// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from goal_target:action/GoalTarget.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "goal_target/action/goal_target.hpp"


#ifndef GOAL_TARGET__ACTION__DETAIL__GOAL_TARGET__BUILDER_HPP_
#define GOAL_TARGET__ACTION__DETAIL__GOAL_TARGET__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "goal_target/action/detail/goal_target__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace goal_target
{

namespace action
{

namespace builder
{

class Init_GoalTarget_Goal_goal
{
public:
  Init_GoalTarget_Goal_goal()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::goal_target::action::GoalTarget_Goal goal(::goal_target::action::GoalTarget_Goal::_goal_type arg)
  {
    msg_.goal = std::move(arg);
    return std::move(msg_);
  }

private:
  ::goal_target::action::GoalTarget_Goal msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::goal_target::action::GoalTarget_Goal>()
{
  return goal_target::action::builder::Init_GoalTarget_Goal_goal();
}

}  // namespace goal_target


namespace goal_target
{

namespace action
{

namespace builder
{

class Init_GoalTarget_Result_success
{
public:
  Init_GoalTarget_Result_success()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::goal_target::action::GoalTarget_Result success(::goal_target::action::GoalTarget_Result::_success_type arg)
  {
    msg_.success = std::move(arg);
    return std::move(msg_);
  }

private:
  ::goal_target::action::GoalTarget_Result msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::goal_target::action::GoalTarget_Result>()
{
  return goal_target::action::builder::Init_GoalTarget_Result_success();
}

}  // namespace goal_target


namespace goal_target
{

namespace action
{

namespace builder
{

class Init_GoalTarget_Feedback_distance
{
public:
  Init_GoalTarget_Feedback_distance()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::goal_target::action::GoalTarget_Feedback distance(::goal_target::action::GoalTarget_Feedback::_distance_type arg)
  {
    msg_.distance = std::move(arg);
    return std::move(msg_);
  }

private:
  ::goal_target::action::GoalTarget_Feedback msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::goal_target::action::GoalTarget_Feedback>()
{
  return goal_target::action::builder::Init_GoalTarget_Feedback_distance();
}

}  // namespace goal_target


namespace goal_target
{

namespace action
{

namespace builder
{

class Init_GoalTarget_SendGoal_Request_goal
{
public:
  explicit Init_GoalTarget_SendGoal_Request_goal(::goal_target::action::GoalTarget_SendGoal_Request & msg)
  : msg_(msg)
  {}
  ::goal_target::action::GoalTarget_SendGoal_Request goal(::goal_target::action::GoalTarget_SendGoal_Request::_goal_type arg)
  {
    msg_.goal = std::move(arg);
    return std::move(msg_);
  }

private:
  ::goal_target::action::GoalTarget_SendGoal_Request msg_;
};

class Init_GoalTarget_SendGoal_Request_goal_id
{
public:
  Init_GoalTarget_SendGoal_Request_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_GoalTarget_SendGoal_Request_goal goal_id(::goal_target::action::GoalTarget_SendGoal_Request::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return Init_GoalTarget_SendGoal_Request_goal(msg_);
  }

private:
  ::goal_target::action::GoalTarget_SendGoal_Request msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::goal_target::action::GoalTarget_SendGoal_Request>()
{
  return goal_target::action::builder::Init_GoalTarget_SendGoal_Request_goal_id();
}

}  // namespace goal_target


namespace goal_target
{

namespace action
{

namespace builder
{

class Init_GoalTarget_SendGoal_Response_stamp
{
public:
  explicit Init_GoalTarget_SendGoal_Response_stamp(::goal_target::action::GoalTarget_SendGoal_Response & msg)
  : msg_(msg)
  {}
  ::goal_target::action::GoalTarget_SendGoal_Response stamp(::goal_target::action::GoalTarget_SendGoal_Response::_stamp_type arg)
  {
    msg_.stamp = std::move(arg);
    return std::move(msg_);
  }

private:
  ::goal_target::action::GoalTarget_SendGoal_Response msg_;
};

class Init_GoalTarget_SendGoal_Response_accepted
{
public:
  Init_GoalTarget_SendGoal_Response_accepted()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_GoalTarget_SendGoal_Response_stamp accepted(::goal_target::action::GoalTarget_SendGoal_Response::_accepted_type arg)
  {
    msg_.accepted = std::move(arg);
    return Init_GoalTarget_SendGoal_Response_stamp(msg_);
  }

private:
  ::goal_target::action::GoalTarget_SendGoal_Response msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::goal_target::action::GoalTarget_SendGoal_Response>()
{
  return goal_target::action::builder::Init_GoalTarget_SendGoal_Response_accepted();
}

}  // namespace goal_target


namespace goal_target
{

namespace action
{

namespace builder
{

class Init_GoalTarget_SendGoal_Event_response
{
public:
  explicit Init_GoalTarget_SendGoal_Event_response(::goal_target::action::GoalTarget_SendGoal_Event & msg)
  : msg_(msg)
  {}
  ::goal_target::action::GoalTarget_SendGoal_Event response(::goal_target::action::GoalTarget_SendGoal_Event::_response_type arg)
  {
    msg_.response = std::move(arg);
    return std::move(msg_);
  }

private:
  ::goal_target::action::GoalTarget_SendGoal_Event msg_;
};

class Init_GoalTarget_SendGoal_Event_request
{
public:
  explicit Init_GoalTarget_SendGoal_Event_request(::goal_target::action::GoalTarget_SendGoal_Event & msg)
  : msg_(msg)
  {}
  Init_GoalTarget_SendGoal_Event_response request(::goal_target::action::GoalTarget_SendGoal_Event::_request_type arg)
  {
    msg_.request = std::move(arg);
    return Init_GoalTarget_SendGoal_Event_response(msg_);
  }

private:
  ::goal_target::action::GoalTarget_SendGoal_Event msg_;
};

class Init_GoalTarget_SendGoal_Event_info
{
public:
  Init_GoalTarget_SendGoal_Event_info()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_GoalTarget_SendGoal_Event_request info(::goal_target::action::GoalTarget_SendGoal_Event::_info_type arg)
  {
    msg_.info = std::move(arg);
    return Init_GoalTarget_SendGoal_Event_request(msg_);
  }

private:
  ::goal_target::action::GoalTarget_SendGoal_Event msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::goal_target::action::GoalTarget_SendGoal_Event>()
{
  return goal_target::action::builder::Init_GoalTarget_SendGoal_Event_info();
}

}  // namespace goal_target


namespace goal_target
{

namespace action
{

namespace builder
{

class Init_GoalTarget_GetResult_Request_goal_id
{
public:
  Init_GoalTarget_GetResult_Request_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::goal_target::action::GoalTarget_GetResult_Request goal_id(::goal_target::action::GoalTarget_GetResult_Request::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return std::move(msg_);
  }

private:
  ::goal_target::action::GoalTarget_GetResult_Request msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::goal_target::action::GoalTarget_GetResult_Request>()
{
  return goal_target::action::builder::Init_GoalTarget_GetResult_Request_goal_id();
}

}  // namespace goal_target


namespace goal_target
{

namespace action
{

namespace builder
{

class Init_GoalTarget_GetResult_Response_result
{
public:
  explicit Init_GoalTarget_GetResult_Response_result(::goal_target::action::GoalTarget_GetResult_Response & msg)
  : msg_(msg)
  {}
  ::goal_target::action::GoalTarget_GetResult_Response result(::goal_target::action::GoalTarget_GetResult_Response::_result_type arg)
  {
    msg_.result = std::move(arg);
    return std::move(msg_);
  }

private:
  ::goal_target::action::GoalTarget_GetResult_Response msg_;
};

class Init_GoalTarget_GetResult_Response_status
{
public:
  Init_GoalTarget_GetResult_Response_status()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_GoalTarget_GetResult_Response_result status(::goal_target::action::GoalTarget_GetResult_Response::_status_type arg)
  {
    msg_.status = std::move(arg);
    return Init_GoalTarget_GetResult_Response_result(msg_);
  }

private:
  ::goal_target::action::GoalTarget_GetResult_Response msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::goal_target::action::GoalTarget_GetResult_Response>()
{
  return goal_target::action::builder::Init_GoalTarget_GetResult_Response_status();
}

}  // namespace goal_target


namespace goal_target
{

namespace action
{

namespace builder
{

class Init_GoalTarget_GetResult_Event_response
{
public:
  explicit Init_GoalTarget_GetResult_Event_response(::goal_target::action::GoalTarget_GetResult_Event & msg)
  : msg_(msg)
  {}
  ::goal_target::action::GoalTarget_GetResult_Event response(::goal_target::action::GoalTarget_GetResult_Event::_response_type arg)
  {
    msg_.response = std::move(arg);
    return std::move(msg_);
  }

private:
  ::goal_target::action::GoalTarget_GetResult_Event msg_;
};

class Init_GoalTarget_GetResult_Event_request
{
public:
  explicit Init_GoalTarget_GetResult_Event_request(::goal_target::action::GoalTarget_GetResult_Event & msg)
  : msg_(msg)
  {}
  Init_GoalTarget_GetResult_Event_response request(::goal_target::action::GoalTarget_GetResult_Event::_request_type arg)
  {
    msg_.request = std::move(arg);
    return Init_GoalTarget_GetResult_Event_response(msg_);
  }

private:
  ::goal_target::action::GoalTarget_GetResult_Event msg_;
};

class Init_GoalTarget_GetResult_Event_info
{
public:
  Init_GoalTarget_GetResult_Event_info()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_GoalTarget_GetResult_Event_request info(::goal_target::action::GoalTarget_GetResult_Event::_info_type arg)
  {
    msg_.info = std::move(arg);
    return Init_GoalTarget_GetResult_Event_request(msg_);
  }

private:
  ::goal_target::action::GoalTarget_GetResult_Event msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::goal_target::action::GoalTarget_GetResult_Event>()
{
  return goal_target::action::builder::Init_GoalTarget_GetResult_Event_info();
}

}  // namespace goal_target


namespace goal_target
{

namespace action
{

namespace builder
{

class Init_GoalTarget_FeedbackMessage_feedback
{
public:
  explicit Init_GoalTarget_FeedbackMessage_feedback(::goal_target::action::GoalTarget_FeedbackMessage & msg)
  : msg_(msg)
  {}
  ::goal_target::action::GoalTarget_FeedbackMessage feedback(::goal_target::action::GoalTarget_FeedbackMessage::_feedback_type arg)
  {
    msg_.feedback = std::move(arg);
    return std::move(msg_);
  }

private:
  ::goal_target::action::GoalTarget_FeedbackMessage msg_;
};

class Init_GoalTarget_FeedbackMessage_goal_id
{
public:
  Init_GoalTarget_FeedbackMessage_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_GoalTarget_FeedbackMessage_feedback goal_id(::goal_target::action::GoalTarget_FeedbackMessage::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return Init_GoalTarget_FeedbackMessage_feedback(msg_);
  }

private:
  ::goal_target::action::GoalTarget_FeedbackMessage msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::goal_target::action::GoalTarget_FeedbackMessage>()
{
  return goal_target::action::builder::Init_GoalTarget_FeedbackMessage_goal_id();
}

}  // namespace goal_target

#endif  // GOAL_TARGET__ACTION__DETAIL__GOAL_TARGET__BUILDER_HPP_
