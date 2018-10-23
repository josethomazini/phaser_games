let G = {};

function load_images(scene) {{{ load_images }}
}

function load_spritesheets(scene) {{{ load_spritesheets }}
}

function load_audios(scene) {{{ load_audios }}
}

function load_bitmap_font(scene) {{{ load_bitmap_font }}
}

function load_assets(scene) {
    load_images(scene);
    load_spritesheets(scene);
    load_audios(scene);
    load_bitmap_font(scene);
}

function make_animation(scene, name, image, start, end, frame_rate) {
    scene.anims.create({
        key: name,
        frames: scene.anims.generateFrameNumbers(
            image,
            {start: start, end: end}
        ),
        frameRate: frame_rate,
        repeat: -1
    });
}

function make_position(scene, name, image, frame, frame_rate) {
    scene.anims.create({
        key: name,
        frames: [
            {key: image, frame: frame}
        ],
        frameRate: frame_rate
    });
}
