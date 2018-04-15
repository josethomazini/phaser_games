let config = {
    type: Phaser.AUTO,
    width: 640,
    height: 360,
    parent: 'phaser-app',
    scenes: {{ state_list }}
};
 
let game = new Phaser.Game(config);