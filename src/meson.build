python = import('python')
python_installation = python.find_installation('python3', required: true)

# Configure launcher
conf = configuration_data()
conf.set('VERSION', meson.project_version())
conf.set('APP_ID', 'io.hersaintel.secretknowledge')
conf.set('PKGDATADIR', get_option('prefix') / get_option('datadir') / 'secret-knowledge')
conf.set('PYTHON', python_installation.full_path())

configure_file(
  input: 'secret-knowledge.in',
  output: 'secret-knowledge',
  configuration: conf,
  install: true,
  install_dir: get_option('bindir'),
  install_mode: 'rwxr-xr-x',
)

# Install Python package
install_data(
  'secret_knowledge/__init__.py',
  'secret_knowledge/main.py',
  install_dir: python_installation.get_install_dir() / 'secret_knowledge',
)
