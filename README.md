# Generation-Zero-Save-Editing

# Prerequists:
- A Hex Editor such as [HxD](https://mh-nexus.de/en/downloads.php?product=HxD20).
- The Generation Zero Game from [Steam](https://store.steampowered.com/app/704270/Generation_Zero/).
- Some Hexadecimal and Simple Low-Level Editing Experience. (Since this guide Uses Binary, Hex, & Decimal).

# Notice:
- Save-File Location is Located [Here](https://savegamelocation.online/generation-zero/index.html): **"C:\Users\USERNAME\Documents\Avalanche Studios\GenerationZero\Saves\YOURID\savegame"**.
- Always Make sure you backup your Save-File before continuing with this guide!
- I am not responsible for Corrupted Save-Files, or other Unofficial Edits to Modify your Game.
- I will refer to the [Pansarvärnsgevär 90](https://generation-zero.fandom.com/wiki/Pansarv%C3%A4rnsgev%C3%A4r_90) as the [Pvg 90](https://generation-zero.fandom.com/wiki/Pansarv%C3%A4rnsgev%C3%A4r_90).


# Editing Player Level:
<details>
  <summary>Player Level Edit.</summary>
  
- Open your Generation Zero Save-File "savegame" in [HxD](https://mh-nexus.de/en/downloads.php?product=HxD20) or your Hex Editor of Choice. ([View Image](https://user-images.githubusercontent.com/78656905/228982927-67b49729-3dca-4e5d-9f10-37ad5b75fce6.png)).

- Click "Seach" and then Click "GoTo..." then type in Offset "3AC". A New byte should have been Highlighted at Offset "3AC". ([View Image](https://user-images.githubusercontent.com/78656905/228983914-c74a2576-2786-45eb-a98f-67636b66b86a.png)).

- After Highlighting the Byte at Offset "3AC" Look at The Window To Your Right (Should be Called **Data Inspector** or Something Like That). ([View Image](https://user-images.githubusercontent.com/78656905/228984773-9157f3d9-aa77-41b5-b9e7-e7eedca28049.png)).

- You Want to Double Click the Value to The Right of Int8 in the "Data Inspector" Window. That Can any Number In-between **0 and 31**. ([View Image](https://user-images.githubusercontent.com/78656905/228985277-ff36e9f1-01ea-42c6-937c-5ac0fef1587d.png)).

- I will change my Value From 29 to 30 in this tutorial. After changing the byte, it will turn to a different color. Such as "Red". Press "Ctrl+S" to Save the File.  ([View Image](https://user-images.githubusercontent.com/78656905/228985634-48164763-15c7-41ed-b80c-b69f9a17e6af.png)).

- Startup "Generation Zero" from Steam. You might need to kill an enemy or two to set your EXP to the Correct Amount.

</details>





# Editing Skill Points Level:
<details>
  <summary>Player Skills Edit.</summary>

# Editing Skill Points:
- Open your Generation Zero Save-File "savegame" in [HxD](https://mh-nexus.de/en/downloads.php?product=HxD20) or your Hex Editor of Choice. ([View Image](https://user-images.githubusercontent.com/78656905/228982927-67b49729-3dca-4e5d-9f10-37ad5b75fce6.png)).

- Click "Seach" and then Click "GoTo..." then type in Offset "3A0". A New byte should have been Highlighted at Offset "3A0". ([View Image](https://user-images.githubusercontent.com/78656905/228987409-1dd7c6e6-8e8f-47fc-a8b1-1b27ca9ff201.png)).

- After Highlighting the Byte at Offset "3A0" Look at The Window To Your Right (Should be Called **Data Inspector** or Something Like That). ([View Image](https://user-images.githubusercontent.com/78656905/228988607-dda65ecd-38a9-4e7d-b890-b63ca46eddbd.png)).

- You Want to Double Click the Value to The Right of Int8 in the "Data Inspector" Window. That Can any Number In-between **0 and 87**. ([View Image](https://user-images.githubusercontent.com/78656905/228988287-7d11aa7a-4736-4fc8-935e-19c0f489618a.png)).

- I will change my Value From 86 to 2 in this tutorial. After changing the byte, it will turn to a different color. Such as "Red". Press "Ctrl+S" to Save the File.  ([View Image](https://user-images.githubusercontent.com/78656905/228988392-1f7667c7-6730-4ea8-80ef-572c47e73f3d.png)).

- Startup "Generation Zero" from Steam. You should see the Correct Ammount of Skill Points.

</details>

# Editing Weapon Rarity:
- Before we continue, make sure to check out the [Weapon Item ID's](https://github.com/Cracko298/Generation-Zero-Save-Editing#weapon-item-id-list) to see if Your Item has an ID that we Know. (Otherwise you can't edit it's Rarity).
- In This Tutorial I will be Switching my **Experimental Pvg 90** to the worse **Dilapidated Pvg 90**. (For Demonstration Purposes).






# Weapon Item ID List:
<details>
  <summary>Weapon Item ID's.</summary>

## Pansarvärnsgevär 90
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


## Älgstudsare Hunting Rifle
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


## AI-76 Assault Rifle
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


## Automatgevär 4 Assault Rifle
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

## Automatgevär 5 Assault Rifle
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










## Kvm 59 Machine Gun
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

## Kvm 89 Squad Automatic Weapon
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

</details>
