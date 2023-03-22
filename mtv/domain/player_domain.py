from mtv.defs.direction import Direction
from mtv.defs.player import GRAVITY, MAX_JUMP_SPEED, MAX_RUN_SPEED, Player


def update_player(player: Player):
    if player.is_jumping:
        player.vely = -(MAX_JUMP_SPEED)
    player.vely += GRAVITY

    current_y = player.rect.y
    player.rect.left += int(player.velx)
    player.rect.top += int(player.vely)
    player.jump_height += abs(player.rect.y - current_y)

    if player.on_ground:
        _land_player(player)

    if player.at_max_height:
        _drop_player(player)


def draw_player(player: Player):
    player.screen.blit(player.image, player.rect)


def make_player_run(player, direction: Direction):
    if direction == Direction.left:
        player.velx = -(MAX_RUN_SPEED)
    elif direction == Direction.right:
        player.velx = MAX_RUN_SPEED


def stop_player_running(self):
    self.velx = 0


def make_player_jump(self):
    if self.can_jump:
        self.is_jumping = True
        self.can_jump = False
    elif self.can_doublejump:
        self.is_jumping = True
        self.can_doublejump = False
        self.height_when_doublejumped = self.jump_height


def stop_player_jumping(self):
    self.is_jumping = False


def _drop_player(player: Player):
    player.is_jumping = False
    if player.can_jump:
        player.can_jump = False


def _land_player(player):
    player.rect.bottom = player.screen.get_rect().bottom
    player.vely = 0
    player.is_jumping = False
    player.can_doublejump = True
    player.can_jump = True
    player.jump_height = 0
    player.height_when_doublejumped = None
