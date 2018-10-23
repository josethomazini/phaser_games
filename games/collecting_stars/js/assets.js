// This file was auto-generated. Do not edit it!

let G = {};

function load_images(scene) {
    scene.load.image('sky', 'image/sky.png');
    scene.load.image('bomb', 'image/bomb.png');
    scene.load.image('platform', 'image/platform.png');
    scene.load.image('star', 'image/star.png');
}

function load_spritesheets(scene) {
    scene.load.spritesheet('dude[32][48]', 'spritesheet/dude[32][48].png', {frameWidth: 32, frameHeight: 48});
}

function load_audios(scene) {
    scene.load.audio('keep', 'audio/keep.temp');
}

function load_bitmap_font(scene) {
    scene.load.bitmapFont('nokia16black', 'font/nokia16black.png', 'font/nokia16black.xml');
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
