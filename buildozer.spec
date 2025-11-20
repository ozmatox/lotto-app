[app]
title = LottoApp
package.name = lottoapp
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,txt
source.include_patterns = css/*,python/*
version = 1.0
requirements = python3,kivy
orientation = portrait
icon.filename = icon.png

# Android
p4a.bootstrap = sdl2
android.archs = arm64-v8a,armeabi-v7a
android.api = 31
android.minapi = 21
android.ndk = 25b
