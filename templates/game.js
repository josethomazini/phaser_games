let config = {
    type: Phaser.AUTO,
    width: 640,
    height: 360,
    parent: 'phaser-app',
    scene: {{ scene_list }}
};
 
let game = new Phaser.Game(config);