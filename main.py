#!/usr/bin/env python3
import sys
assert sys.version_info >= (3,9), "This script requires at least Python 3.9"
import time

world = {
  "uuid": "43BE2F03-2B10-4885-A6BB-6BFA7BEFBBD8",
  "name": "A Spacedog Named Steve",
  "creator": "Twine",
  "creatorVersion": "2.3.14",
  "schemaName": "Harlowe 3 to JSON",
  "schemaVersion": "0.0.6",
  "createdAtMs": 1631408066557,
  "passages": [
    {
      "name": "KEVIN'S ROOM",
      "tags": "",
      "id": "1",
      "text": "A bit messy like always, with a dog bed on the floor next to the desk and two bookshelves crammed full.\n\n[[LEAVE ->West Hallway]]",
      "links": [
        {
          "linkText": "LEAVE",
          "passageName": "WEST HALLWAY",
          "original": "[[LEAVE ->WEST HALLWAY]]"
        }
      ],
      "hooks": [],
      "cleanText": "A bit messy like always, with a dog bed on the floor next to the desk and two bookshelves crammed full. Paths: Leave"
    },
    {
      "name": "CAFETERIA",
      "tags": "",
      "id": "2",
      "text": "A good place to make puppy dog eyes at the crew until they give you leftovers.\n\n[[Social Room]] \n[[Kitchen]] \n[[LEAVE ->Southern Hallway]]",
      "links": [
        {
          "linkText": "SOCIAL ROOM",
          "passageName": "SOCIAL ROOM",
          "original": "[[SOCIAL ROOM]]"
        },
        {
          "linkText": "KITCHEN",
          "passageName": "KITCHEN",
          "original": "[[KITCHEN]]"
        },
        {
          "linkText": "LEAVE",
          "passageName": "SOUTHERN HALLWAY",
          "original": "[[LEAVE ->SOUTHERN HALLWAY]]"
        }
      ],
      "hooks": [],
      "cleanText": "A good place to make puppy dog eyes at the crew until they give you leftovers. Paths: Social Room, Kitchen, Leave"
    },
    {
      "name": "COCKPIT",
      "tags": "",
      "id": "3",
      "text": "A room with a lot of buttons and lights. Frankie likes to come in here and sit for a long time, I wonder what she does all day.\n\n[[LEAVE ->Northern Hallway]] \n[[SEARCH ->Frankie's Keycard]]",
      "links": [
        {
          "linkText": "LEAVE",
          "passageName": "NORTHERN HALLWAY",
          "original": "[[LEAVE ->NORTHERN HALLWAY]]"
        },
        {
          "linkText": "SEARCH",
          "passageName": "FRANKIE'S KEYCARD",
          "original": "[[SEARCH ->FRANKIE'S KEYCARD]]"
        }
      ],
      "hooks": [],
      "cleanText": "A room with a lot of buttons and lights. Frankie likes to come in here and sit for a long time, I wonder what she does all day. Paths: Search, Leave"
    },
    {
      "name": "CAPTAIN'S QUARTERS",
      "tags": "",
      "id": "4",
      "text": "This is Captain Frankie's room.\n\n[[LEAVE ->West Hallway]]",
      "links": [
        {
          "linkText": "LEAVE",
          "passageName": "WEST HALLWAY",
          "original": "[[LEAVE ->WEST HALLWAY]]"
        }
      ],
      "hooks": [],
      "cleanText": "This is Captain Frankie's room. Paths: Leave"
    },
    {
      "name": "KITCHEN",
      "tags": "",
      "id": "5",
      "text": "The Chef doesn't like it when I come in here.\n\n[[LEAVE ->Cafeteria]] \n[[SEARCH ->Patrick's Keycard]]",
      "links": [
        {
          "linkText": "LEAVE",
          "passageName": "CAFETERIA",
          "original": "[[LEAVE ->CAFETERIA]]"
        },
        {
          "linkText": "SEARCH",
          "passageName": "PATRICK'S KEYCARD",
          "original": "[[SEARCH ->PATRICK'S KEYCARD]]"
        }
      ],
      "hooks": [],
      "cleanText": "The Chef doesn't like it when I come in here. Paths: Search, Leave"
    },
    {
      "name": "EAST HALLWAY",
      "tags": "",
      "id": "6",
      "text": "A hallway on the East side of the ship, leads to the airlock and excercise room.\n\n[[NORTHERN HALLWAY]] \n[[SECURITY ROOM]] \n[[EXERCISE ROOM]] \n[[GALLERY]] \n[[AIRLOCK]] \n[[ELECTRICAL ROOM]] \n[[STORAGE ROOM]] \n[[SOUTHERN HALLWAY]]",
      "links": [
        {
          "linkText": "NORTHERN HALLWAY",
          "passageName": "NORTHERN HALLWAY",
          "original": "[[NORTHERN HALLWAY]]"
        },
        {
          "linkText": "SECURITY ROOM",
          "passageName": "SECURITY ROOM",
          "original": "[[SECURITY ROOM]]"
        },
        {
          "linkText": "EXERCISE ROOM",
          "passageName": "EXERCISE ROOM",
          "original": "[[EXERCISE ROOM]]"
        },
        {
          "linkText": "GALLERY",
          "passageName": "GALLERY",
          "original": "[[GALLERY]]"
        },
        {
          "linkText": "AIRLOCK",
          "passageName": "AIRLOCK",
          "original": "[[AIRLOCK]]"
        },
        {
          "linkText": "ELECTRICAL ROOM",
          "passageName": "ELECTRICAL ROOM",
          "original": "[[ELECTRICAL ROOM]]"
        },
        {
          "linkText": "STORAGE ROOM",
          "passageName": "STORAGE ROOM",
          "original": "[[STORAGE ROOM]]"
        },
        {
          "linkText": "SOUTHERN HALLWAY",
          "passageName": "SOUTHERN HALLWAY",
          "original": "[[SOUTHERN HALLWAY]]"
        }
      ],
      "hooks": [],
      "cleanText": "A hallway on the East side of the ship, leads to the airlock and excercise room. Paths: Northern Hallway, Security Room, Exercise Room, Gallery, Airlock, Electrical Room, Storage, Southern Hallway"
    },
    {
      "name": "AIRLOCK",
      "tags": "",
      "id": "7",
      "text": "Lockers lining the wall each hold a spacesuit and an air tank. One of the lockers is empty.\n\n[[LEAVE ->East Hallway]]",
      "links": [
        {
          "linkText": "LEAVE",
          "passageName": "EAST HALLWAY",
          "original": "[[LEAVE ->EAST HALLWAY]]"
        }
      ],
      "hooks": [],
      "cleanText": "Lockers lining the wall each hold a spacesuit and an air tank. One of the lockers is empty. Paths: Leave"
    },
    {
      "name": "ENGINE ROOM",
      "tags": "",
      "id": "8",
      "text": "A very loud room that Kevin spends a lot of time in.\n\n[[LEAVE ->Southern Hallway]]",
      "links": [
        {
          "linkText": "LEAVE",
          "passageName": "SOUTHERN HALLWAY",
          "original": "[[LEAVE ->SOUTHERN HALLWAY]]"
        }
      ],
      "hooks": [],
      "cleanText": "A very loud room that Kevin spends a lot of time in. Paths: Leave"
    },
    {
      "name": "EXERCISE ROOM,",
      "tags": "",
      "id": "9",
      "text": "Kevin and I go for runs on the moving sidewalks in here. Sometimes Frankie or NAME will play fetch with me if he's busy.\n\n[[LEAVE ->East Hallway]] \n[[SEARCH ->Dog Toys]]",
      "links": [
        {
          "linkText": "LEAVE",
          "passageName": "EAST HALLWAY",
          "original": "[[LEAVE ->EAST HALLWAY]]"
        },
        {
          "linkText": "SEARCH",
          "passageName": "DOG TOYS",
          "original": "[[SEARCH ->DOG TOYS]]"
        }
      ],
      "hooks": [],
      "cleanText": "Kevin and I go for runs on the moving sidewalks in here. Sometimes Frankie or NAME will play fetch with me if he's busy. Paths: Search, Leave"
    },
    {
      "name": "LABORATORY",
      "tags": "",
      "id": "10",
      "text": "Robin spends most of their day in here. It has a bunch of weird equipment and smells.\n\n[[LEAVE ->Northern Hallway]]",
      "links": [
        {
          "linkText": "LEAVE",
          "passageName": "NORTHERN HALLWAY",
          "original": "[[LEAVE ->NORTHERN HALLWAY]]"
        }
      ],
      "hooks": [],
      "cleanText": "Robin spends most of their day in here. It has a bunch of weird equipment and smells. Paths: Leave"
    },
    {
      "name": "MEDICAL ROOM",
      "tags": "",
      "id": "11",
      "text": "It always smells bad in here, kinda like how the chef has been smelling lately. The hurt humans go in here to get better.\n\n[[LEAVE ->Northern Hallway]] \n[[SEARCH ->Robin's Keycard]]",
      "links": [
        {
          "linkText": "LEAVE",
          "passageName": "NORTHERN HALLWAY",
          "original": "[[LEAVE ->NORTHERN HALLWAY]]"
        },
        {
          "linkText": "SEARCH",
          "passageName": "ROBIN'S KEYCARD",
          "original": "[[SEARCH ->ROBIN'S KEYCARD]]"
        }
      ],
      "hooks": [],
      "cleanText": "It always smells bad in here, kinda like how the chef has been smelling lately. The hurt humans go in here to get better. Paths: Search, Leave"
    },
    {
      "name": "CHEF'S ROOM",
      "tags": "",
      "id": "12",
      "text": "The chef doesn't like me in here without Kevin.\n\n[[LEAVE ->West Hallway]] \n[[SEARCH ->Photo Album]]",
      "links": [
        {
          "linkText": "LEAVE",
          "passageName": "WEST HALLWAY",
          "original": "[[LEAVE ->WEST HALLWAY]]"
        },
        {
          "linkText": "SEARCH",
          "passageName": "PHOTO ALBUM",
          "original": "[[SEARCH ->PHOTO ALBUM]]"
        }
      ],
      "hooks": [],
      "cleanText": "The chef doesn't like me in here without Kevin. Paths: Search, Leave"
    },
    {
      "name": "SECURITY ROOM",
      "tags": "",
      "id": "13",
      "text": "Charlie lets me hangout with them in here sometimes. The walls have a bunch of screens showing the different parts of the ship.\n\n[[SEARCH ->Charlie's Keycard]] \n[[LEAVE ->East Hallway]]",
      "links": [
        {
          "linkText": "SEARCH",
          "passageName": "CHARLIE'S KEYCARD",
          "original": "[[SEARCH ->CHARLIE'S KEYCARD]]"
        },
        {
          "linkText": "LEAVE",
          "passageName": "EAST HALLWAY",
          "original": "[[LEAVE ->EAST HALLWAY]]"
        }
      ],
      "hooks": [],
      "cleanText": "Charlie lets me hangout with them in here sometimes. The walls have a bunch of screens showing the different parts of the ship. Paths: Search, Leave"
    },
    {
      "name": "CHARLIE'S ROOM",
      "tags": "",
      "id": "14",
      "text": "This is Charlie's room. They're head of security so they don't usually spend a lot of time in here.\n\n[[LEAVE ->West Hallway]]",
      "links": [
        {
          "linkText": "LEAVE",
          "passageName": "WEST HALLWAY",
          "original": "[[LEAVE ->WEST HALLWAY]]"
        }
      ],
      "hooks": [],
      "cleanText": "This is Charlie's room. They're head of security so they don't usually spend a lot of time in here. Paths: Leave"
    },
    {
      "name": "ROBIN'S ROOM",
      "tags": "",
      "id": "15",
      "text": "This is Robin's room. They have a lot of blueprints, manuals, and tools in here, as well as a stack of notebooks with invention ideas.\n\n[[LEAVE ->West Hallway]] \n[[SEARCH ->Toolkit]]",
      "links": [
        {
          "linkText": "LEAVE",
          "passageName": "WEST HALLWAY",
          "original": "[[LEAVE ->WEST HALLWAY]]"
        },
        {
          "linkText": "SEARCH",
          "passageName": "TOOLKIT",
          "original": "[[SEARCH ->TOOLKIT]]"
        }
      ],
      "hooks": [],
      "cleanText": "This is Robin's room. They have a lot of blueprints, manuals, and tools in here, as well as a stack of notebooks with invention ideas. Paths: Search, Leave"
    },
    {
      "name": "GALLERY",
      "tags": "",
      "id": "16",
      "text": "This is where I can sit and look outside at the small lights. The last time Kevin went out there, he came back different.\n\n[[LEAVE ->East Hallway]] \n[[SEARCH ->Bouquet]]",
      "links": [
        {
          "linkText": "LEAVE",
          "passageName": "EAST HALLWAY",
          "original": "[[LEAVE ->EAST HALLWAY]]"
        },
        {
          "linkText": "SEARCH",
          "passageName": "BOUQUET",
          "original": "[[SEARCH ->BOUQUET]]"
        }
      ],
      "hooks": [],
      "cleanText": "This is where I can sit and look outside at the small lights. The last time Kevin went out there, he came back different. Paths: Search, Leave"
    },
    {
      "name": "STORAGE ROOM",
      "tags": "",
      "id": "17",
      "text": "There are a bunch of boxes of food and other supplies in here.\n\n[[LEAVE ->East Hallway]] \n[[SEARCH ->Box of Carrots]]",
      "links": [
        {
          "linkText": "LEAVE",
          "passageName": "EAST HALLWAY",
          "original": "[[LEAVE ->EAST HALLWAY]]"
        },
        {
          "linkText": "SEARCH",
          "passageName": "BOX OF CARROTS",
          "original": "[[SEARCH ->BOX OF CARROTS]]"
        }
      ],
      "hooks": [],
      "cleanText": "There are a bunch of boxes of food and other supplies in here. Paths: Search, Leave"
    },
    {
      "name": "SOCIAL ROOM",
      "tags": "",
      "id": "18",
      "text": "This is where Kevin and I hang out with the other crewmates when we have free time. I have my own spot on the couch.\n\n[[LEAVE ->Cafeteria]]",
      "links": [
        {
          "linkText": "LEAVE",
          "passageName": "CAFETERIA",
          "original": "[[LEAVE ->CAFETERIA]]"
        }
      ],
      "hooks": [],
      "cleanText": "This is where Kevin and I hang out with the other crewmates when we have free time. I have my own spot on the couch. Paths: Leave"
    },
    {
      "name": "KEVIN",
      "tags": "",
      "id": "19",
      "text": "My owner, Kevin, is sitting in the hallway. Maybe if I bring him a toy or something it'll get his attention.\n\n[[LEAVE ->West Hallway]]",
      "links": [
        {
          "linkText": "LEAVE",
          "passageName": "WEST HALLWAY",
          "original": "[[LEAVE ->WEST HALLWAY]]"
        }
      ],
      "hooks": [],
      "cleanText": "My owner, Kevin, is sitting in the hallway. Maybe if I bring him a toy or something it'll get his attention. Paths: Leave"
    },
    {
      "name": "SOUTHERN HALLWAY",
      "tags": "",
      "id": "20",
      "text": "Hallway on the Southern end of the ship that connects the East and West Hallways.\n\n[[West Hallway]] \n[[East Hallway]] \n[[Engine Room]] \n[[Cafeteria]]",
      "links": [
        {
          "linkText": "WEST HALLWAY",
          "passageName": "WEST HALLWAY",
          "original": "[[WEST HALLWAY]]"
        },
        {
          "linkText": "EAST HALLWAY",
          "passageName": "EAST HALLWAY",
          "original": "[[EAST HALLWAY]]"
        },
        {
          "linkText": "ENGINE ROOM",
          "passageName": "ENGINE ROOM",
          "original": "[[ENGINE ROOM]]"
        },
        {
          "linkText": "CAFETERIA",
          "passageName": "CAFETERIA",
          "original": "[[CAFETERIA]]"
        }
      ],
      "hooks": [],
      "cleanText": "Hallway on the Southern end of the ship that connects the East and West Hallways. Paths: West Hallway, Cafeteria, Engine Room, East Hallway"
    },
    {
      "name": "NORTHERN HALLWAY",
      "tags": "",
      "id": "21",
      "text": "A hallway on the Northern end of the ship, connecting the West and East Hallways.\n\n[[West Hallway]] \n[[East Hallway]] \n[[Cockpit]]",
      "links": [
        {
          "linkText": "WEST HALLWAY",
          "passageName": "WEST HALLWAY",
          "original": "[[WEST HALLWAY]]"
        },
        {
          "linkText": "EAST HALLWAY",
          "passageName": "EAST HALLWAY",
          "original": "[[EAST HALLWAY]]"
        },
        {
          "linkText": "COCKPIT",
          "passageName": "COCKPIT",
          "original": "[[COCKPIT]]"
        }
      ],
      "hooks": [],
      "cleanText": "A hallway on the Northern end of the ship, connecting the West and East Hallways. Paths: West Hallway, Cockpit, East Hallway"
    },
    {
      "name": "ELECTRICAL ROOM",
      "tags": "",
      "id": "22",
      "text": "Kevin only comes in here every once in a while, but he doesn't like me in here by myself.\n\n[[LEAVE ->East Hallway]]",
      "links": [
        {
          "linkText": "LEAVE",
          "passageName": "EAST HALLWAY",
          "original": "[[LEAVE ->EAST HALLWAY]]"
        }
      ],
      "hooks": [],
      "cleanText": "Kevin only comes in here every once in a while, but he doesn't like me in here by myself. Paths: Leave"
    },
    {
      "name": "WEST HALLWAY",
      "tags": "",
      "id": "23",
      "text": "Hallway on the west side of the ship, leads to the crews' quarters.\n\n[[Northern Hallway]] \n[[Captain's Quarters]] \n[[Charlie's Room]] \n[[Robin's Room]] \n[[Kevin]] \n[[Kevin's Room]]\n[[Chef's Room]]  \n[[Southern Hallway]]",
      "links": [
        {
          "linkText": "NORTHERN HALLWAY",
          "passageName": "NORTHERN HALLWAY",
          "original": "[[NORTHERN HALLWAY]]"
        },
        {
          "linkText": "CAPTAIN'S QUARTERS",
          "passageName": "CAPTAIN'S QUARTERS",
          "original": "[[CAPTAIN'S QUARTERS]]"
        },
        {
          "linkText": "CHARLIE'S ROOM",
          "passageName": "CHARLIE'S ROOM",
          "original": "[[CHARLIE'S ROOM]]"
        },
        {
          "linkText": "ROBIN'S ROOM",
          "passageName": "ROBIN'S ROOM",
          "original": "[[ROBIN'S ROOM]]"
        },
        {
          "linkText": "KEVIN",
          "passageName": "KEVIN",
          "original": "[[KEVIN]]"
        },
        {
          "linkText": "KEVIN'S ROOM",
          "passageName": "KEVIN'S ROOM",
          "original": "[[KEVIN'S ROOM]]"
        },
        {
          "linkText": "CHEF'S ROOM",
          "passageName": "CHEF'S ROOM",
          "original": "[[CHEF'S ROOM]]"
        },
        {
          "linkText": "SOUTHERN HALLWAY",
          "passageName": "SOUTHERN HALLWAY",
          "original": "[[SOUTHERN HALLWAY]]"
        }
      ],
      "hooks": [],
      "cleanText": "Hallway on the west side of the ship, leads to the crews' quarters. Paths: Northern Hallway, Captain's Quarters, Charlie's Room, Robin's Room, Kevin's Room, Chef's Room, Southern Hallway"
    },
    {
      "name": "PHOTO ALBUM",
      "tags": "",
      "id": "24",
	  "item": "photo",
      "text": "You found a photo album with pictures of the Chef and the other crewmates. Most of the photos are of the Chef and Kevin though.\n\n[[LEAVE ->Chef's Room]]",
      "links": [
        {
          "linkText": "LEAVE",
          "passageName": "CHEF'S ROOM",
          "original": "[[LEAVE ->CHEF'S ROOM]]"
        }
      ],
      "hooks": [],
      "cleanText": "You found a photo album with pictures of the Chef and the other crewmates. Most of the photos are of the Chef and Kevin though. Paths: Leave"
    },
    {
      "name": "TOOLKIT",
      "tags": "",
      "id": "25",
	  "item": "screwdriver",
      "text": "You found a toolkit. All of the tools have red handles except for a screwdriver with a yellow one.\n\n[[LEAVE ->Robin's Room]]",
      "links": [
        {
          "linkText": "LEAVE",
          "passageName": "ROBIN'S ROOM",
          "original": "[[LEAVE ->ROBIN'S ROOM]]"
        }
      ],
      "hooks": [],
      "cleanText": "You found a toolkit. All of the tools have red handles except for a screwdriver with a yellow one. Paths: Leave"
    },
    {
      "name": "DOG TOYS",
      "tags": "",
      "id": "26",
	  "item": "tennis ball",
      "text": "You found a pile of dog toys. My favorite tennis ball is sitting on the top.\n\n[[LEAVE ->Excercise Room]]",
      "links": [
        {
          "linkText": "LEAVE",
          "passageName": "EXERCISE ROOM",
          "original": "[[LEAVE ->EXERCISE ROOM]]"
        }
      ],
      "hooks": [],
      "cleanText": "You found a pile of dog toys. My favorite tennis ball is sitting on the top. Paths: Leave"
    },
    {
      "name": "BOUQUET",
      "tags": "",
      "id": "27",
	  "item": "flower",
      "text": "You found a bouquet of flowers sitting by the window.\n\n[[LEAVE ->Gallery]]",
      "links": [
        {
          "linkText": "LEAVE",
          "passageName": "GALLERY",
          "original": "[[LEAVE ->GALLERY]]"
        }
      ],
      "hooks": [],
      "cleanText": "You found a bouquet of flowers sitting by the window. Paths: Leave"
    },
    {
      "name": "BOX OF CARROTS",
      "tags": "",
      "id": "28",
	  "item": "carrot",
      "text": "You found a box of carrots. Stealing one won't hurt anybody.\n\n[[LEAVE ->Storage Room]]",
      "links": [
        {
          "linkText": "LEAVE",
          "passageName": "STORAGE ROOM",
          "original": "[[LEAVE ->STORAGE ROOM]]"
        }
      ],
      "hooks": [],
      "cleanText": "You found a box of carrots. Stealing one won't hurt anybody. Paths: Leave"
    },
    {
      "name": "CHARLIE'S KEYCARD",
      "tags": "",
      "id": "29",
	  "keycard": "Charlie's Keycard",
      "text": "You found Charlie's Keycard.\n\n[[LEAVE ->SECURITY ROOM]]",
      "links": [
        {
          "linkText": "LEAVE",
          "passageName": "SECURITY ROOM",
          "original": "[[LEAVE ->SECURITY ROOM]]"
        }
      ],
      "hooks": [],
      "cleanText": "You found Charlie's Keycard. Paths: Leave"
    },
    {
      "name": "ROBIN'S KEYCARD",
      "tags": "",
      "id": "30",
	  "keycard": "Robin's Keycard",
      "text": "You found Robin's Keycard.\n\n[[LEAVE ->MEDICAL ROOM]]",
      "links": [
        {
          "linkText": "LEAVE",
          "passageName": "MEDICAL ROOM",
          "original": "[[LEAVE ->MEDICAL ROOM]]"
        }
      ],
      "hooks": [],
      "cleanText": "You found Robin's Keycard. Paths: Leave."
    },
    {
      "name": "FRANKIE'S KEYCARD",
      "tags": "",
      "id": "31",
	  "keycard": "Frankie's Keycard",
      "text": "You found Frankie's Keycard.\n\n[[LEAVE ->COCKPIT]]",
      "links": [
        {
          "linkText": "LEAVE",
          "passageName": "COCKPIT",
          "original": "[[LEAVE ->COCKPIT]]"
        }
      ],
      "hooks": [],
      "cleanText": "You found Frankie's Keycard. Paths: Leave"
    },
    {
      "name": "PATRICK'S KEYCARD",
      "tags": "",
      "id": "32",
	  "keycard": "Patrick's Keycard",
      "text": "You found the Chef's Keycard.\n\n[[LEAVE ->KITCHEN]]",
      "links": [
        {
          "linkText": "LEAVE",
          "passageName": "KITCHEN",
          "original": "[[LEAVE ->KITCHEN]]"
        }
      ],
      "hooks": [],
      "cleanText": "You found the Chef's Keycard. Paths: Leave"
    }
  ]
}

