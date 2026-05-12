import random


class Character:
    """Base class for all characters in the game."""

    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.max_health = health          # Track max health for heal cap
        self.attack_power = attack_power

    def attack(self, opponent):
        """Deal randomized damage within ±5 of base attack_power."""
        damage = random.randint(self.attack_power - 5, self.attack_power + 5)
        opponent.health -= damage
        print(f"\n⚔️  {self.name} attacks {opponent.name} for {damage} damage!")

    def display_stats(self):
        """Show current health and attack power."""
        print(f"{self.name}  |  HP: {self.health}/{self.max_health}  |  ATK: {self.attack_power}")

    def heal(self):
        """Restore 15-25 HP without exceeding max health."""
        heal_amount = random.randint(15, 25)
        old_health = self.health
        self.health = min(self.health + heal_amount, self.max_health)
        actual_heal = self.health - old_health
        print(f"\n💚 {self.name} heals for {actual_heal} HP! ({self.health}/{self.max_health})")


class Warrior(Character):
    """Sturdy melee fighter with a powerful swing and a shield."""

    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)
        self.shield_active = False        # Tracks Shield Wall status

    def power_attack(self, opponent):
        """Heavy swing that deals 1.5× base damage."""
        damage = random.randint(
            int(self.attack_power * 1.3),
            int(self.attack_power * 1.7)
        )
        opponent.health -= damage
        print(f"\n🗡️  {self.name} unleashes a POWER ATTACK on {opponent.name} for {damage} damage!")

    def shield_wall(self):
        """Raise a shield that blocks the next incoming attack."""
        self.shield_active = True
        print(f"\n🛡️  {self.name} raises a mighty Shield Wall! The next attack will be blocked.")

    def special_abilities(self, opponent):
        """Menu for Warrior-specific abilities."""
        print("\n--- Warrior Abilities ---")
        print("1. Power Attack  (1.5× damage)")
        print("2. Shield Wall   (block next attack)")
        choice = input("Choose ability (1-2): ").strip()
        if choice == "1":
            self.power_attack(opponent)
        elif choice == "2":
            self.shield_wall()
        else:
            print("Invalid choice. Performing a basic attack instead.")
            self.attack(opponent)


class Mage(Character):
    """Glass cannon who wields devastating spells."""

    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)

    def cast_spell(self, opponent):
        """Cast a spell dealing 1.5-2× base damage."""
        damage = random.randint(
            int(self.attack_power * 1.5),
            int(self.attack_power * 2.0)
        )
        opponent.health -= damage
        print(f"\n🔥 {self.name} casts a devastating spell on {opponent.name} for {damage} damage!")

    def magic_barrier(self):
        """Conjure a barrier that restores some health."""
        heal_amount = random.randint(20, 35)
        old_health = self.health
        self.health = min(self.health + heal_amount, self.max_health)
        actual = self.health - old_health
        print(f"\n🔮 {self.name} conjures a Magic Barrier, restoring {actual} HP! ({self.health}/{self.max_health})")

    def special_abilities(self, opponent):
        """Menu for Mage-specific abilities."""
        print("\n--- Mage Abilities ---")
        print("1. Cast Spell     (heavy magic damage)")
        print("2. Magic Barrier  (restore health)")
        choice = input("Choose ability (1-2): ").strip()
        if choice == "1":
            self.cast_spell(opponent)
        elif choice == "2":
            self.magic_barrier()
        else:
            print("Invalid choice. Performing a basic attack instead.")
            self.attack(opponent)


