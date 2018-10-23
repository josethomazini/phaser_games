let stage = new Phaser.Scene('stage');

stage.create = function() {
    this.add.image(400, 300, 'sky');

    G['bombs'] = this.physics.add.group();

    G['stars'] = this.physics.add.group({
        key: 'star',repeat: 11,
        setXY: {x: 12, y: 0, stepX: 70}
    });

    G['stars'].children.iterate(function (child) {
        child.setBounceY(Phaser.Math.FloatBetween(0.4, 0.8));
    });

    G['stage_platforms'] = this.physics.add.staticGroup();
    G['stage_platforms'].create(400, 568, 'platform').setScale(2).refreshBody();
    G['stage_platforms'].create(600, 400, 'platform');
    G['stage_platforms'].create(50, 250, 'platform');
    G['stage_platforms'].create(750, 220, 'platform');

    new Score(this);
    new Dude(this);

    this.cursors = this.input.keyboard.createCursorKeys();

    this.physics.add.collider(
        G['dude'].sprite, G['stage_platforms']);
    this.physics.add.collider(
        G['stars'], G['stage_platforms']);
    this.physics.add.collider(
        G['bombs'], G['stage_platforms']);
    this.physics.add.collider(
        G['dude'].sprite, G['bombs'], bomb_dude_collision, null, this);
    this.physics.add.overlap(
        G['dude'].sprite, G['stars'], dude_star_collision, null, this);
};

stage.update = function() {
    if (this.cursors.left.isDown) {
        G['dude'].go_left();
    } else if (this.cursors.right.isDown) {
        G['dude'].go_right();
    } else {
        G['dude'].stop();
    }

    if (this.cursors.up.isDown) {
        G['dude'].jump();
    }
};

function bomb_dude_collision(player, bomb) {
    stage.physics.pause();
    G['dude'].dead();
};

function dude_star_collision(player, star) {
    star.disableBody(true, true);

    G['score'].increment();

    if (G['stars'].countActive(true) === 0) {
        G['stars'].children.iterate(function (child) {
            child.enableBody(true, child.x, 0, true, true);
        });

        var x = (G['dude'].sprite.x < 400) ?
            Phaser.Math.Between(400, 800) :
            Phaser.Math.Between(0, 400);

        bomb = G['bombs'].create(x, 16, 'bomb');
        bomb.setBounce(1);
        bomb.setCollideWorldBounds(true);
        bomb.setVelocity(Phaser.Math.Between(-200, 200), 20);
        bomb.allowGravity = false;
    }
};
