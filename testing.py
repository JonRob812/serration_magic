import ezdxf

doc = ezdxf.readfile('tk213.dxf')

msp = doc.modelspace()

circles = msp.query('CIRCLE')

for each in circles.entities:
    print(round(float(each.dxf.radius) * 2, 4))
    print([f"{i:.5f}" for i in each.dxf.center])


# entity query for all LINE entities in modelspace
for e in msp.query('LINE'):
    print_entity(e)




