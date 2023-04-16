from typing import List

from mtv.defs.platform import Platform


# def draw_platform(platform: Platform) -> None:
#     # platform.screen.blit(platform.image, platform.rect)
#     pl


def draw_platforms(platforms: List[Platform]) -> None:
    for platform in platforms:
        platform.draw()
        # draw_platform(platform)

# def update_platform(platform: Platform) -> None:
#     pass


# def update_platforms(platforms: List[Platform]) -> None:
#     for platform in platforms:
#         update_platform(platform)
