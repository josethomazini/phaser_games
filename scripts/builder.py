#!/usr/bin/env python3

import codecs
import hashlib
import os

MAIN_GAME_FILE_NAME = 'game.js'
CONFIGS_FILE_NAME = 'configs.js'
ASSETS_FILE_NAME = 'assets.js'
ACTORS_FILE_NAME = 'actors.js'

TEMPLATES_FOLDER = '../../templates/'
MAIN_GAME_TEMPLATE = TEMPLATES_FOLDER + MAIN_GAME_FILE_NAME
ASSETS_TEMPLATE = TEMPLATES_FOLDER + ASSETS_FILE_NAME
INDEX_TEMPLATE = TEMPLATES_FOLDER + 'index.html'
BUFFER_SIZE = 65536

AUDIO_FOLDER = 'audio/'
FONT_FOLDER = 'font/'
IMAGE_FOLDER = 'image/'
SPRITESHEET_FOLDER = 'spritesheet/'
CSS_FOLDER = 'css/'
JS_FOLDER = 'js/'
SCENE_JS_FOLDER = JS_FOLDER + 'scene/'

MAIN_GAME_FILE_PATH = JS_FOLDER + MAIN_GAME_FILE_NAME
CONFIGS_FILE_PATH = JS_FOLDER + CONFIGS_FILE_NAME
ASSETS_FILE_PATH = JS_FOLDER + ASSETS_FILE_NAME
ACTORS_FILE_PATH = JS_FOLDER + ACTORS_FILE_NAME

JS_MSG_DO_NOT_EDIT = '// This file was auto-generated. Do not edit it!\n\n'
HTML_MSG_DO_NOT_EDIT = '<!-- This file was auto-generated. Do not edit it! -->'

