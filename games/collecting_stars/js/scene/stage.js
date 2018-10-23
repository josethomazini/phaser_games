let stage = new Phaser.Scene('stage');

stage.create = function() {
    this.add_sky();
    this.add_platforms();
    this.add_player()
    this.add_stars();
    this.add_bombs();
    this.add_score();
    this.add_cursors();
};

stage.update = function() {
    this.parse_controls();
}

// ############################################################################

stage.add_sky = function() {
    this.add.image(400, 300, 'sky');
}

stage.add_platforms = function() {
    this.platforms = this.physics.add.staticGroup();

    this.platforms.create(400, 568, 'platform').setScale(2).refreshBody();

    this.platforms.create(600, 400, 'platform');
    this.platforms.create(50, 250, 'platform');
    this.platforms.create(750, 220, 'platform');
}

stage.add_player = function() {
    this.player = this.physics.add.sprite(100, 450, 'dude[32][48]');

    this.physics.add.collider(this.player, this.platforms);
    this.player.setBounce(0.2);
    this.player.setCollideWorldBounds(true);

    this.anims.create({
        key: 'left',
        frames: this.anims.generateFrameNumbers(
            'dude[32][48]', { start: 0, end: 3 }
        ),
        frameRate: 10,
        repeat: -1
    });

    this.anims.create({
        key: 'turn',
        frames: [ { key: 'dude[32][48]', frame: 4 } ],
        frameRate: 20
    });

    this.anims.create({
        key: 'right',
        frames: this.anims.generateFrameNumbers(
            'dude[32][48]',
            { start: 5, end: 8 }
        ),
        frameRate: 10,
        repeat: -1
    });
}

stage.add_stars = function() {
    this.stars = this.physics.add.group({
        key: 'star',
        repeat: 11,
        setXY: { x: 12, y: 0, stepX: 70 }
    });

    this.stars.children.iterate(function (child) {

        child.setBounceY(Phaser.Math.FloatBetween(0.4, 0.8));

    });

    this.physics.add.collider(this.stars, this.platforms);

    this.physics.add.overlap(this.player, this.stars, collect_star, null, this);

}

stage.add_bombs = function() {
    this.bombs = this.physics.add.group();

    this.physics.add.collider(this.bombs, this.platforms);

    this.physics.add.collider(this.player, this.bombs, hit_bomb, null, this);
}

stage.add_score = function() {
    this.score = 0;
    this.score_text = this.add.text(
        16, 16, 'Score: 0',
        {font: '32px Arial', fill: '#000'}
    );
}

stage.add_cursors = function() {
    this.cursors = this.input.keyboard.createCursorKeys();
}

stage.parse_controls = function() {
    if (this.cursors.left.isDown)
    {
        this.player.setVelocityX(-160);

        this.player.anims.play('left', true);
    }
    else if (this.cursors.right.isDown)
    {
        this.player.setVelocityX(160);

        this.player.anims.play('right', true);
    }
    else
    {
        this.player.setVelocityX(0);

        this.player.anims.play('turn');
    }

    if (this.cursors.up.isDown && this.player.body.touching.down)
    {
        this.player.setVelocityY(-330);
    }
}

function collect_star(player, star) {
    star.disableBody(true, true);

    stage.score += 10;
    stage.score_text.setText('Score: ' + stage.score);

    if (stage.stars.countActive(true) === 0)
    {
        stage.stars.children.iterate(function (child) {

            child.enableBody(true, child.x, 0, true, true);

        });

        var x = (stage.player.x < 400) ? Phaser.Math.Between(400, 800) : Phaser.Math.Between(0, 400);

        stage.bomb = stage.bombs.create(x, 16, 'bomb');
        stage.bomb.setBounce(1);
        stage.bomb.setCollideWorldBounds(true);
        stage.bomb.setVelocity(Phaser.Math.Between(-200, 200), 20);
        stage.bomb.allowGravity = false;

    }
}

function hit_bomb(player, bomb) {
    this.physics.pause();

    this.player.setTint(0xff0000);

    this.player.anims.play('turn');

    this.game_over = true;
}