#------------------------------------
#dog emote for search

def emote():
    time.sleep(1)
    print("U ^ x ^ U" +"\n" + "   / \  /" + "\n" + " [     ]" + "\n")
    time.sleep(1)
    print("U ^ x ^ U" +"\n" + "   / \ " + "\ " + "\n" + " [     ]" + "\n")
    time.sleep(1)
    print("U ^ x ^ U" +"\n" + "   / \  /" + "\n" + " [     ]" + "\n")



# ----------------------------------------------------------------

def find_current_location(location_label):
	if "passages" in world:
		for passage in world["passages"]:
			if location_label == passage["name"]:
				return passage
	return {}

# ----------------------------------------------------------------

def render(current_location, keycards, items):
	if "name" in current_location and "cleanText" in current_location:
		print("Keycards: {},  Items: {}".format(items, keycards))
		print("You are at " + str(current_location["name"]))
		print(current_location["cleanText"] + "\n")

def get_input():
	response = input("What do you want to do? ")
	response = response.upper().strip()
	return response

def update(current_location, location_label, response):
	if response == "":
		return location_label
	if "links" in current_location:
		for link in current_location["links"]:
			if link["linkText"] == response:
				return link["passageName"]
	print("I don't understand what you are trying to do. Try again.")
	return location_label


