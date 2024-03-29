# Solve the problem of finding the tangent of the angle alpha given the sine of alpha and the cosine of alpha and add
# event logging to the "app.log" file.
# Catching the resulting sine and cosine values should be implemented using the "info" level.
# In the case of successful finding of the tangent of the alpha angle, logging should be with the "debug" level.
# In the event that cosine alpha = 0, logging should be with the "warning" level and the notification:
# "The cosine of the angle alpha = 0. The tangent is not defined.".
# In the event that the tangent is not defined, logging should be with the "critical" level and the notification:
# "The tangent of the angle alpha is not defined.".
# tan(α) = sin(α) / cos(α)
# Don't use: encoding='utf-8'.
# Don't use'print()'.
# Don't use'return'.
# Please use logging. ....

# For example:
# Test	                  Input	                           Result
# print_file("app.log")     sin_alpha = 0.5                  INFO:root:A value has been entered sin(alpha) = 0.5
#                           cos_alpha = math.sqrt(3) / 2     INFO:root:A value has been entered cos(alpha) = 0.8660254037844386
#                                                            DEBUG:root:The value of the tangent of the angle alpha is found = 0.5773502691896258
#                           sin_alpha = 0.5                  INFO:root:A value has been entered sin(alpha) = 0.5
#                           cos_alpha = 'w'                  INFO:root:A value has been entered cos(alpha) = w
#                                                            CRITICAL:root:The tangent of the angle alpha is not defined.
#                           sin_alpha = 0.5                  INFO:root:A value has been entered sin(alpha) = 0.5
#                           cos_alpha = 0                    INFO:root:A value has been entered cos(alpha) = 0
#                                                            WARNING:root:The cosine of the angle alpha = 0. The tangent is not defined.

import math
import logging

logging.basicConfig(filename='app.log', filemode="w", format='%(levelname)s:%(name)s:%(message)s', level=logging.DEBUG)

def findingTangent(sin_alpha, cos_alpha):
    logging.info(f"A value has been entered sin(alpha) = {sin_alpha}")
    logging.info(f"A value has been entered cos(alpha) = {cos_alpha}")
    if type(sin_alpha) not in [int, float] or type(cos_alpha) not in [int, float]:
        logging.critical("The tangent of the angle alpha is not defined.")
    elif cos_alpha == 0:
        logging.warning("The cosine of the angle alpha = 0. The tangent is not defined.")
    else:
        tan_alpha = sin_alpha/cos_alpha
        logging.debug(f"The value of the tangent of the angle alpha is found = {tan_alpha}")

findingTangent(0.5, math.sqrt(3) / 2)
findingTangent(0.5, 'w')
findingTangent(0.5, 0)

