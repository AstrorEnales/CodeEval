import sys
import colorsys

def printRgb(r, g, b):
    print('RGB(%s,%s,%s)' % (int(round(r)), int(round(g)), int(round(b))))

lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.replace('\n', '').replace('\r', '')
    if len(line) > 0:
        if line.startswith('#'):
            print('RGB(%s,%s,%s)' % (int(line[1:3], 16), int(line[3:5], 16), int(line[5:7], 16)))
        elif line.startswith('('):
            c, m, y, k = [float(x) for x in line[1:len(line) - 1].split(',')]
            r = 255 * (1 - c) * (1 - k)
            g = 255 * (1 - m) * (1 - k)
            b = 255 * (1 - y) * (1 - k)
            printRgb(r, g, b)
        elif line.startswith('HSL'):
            h, s, l = [float(x) for x in line[4:len(line) - 1].split(',')]
            r, g, b =  colorsys.hls_to_rgb(h / 360.0, l / 100.0, s / 100.0)
            printRgb(r * 255, g * 255, b * 255)
        elif line.startswith('HSV'):
            h, s, v = [float(x) for x in line[4:len(line) - 1].split(',')]
            r, g, b =  colorsys.hsv_to_rgb(h / 360.0, s / 100.0, v / 100.0)
            printRgb(r * 255, g * 255, b * 255)

lines.close()
