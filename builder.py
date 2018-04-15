#!/usr/bin/env python3

import codecs
import hashlib
import os

MAIN_GAME_FILE_NAME = 'game.js'

TEMPLATES_FOLDER = '../templates/'
MAIN_GAME_TEMPLATE = TEMPLATES_FOLDER + MAIN_GAME_FILE_NAME
INDEX_TEMPLATE = TEMPLATES_FOLDER + 'index.html'
BUFFER_SIZE = 65536

JS_FOLDER = 'js/'
STATE_JS_FOLDER = JS_FOLDER + 'state/'
CSS_FOLDER = 'css/'

MAIN_GAME_FILE_PATH = JS_FOLDER + MAIN_GAME_FILE_NAME

class Builder:
    def __init__(self):
        self.hashes = {}
        self._calculate_hashes()
        self._render_main_game()
        self._render_index()

    def _calc_hash_from_file(self, file_name):
        sha1 = hashlib.sha1()
        with open(file_name, 'rb') as f:
            while True:
                data = f.read(BUFFER_SIZE)
                if not data:
                    break
                sha1.update(data)

        calc_hash = sha1.hexdigest()
        self.hashes[file_name] = "{0}".format(calc_hash)

    def _calculate_hashes(self):
        # MAIN GAME
        self._calc_hash_from_file(MAIN_GAME_FILE_PATH)

        # STATES
        for js_file_name in [
            f for f in os.listdir(STATE_JS_FOLDER) if
                os.path.isfile(os.path.join(STATE_JS_FOLDER, f))
        ]:
            state_path = STATE_JS_FOLDER + js_file_name
            self._calc_hash_from_file(state_path)

        # STYLES
        for css_file_name in [
            f for f in os.listdir(CSS_FOLDER) if
                os.path.isfile(os.path.join(CSS_FOLDER, f))
        ]:
            style_path = CSS_FOLDER + css_file_name
            self._calc_hash_from_file(style_path)

    def _set_states_js(self, text):
        scripts = []
        for js_file_name in [
            f for f in os.listdir(STATE_JS_FOLDER) if (
                os.path.isfile(os.path.join(STATE_JS_FOLDER, f))
            )
        ]:
            state_path = STATE_JS_FOLDER + js_file_name
            scripts.append(
                '<script src="' + state_path + '?sha1=' +
                self.hashes[state_path] + '"></script>'
            )
        return text.replace(
            '{{ states_js }}',
            ''.join(scripts)
        )

    def _set_styles(self, text):
        styles = []
        for css_file_name in [
            f for f in os.listdir('css') if
                os.path.isfile(os.path.join('css', f))
        ]:
            style_path = CSS_FOLDER + css_file_name
            styles.append(
                '<link rel="stylesheet" ' +
                'href="' + style_path + '?sha1=' +
                self.hashes[style_path] + '">'
            )
        return text.replace(
            '{{ styles }}',
            ''.join(styles)
        )

    def _set_game_js(self, text):
        return text.replace(
            '{{ game_js }}',
            '<script src="' + MAIN_GAME_FILE_PATH +
                '?sha1=' +
                self.hashes[MAIN_GAME_FILE_PATH] +
                '"></script>'
        )

    def _set_state_list(self, text):
        # load tem que ser o primeiro
        for js_file_name in [
            f for f in os.listdir(STATE_JS_FOLDER) if (
                os.path.isfile(os.path.join(STATE_JS_FOLDER, f))
            )
        ]:
            state_path = STATE_JS_FOLDER + js_file_name
        return text.replace(
            '{{ state_list }}',
            '[load]'
        )

    def _render_main_game(self):
        with codecs.open(MAIN_GAME_TEMPLATE, 'r', 'utf-8') as src:
            with codecs.open(MAIN_GAME_FILE_PATH, 'w', 'utf-8') as dest:
                text = src.read()
                text = self._set_state_list(text)
                dest.write(text)

    def _render_index(self):
        with codecs.open(INDEX_TEMPLATE, 'r', 'utf-8') as src:
            with codecs.open('index.html', 'w', 'utf-8') as dest:
                text = src.read()
                text = self._set_styles(text)
                text = self._set_states_js(text)
                text = self._set_game_js(text)
                dest.write(text)


if __name__ == "__main__":
    Builder()
