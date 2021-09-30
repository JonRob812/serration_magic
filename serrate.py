from serration_magic import *

# Serrate('A54951', 4951, 54, 19, 0, -17.5, 0, 26.5, .006, .1, 18.5, 15, .018, 100,
#         'F:\\CNC DATA\\Posted Code\\Serration Magic').magic()
#
# Serrate('B-204524196', 4196, 54, 19, 180, 17.5, 0, 36.75, .006, .1, 21, 17, .018, 100,
#         'F:\\CNC DATA\\Posted Code\\Serration Magic').magic()

Serrate(part_no='D7232',
        program_number=150,
        work_offset=54,
        tool_number=19,
        b=0,
        x_center=0,
        y_center=0,
        z_top=24.19,
        depth=.003,
        clearance=.1,
        start_diam=8.5,
        end_diam=5.6,
        pitch=1/32,
        feed_rate=100,
        directory='.').magic()