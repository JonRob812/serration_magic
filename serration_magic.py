import math
import os

# TODO add Femco to the party - post file?


class Serrate:
    def __init__(self, part_no, program_number, work_offset, tool_number, b, x_center, y_center, z_top, depth,
                 clearance, start_diam, end_diam, pitch, feed_rate, directory):
        self.part_no = part_no
        self.program_number = program_number
        self.work_offset = work_offset
        self.tool_number = tool_number
        self.b = b
        self.x_center = x_center
        self.y_center = y_center
        self.z_top = z_top
        self.depth = depth
        self.clearance = .1
        self.start_diam = start_diam
        self.end_diam = end_diam
        self.pitch = pitch
        self.feed_rate = feed_rate
        self.directory = directory
        self.file_name = self.directory + '/' + self.part_no + ' Serration.NC'
        self.max_feed = 120.

    def magic(self):
        # start magic
        program_number = str(self.program_number).zfill(4)

        pgm_comment = self.part_no + ' SERRATE'
        b = float(self.b)

        start_diam = self.start_diam + 2 * self.pitch
        end_diam = self.end_diam - 2 * self.pitch
        revolutions = math.ceil(((start_diam - end_diam) / 2) / self.pitch)
        x_left = round(self.x_center - (start_diam / 2), 4)
        x_right = round(self.x_center + (start_diam / 2), 4)
        plunge_feed = round((self.clearance + self.depth) * 2, 2)

        code = open(self.file_name, 'w+')

        code.write(f'%\nO{program_number}( {pgm_comment} )\n' 
                   '( THIS CODE BROUGHT TO YOU BY - SERRATION MAGIC )\n' 
                   f'( START DIAM - {self.start_diam} )\n' 
                   f'( END DIAM - {self.end_diam} )\n'
                   f'( PITCH - {self.pitch} )\n'
                   f'( CENTER POINT - X{self.x_center} )\n'
                   f'( CENTER POINT - Y{self.y_center} )\n'
                   f'( CENTER POINT - Z{self.z_top} )\n'
                   f'( FEED RATE - {self.feed_rate} ) \n'
                   'G0 G17 G20 G40 G49 G80 G90\n'
                   'M17\n' 
                   f'G90 B{b:.1f}\n' 
                   f'M18\nG00 G90 G{self.work_offset} M03 S3' 
                   f' X{x_left} Y{self.y_center}\n' 
                   'W0.\n' 
                   f'G43 H{self.tool_number} Z{self.z_top + 2.}\n' 
                   'M19\n' 
                   f'G00 Z{round(self.z_top + self.clearance, 4)}\n'
                   f'G95 F{round(start_diam * math.pi, 2)}\n'
                   f'G01 Z{self.z_top - self.depth} M03 S3 F{plunge_feed}\n' 
                   'M49\n'
                   )

        for rev in range(revolutions):
            x_1 = round(x_right - (rev * self.pitch), 4)
            i_1 = round((start_diam - ((2 * self.pitch) * rev)) / 2, 4)
            x_2 = round(x_left + self.pitch + (rev * self.pitch), 4)
            i_2 = round((((2 * self.pitch) * rev) - start_diam + self.pitch) / 2, 4)
            f_1 = round(((start_diam - (rev * (2 * self.pitch))) * math.pi), 2)
            f_2 = round((((start_diam - self.pitch) - (rev * (2 * self.pitch))) * math.pi), 2)
            s_1 = math.ceil(self.feed_rate / ((start_diam - (rev * (2 * self.pitch))) * math.pi))
            s_2 = math.ceil(self.feed_rate / (((start_diam - self.pitch) - (rev * (2 * self.pitch))) * math.pi))
            if s_1 * f_1 > self.max_feed:
                s_1 = s_1 - 1
            if s_2 * f_2 > self.max_feed:
                s_2 = s_2 - 1

            if rev == 0:
                code.write(f'G02 X{x_1} I{i_1} J0. M03 S{s_1} F{f_1} ( {rev + 1} OF {revolutions} )\n')
            else:
                code.write(f'G02 X{x_1} I{i_1} J0. S{s_1} F{f_1} ( {rev + 1} OF {revolutions} )\n')
            code.write(f'G02 X{x_2} I{i_2} J0. S{s_2} F{f_2}\n')

        code.write('S0\n' 
                   f'G00 Z{round(self.z_top + self.clearance, 4)}\n' 
                   'M5\n' 
                   'M48\nM78\nG94\n' 
                   'G91 G28 Z0. M9\n' 
                   'G91 G28 W0.\n'
                   'M30\n'
                   '( WITH LOVE - JON ROB )\n' 
                   '%')

        code.close()
        os.startfile(self.file_name)
