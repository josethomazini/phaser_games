let game = null;

let config = {
    scene: {{ scene_list }}
};

update_game_config(config);

set_title();

window.onload = function() {
    game = new Phaser.Game(config);
};
