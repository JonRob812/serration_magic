import math

tool_radius = .03
pitch = .025


depth = tool_radius - math.sqrt(tool_radius**2 - (pitch / 2)**2)


print(depth)