# ----------------------------------------------------------------

location_label = "KEVIN'S ROOM"
current_location = {}
response = ""
items = 0
keycards = 0
room_charlie = False
room_frankie = False
room_patrick = False
room_robin = False

print("A Spacedog Named Steve" + "\n" + "An interactive fiction game by Avriel Donaldson" + "\n")
time.sleep(1.5)
emote()

while True:
	if response == "QUIT":
		break
	location_label = update(current_location, location_label, response)
	current_location = find_current_location(location_label)
	if "keycard" in current_location:
		keycards = keycards + 1
		if "keycard" == "Charlie's Keycard":
			if room_charlie == False:
				room_charlie = True
				print("Charlie's Keycard added to inventory.")
			if room_charlie == True:
				print("Keycard already in inventory")
		if "keycard" == "Frankie's Keycard":
			if room_frankie == False:
				room_frankie = True
				print("Frankie's Keycard added to inventory.")
			if room_frankie == True:
				print("Keycard already in inventory")
		if "keycard" == "Patrick's Keycard":
			if room_patrick == False:
				room_patrick = True
				print("Chef's Keycard added to inventory.")
			if room_patrick == True:
				print("Keycard already in inventory")
		if "keycard" == "Robin's Keycard":
			if room_robin == False:
				room_robin = True
				print("Robin's Keycard added to inventory.")
			if room_robin == True:
				print("Keycard already in inventory")

	if "item" in current_location:
		items = items + 1
		print("Item added to inventory.")

	render(current_location, items, keycards)
	response = get_input()