import os
import json

games = ["trials", "parkour", "bingo", "tag", "multilap", "build_masters", "armsrace", "bowpvp"]

games_icon = {
    "trials":"minecraft:red_concrete",
    "parkour":"minecraft:orange_concrete",
    "bingo":"minecraft:yellow_concrete",
    "tag":"minecraft:lime_concrete",
    "multilap":"minecraft:light_blue_concrete",
    "build_masters":"minecraft:blue_concrete",
    "armsrace":"minecraft:purple_concrete",
    "bowpvp":"minecraft:pink_concrete"
}

games_color = {
    "trials":"§c",
    "parkour":"§6",
    "bingo":"§e",
    "tag":"§a",
    "multilap":"§b",
    "build_masters":"§9",
    "armsrace":"§5",
    "bowpvp":"§d"
}

games_names = {
    "trials":"Trials",
    "parkour":"Parkour",
    "bingo":"Bingo",
    "tag":"Tag",
    "multilap":"Multilap",
    "build_masters":"Build Masters",
    "armsrace":"Arms Race",
    "bowpvp":"Bow PVP"
}

path = "C:/Users/ellio/Code/Datapacks/TheEvent580-Datapack/TheEvent580-Datapack/data/theevent580/advancement/event_progression/start"

file_success = 0
folder_success = 0

