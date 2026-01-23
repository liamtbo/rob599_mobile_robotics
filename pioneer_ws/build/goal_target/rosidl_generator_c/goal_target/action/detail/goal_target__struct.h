// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from goal_target:action/GoalTarget.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "goal_target/action/goal_target.h"


#ifndef GOAL_TARGET__ACTION__DETAIL__GOAL_TARGET__STRUCT_H_
#define GOAL_TARGET__ACTION__DETAIL__GOAL_TARGET__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'goal'
#include "geometry_msgs/msg/detail/point_stamped__struct.h"

/// Struct defined in action/GoalTarget in the package goal_target.
typedef struct goal_target__action__GoalTarget_Goal
{
  geometry_msgs__msg__PointStamped goal;
} goal_target__action__GoalTarget_Goal;

// Struct for a sequence of goal_target__action__GoalTarget_Goal.
typedef struct goal_target__action__GoalTarget_Goal__Sequence
{
  goal_target__action__GoalTarget_Goal * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} goal_target__action__GoalTarget_Goal__Sequence;

// Constants defined in the message

/// Struct defined in action/GoalTarget in the package goal_target.
typedef struct goal_target__action__GoalTarget_Result
{
  bool success;
} goal_target__action__GoalTarget_Result;

// Struct for a sequence of goal_target__action__GoalTarget_Result.
typedef struct goal_target__action__GoalTarget_Result__Sequence
{
  goal_target__action__GoalTarget_Result * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} goal_target__action__GoalTarget_Result__Sequence;

// Constants defined in the message

// Include directives for member types
// Member 'distance'
#include "std_msgs/msg/detail/float32__struct.h"

/// Struct defined in action/GoalTarget in the package goal_target.
typedef struct goal_target__action__GoalTarget_Feedback
{
  std_msgs__msg__Float32 distance;
} goal_target__action__GoalTarget_Feedback;

// Struct for a sequence of goal_target__action__GoalTarget_Feedback.
typedef struct goal_target__action__GoalTarget_Feedback__Sequence
{
  goal_target__action__GoalTarget_Feedback * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} goal_target__action__GoalTarget_Feedback__Sequence;

// Constants defined in the message

// Include directives for member types
// Member 'goal_id'
#include "unique_identifier_msgs/msg/detail/uuid__struct.h"
// Member 'goal'
#include "goal_target/action/detail/goal_target__struct.h"

/// Struct defined in action/GoalTarget in the package goal_target.
typedef struct goal_target__action__GoalTarget_SendGoal_Request
{
  unique_identifier_msgs__msg__UUID goal_id;
  goal_target__action__GoalTarget_Goal goal;
} goal_target__action__GoalTarget_SendGoal_Request;

// Struct for a sequence of goal_target__action__GoalTarget_SendGoal_Request.
typedef struct goal_target__action__GoalTarget_SendGoal_Request__Sequence
{
  goal_target__action__GoalTarget_SendGoal_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} goal_target__action__GoalTarget_SendGoal_Request__Sequence;

// Constants defined in the message

// Include directives for member types
// Member 'stamp'
#include "builtin_interfaces/msg/detail/time__struct.h"

/// Struct defined in action/GoalTarget in the package goal_target.
typedef struct goal_target__action__GoalTarget_SendGoal_Response
{
  bool accepted;
  builtin_interfaces__msg__Time stamp;
} goal_target__action__GoalTarget_SendGoal_Response;

// Struct for a sequence of goal_target__action__GoalTarget_SendGoal_Response.
typedef struct goal_target__action__GoalTarget_SendGoal_Response__Sequence
{
  goal_target__action__GoalTarget_SendGoal_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} goal_target__action__GoalTarget_SendGoal_Response__Sequence;

// Constants defined in the message

// Include directives for member types
// Member 'info'
#include "service_msgs/msg/detail/service_event_info__struct.h"

// constants for array fields with an upper bound
// request
enum
{
  goal_target__action__GoalTarget_SendGoal_Event__request__MAX_SIZE = 1
};
// response
enum
{
  goal_target__action__GoalTarget_SendGoal_Event__response__MAX_SIZE = 1
};

