from cx_Freeze import setup, Executable

target = Executable(
    script="snakeGame.py",
    icon="iconeGame.ico"
    )

setup(
    name="SnakeGame",
    version="1.0",
    description="Jogo para fins de estudo",
    author="Vinícius Sarmento Costa Siqueira",
    options={"build_exe": {'packages':['pygame'],
                            'include_files':['musica']
                           }},
    executables=[target]
    )