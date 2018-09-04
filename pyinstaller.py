import  os
if __name__ == '__main__':
    from PyInstaller.__main__ import run
    opts=['main.py','-w','--icon=shuoGG_re.ico']
    run(opts)
