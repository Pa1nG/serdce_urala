# Asset definitions with graceful fallbacks

# Backgrounds: prefer files from images/, fallback to Solid colors
image bg meadow = ConditionSwitch(
    renpy.loadable("images/bg_meadow.jpg"), "images/bg_meadow.jpg",
    renpy.loadable("images/bg_meadow.png"), "images/bg_meadow.png",
    True, Solid("#9cd6ff")
)

image bg hall = ConditionSwitch(
    renpy.loadable("images/bg_hall.jpg"), "images/bg_hall.jpg",
    renpy.loadable("images/bg_hall.png"), "images/bg_hall.png",
    True, Solid("#d8c49c")
)

image bg forest day = ConditionSwitch(
    renpy.loadable("images/bg_forest_day.jpg"), "images/bg_forest_day.jpg",
    renpy.loadable("images/bg_forest_day.png"), "images/bg_forest_day.png",
    True, Solid("#89c07a")
)

image bg lair = ConditionSwitch(
    renpy.loadable("images/bg_lair.jpg"), "images/bg_lair.jpg",
    renpy.loadable("images/bg_lair.png"), "images/bg_lair.png",
    True, Solid("#5a4a66")
)

image bg kiev = ConditionSwitch(
    renpy.loadable("images/bg_kiev.jpg"), "images/bg_kiev.jpg",
    renpy.loadable("images/bg_kiev.png"), "images/bg_kiev.png",
    True, Solid("#c6e2ff")
)

# Character sprites (optional): place files in images/
# Alyosha
image alyosha neutral = ConditionSwitch(
    renpy.loadable("images/alyosha_neutral.png"), "images/alyosha_neutral.png",
    True, Solid("#ffffff")
)
image alyosha smile = ConditionSwitch(
    renpy.loadable("images/alyosha_smile.png"), "images/alyosha_smile.png",
    True, Solid("#ffffff")
)

# Tugarin
image tugarin angry = ConditionSwitch(
    renpy.loadable("images/tugarin_angry.png"), "images/tugarin_angry.png",
    True, Solid("#333333")
)

# Yelena
image yelena smile = ConditionSwitch(
    renpy.loadable("images/yelena_smile.png"), "images/yelena_smile.png",
    True, Solid("#ffeeee")
)

# Transforms/positions
transform appear:
    alpha 0.0
    linear 0.3 alpha 1.0

transform slight_bounce:
    yoffset 0
    linear 0.2 yoffset -6
    linear 0.2 yoffset 0

# Positions
define left_pos = Position(xalign=0.2, yalign=1.0)
define center_pos = Position(xalign=0.5, yalign=1.0)
define right_pos = Position(xalign=0.8, yalign=1.0)

# Audio aliases
define audio.lyre_theme = "audio/lyre_theme.ogg"
define audio.tense_drums = "audio/tense_drums.ogg"
define audio.sfx_sword = "audio/sfx_sword.ogg"
