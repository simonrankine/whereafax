config = {
    "tti_path" : "/home/pi/teletext/",
    "page_number" : 100,
    "header_separator": "cyan",
    "header_colour": "blue",
    "page_title": "whereafax",
    "cycle_time": "20"
}

mode = "w+"
subpage = 1

ESCAPE = chr(27)
DOUBLE_HEIGHT = ESCAPE + chr(77)
SET_BACKGROUND = ESCAPE + chr(93)
TWITTER_BIRD = chr(41) + chr(108) + chr(39)
text_colours = {"red" : 65, "green" : 66, "yellow" : 67 , "blue" : 68, "magenta" : 69, "cyan" : 70, "white" : 71}
mosaic_colours = {"red" : 81, "green" : 82, "yellow" : 83, "blue" : 84, "magenta" : 85, "cyan" : 86, "white" : 87}

page_title = config["page_title"] + " " + "{:02d}".format(subpage)
logo_spacer = " " * (39 - (4 + len(page_title) + 8))
with open(config['tti_path'] + "P" + str(config["page_number"]) + ".tti", mode) as file:
    if mode == "w+":
        file.write("DE,Autogenerated by Teletext-Twitter\r\n")
        file.write("SC,0000\r\n")
        file.write("PS,8000\r\n")
        file.write("CT," + str(config["cycle_time"]) + ",T\r\n")
        file.write("PN," + str(config["page_number"]) + "{:02}\r\n".format(subpage))
        file.write("OL,1," + ESCAPE + chr(text_colours[config["header_colour"]]) + SET_BACKGROUND +
            DOUBLE_HEIGHT + ESCAPE + chr(text_colours["white"]) +
            page_title + logo_spacer + ESCAPE + chr(mosaic_colours["cyan"]) + "\r\n")
        file.write("OL,3," + ESCAPE + chr(mosaic_colours[config["header_separator"]]) + (chr(35) * 39) + "\r\n")
        file.write("OL,4," + ESCAPE + chr(text_colours['red']) + "This is a test" + (" " * 25) + "\r\n")