# -*- mode: python ; coding: utf-8 -*-
import sys
sys.setrecursionlimit(5000)
block_cipher = None


a = Analysis(['src\\stockCrawling_window.py'],
             pathex=['D:\\REPOSITORY_MANAGE\\kchhero\\suker_python_project\\sukerStock\\sRIMprj'],
             binaries=[],
             datas=[],
             hiddenimports=["src.stockCrawling_database",
                            "src.stockCrawling_ratio",
                            "src.stockCrawling_snapshot",
                            ],
             hookspath=[],
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
          [],
          exclude_binaries=True,
          name='stockCrawling_window',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='stockCrawling_window')
