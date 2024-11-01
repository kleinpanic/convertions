# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['convertions.py'],
    pathex=[],
    binaries=[],
    datas=[('audiototext.py', '.'), ('exceltocsv.py', '.'), ('mdtabletocsv.py', '.'), ('exceltojson.py', '.'), ('mdtodocx.py', '.'), ('htmltomd.py', '.'), ('htmltopdf.py', '.'), ('mdtohtml.py', '.'), ('mdtopdf.py', '.'), ('mdtoyaml.py', '.'), ('imagetomd.py', '.'), ('jpgstopdf.py', '.'), ('jpgtopng.py', '.'), ('pdftojpg.py', '.'), ('pdftomd.py', '.'), ('csvmerge.py', '.'), ('csvtoexcel.py', '.'), ('csvtojson.py', '.'), ('csvtoyaml.py', '.'), ('docxtomd.py', '.'), ('jsontocsv.py', '.'), ('jsontoexcel.py', '.'), ('jsontoyaml.py', '.'), ('pdftotext.py', '.'), ('pngtojpg.py', '.'), ('texttospeech.py', '.'), ('videotoaudio.py', '.'), ('yamltojson.py', '.'), ('yamltomd.py', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='convertions',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
