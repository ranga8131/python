# Module - A file containing code you want to include in your program.
#           Use 'import' to include a module (built-in or your own).
#               Useful to break up a large program reusable separate files.

import ex_modules as m

radius = int(input("Enter the radius: "))
height = int(input("Enter the height: "))

surf_area = m.surface_area(radius,height)
print(surf_area)
  
            