/// Struct defined in action/GoalTarget in the package goal_target.
typedef struct goal_target__action__GoalTarget_SendGoal_Event
{
  service_msgs__msg__ServiceEventInfo info;
  goal_target__action__GoalTarget_SendGoal_Request__Sequence request;
  goal_target__action__GoalTarget_SendGoal_Response__Sequence response;
} goal_target__action__GoalTarget_SendGoal_Event;

// Struct for a sequence of goal_target__action__GoalTarget_SendGoal_Event.
typedef struct goal_target__action__GoalTarget_SendGoal_Event__Sequence
{
  goal_target__action__GoalTarget_SendGoal_Event * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} goal_target__action__GoalTarget_SendGoal_Event__Sequence;

// Constants defined in the message

// Include directives for member types
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__struct.h"

/// Struct defined in action/GoalTarget in the package goal_target.
typedef struct goal_target__action__GoalTarget_GetResult_Request
{
  unique_identifier_msgs__msg__UUID goal_id;
} goal_target__action__GoalTarget_GetResult_Request;

// Struct for a sequence of goal_target__action__GoalTarget_GetResult_Request.
typedef struct goal_target__action__GoalTarget_GetResult_Request__Sequence
{
  goal_target__action__GoalTarget_GetResult_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} goal_target__action__GoalTarget_GetResult_Request__Sequence;

// Constants defined in the message

// Include directives for member types
// Member 'result'
// already included above
// #include "goal_target/action/detail/goal_target__struct.h"

/// Struct defined in action/GoalTarget in the package goal_target.
typedef struct goal_target__action__GoalTarget_GetResult_Response
{
  int8_t status;
  goal_target__action__GoalTarget_Result result;
} goal_target__action__GoalTarget_GetResult_Response;

// Struct for a sequence of goal_target__action__GoalTarget_GetResult_Response.
typedef struct goal_target__action__GoalTarget_GetResult_Response__Sequence
{
  goal_target__action__GoalTarget_GetResult_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} goal_target__action__GoalTarget_GetResult_Response__Sequence;

// Constants defined in the message

// Include directives for member types
// Member 'info'
// already included above
// #include "service_msgs/msg/detail/service_event_info__struct.h"

// constants for array fields with an upper bound
// request
enum
{
  goal_target__action__GoalTarget_GetResult_Event__request__MAX_SIZE = 1
};
// response
enum
{
  goal_target__action__GoalTarget_GetResult_Event__response__MAX_SIZE = 1
};

/// Struct defined in action/GoalTarget in the package goal_target.
typedef struct goal_target__action__GoalTarget_GetResult_Event
{
  service_msgs__msg__ServiceEventInfo info;
  goal_target__action__GoalTarget_GetResult_Request__Sequence request;
  goal_target__action__GoalTarget_GetResult_Response__Sequence response;
} goal_target__action__GoalTarget_GetResult_Event;

// Struct for a sequence of goal_target__action__GoalTarget_GetResult_Event.
typedef struct goal_target__action__GoalTarget_GetResult_Event__Sequence
{
  goal_target__action__GoalTarget_GetResult_Event * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} goal_target__action__GoalTarget_GetResult_Event__Sequence;

// Constants defined in the message

// Include directives for member types
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__struct.h"
// Member 'feedback'
// already included above
// #include "goal_target/action/detail/goal_target__struct.h"

/// Struct defined in action/GoalTarget in the package goal_target.
typedef struct goal_target__action__GoalTarget_FeedbackMessage
{
  unique_identifier_msgs__msg__UUID goal_id;
  goal_target__action__GoalTarget_Feedback feedback;
} goal_target__action__GoalTarget_FeedbackMessage;

// Struct for a sequence of goal_target__action__GoalTarget_FeedbackMessage.
typedef struct goal_target__action__GoalTarget_FeedbackMessage__Sequence
{
  goal_target__action__GoalTarget_FeedbackMessage * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} goal_target__action__GoalTarget_FeedbackMessage__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // GOAL_TARGET__ACTION__DETAIL__GOAL_TARGET__STRUCT_H_
