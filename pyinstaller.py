if __name__ == '__main__':
    from PyInstaller.__main__ import run
    opts = ['main.py', '-F', '-w', '--hidden-import=queue', '--icon=shuoGG_re.ico']
    run(opts)
