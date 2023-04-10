# Starter Content

## Prerequists:
- Some of The Weapon Item ID's where tested and pulled from [Generation Zero (GenZ) Save-Editor](https://github.com/GrimChan/GenZ-Save-File-Editor/blob/c-sharp/Resources/WeaponIDs.csv).
- A Hex Editor such as [HxD](https://mh-nexus.de/en/downloads.php?product=HxD20).
- The Generation Zero Game from [Steam](https://store.steampowered.com/app/704270/Generation_Zero/).
- Some Hexadecimal and Simple Low-Level Editing Experience. (Since this guide Uses Binary, Hex, & Decimal).

## Notice:
- Save-File Location is Located [Here](https://savegamelocation.online/generation-zero/index.html): **"C:\Users\USERNAME\Documents\Avalanche Studios\GenerationZero\Saves\YOURID\savegame"**.
- Always Make sure you backup your Save-File before continuing with this guide!
- I am not responsible for Corrupted Save-Files, or other Unofficial Edits to Modify your Game.
- I will refer to the [Pansarvärnsgevär 90](https://generation-zero.fandom.com/wiki/Pansarv%C3%A4rnsgev%C3%A4r_90) as the [Pvg 90](https://generation-zero.fandom.com/wiki/Pansarv%C3%A4rnsgev%C3%A4r_90).

## WARNING:
### Other Save Slots (Not Including Save-Slot #1).
- **This Guide only works for Save-Slot #1**
- **You are able to follow a similar guide, with Player-Level, EXP, and Skill Points.
- **You'll need to Look at the [Character Offset List]() and Might need to do some Math.





# <ins> Save-Editing Guides </ins>




## Editing Player Level:
<details>
  <summary>*Player Level Edit.</summary>
  
### Editing Player Level:
- Open your Generation Zero Save-File "savegame" in [HxD](https://mh-nexus.de/en/downloads.php?product=HxD20) or your Hex Editor of Choice. ([View Image](https://user-images.githubusercontent.com/78656905/228982927-67b49729-3dca-4e5d-9f10-37ad5b75fce6.png)).

- Click "Seach" and then Click "GoTo..." then type in Offset "3AC". A New byte should have been Highlighted at Offset "3AC". ([View Image](https://user-images.githubusercontent.com/78656905/228983914-c74a2576-2786-45eb-a98f-67636b66b86a.png)).

- After Highlighting the Byte at Offset "3AC" Look at The Window To Your Right (Should be Called **Data Inspector** or Something Like That). ([View Image](https://user-images.githubusercontent.com/78656905/228984773-9157f3d9-aa77-41b5-b9e7-e7eedca28049.png)).

- You Want to Double Click the Value to The Right of Int8 in the "Data Inspector" Window. That Can any Number In-between **0 and 31**. ([View Image](https://user-images.githubusercontent.com/78656905/228985277-ff36e9f1-01ea-42c6-937c-5ac0fef1587d.png)).

- I will change my Value From 29 to 30 in this tutorial. After changing the byte, it will turn to a different color. Such as "Red". Press "Ctrl+S" to Save the File.  ([View Image](https://user-images.githubusercontent.com/78656905/228985634-48164763-15c7-41ed-b80c-b69f9a17e6af.png)).

- Startup "Generation Zero" from Steam. You might need to kill an enemy or two to set your EXP to the Correct Amount.

</details>



## Editing Skill Points Level:
<details>
  <summary>*Player Skills Edit.</summary>

### Editing Skill Points:
- Open your Generation Zero Save-File "savegame" in [HxD](https://mh-nexus.de/en/downloads.php?product=HxD20) or your Hex Editor of Choice. ([View Image](https://user-images.githubusercontent.com/78656905/228982927-67b49729-3dca-4e5d-9f10-37ad5b75fce6.png)).

- Click "Seach" and then Click "GoTo..." then type in Offset "3A0". A New byte should have been Highlighted at Offset "3A0". ([View Image](https://user-images.githubusercontent.com/78656905/228987409-1dd7c6e6-8e8f-47fc-a8b1-1b27ca9ff201.png)).

- After Highlighting the Byte at Offset "3A0" Look at The Window To Your Right (Should be Called **Data Inspector** or Something Like That). ([View Image](https://user-images.githubusercontent.com/78656905/228988607-dda65ecd-38a9-4e7d-b890-b63ca46eddbd.png)).

- You Want to Double Click the Value to The Right of Int8 in the "Data Inspector" Window. That Can any Number In-between **0 and 87**. ([View Image](https://user-images.githubusercontent.com/78656905/228988287-7d11aa7a-4736-4fc8-935e-19c0f489618a.png)).

- I will change my Value From 86 to 2 in this tutorial. After changing the byte, it will turn to a different color. Such as "Red". Press "Ctrl+S" to Save the File.  ([View Image](https://user-images.githubusercontent.com/78656905/228988392-1f7667c7-6730-4ea8-80ef-572c47e73f3d.png)).

- Startup "Generation Zero" from Steam. You should see the Correct Ammount of Skill Points.

</details>


## Editing Weapon Rarity:
<details>
  <summary>*Weapon Rarity/ID Edit.</summary>
  
### Editing Weapon Rarity:
- Before we continue, make sure to check out the [Weapon Item ID's](https://github.com/Cracko298/Generation-Zero-Save-Editing#weapon-item-id-list) to see if Your Item has an ID that we Know. (Otherwise you can't edit it's Rarity ATM).

- Also, make sure that the Weapon is in your Inventory/Hand, and assigned to a slot. (Any of the slots work).

- In This Tutorial I will be Switching my **Experimental Pvg 90** to the worse **Worn Pvg 90**. (For Demo Purposes).

- You'll want to copy the Weapon ID you currently have from the [Weapon Item ID's](https://github.com/Cracko298/Generation-Zero-Save-Editing#weapon-item-id-list) below. (Meaning if you have a Pvg 2-Star, copy that). ([View Image](https://user-images.githubusercontent.com/78656905/228991204-dc74c77c-8c53-4f14-97a8-e592fb9ee028.png)).

- With that ID now copied, head into your preffered Hex Editor (I am using HxD). Press "Ctrl+F" to open up the Search Dialouge, and Click "Integer Number" Tab. ([View Image](https://user-images.githubusercontent.com/78656905/228991732-062b6558-9494-477e-a9ce-700bf30baa18.png)).

- Paste in the Copied Weapon ID, make sure that the "Search Direction" is set to "all",  and Click "Seach All". ([View Image](https://user-images.githubusercontent.com/78656905/228992118-9bf17f41-0d33-4307-b86b-dfd12ad236eb.png)).

- Now, glance down at the bottom for Search Hit(s). You should have roughly **1 to 6** results. Only **1** of the results is your actual weapon. For me, it only has one hit(s). ([View Image](https://user-images.githubusercontent.com/78656905/228992923-57116f10-5b87-499b-94bf-26ebfb286e1a.png)).

- The weapons within an Assigned Slot are normally within the Offset range of 1000 - 2300. Since I only have one hit(s) I'll select that one. ([View Image](https://user-images.githubusercontent.com/78656905/228993639-723d6c8c-a6d2-423c-bafa-89222d393f94.png)).

- Since the found Value is a 4-Byte Integer, We'll edit the "Int32" value, in this case I will replace the Value with the **2-Star Pvg 90** ID. ([View Image](https://user-images.githubusercontent.com/78656905/228995140-c3263ba6-7d84-468d-810e-f6dea998c94b.jpg)).

- Save with "Ctrl+S" and startup "Generation Zero", If you did it correctly, you should see an Increase (or decrease in Rarity).

![image](https://user-images.githubusercontent.com/78656905/228996729-fca4a3e9-7a3e-4edc-96bb-8ee46dd8abd9.png)

</details>








# <ins> Guide-Lists </ins>


## Item ID List:
<details>
  <summary>*Normal Item ID's.</summary>
  
  ### First Aid Packs
  
  <details>
    <summary>Click For "First AID Pack" ID's.</summary>
    
  ### First AID Pack - Item ID's
      
**- "Simple" First Aid Pack: 2050144797**
      
**- "Standard" First Aid Pack: 154430305**
      
**- "Advanced" First Aid Pack: 4135535880**

**- Adrenaline Shot: 3938124543**
      
</details>
  
  ### Deployable Items
  
  <details>
    <summary>Click For "Deployable" ID's.</summary>
    
  ### Deployable Items - Item ID's
  
**- Field Radio ID: 2159829079**

</details>

</details>


## Weapon Item ID List:
<details>
  <summary>*Weapon Item ID's.</summary>

### Pansarvärnsgevär 90
<details>
  <summary>Click For "Pvg 90" ID's.</summary>
  
  ### Pvg 90 - Item ID's
  
**- 1-Star ID: 2727348298**
  
**- 2-Star ID: 1113029778**
  
**- 3-Star ID: 1708071827**
  
**- 4-Star ID: 1940676808**
  
**- 5-Star ID: 1287668466**
  
**- Experimental (6-Star) ID: 1135722230**
</details>


### Älgstudsare Hunting Rifle
<details>
  <summary>Click For "ÄHR" ID's.</summary>
  
  ### ÄHR - Item ID's
  
**- 1-Star ID: 1512823500**
  
**- 2-Star ID: 3797852091**
  
**- 3-Star ID: 1384764071**
  
**- 4-Star ID: 789944801**
  
**- 5-Star ID: 2926162563**
  
**- Experimental (6-Star) ID: No Item ID.**
</details>


### AI-76 Assault Rifle
<details>
  <summary>Click For "AI-76" ID's.</summary>
  
  ### AI-76 - Item ID's
  
**- 1-Star ID: 3528235377**
  
**- 2-Star ID: 4170566388**
  
**- 3-Star ID: 3252499511**
  
**- 4-Star ID: 2593629241**
  
**- 5-Star ID: 2623516647**
  
**- Experimental (6-Star) ID: No Item ID.**
</details>


### Automatgevär 4 Assault Rifle
<details>
  <summary>Click For "AG4" ID's.</summary>
  
  ### AG4 - Item ID's
  
**- 1-Star ID: 2475865089**
  
**- 2-Star ID: 1938816247**
  
**- 3-Star ID: 1564277953**
  
**- 4-Star ID: 1078124586**
  
**- 5-Star ID: 821390159**
  
**- Experimental (6-Star) ID: 1986398252**
</details>

### Automatgevär 5 Assault Rifle
<details>
  <summary>Click For "AG5" ID's.</summary>
  
  ### AG5 - Item ID's
  
**- 1-Star ID: 1858075135**
  
**- 2-Star ID: 4038009463**
  
**- 3-Star ID: 1063891050**
  
**- 4-Star ID: 1628079621**
  
**- 5-Star ID: 3458907921**
  
**- Experimental (6-Star) ID: No Item ID.**
</details>










### Kvm 59 Machine Gun
<details>
  <summary>Click For "Kvm 59" ID's.</summary>
  
  ### Kvm 59 - Item ID's
  
**- 1-Star ID: 1601066909**
  
**- 2-Star ID: 756346513**
  
**- 3-Star ID: 1600997944**
  
**- 4-Star ID: 470978427**
  
**- 5-Star ID: 2318892602**
  
**- Experimental (6-Star) ID: 3823899603**
</details>

### Kvm 89 Squad Automatic Weapon
<details>
  <summary>Click For "Kvm 89" ID's.</summary>
  
  ### Kvm 89 - Item ID's
  
**- 1-Star ID: 862304831**
  
**- 2-Star ID: 3522034483**
  
**- 3-Star ID: 2700579659**
  
**- 4-Star ID: 269593219**
  
**- 5-Star ID: 1115833621**
  
**- Experimental (6-Star) ID: No Item ID.**
</details>

### Granatgevär m/49 Rocket Launcher
<details>
  <summary>Click For "Gng m/49" ID's.</summary>
  
  ### Gng m/49 - Item ID's
  
**- 1-Star ID: 413303018**
  
**- 2-Star ID: 678720182**
  
**- 3-Star ID: 1930252139**
  
**- 4-Star ID: 3849365488**
  
**- 5-Star ID: 1756453791**
  
**- Experimental (6-Star) ID: 2237628567**
</details>



### Meusser Hunting Rifle
<details>
  <summary>Click For "MHR" ID's.</summary>
  
  ### MHR - Item ID's
  
**- 1-Star ID: 2052912546**
  
**- 2-Star ID: 60111070**
  
**- 3-Star ID: 2700874240**
  
**- 4-Star ID: 2214328775**
  
**- 5-Star ID: 345450212**
  
**- Experimental (6-Star) ID: No Item ID.**
</details>

### HP5 Submachine Gun
<details>
  <summary>Click For "HP5" ID's.</summary>
  
  ### HP5 - Item ID's
  
**- 1-Star ID: 3329358393**
  
**- 2-Star ID: 1919634899**
  
**- 3-Star ID: 894785287**
  
**- 4-Star ID: 764274991**
  
**- 5-Star ID: 3995651919**
  
**- Experimental (6-Star) ID: No Item ID.**
</details>

### M/46 "Kpist" SMG Submachine Gun
<details>
  <summary>Click For "Kpist" ID's.</summary>
  
  ### Kpist - Item ID's
  
**- 1-Star ID: 1438049323**
  
**- 2-Star ID: 2562218223**
  
**- 3-Star ID: 471434641**
  
**- 4-Star ID: 3343263738**
  
**- 5-Star ID: 1938906168**
  
**- Experimental (6-Star) ID: 1734102884**
</details>

### Sjöqvist Semi-Auto Shotgun
<details>
  <summary>Click For "Sjöqvist" ID's.</summary>
  
  ### Sjöqvist - Item ID's
  
**- 1-Star ID: 1668043928**
  
**- 2-Star ID: 3944939440**
  
**- 3-Star ID: 3723204762**
  
**- 4-Star ID: 1343436027**
  
**- 5-Star ID: 3777482652**
  
**- Experimental (6-Star) ID: No Item ID.**
</details>

### 12G Pump Action Shotgun
<details>
  <summary>Click For "12G Pump" ID's.</summary>
  
  ### 12G Pump - Item ID's
  
**- 1-Star ID: 3522570570**
  
**- 2-Star ID: 2946942083**
  
**- 3-Star ID: 400886324**
  
**- 4-Star ID: 1211181616**
  
**- 5-Star ID: 2270892881**
  
**- Experimental (6-Star) ID: 1883785329**
</details>

### .44 Magnus Revolver
<details>
  <summary>Click For "Magnus" ID's.</summary>
  
  ### Magnus - Item ID's
  
**- 1-Star ID: 525713563**
  
**- 2-Star ID: 3669591716**
  
**- 3-Star ID: 1539616687**
  
**- 4-Star ID: 3654146736**
  
**- 5-Star ID: 4030765418**
  
**- Experimental (6-Star) ID: No Item ID.**
</details>


### Möller PP Pistol
<details>
  <summary>Click For "Möller" ID's.</summary>
  
  ### Möller - Item ID's
  
**- 1-Star ID: 3055879776**
  
**- 2-Star ID: 2800125862**
  
**- 3-Star ID: 3155991537**
  
**- 4-Star ID: 1225959613**
  
**- 5-Star ID: 358135215**
  
**- Experimental (6-Star) ID: No Item ID.**
</details>





### Klaucke 17 Pistol
<details>
  <summary>Click For "Klaucke" ID's.</summary>
  
  ### Klaucke - Item ID's
  
**- 1-Star ID: 1920462793**
  
**- 2-Star ID: 30913048**
  
**- 3-Star ID: 317912168**
  
**- 4-Star ID: 1158656473**
  
**- 5-Star ID: 1250828800**
  
**- Experimental (6-Star) ID: 2290286314**
</details>







</details>









## Character Offsets
<details>
  <summary>*List of Character Offsets.</summary>
  
  ### Character #2 (Slot #2)
  
  <details>
    <summary>Click For "Character #2 Offsets"</summary>
    
      
**- Player Level Offset: **
      
**- Skill Points Offset:**

**- Gained EXP Offset: **


</details>
  
  ### Deployable Items
  
  <details>
    <summary>Click For "Deployable" ID's.</summary>
    
  ### Deployable Items - Item ID's
  
**- Field Radio ID: 2159829079**

</details>

</details>
