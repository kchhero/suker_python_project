# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['srimMain.py'],
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
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='srimMain',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False )
