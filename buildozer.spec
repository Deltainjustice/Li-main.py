[app]
# Nom de ton application
title = Matrix Performers
package.name = matrixperformers
package.domain = org.matrix

# Fichiers sources inclus (on renomme ton script en main.py pour qu'il soit le point d'entrée)
source.dir = .
source.include_exts = py,json,txt

# Version
version = 1.0

# Dépendances Python nécessaires pour ton script (par exemple, urllib et standard libs sont intégrées)
requirements = python3

# Orientation de l'écran
orientation = portrait

# Permissions Android si besoin
android.permissions = INTERNET

[buildozer]
log_level = 2
warn_on_root = 1