class Archer(Character):
    """Agile ranged fighter with evasion and rapid shots."""

    def __init__(self, name):
        super().__init__(name, health=110, attack_power=30)
        self.evade_active = False         # Tracks Evade status

    def quick_shot(self, opponent):
        """Fire two quick arrows in rapid succession (double attack)."""
        total_damage = 0
        for i in range(2):
            damage = random.randint(self.attack_power - 5, self.attack_power + 5)
            total_damage += damage
        opponent.health -= total_damage
        print(f"\n🏹 {self.name} fires a QUICK SHOT at {opponent.name}!")
        print(f"   Arrow 1 + Arrow 2 = {total_damage} total damage!")

    def evade(self):
        """Prepare to dodge the next incoming attack entirely."""
        self.evade_active = True
        print(f"\n💨 {self.name} prepares to Evade! The next attack will miss entirely.")

    def special_abilities(self, opponent):
        """Menu for Archer-specific abilities."""
        print("\n--- Archer Abilities ---")
        print("1. Quick Shot  (fire two arrows)")
        print("2. Evade       (dodge next attack)")
        choice = input("Choose ability (1-2): ").strip()
        if choice == "1":
            self.quick_shot(opponent)
        elif choice == "2":
            self.evade()
        else:
            print("Invalid choice. Performing a basic attack instead.")
            self.attack(opponent)


class Paladin(Character):
    """Holy knight with divine power and resilience."""

    def __init__(self, name):
        super().__init__(name, health=150, attack_power=20)
        self.divine_shield_active = False  # Tracks Divine Shield status

    def holy_strike(self, opponent):
        """Smite the enemy with divine power for bonus damage."""
        bonus = random.randint(15, 30)
        damage = random.randint(self.attack_power - 3, self.attack_power + 3) + bonus
        opponent.health -= damage
        print(f"\n✝️  {self.name} delivers a HOLY STRIKE on {opponent.name} for {damage} damage!")

    def divine_shield(self):
        """Invoke a divine shield that blocks the next attack completely."""
        self.divine_shield_active = True
        print(f"\n🌟 {self.name} raises a Divine Shield! The next attack will be fully blocked.")

    def special_abilities(self, opponent):
        """Menu for Paladin-specific abilities."""
        print("\n--- Paladin Abilities ---")
        print("1. Holy Strike    (bonus divine damage)")
        print("2. Divine Shield  (block next attack)")
        choice = input("Choose ability (1-2): ").strip()
        if choice == "1":
            self.holy_strike(opponent)
        elif choice == "2":
            self.divine_shield()
        else:
            print("Invalid choice. Performing a basic attack instead.")
            self.attack(opponent)


class EvilWizard(Character):
    """The final boss. Regenerates health and has random special attacks."""

    def __init__(self, name):
        super().__init__(name, health=200, attack_power=25)

    def regenerate(self):
        """Regenerate 5-15 HP each turn (cannot exceed max)."""
        regen = random.randint(5, 15)
        old = self.health
        self.health = min(self.health + regen, self.max_health)
        actual = self.health - old
        if actual > 0:
            print(f"\n🧙 {self.name} regenerates {actual} HP! ({self.health}/{self.max_health})")

    def wizard_attack(self, opponent):
        """Choose a random attack: normal, Fireball, Lightning, or Summon Minion."""
        roll = random.randint(1, 100)

        # Check if the player can block/evade
        blocked = False
        if hasattr(opponent, 'shield_active') and opponent.shield_active:
            opponent.shield_active = False
            blocked = True
        elif hasattr(opponent, 'evade_active') and opponent.evade_active:
            opponent.evade_active = False
            blocked = True
        elif hasattr(opponent, 'divine_shield_active') and opponent.divine_shield_active:
            opponent.divine_shield_active = False
            blocked = True

        if blocked:
            print(f"\n🛡️  {opponent.name} blocks/evades the wizard's attack! No damage taken.")
            return

        if roll <= 40:
            # Normal attack, 40% chance
            damage = random.randint(self.attack_power - 5, self.attack_power + 5)
            opponent.health -= damage
            print(f"\n🧙 {self.name} strikes {opponent.name} for {damage} damage!")

        elif roll <= 65:
            # Fireball, 25% chance, high damage
            damage = random.randint(self.attack_power + 5, self.attack_power + 20)
            opponent.health -= damage
            print(f"\n🔥 {self.name} hurls a FIREBALL at {opponent.name} for {damage} damage!")

        elif roll <= 85:
            # Lightning Bolt, 20% chance, moderate damage
            damage = random.randint(self.attack_power, self.attack_power + 10)
            opponent.health -= damage
            print(f"\n⚡ {self.name} calls down LIGHTNING on {opponent.name} for {damage} damage!")

        else:
            # Summon Minion, 15% chance, minion attacks then wizard attacks
            minion_damage = random.randint(10, 20)
            wizard_damage = random.randint(self.attack_power - 8, self.attack_power - 3)
            total = minion_damage + wizard_damage
            opponent.health -= total
            print(f"\n👹 {self.name} summons a MINION!")
            print(f"   Minion attacks for {minion_damage} damage!")
            print(f"   {self.name} also attacks for {wizard_damage} damage!")
            print(f"   Total damage: {total}!")


