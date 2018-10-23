function update_game_config(config) {
    config.backgroundColor = '#2d2d2d';
    config.game_name = 'Collecting Stars';
    config.height = 600;
    config.parent = 'phaser-app';
    config.physics = {
        default: 'arcade',
        arcade: {
            gravity: {
                y: 300
            },
            debug: false
        }
    };
    config.pixelArt = true;
    config.type = Phaser.AUTO;
    config.width = 800;
}
