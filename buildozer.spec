[app]

title = Jarvis

package.name = jarvis

package.domain = org.test

source.dir = .

source.include_exts = py,png,jpg,kv,atlas

version = 1.0

requirements = python3,kivy

orientation = portrait

fullscreen = 0

android.permissions = INTERNET

android.api = 33

android.minapi = 21

android.ndk = 25b

p4a.branch = stable

p4a.bootstrap = sdl2

android.accept_sdk_license = True

android.skip_update = True

android.sdk_path = /usr/local/lib/android/sdk


[buildozer]

log_level = 2

warn_on_root = 1
