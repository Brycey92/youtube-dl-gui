# -*- coding: UTF-8 -*-

import gettext

from .utils import TwoWayOrderedDict as tdict


OUTPUT_FORMATS = tdict([
    (0, _("ID")),
    (1, _("Title")),
    (2, _("Title + ID")),
    (4, _("Title + Quality")),
    (5, _("Title + ID + Quality")),
    (3, _("Custom"))
])


DEFAULT_FORMATS = tdict([
    ("0", _("default"))
])


VIDEO_FORMATS = tdict([
    ("3gp", "3gp"),
    ("17",  "3gp [144p] <17>"),
    ("36",  "3gp [240p] <36>"),
    ("flv", "flv"),
    ("5",   "flv [240p] <5>"),
    ("6",   "flv [270p] <6>"),
    ("34",  "flv [360p] <34>"),
    ("35",  "flv [480p] <35>"),
    ("webm", "webm"),
    ("43",  "webm [360p] <43>"),
    ("44",  "webm [480p] <44>"),
    ("45",  "webm [720p] <45>"),
    ("46",  "webm [1080p] <46>"),
    ("mp4", "mp4"),
    ("18",  "mp4 [360p] <18>"),
    ("22",  "mp4 [720p] <22>"),
    ("37",  "mp4 [1080p] <37>"),
    ("38",  "mp4 [4K] <38>"),
    ("160", "mp4 [144p] (DASH Video) <160>"),
    ("133", "mp4 [240p] (DASH Video) <133>"),
    ("134", "mp4 [360p] (DASH Video) <134>"),
    ("135", "mp4 [480p] (DASH Video) <135>"),
    ("136", "mp4 [720p] (DASH Video) <136>"),
    ("298", "mp4 [720p 60fps] (DASH Video) <298>"),
    ("137", "mp4 [1080p] (DASH Video) <137>"),
    ("299", "mp4 [1080p 60fps] (DASH Video) <299>"),
    ("264", "mp4 [1440p] (DASH Video) <264>"),
    ("138", "mp4 [2160p] (DASH Video) <138>"),
    ("266", "mp4 [2160p 60fps] (DASH Video) <266>"),
    ("151", "hls [72p] <151>"),
    ("132", "hls [240p] <132>"),
    ("92",  "hls [240p] (3D) <92>"),
    ("93",  "hls [360p] (3D) <93>"),
    ("94",  "hls [480p] (3D) <94>"),
    ("95",  "hls [720p] (3D) <95>"),
    ("96",  "hls [1080p] <96>"),
    ("394", "mp4 [144p] <394>"),
    ("395", "mp4 [240p] <395>"),
    ("396", "mp4 [360p] <396>"),
    ("397", "mp4 [480p] <397>"),
    ("398", "mp4 [720p] <398>"),
    ("399", "mp4 [1080p] <399>"),
    ("400", "mp4 [1440p] <400>"),
    ("401", "mp4 [2160p] <401>"),
    ("402", "mp4 [2880p] <402>"),
    ("242", "webm [240p] (DASH Video) <242>"),
    ("243", "webm [360p] (DASH Video) <243>"),
    ("244", "webm [480p] (DASH Video) <244>"),
    ("247", "webm [720p] (DASH Video) <247>"),
    ("302", "webm [720p 60fps] (DASH Video) <302>"),
    ("248", "webm [1080p] (DASH Video) <248>"),
    ("303", "webm [1080p 60fps] (DASH Video) <303>"),
    ("271", "webm [1440p] (DASH Video) <271>"),
    ("308", "webm [1440p 60fps] (DASH Video) <300>"),
    ("313", "webm [2160p] (DASH Video) <313>"),
    ("315", "webm [2160p 60fps] (DASH Video) <315>"),
    ("272", "webm [4320p] (DASH Video) <272>"),
    ("82",  "mp4 [360p] (3D) <82>"),
    ("83",  "mp4 [480p] (3D) <83>"),
    ("84",  "mp4 [720p] (3D) <84>"),
    ("85",  "mp4 [1080p] (3D) <85>"),
    ("100", "webm [360p] (3D) <100>"),
    ("101", "webm [480p] (3D) <101>"),
    ("102", "webm [720p] (3D) <102>"),
    ("219", "webm [144p] <219>"),
    ("278", "webm [144p] <278>"),
    ("167", "webm [360p] <167>"),
    ("168", "webm [480p] <168>"),
    ("218", "webm [480p] <218>"),
    ("245", "webm [480p] <245>"),
    ("246", "webm [480p] <246>"),
    ("169", "webm [1080p] <169>"),
    ("330", "webm [144p 60fps] (HDR) <330>"),
    ("331", "webm [240p 60fps] (HDR) <331>"),
    ("332", "webm [360p 60fps] (HDR) <332>"),
    ("333", "webm [480p 60fps] (HDR) <333>"),
    ("334", "webm [720p 60fps] (HDR) <334>"),
    ("335", "webm [1080p 60fps] (HDR) <335>"),
    ("336", "webm [1440p 60fps] (HDR) <336>"),
    ("337", "webm [2160p 60fps] (HDR) <337>"),
    ("139", "m4a 48k (DASH Audio) <139>"),
    ("140", "m4a 128k (DASH Audio) <140>"),
    ("141", "m4a 256k (DASH Audio) <141>"),
    ("600", "webm (36k Audio) <600>"),
    ("171", "webm 48k (DASH Audio) <171>"),
    ("249", "webm (52k Audio) <249>"),
    ("250", "webm (64k Audio) <250>"),
    ("251", "webm (116k Audio) <251>"),
    ("172", "webm 256k (DASH Audio) <172>")
])


