import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def detect_collision(self, circle_shape):
        '''
        calc distance between circles
        if the distance is <= r1 + r2, then circles are colliding
        '''
        r1 = self.radius
        r2 = circle_shape.radius

        distance = pygame.math.Vector2.distance_to(self.position, circle_shape.position)

        if distance <= r1 + r2:
            b_collide = True
        else:
            b_collide = False
        return b_collide