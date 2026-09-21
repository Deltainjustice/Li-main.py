[app]
# Nom de l'application affiché sur l'appareil mobile
title = Lilit Station

# Nom du paquet (uniquement des minuscules, sans espaces)
package.name = lilitstation

# Domaine du paquet
package.domain = org.lilit

# Répertoire source contenant ton code (le dossier courant)
source.dir = .

# Extensions de fichiers à inclure dans le paquet
source.include_exts = py,json,txt

# Version de l'application
version = 1.0

# Dépendances requises pour faire tourner l'interface Kivy sur mobile
requirements = python3,kivy

# Orientation de l'écran (portrait recommandé pour cette interface)
orientation = portrait

# Permissions Android nécessaires (accès réseau pour les flux et passerelles)
android.permissions = INTERNET

# Configuration SDK / API Android
android.api = 33
android.min_api = 21
android.accept_sdk_license = True

[buildozer]
# Niveau de log (2 pour avoir le suivi détaillé en cas de besoin)
log_level = 2

# Autoriser l'exécution sous root (nécessaire sur certains environnements CI type GitHub Actions)
warn_on_root = 1
