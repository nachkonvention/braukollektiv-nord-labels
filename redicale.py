from escpos import printer

p = printer.File("/dev/usb/lp0")

p.set(align="center", width=2)
p.text("\n")
p.text("Braukollektiv\n")
p.text("Nord")
p.text("\n")
p.text("\n")
p.text("\n")
p.image("/home/nachkonvention/favorite.jpg")
p.text("\n")
p.text("\n")
p.text("Redicale")
p.text("\n")
p.text("Red Ale")
p.cut()
