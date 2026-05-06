class Settings:
    """Клас для збереження всіх налаштувань гри."""

    def __init__(self):
        """Ініціалізація постійних налаштувань гри."""
        # Screen settings
        self.screen_width = 1200
        self.screen_heiht = 800
        self.bg_color = (230, 230, 230)

        # Налаштування корабля
        self.ship_limit = 3

        # Налаштуваненя кулі
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color =(60, 60, 60)
        self.bullets_allowed = 5

        # Налаштування прибульця
        self.fleet_drop_speed = 10
        self.fleet_direction = 1

        # Як швидкодко гра має прискорюватися
        self.speedup_scale = 1.1

        # Як швидко збільшується вартість прибульців
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    
    def initialize_dynamic_settings(self):
        """Ініцілазація змінних налаштувань."""
        self.ship_speed = 0.8
        self.bullet_speed = 1.6
        self.alien_speed = 0.4
        
        # fleet_direction 1 - праворуч, -1 - ліворуч.
        self.fleet_direction = 1
    
        # Отримання балів
        self.alien_points = 50
    
    
    def increse_speed(self):
        """Збільшити налаштування швидкості та вартості прибульців."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)