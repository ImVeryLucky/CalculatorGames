# Overview
These are some game(s) that I have made during my calclus period.  Coding is slow but it's way better than notetaking C:<br/>
Games with saving require TI84 because saving to TI84 requires TI System module.<br/>

[Real Calculator Game](#real-calculator-game).<br/>
[Calculator Type](#calculator-type).<br/>
## Real Calculator Game
Delve into the world of Los Angelos as a investiagtor, sent to investigate some suspicious happenins at a suspicious apartment. Fight goblins, dinosaurs, and.... kid touchers????? Endless mode is also an option.
### WIP
- Getting the story done :C
- Optimize memory to use only 1 lane instead of 3
- Add a potential inventory system to the amount of armor and weapons the player has.

### Update Logs
<details>
<summary>Alpha Version Update Log</summary>

### Version 0.0.0A
- Game "finished" in its most barebones state.<br /> 
- Players can battle 3 mobs; Dino, Goblin, and Orphan<br />
- Players can access a shop, which sells weapons (Increases attack) and armor (Increases health).
### Version 0.0.1A
- Changed shop from being 0 indexed to 1 indexed
- Added 2 more new mobs (Dino Orphan and Kid Toucher) as bosses that occured upon beating a certain number of enemies ( 7 and 25 respectively )
### Version 0.1.0A
- Added Saving stats (Unable to save names yet)
- Timed delay between inputs to fix some weird bug relating to inputs (It didn't work)
- QOL Shop update where the quantity is asked before buying so people don't spam click the buy button.
   - Bug then appeared where one can buy negative quantities, thus selling and earning infinite gold.
   - Another bug was also found where one can buy more than they're gold allows by an extreme amount.
### Version 0.1.1A
- Nerfed Kid toucher by around 50% in hp.
- Debt collector added when a player's gold is less than 100. It's health stacks exponentially so its nigh unkillable.

</details>

<details>
<summary>Version Update Log</summary>
  
### Version 1.0.0
- Names can now be saved. Thus, full player data is saved and the game I have imagined has been realized
- Fixed the input related bug; it turns out that if a player inputs nothing when a number is expected, python spazzes out
  - Added some code that helped prevent this from happening anywhere in the game.
  - Doing this also happened to fix the bug that allowed players to sell negative quantities of any item.
### Version 1.0.1
- (Temp)Fixed memory overload error (It concurrently returns)
- Optimized some code relating to the input bug.
### Version 1.1.0 ( Peak Update )
- Loading Screen Added
- Shop UI Improved
  - Also removed weird shop formatting for weapons
  - Now index is shown instead of implied
  - Same with Armor Shop Section
- General UI Improved
- Death stops the game and also empties the save file.
  - Long time bug where dying in battle skipped the battle.
### Version 1.1.1 
- New title screen
- New potential gamemode (Story Mode!!!!)
- Fixed bug occurence of memory overload (The fix consists of moving the order in which the modules are imported in the game code. I have no idea why the game runs)
### Version 1.1.2 (11/4/2024)
- White spaced everything
- Combined some input number checking code, and applied it to all other parts of the game.
### Version 1.1.3 (11/22/2024)
- Huge optimization gains, halfing the memory lists (From 6 to 3) used and allowing some to be potentially used in other games.
- Made cool speech bubbles and set the framework for the story.
</details>

## Calculator Type
The (in my mind) better version of Nitro Type. Sentences are now randomly generated to form true typing challenges, and cars have an impact on races.
### WIP
- Add save file potential
- More cars
- More sentence words ( More nouns, adj, adv, verb, etc.)

### Update Logs
<details>
<summary>Alpha Version Update Log</summary>

### Version 0.0.0A
- Game not finished but the mechanics are done.
- Players could "race" and type sentences.
### Version 0.0.1A
- Fixed bug where races ended with one word left.
- Added shop functionality.

</details>
