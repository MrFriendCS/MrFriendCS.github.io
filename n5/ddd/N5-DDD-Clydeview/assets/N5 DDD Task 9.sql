-- N5 DDD - Task 9

-- Q1
SELECT name, role, mainAbility
    FROM SuperHero
    WHERE role = "Super Hero"
      AND mainAbility = "Acrobatics";


-- Q2
SELECT name, role, mainAbility
    FROM SuperHero
    WHERE role = "Henchman"
      AND mainAbility = "Strength";


-- Q3
SELECT name, role, mainAbility, originOfPower
    FROM SuperHero
    WHERE role = "Super Villain"
      AND mainAbility = "Magic"
      AND originOfPower = "Training";


-- Q4
SELECT name, role, mainAbility, originOfPower
    FROM SuperHero
    WHERE role = "Super Hero"
      AND mainAbility = "Magic"
      AND originOfPower = "Training";


-- Q5
SELECT name, role, ability2, originOfPower
    FROM SuperHero
    WHERE role = "Super Villain"
      AND originOfPower = "Chemicals"
      AND ability2 = "Gadgets";


-- Q6
SELECT name, role, mainAbility
    FROM SuperHero
    WHERE role = "Team member"
      AND mainAbility = "Water breathing";


-- Q7
SELECT name, role, mainAbility, ability2, originOfPower
    FROM SuperHero
    WHERE role = "Super Hero"
      AND mainAbility = "Flight"
      AND ability2 = "Super-strength"
      AND originOfPower = "Technology";


-- Q8
SELECT name, role, mainAbility, ability2
    FROM SuperHero
    WHERE role = "Super Villain"
      AND mainAbility = "Intelligence"
      AND ability2 = "Martial arts";
