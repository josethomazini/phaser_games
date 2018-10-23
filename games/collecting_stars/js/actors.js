function Score(scene) {
    this.total = 0;
    this.x = 16;
    this.y = 16;
    this.increment_value = 10;
    this.font_config = {font: '32px Arial', fill: '#000'};


    this.to_str = function() {
        return 'Score: ' + this.total;
    }

    this.text = scene.add.text(
        this.x, this.y, this.to_str(),
        this.font_config
    );

    this.increment = function() {
        this.total += this.increment_value;
        this.text.setText(this.to_str());
    };

    G['score'] = this;
}

function Dude(scene) {
    this.image = 'dude[32][48]';
    this.x = 100;
    this.y = 450;

    this.sprite = scene.physics.add.sprite(this.x, this.y, this.image);

    this.sprite.setBounce(0.2);
    this.sprite.setCollideWorldBounds(true);

    make_animation(scene, 'dude_left', this.image, 0, 3, 10);
    make_animation(scene, 'dude_right', this.image, 5, 8, 10);
    make_position(scene, 'dude_turn', this.image, 4);

    this.dead = function() {
        this.sprite.setTint(0xff0000);
        this.sprite.anims.play('dude_turn');
    };

    this.go_left = function() {
        this.sprite.setVelocityX(-160);
        this.sprite.anims.play('dude_left', true);
    };

    this.go_right = function() {
        this.sprite.setVelocityX(160);
        this.sprite.anims.play('dude_right', true);
    };

    this.stop = function() {
        this.sprite.setVelocityX(0);
        this.sprite.anims.play('dude_turn');
    };

    this.jump = function() {
        if(this.sprite.body.touching.down) {
            this.sprite.setVelocityY(-330);
        }
    };

    G['dude'] = this;
};
