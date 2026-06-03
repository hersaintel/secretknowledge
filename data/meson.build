# Desktop file
desktop_file = i18n.merge_file(
  input: 'io.github.hersaintel.secretknowledge.desktop.in',
  output: 'io.github.hersaintel.secretknowledge.desktop',
  type: 'desktop',
  po_dir: '../po',
  install: true,
  install_dir: get_option('datadir') / 'applications',
)

# Validate desktop file
desktop_utils = find_program('desktop-file-validate', required: false)
if desktop_utils.found()
  test('Validate desktop file', desktop_utils,
    args: [desktop_file]
  )
endif

# AppStream metainfo
appstream_file = i18n.merge_file(
  input: 'io.github.hersaintel.secretknowledge.metainfo.xml.in',
  output: 'io.github.hersaintel.secretknowledge.metainfo.xml',
  po_dir: '../po',
  install: true,
  install_dir: get_option('datadir') / 'metainfo',
)

# Validate appstream
appstreamcli = find_program('appstreamcli', required: false)
if appstreamcli.found()
  test('Validate appstream file', appstreamcli,
    args: ['validate', '--no-net', '--explain', appstream_file]
  )
endif

# App data directory
install_data(
  'secret-knowledge-v2.html',
  install_dir: get_option('datadir') / 'secret-knowledge' / 'data',
)

# Icons
install_data(
  'io.github.hersaintel.secretknowledge.svg',
  install_dir: get_option('datadir') / 'icons' / 'hicolor' / 'scalable' / 'apps',
)

install_data(
  'io.github.hersaintel.secretknowledge-symbolic.svg',
  install_dir: get_option('datadir') / 'icons' / 'hicolor' / 'symbolic' / 'apps',
)

foreach size : ['16x16', '24x24', '32x32', '48x48', '64x64', '128x128', '256x256']
  install_data(
    '../icons/hicolor' / size / 'apps' / 'io.github.hersaintel.secretknowledge.png',
    install_dir: get_option('datadir') / 'icons' / 'hicolor' / size / 'apps',
  )
endforeach
