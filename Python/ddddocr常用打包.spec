# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['run.py'],
    pathex=['.\\venv\\Lib\\site-package'],
    binaries=[],
    datas=[('C:\\Users\\User\\PycharmProjects\\專案名稱\\venv\\Lib\\site-packages\\onnxruntime\\capi\\onnxruntime_providers_shared.dll','onnxruntime\\capi'),('C:\\Users\\User\\PycharmProjects\\專案名稱\\venv\\Lib\\site-packages\\ddddocr','ddddocr')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='專案名稱',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='main',
)
