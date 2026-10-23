# -*- coding: utf-8 -*-

# 小龙智脑 (XiaoLong Brain) - 全新原创项目

# 作者 / 版权人: 小龙 (XiaoLong)

# License: MIT。本项目所有代码均为原创，保留署名即可自由使用。



import json

import os

import time

import hashlib





class JsonCache:

    def __init__(self, path="./xiaolong_cache.json", ttl=3600):

        self.path = path

        self.ttl = ttl

        self.store = self._load()



    def _load(self):

        if os.path.exists(self.path):

            try:

                with open(self.path, "r", encoding="utf-8") as f:

                    return json.load(f)

            except Exception:

                return {}

        return {}



    def _save(self):

        with open(self.path, "w", encoding="utf-8") as f:

            json.dump(self.store, f, ensure_ascii=False)



    def get(self, key):

        item = self.store.get(key)

        if not item:

            return None

        if self.ttl > 0 and time.time() - item["t"] > self.ttl:

            return None

        return item["v"]



    def set(self, key, value):

        self.store[key] = {"t": time.time(), "v": value}

        self._save()



    @staticmethod

    def key(*parts):

        return hashlib.md5("|".join(str(p) for p in parts).encode("utf-8")).hexdigest()

