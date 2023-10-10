# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['smartsheet_bic_open_task_list.py'],
             pathex=['/home/fwarren/builds/smartsheet_bic_open_task_list'],
             binaries=[],
             datas=[
                 ('.env','.'),
             ],
             hiddenimports=[
                 'smartsheet.reports',
                 'emailer.emailer',
             ],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,  
          [],
          name='smartsheet_bic_open_task_list',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
