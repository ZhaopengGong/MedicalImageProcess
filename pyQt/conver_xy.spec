# -*- mode: python -*-

block_cipher = None


a = Analysis(['F:\\workspace\\pycharm\\convert_xy_coordinate\\TestConver_xy.py'],
             pathex=['F:\\workspace\\pycharm\\convert_xy_coordinate'],
             binaries=[],
             datas=[('conver_xy.ui', 'ConvertCoordinateWindow.py', 'ConvertCoordinateWorkThread.py', 'conver_xy.py')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='conver_xy',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False )
