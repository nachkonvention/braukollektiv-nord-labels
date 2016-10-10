from escpos import printer

p = printer.File("/dev/usb/lp0")

p.set(align="center", width=2)
p.text("\n")
p.text("Braukollektiv\n")
p.text("Nord")
p.text("\n")
p.text("\n")
p.text("\n")
p.image("/home/nachkonvention/food.jpg")
p.text("\n")
p.text("\n")
p.text("Corn On The Hop")
p.text("\n")
p.text("Pale Ale")
p.cut()
