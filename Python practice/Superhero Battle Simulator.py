from collections import deque

class Superhero:
    def __init__(self, name, alias, power_level):
        self.details = (name, alias, power_level)  # Tuple: Immutable superhero details
        self.powers = []  # List: Stores superhero powers
        self.power_levels = {}  # Dictionary: Maps power names to their levels
        self.defeat_bad = set()  # Set: Unique villains defeated
        self.mission_queue = deque()  # Queue: Upcoming missions
        self.battle_history = []  # Stack: Previous battles

    def add_power(self, power, level):
        """Add a new power with its level"""
        self.powers.append(power)
        self.power_levels[power] = level
        print(f"{self.details[1]} gained a new power: {power} (Level {level})")

    def defeat_bad(self, villain):
        """Defeat a bad person and add to defeated list"""
        self.defeated_villains.add(villain)
        self.battle_history.append(f"Defeated {villain}")
        print(f"{self.details[1]} defeated {villain}!")

    def add_mission(self, mission):
        """Add a mission to the queue"""
        self.mission_queue.append(mission)
        print(f"New mission added: {mission}")

    def complete_mission(self):
        """Complete the next mission in queue"""
        if self.mission_queue:
            mission = self.mission_queue.popleft()
            self.battle_history.append(f"Completed mission: {mission}")
            print(f"{self.details[1]} completed mission: {mission}")
        else:
            print("No missions left!")

    def show_status(self):
        """Display superhero's status"""
        print("\n=== Superhero Status ===")
        print(f"Name: {self.details[0]}")
        print(f"Alias: {self.details[1]}")
        print(f"Power Level: {self.details[2]}")
        print(f"Powers: {self.powers}")
        print(f"Power Levels: {self.power_levels}")
        print(f"Defeated Villains: {self.defeated_villains}")
        print(f"Upcoming Missions: {list(self.mission_queue)}")
        print(f"Battle History: {self.battle_history}")
        print("=======================\n")


# 🎮 Example Gameplay
hero = Superhero("Bruce Wayne", "Batman", 90)

hero.add_power("Martial Arts", 80)
hero.add_power("Gadgets", 85)

hero.defeat_bad("Joker")
hero.defeat_bad("Bane")

hero.add_mission("Save Gotham")
hero.add_mission("Stop Bank Robbery")

hero.show_status()

hero.complete_mission()
hero.complete_mission()
hero.complete_mission()  # No missions left

hero.show_status()