AUDIO_FORMATS = tdict([
    ("mp3", "mp3"),
    ("wav", "wav"),
    ("aac", "aac"),
    ("m4a", "m4a"),
    ("vorbis", "vorbis"),
    ("opus", "opus"),
    ("flac", "flac")
])


FORMATS = DEFAULT_FORMATS.copy()
FORMATS.update(VIDEO_FORMATS)
FORMATS.update(AUDIO_FORMATS)


def reload_strings():
    # IF YOU DONT WANT YOUR EYES TO BLEED STOP HERE
    # YOU HAVE BEEN WARNED
    # DO NOT LOOK THE CODE BELOW
    #
    #
    #
    #
    #
    #
    #
    #
    #NOTE Remove
    # Code is so messed up that i need to reload strings else
    # the translations wont work on the about gettext tags
    global OUTPUT_FORMATS
    global DEFAULT_FORMATS
    global VIDEO_FORMATS
    global AUDIO_FORMATS
    global FORMATS

    OUTPUT_FORMATS = tdict([
        (0, _("ID")),
        (1, _("Title")),
        (2, _("Title + ID")),
        (4, _("Title + Quality")),
        (5, _("Title + ID + Quality")),
        (3, _("Custom"))
    ])


    DEFAULT_FORMATS = tdict([
        ("0", _("default"))
    ])


    VIDEO_FORMATS = tdict([
        ("3gp", "3gp"),
        ("17",  "3gp [144p] <17>"),
        ("36",  "3gp [240p] <36>"),
        ("flv", "flv"),
        ("5",   "flv [240p] <5>"),
        ("6",   "flv [270p] <6>"),
        ("34",  "flv [360p] <34>"),
        ("35",  "flv [480p] <35>"),
        ("webm", "webm"),
        ("43",  "webm [360p] <43>"),
        ("44",  "webm [480p] <44>"),
        ("45",  "webm [720p] <45>"),
        ("46",  "webm [1080p] <46>"),
        ("mp4", "mp4"),
        ("18",  "mp4 [360p] <18>"),
        ("22",  "mp4 [720p] <22>"),
        ("37",  "mp4 [1080p] <37>"),
        ("38",  "mp4 [4K] <38>"),
        ("160", "mp4 [144p] (DASH Video) <160>"),
        ("133", "mp4 [240p] (DASH Video) <133>"),
        ("134", "mp4 [360p] (DASH Video) <134>"),
        ("135", "mp4 [480p] (DASH Video) <135>"),
        ("136", "mp4 [720p] (DASH Video) <136>"),
        ("298", "mp4 [720p 60fps] (DASH Video) <298>"),
        ("137", "mp4 [1080p] (DASH Video) <137>"),
        ("299", "mp4 [1080p 60fps] (DASH Video) <299>"),
        ("264", "mp4 [1440p] (DASH Video) <264>"),
        ("138", "mp4 [2160p] (DASH Video) <138>"),
        ("266", "mp4 [2160p 60fps] (DASH Video) <266>"),
        ("151", "hls [72p] <151>"),
        ("132", "hls [240p] <132>"),
        ("92",  "hls [240p] (3D) <92>"),
        ("93",  "hls [360p] (3D) <93>"),
        ("94",  "hls [480p] (3D) <94>"),
        ("95",  "hls [720p] (3D) <95>"),
        ("96",  "hls [1080p] <96>"),
        ("394", "mp4 [144p] <394>"),
        ("395", "mp4 [240p] <395>"),
        ("396", "mp4 [360p] <396>"),
        ("397", "mp4 [480p] <397>"),
        ("398", "mp4 [720p] <398>"),
        ("399", "mp4 [1080p] <399>"),
        ("400", "mp4 [1440p] <400>"),
        ("401", "mp4 [2160p] <401>"),
        ("402", "mp4 [2880p] <402>"),
        ("242", "webm [240p] (DASH Video) <242>"),
        ("243", "webm [360p] (DASH Video) <243>"),
        ("244", "webm [480p] (DASH Video) <244>"),
        ("247", "webm [720p] (DASH Video) <247>"),
        ("302", "webm [720p 60fps] (DASH Video) <302>"),
        ("248", "webm [1080p] (DASH Video) <248>"),
        ("303", "webm [1080p 60fps] (DASH Video) <303>"),
        ("271", "webm [1440p] (DASH Video) <271>"),
        ("308", "webm [1440p 60fps] (DASH Video) <300>"),
        ("313", "webm [2160p] (DASH Video) <313>"),
        ("315", "webm [2160p 60fps] (DASH Video) <315>"),
        ("272", "webm [4320p] (DASH Video) <272>"),
        ("82",  "mp4 [360p] (3D) <82>"),
        ("83",  "mp4 [480p] (3D) <83>"),
        ("84",  "mp4 [720p] (3D) <84>"),
        ("85",  "mp4 [1080p] (3D) <85>"),
        ("100", "webm [360p] (3D) <100>"),
        ("101", "webm [480p] (3D) <101>"),
        ("102", "webm [720p] (3D) <102>"),
        ("219", "webm [144p] <219>"),
        ("278", "webm [144p] <278>"),
        ("167", "webm [360p] <167>"),
        ("168", "webm [480p] <168>"),
        ("218", "webm [480p] <218>"),
        ("245", "webm [480p] <245>"),
        ("246", "webm [480p] <246>"),
        ("169", "webm [1080p] <169>"),
        ("330", "webm [144p 60fps] (HDR) <330>"),
        ("331", "webm [240p 60fps] (HDR) <331>"),
        ("332", "webm [360p 60fps] (HDR) <332>"),
        ("333", "webm [480p 60fps] (HDR) <333>"),
        ("334", "webm [720p 60fps] (HDR) <334>"),
        ("335", "webm [1080p 60fps] (HDR) <335>"),
        ("336", "webm [1440p 60fps] (HDR) <336>"),
        ("337", "webm [2160p 60fps] (HDR) <337>"),
        ("139", "m4a 48k (DASH Audio) <139>"),
        ("140", "m4a 128k (DASH Audio) <140>"),
        ("141", "m4a 256k (DASH Audio) <141>"),
        ("600", "webm (36k Audio) <600>"),
        ("171", "webm 48k (DASH Audio) <171>"),
        ("249", "webm (52k Audio) <249>"),
        ("250", "webm (64k Audio) <250>"),
        ("251", "webm (116k Audio) <251>"),
        ("172", "webm 256k (DASH Audio) <172>")
    ])


    AUDIO_FORMATS = tdict([
        ("mp3", "mp3"),
        ("wav", "wav"),
        ("aac", "aac"),
        ("m4a", "m4a"),
        ("vorbis", "vorbis"),
        ("opus", "opus"),
        ("flac", "flac")
    ])


    FORMATS = DEFAULT_FORMATS.copy()
    FORMATS.update(VIDEO_FORMATS)
    FORMATS.update(AUDIO_FORMATS)
