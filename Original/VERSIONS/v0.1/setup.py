from cx_Freeze import setup,Executable
base ="Win32GUI"
setup(name="A* Pathfinding",
      version='0.3',
      decription="A* Pathfinding",
      executables = [Executable(script="Pathfinding.py",icon="Interface\ICO\Icon.ico",base=base)])
