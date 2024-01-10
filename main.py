from render import AutoPlayRenderer,PlayRenderer
from levels import getLevel

auto = False

if (auto):
    renderer = AutoPlayRenderer()
else:
    renderer = PlayRenderer(getLevel(int(input("what level?: "))))

renderer.mainloop()