project('secret-knowledge',
  version: '2.0.0',
  meson_version: '>= 0.59.0',
)

i18n = import('i18n')
python = import('python')

# Subdirectories
subdir('po')
subdir('data')
subdir('src')

gnome = import('gnome')
gnome.post_install(
  gtk_update_icon_cache: true,
  update_desktop_database: true,
)
