if __name__ == '__main__':
    from PyInstaller.__main__ import run
    opts = ['main.py', '-D', '-w', '--hidden-import=queue', '--icon=shuoGG_re.ico']
    run(opts)
