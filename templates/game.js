let game = null;

let config = {
    scene: {{ scene_list }}
};

update_game_config(config);

document.title = config.game_name;

window.onload = function() {
    game = new Phaser.Game(config);
};
