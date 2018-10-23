// This file was auto-generated. Do not edit it!

let game = null;

let config = {
    scene: [load, stage]
};

update_game_config(config);

document.title = config.game_name;

window.onload = function() {
    game = new Phaser.Game(config);
};