def create_character():
    """Let the player choose a class and name their hero."""
    print("\n╔══════════════════════════════════╗")
    print("║       CHOOSE YOUR CLASS          ║")
    print("╠══════════════════════════════════╣")
    print("║  1. Warrior  (HP:140  ATK:25)    ║")
    print("║  2. Mage     (HP:100  ATK:35)    ║")
    print("║  3. Archer   (HP:110  ATK:30)    ║")
    print("║  4. Paladin  (HP:150  ATK:20)    ║")
    print("╚══════════════════════════════════╝")

    while True:
        choice = input("\nEnter class number (1-4): ").strip()
        if choice in ("1", "2", "3", "4"):
            break
        print("Invalid choice. Please enter 1, 2, 3, or 4.")

    name = input("Enter your character's name: ").strip()
    if not name:
        name = "Hero"

    if choice == "1":
        return Warrior(name)
    elif choice == "2":
        return Mage(name)
    elif choice == "3":
        return Archer(name)
    else:
        return Paladin(name)


def battle(player, wizard):
    """Main turn-based battle loop between the player and the Evil Wizard."""

    turn = 1

    while player.health > 0 and wizard.health > 0:
        print("\n" + "=" * 50)
        print(f"  TURN {turn}")
        print("=" * 50)

        # Display both combatants' stats
        player.display_stats()
        wizard.display_stats()

        # Player turn
        print("\n--- Your Turn ---")
        print("1. Basic Attack")
        print("2. Special Ability")
        print("3. Heal")

        action = input("Choose action (1-3): ").strip()

        if action == "1":
            player.attack(wizard)
        elif action == "2":
            player.special_abilities(wizard)
        elif action == "3":
            player.heal()
        else:
            print("Invalid choice. You hesitate and lose your turn!")

        # Check if the wizard is defeated after the player's action
        if wizard.health <= 0:
            break

        # Evil Wizard turn
        print("\n--- Evil Wizard's Turn ---")

        # Wizard regenerates health each turn
        wizard.regenerate()

        # Wizard performs a random attack
        wizard.wizard_attack(player)

        # Check if the player is defeated
        if player.health <= 0:
            break

        turn += 1

    # End-of-battle messages
    print("\n" + "=" * 50)

    if wizard.health <= 0:
        print("🎉🎉🎉  VICTORY!  🎉🎉🎉")
        print(f"{player.name} has defeated {wizard.name}!")
        print(f"You survived with {player.health}/{player.max_health} HP.")
        print("The realm is saved, for now...")
    else:
        print("💀💀💀  DEFEAT  💀💀💀")
        print(f"{wizard.name} has vanquished {player.name}...")
        print("Darkness spreads across the land.")

    print("=" * 50)


def main():
    """Start the game."""
    print("\n" + "=" * 50)
    print("  ⚔️  EVIL WIZARD BATTLE  ⚔️")
    print("  Defeat the Evil Wizard to save the realm!")
    print("=" * 50)

    # Create the player character
    player = create_character()
    print(f"\nWelcome, {player.name} the {type(player).__name__}!")

    # Create the Evil Wizard boss
    wizard = EvilWizard("The Dark Sorcerer")
    print(f"Your enemy: {wizard.name} (HP: {wizard.health}, ATK: {wizard.attack_power})")
    print("\nPrepare for battle!\n")

    # Start the battle
    battle(player, wizard)

    # Play again prompt
    again = input("\nPlay again? (y/n): ").strip().lower()
    if again == "y":
        main()
    else:
        print("Thanks for playing! Farewell, brave hero. 👋")


if __name__ == "__main__":
    main()
