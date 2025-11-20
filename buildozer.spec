[app]

# Nazwa aplikacji
title = LottoApp
package.name = lottoapp
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,txt
version = 1.0
requirements = python3,kivy
orientation = portrait
icon.filename = icon.png

# Foldery do uwzględnienia w APK
source.include_patterns = css/*,python/*

# Opcje Buildozera
android.api = 31
android.minapi = 21
android.arch = arm64-v8a,armeabi-v7a
android.sdk = 31
android.ndk = 25b
android.bootstrap = sdl2