class Builder:
    def __init__(self):
        self.hashes = {}

        self._render_main_game()
        self._render_assets()

        self._calculate_hashes()
        self._render_index()

    # ######################################
    # HASH
    # ######################################

    def _calculate_hashes(self):
        # MAIN GAME
        self._calc_hash_from_file(MAIN_GAME_FILE_PATH)

        # CONFIGS
        self._calc_hash_from_file(CONFIGS_FILE_PATH)

        # ASSETS
        self._calc_hash_from_file(ASSETS_FILE_PATH)

        # ASSETS
        self._calc_hash_from_file(ACTORS_FILE_PATH)

        # SCENES
        for js_file_name in [
            f for f in os.listdir(SCENE_JS_FOLDER) if
                os.path.isfile(os.path.join(SCENE_JS_FOLDER, f))
        ]:
            scene_path = SCENE_JS_FOLDER + js_file_name
            self._calc_hash_from_file(scene_path)

        # STYLES
        for css_file_name in [
            f for f in os.listdir(CSS_FOLDER) if
                os.path.isfile(os.path.join(CSS_FOLDER, f))
        ]:
            style_path = CSS_FOLDER + css_file_name
            self._calc_hash_from_file(style_path)

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

    # ######################################
    # RENDERES
    # ######################################

    def _render_main_game(self):
        with codecs.open(MAIN_GAME_TEMPLATE, 'r', 'utf-8') as src:
            with codecs.open(MAIN_GAME_FILE_PATH, 'w', 'utf-8') as dest:
                text = src.read()
                text = self._set_scenes_list(text)
                dest.write(JS_MSG_DO_NOT_EDIT)
                dest.write(text)

    def _render_assets(self):
        with codecs.open(ASSETS_TEMPLATE, 'r', 'utf-8') as src:
            with codecs.open(ASSETS_FILE_PATH, 'w', 'utf-8') as dest:
                text = src.read()
                text = self._set_load_images(text)
                text = self._set_load_spritesheets(text)
                text = self._set_load_audios(text)
                text = self._set_load_bitmap_font(text)
                dest.write(JS_MSG_DO_NOT_EDIT)
                dest.write(text)

    def _render_index(self):
        with codecs.open(INDEX_TEMPLATE, 'r', 'utf-8') as src:
            with codecs.open('index.html', 'w', 'utf-8') as dest:
                text = src.read()
                text = self._set_styles(text)
                text = self._set_scenes_js(text)
                text = self._set_assets_js(text)
                text = self._set_actors_js(text)
                text = self._set_configs_js(text)
                text = self._set_game_js(text)
                dest.write(HTML_MSG_DO_NOT_EDIT)
                dest.write(text)

    # ######################################
    # INDEX.HTML REPLACERS
    # ######################################

    def _set_scenes_js(self, text):
        scripts = []
        for js_file_name in [
            f for f in os.listdir(SCENE_JS_FOLDER) if (
                os.path.isfile(os.path.join(SCENE_JS_FOLDER, f))
            )
        ]:
            scene_path = SCENE_JS_FOLDER + js_file_name
            scripts.append(
                '<script src="' + scene_path + '?sha1=' +
                self.hashes[scene_path] + '"></script>'
            )
        return text.replace(
            '{{ scenes_js }}',
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

    def _set_actors_js(self, text):
        return text.replace(
            '{{ actors_js }}',
            '<script src="' + ACTORS_FILE_PATH +
                '?sha1=' +
                self.hashes[ACTORS_FILE_PATH] +
                '"></script>'
        )

    def _set_assets_js(self, text):
        return text.replace(
            '{{ assets_js }}',
            '<script src="' + ASSETS_FILE_PATH +
                '?sha1=' +
                self.hashes[ASSETS_FILE_PATH] +
                '"></script>'
        )

    def _set_configs_js(self, text):
        return text.replace(
            '{{ configs_js }}',
            '<script src="' + CONFIGS_FILE_PATH +
                '?sha1=' +
                self.hashes[CONFIGS_FILE_PATH] +
                '"></script>'
        )

    # ######################################
    # GAME.JS REPLACERS
    # ######################################

    def _set_scenes_list(self, text):
        classes = ['load']
        for js_file_name in [
            f for f in os.listdir(SCENE_JS_FOLDER) if (
                os.path.isfile(os.path.join(SCENE_JS_FOLDER, f))
            ) if f != 'load.js'
        ]:
            class_name = js_file_name.replace('.js', '')
            classes.append(class_name)

        return text.replace(
            '{{ scene_list }}',
            '[%s]' % ', '.join(classes)
        )

    # ######################################
    # ASSETS.JS REPLACERS
    # ######################################

    def _set_load_images(self, text):
        images = []
        for image_file_name in [
            f for f in os.listdir(IMAGE_FOLDER) if (
                os.path.isfile(os.path.join(IMAGE_FOLDER, f))
            )
        ]:
            image_name = image_file_name[0:image_file_name.rindex('.')]

            statement = "\n    scene.load.image('%s', '%s%s');" % (
                image_name,
                IMAGE_FOLDER,
                image_file_name,
            )
            images.append(statement)

        return text.replace(
            '{{ load_images }}',
            ''.join(images)
        )

    def _set_load_spritesheets(self, text):
        spritesheets = []
        for spritesheet_file_name in [
            f for f in os.listdir(SPRITESHEET_FOLDER) if (
                os.path.isfile(os.path.join(SPRITESHEET_FOLDER, f))
            )
        ]:
            spritesheet_name = spritesheet_file_name[0:spritesheet_file_name.rindex('.')]

            first_opening_bracket = spritesheet_name.index('[')
            last_closing_bracket = spritesheet_name.rindex(']')
            between_brackets = spritesheet_name.index('][')
            width = spritesheet_name[first_opening_bracket + 1:between_brackets]
            height = spritesheet_name[between_brackets + 2:-1]

            statement = "\n    scene.load.spritesheet('%s', '%s%s', {frameWidth: %s, frameHeight: %s});" % (
                spritesheet_name,
                SPRITESHEET_FOLDER,
                spritesheet_file_name,
                width,
                height,
            )
            spritesheets.append(statement)

        return text.replace(
            '{{ load_spritesheets }}',
            ''.join(spritesheets)
        )

    def _set_load_audios(self, text):
        audios = []
        for audio_file_name in [
            f for f in os.listdir(AUDIO_FOLDER) if (
                os.path.isfile(os.path.join(AUDIO_FOLDER, f))
            )
        ]:
            audio_name = audio_file_name[0:audio_file_name.rindex('.')]

            statement = "\n    scene.load.audio('%s', '%s%s');" % (
                audio_name,
                AUDIO_FOLDER,
                audio_file_name,
            )
            audios.append(statement)

        return text.replace(
            '{{ load_audios }}',
            ''.join(audios)
        )

    def _set_load_bitmap_font(self, text):
        png_file_name = None
        xml_file_name = None
        font_name = None

        for font_file_name in [
            f for f in os.listdir(FONT_FOLDER) if (
                os.path.isfile(os.path.join(FONT_FOLDER, f))
            )
        ]:
            if font_file_name.endswith('.png'):
                png_file_name = '%s%s' % (
                    FONT_FOLDER,
                    font_file_name,
                )
                font_name = font_file_name[0:font_file_name.rindex('.')]
            elif font_file_name.endswith('.xml'):
                xml_file_name = '%s%s' % (
                    FONT_FOLDER,
                    font_file_name,
                )

        statement = "\n    scene.load.bitmapFont('%s', '%s', '%s');" % (
            font_name,
            png_file_name,
            xml_file_name,
        )

        return text.replace(
            '{{ load_bitmap_font }}',
            statement
        )


if __name__ == "__main__":
    Builder()
