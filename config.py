from typing import List  # noqa: F401

from libqtile import bar, layout, widget, extension
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
import os

mod = "mod4"
terminal = "konsole" #guess_terminal()

keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"), Key([mod], "o", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in curent stack.  Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "o", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "o", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.run_extension(extension.DmenuRun(background="#2e3440", selected_background="#88c0d0", foreground="#ffffff" )),
        desc="Spawn a command using a prompt widget"),
]




group_names = [("   SYS ", {'layout': 'monadtall'}),
               ("   DEV ", {'layout': 'monadtall'}),
               ("   CHAT ", {'layout': 'monadtall'}),
               ("   WEB ", {'layout': 'monadtall'}),
              # (" 1 ", {'layout': 'monadtall'}),
              # (" 2 ", {'layout': 'monadtall'}),
              # (" 3 ", {'layout': 'monadtall'})
               ]
 
groups = [Group(name, **kwargs) for name, kwargs in group_names]
 
for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))        # Switch to another group
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name))) # Send current window to another group






layouts = [
    #layout.Columns(border_focus_stack=['#d75f5f', '#8f3d3d'], border_width=4),
    #layout.Max(),
    # Try more layouts by unleashing below layouts.
     #layout.Stack(num_stacks=2),
     #layout.Bsp(),
     #layout.Matrix(),
     layout.MonadTall(
     border_normal="#2e3440",
     border_focus="#88c0d0",
     border_width=3,
     change_size= 10,
     single_border_width=0,
     margin=15,
     single_margin=10
    ),
    # layout.MonadWide(),
     #layout.RatioTile(),
     layout.Tile(
        border_normal="#2e3440",
        border_focus="#88c0d0",
        border_width=3,
        margin= 50,
        single_margin=10
    ),
     layout.Max(),
     #layut.TreeTab(),
     #layout.VerticalTile(),
     #layout.Zoomy(),
]

widget_defaults = dict(
    font='Caskaydia Cove Nerd Font',
    fontsize=15,
    padding=3,
)
extension_defaults = widget_defaults.copy()

fgg = "#c7d991"
backgg = "#231d2e"
colors = [["#2e3440", "#2e3440"],  
          ["#4c566a", "#4c566a"], 
          ["#88c0d0", "#88c0d0"], 
          ["#434c5e", "#434c5e"], 
          ["#3b4252", "#3b4252"], 
          ["#81a1c1", "#81a1c1"], 
          ["#5e81ac", "#5e81ac"], 
          ["#eceff4", "#eceff4"],
          ["#d8dee9", "#d8dee9"]]
widget_defaults = dict(
    font="Ubuntu Mono",
    fontsize = 12,
    padding = 2,
    background=colors[2]
)
extension_defaults = widget_defaults.copy()


screens = [
    Screen(
        top=bar.Bar(
            [
               #widget.Sep(linewidth = 0, padding = 6, foreground = colors[2], background = colors[2]),
           
            #widget.Image(filename = "~/.config/qtile/icons/arch2.png",scale = "True", mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal)}),
            widget.Sep(linewidth = 0, padding = 6, foreground = colors[2], background = colors[2]),
            widget.Sep(linewidth = 0, padding = 6, foreground = colors[2], background = colors[0]),
            widget.GroupBox(
                       margin_y = 3,
                       margin_x = 0,
                       padding_y = 5,
                       padding_x = 3,
                       borderwidth = 3,
                       active = colors[2],
                       inactive = colors[7],
                       rounded = False,
                       highlight_color = colors[3],
                       highlight_method = "line",
                       this_current_screen_border = colors[2],
                       this_screen_border = colors [2],
                       foreground = colors[2],
                       background = colors[0],
                       fontsize = 16
                       ),
                widget.Sep(linewidth = 0, padding = 6, background = colors[0]),
                widget.Sep(linewidth = 0, padding = 6, background = colors[4]),
                widget.Prompt(),
                widget.WindowName(background= colors[4], foreground = colors[2]),
                widget.Chord(
                    chords_colors={
                       'launch': ("#5e81ac", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
               
 
                widget.Sep(linewidth = 0, padding = 6, foreground = colors[2], background = colors[4]),
                widget.Systray(padding = 6, foreground = colors[2], background = colors[4]),
                widget.Sep(linewidth = 0, padding = 12, foreground = colors[2], background = colors[4]),
                #widget.Sep(linewidth = 0, padding = 12, foreground = colors[2], background = colors[0]),
                #widget.Sep(linewidth = 0, padding = 3, foreground = colors[2], background = colors[2]),
                widget.TextBox(
                       text = '',
                       background = colors[4],
                       foreground = colors[5],
                       padding = -16,
                       fontsize = 78
                       ),
              widget.TextBox(
                       text = '',
                       background = colors[5],
                       foreground = colors[4],
                       padding = -16,
                       fontsize = 78
                       ),
             widget.TextBox(
                       text = " 🌡",
                       padding = 2,
                       foreground = colors[2],
                       background = colors[4],
                       fontsize = 11
                       ),
              widget.ThermalSensor(
                       foreground = colors[2],
                       background = colors[4],
                       threshold = 90,
                       padding = 5
                       ),
              widget.TextBox(
                       text='',
                       background = colors[4],
                       foreground = colors[5],
                       padding = -16,
                       fontsize = 78
                       ),
              widget.TextBox(
                       text = " ⟳",
                       padding = 2,
                       foreground = colors[2],
                       background = colors[5],
                       fontsize = 14
                       ),
              widget.CheckUpdates(
                       update_interval = 1800,
                       distro = "Arch_checkupdates",
                       display_format = "{updates} Updates",
                       foreground = colors[2],
                       mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e sudo pacman -Syu')},
                       background = colors[5]
                       ),
              widget.TextBox(
                       text = '',
                       background = colors[5],
                       foreground = colors[4],
                       padding = -16,
                       fontsize = 78
                       ),
              widget.TextBox(
                       text = " 🖬",
                       foreground = colors[2],
                       background = colors[4],
                       padding = 0,
                       fontsize = 14
                       ),
              widget.Memory(
                       foreground = colors[2],
                       background = colors[4],
                       mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e htop')},
                       padding = 5
                       ),
              widget.TextBox(
                       text = '',
                       background = colors[4],
                       foreground = colors[5],
                       padding = -16,
                       fontsize = 78
                       ),
              widget.TextBox(
                      text = " Vol:",
                       foreground = colors[2],
                       background = colors[5],
                       padding = 0
                       ),
              widget.Volume(
                       foreground = colors[2],
                       background = colors[5],
                       padding = 5
                       ),
              widget.TextBox(
                       text = '',
                       background = colors[5],
                       foreground = colors[4],
                       padding = -16,
                       fontsize = 78
                       ),
              widget.CurrentLayout(
                       foreground = colors[2],
                       background = colors[4],
                       padding = 5
                       ),
              widget.TextBox(
                       text = '',
                       background = colors[4],
                       foreground = colors[5],
                       padding = -16,
                       fontsize = 78
                       ),
              widget.Clock(
                       foreground = colors[2],
                       background = colors[5],
                       format = "%A, %B %d - %H:%M "
                       ),

            ],
            24,
            fontsize = 37,
            background="#202120",
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
runonstart = [
    "feh --bg-fill /home/noisex/.config/qtile/archnord.png",
    "picom --no-vsync &",
    #"rustyvibes /home/noisex/Descargas/Soundpacks/nk-cream &"
]


for i in runonstart:
    os.system(i)