for game1 in games:
    if os.path.exists(os.path.join(path, f"{game1}.json")):
        pass
    else:
        dico = {
            "display": {
                "icon": {
                    "id":f"{games_icon[game1]}"
                },
                "title": f"{games_color[game1]}Game 1 : {games_names[game1]}",
                "description": f"{games_color[game1]}{games_names[game1]} was the 1st game chosen (x1 multiplier)",
                "frame": "task",
                "show_toast": True,
                "announce_to_chat": False,
                "hidden": True
            },
            "parent": "theevent580:event_progression/start",
            "criteria": {
                "game_chosen": {
                    "trigger": "minecraft:impossible"
                }
            }
        }
        json_file = json.dumps(dico, indent=2)
        with open(f"{path}/{game1}.json", "x") as f:
            f.write(json_file)
    file_success += 1
    if os.path.exists(os.path.join(path, f"{game1}")):
        pass
    else:
        os.mkdir(f"{path}/{game1}")
    folder_success += 1
    for game2 in games:
        if game1 != game2:
            if os.path.exists(os.path.join(path, f"{game1}/{game2}.json")):
                pass
            else:
                dico = {
                    "display": {
                        "icon": {
                            "id":f"{games_icon[game2]}"
                        },
                        "title": f"{games_color[game2]}Game 2 : {games_names[game2]}",
                        "description": f"{games_color[game2]}{games_names[game2]} was the 2nd game chosen (x1 multiplier)",
                        "frame": "task",
                        "show_toast": True,
                        "announce_to_chat": False,
                        "hidden": True
                    },
                    "parent": f"theevent580:event_progression/start/{game1}",
                    "criteria": {
                        "game_chosen": {
                            "trigger": "minecraft:impossible"
                        }
                    }
                }
                json_file = json.dumps(dico, indent=2)
                with open(f"{path}/{game1}/{game2}.json", "x") as f:
                    f.write(json_file)
            file_success += 1
            if os.path.exists(os.path.join(path, f"{game1}/{game2}")):
                pass
            else:
                os.mkdir(f"{path}/{game1}/{game2}")
            folder_success += 1
            for game3 in games:
                if game1 != game3 and game2 != game3:
                    if os.path.exists(os.path.join(path, f"{game1}/{game2}/{game3}.json")):
                        pass
                    else:
                        dico = {
                            "display": {
                                "icon": {
                                    "id":f"{games_icon[game3]}"
                                },
                                "title": f"{games_color[game3]}Game 3 : {games_names[game3]}",
                                "description": f"{games_color[game3]}{games_names[game3]} was the 3rd game chosen (x1 multiplier)",
                                "frame": "task",
                                "show_toast": True,
                                "announce_to_chat": False,
                                "hidden": True
                            },
                            "parent": f"theevent580:event_progression/start/{game1}/{game2}",
                            "criteria": {
                                "game_chosen": {
                                    "trigger": "minecraft:impossible"
                                }
                            }
                        }
                        json_file = json.dumps(dico, indent=2)
                        with open(f"{path}/{game1}/{game2}/{game3}.json", "x") as f:
                            f.write(json_file)
                    file_success += 1
                    if os.path.exists(os.path.join(path, f"{game1}/{game2}/{game3}")):
                        pass
                    else:
                        os.mkdir(f"{path}/{game1}/{game2}/{game3}")
                    folder_success += 1
                    if os.path.exists(os.path.join(path, f"{game1}/{game2}/{game3}/pause.json")):
                        pass
                    else:
                        dico = {
                            "display": {
                                "icon": {
                                    "id":"minecraft:structure_void"
                                },
                                "title": f"\u00a77Pause",
                                "description": f"\u00a77We're going on a 6-minute break",
                                "frame": "goal",
                                "show_toast": True,
                                "announce_to_chat": False,
                                "hidden": True
                            },
                            "parent": f"theevent580:event_progression/start/{game1}/{game2}/{game3}",
                            "criteria": {
                                "game_chosen": {
                                    "trigger": "minecraft:impossible"
                                }
                            }
                        }
                        json_file = json.dumps(dico, indent=2)
                        with open(f"{path}/{game1}/{game2}/{game3}/pause.json", "x") as f:
                            f.write(json_file)
                    file_success += 1
                    if os.path.exists(os.path.join(path, f"{game1}/{game2}/{game3}/pause")):
                        pass
                    else:
                        os.mkdir(f"{path}/{game1}/{game2}/{game3}/pause")
                    folder_success += 1
                    for game4 in games:
                        if game1 != game4 and game2 != game4 and game3 != game4:
                            if os.path.exists(os.path.join(path, f"{game1}/{game2}/{game3}/pause/{game4}.json")):
                                pass
                            else:
                                dico = {
                                    "display": {
                                        "icon": {
                                            "id":f"{games_icon[game4]}"
                                        },
                                        "title": f"{games_color[game4]}Game 4 : {games_names[game4]}",
                                        "description": f"{games_color[game4]}{games_names[game4]} was the 4th game chosen (x1.5 multiplier)",
                                        "frame": "task",
                                        "show_toast": True,
                                        "announce_to_chat": False,
                                        "hidden": True
                                    },
                                    "parent": f"theevent580:event_progression/start/{game1}/{game2}/{game3}/pause",
                                    "criteria": {
                                        "game_chosen": {
                                            "trigger": "minecraft:impossible"
                                        }
                                    }
                                }
                                json_file = json.dumps(dico, indent=2)
                                with open(f"{path}/{game1}/{game2}/{game3}/pause/{game4}.json", "x") as f:
                                    f.write(json_file)
                            file_success += 1
                            if os.path.exists(os.path.join(path, f"{game1}/{game2}/{game3}/pause/{game4}")):
                                pass
                            else:
                                os.mkdir(f"{path}/{game1}/{game2}/{game3}/pause/{game4}")
                            folder_success += 1
                            for game5 in games:
                                if game1 != game5 and game2 != game5 and game3 != game5 and game4 != game5:
                                    if os.path.exists(os.path.join(path, f"{game1}/{game2}/{game3}/pause/{game4}/{game5}.json")):
                                        pass
                                    else:
                                        dico = {
                                            "display": {
                                                "icon": {
                                                    "id":f"{games_icon[game5]}"
                                                },
                                                "title": f"{games_color[game5]}Game 5 : {games_names[game5]}",
                                                "description": f"{games_color[game5]}{games_names[game5]} was the 5th game chosen (x1.5 multiplier)",
                                                "frame": "task",
                                                "show_toast": True,
                                                "announce_to_chat": False,
                                                "hidden": True
                                            },
                                            "parent": f"theevent580:event_progression/start/{game1}/{game2}/{game3}/pause/{game4}",
                                            "criteria": {
                                                "game_chosen": {
                                                    "trigger": "minecraft:impossible"
                                                }
                                            }
                                        }
                                        json_file = json.dumps(dico, indent=2)
                                        with open(f"{path}/{game1}/{game2}/{game3}/pause/{game4}/{game5}.json", "x") as f:
                                            f.write(json_file)
                                    file_success += 1
                                    if os.path.exists(os.path.join(path, f"{game1}/{game2}/{game3}/pause/{game4}/{game5}")):
                                        pass
                                    else:
                                        os.mkdir(f"{path}/{game1}/{game2}/{game3}/pause/{game4}/{game5}")
                                    folder_success += 1
                                    for game6 in games:
                                        if game1 != game6 and game2 != game6 and game3 != game6 and game4 != game6 and game5 != game6:
                                            print(f"Looking at {game1} -> {game2} -> {game3} => pause => {game4} -> {game5} -> {game6}")
                                            if os.path.exists(os.path.join(path, f"{game1}/{game2}/{game3}/pause/{game4}/{game5}/{game6}.json")):
                                                pass
                                            else:
                                                dico = {
                                                    "display": {
                                                        "icon": {
                                                            "id":f"{games_icon[game6]}"
                                                        },
                                                        "title": f"{games_color[game6]}Game 6 : {games_names[game6]}",
                                                        "description": f"{games_color[game6]}{games_names[game6]} was the 6th game chosen (x2 multiplier)",
                                                        "frame": "task",
                                                        "show_toast": True,
                                                        "announce_to_chat": False,
                                                        "hidden": True
                                                    },
                                                    "parent": f"theevent580:event_progression/start/{game1}/{game2}/{game3}/pause/{game4}/{game5}",
                                                    "criteria": {
                                                        "game_chosen": {
                                                            "trigger": "minecraft:impossible"
                                                        }
                                                    }
                                                }
                                                json_file = json.dumps(dico, indent=2)
                                                with open(f"{path}/{game1}/{game2}/{game3}/pause/{game4}/{game5}/{game6}.json", "x") as f:
                                                    f.write(json_file)
                                            file_success += 1
                                            if os.path.exists(os.path.join(path, f"{game1}/{game2}/{game3}/pause/{game4}/{game5}/{game6}")):
                                                pass
                                            else:
                                                os.mkdir(f"{path}/{game1}/{game2}/{game3}/pause/{game4}/{game5}/{game6}")
                                            folder_success += 1
                                            if os.path.exists(os.path.join(path, f"{game1}/{game2}/{game3}/pause/{game4}/{game5}/{game6}/end.json")):
                                                pass
                                            else:
                                                dico = {
                                                    "display": {
                                                        "icon": {
                                                            "id":"minecraft:barrier"
                                                        },
                                                        "title": f"\u00a74The End",
                                                        "description": f"\u00a74TheEvent580 has ended, thanks for playing!",
                                                        "frame": "challenge",
                                                        "show_toast": True,
                                                        "announce_to_chat": False,
                                                        "hidden": True
                                                    },
                                                    "parent": f"theevent580:event_progression/start/{game1}/{game2}/{game3}/pause/{game4}/{game5}/{game6}",
                                                    "criteria": {
                                                        "game_chosen": {
                                                            "trigger": "minecraft:impossible"
                                                        }
                                                    }
                                                }
                                                json_file = json.dumps(dico, indent=2)
                                                with open(f"{path}/{game1}/{game2}/{game3}/pause/{game4}/{game5}/{game6}/end.json", "x") as f:
                                                    f.write(json_file)
                                            file_success += 1

print(f"Total files = {file_success}")
print(f"Total folders = {folder_success}")
print(f"Total success = {file_success + folder_success}")