from gi.repository import Gtk, GObject
from subprocess import check_output
from os import system
import actions

version=0.3
class MainWindow(Gtk.Window):
	def __init__(self):

		# Main window
		Gtk.Window.__init__(self, title="gtmocp v. %s" %version)
		
		# Boxes
		# Main box - holds everything
		self.mainbox = Gtk.VBox(spacing = 6)
		self.add(self.mainbox)		

		# Button box - holds clickables
		self.buttonbox = Gtk.HBox(spacing = 4)
		self.mainbox.add(self.buttonbox)
		
		# Time box - holds time info
		self.timebox = Gtk.HBox(spacing = 4)
		self.mainbox.add(self.timebox)

		# Track box - holds track info
		self.trackbox = Gtk.HBox(spacing = 8)
		self.mainbox.add(self.trackbox)

		# Progress bar
		self.prog = Gtk.ProgressBar()
		self.timeout_prog = GObject.timeout_add(1000, self.timeout, None)
				
		# Buttons
		self.next = Gtk.Button(label="next")
		self.next.connect("clicked", actions.next)
	
		self.prev = Gtk.Button(label="prev")
		self.prev.connect("clicked", actions.prev)

		self.togg = Gtk.Button(label="play/pause")
		self.togg.connect("clicked", actions.togg)

		# Labels (artist, title and time)
		self.artist = Gtk.Label("bar")
		self.song = Gtk.Label("song")
		self.tt = Gtk.Label()
		self.ct = Gtk.Label()		

		# Pack everything to boxes
		self.buttonbox.pack_start(self.prev, True, True, 0)
		self.buttonbox.pack_start(self.togg, True, True, 0)
		self.buttonbox.pack_start(self.next, True, True, 0)
		
		self.timebox.pack_start(self.ct, True, True, 0)
		self.timebox.pack_end(self.tt, True, True, 0)

		self.trackbox.pack_start(self.artist, True, True, 0)
		self.trackbox.pack_start(self.song, True, True, 0)

		self.mainbox.pack_start(self.prog, True, True, 0)

		
	def timeout(self, data):
		try:
			new_value = float(check_output(('mocp', '-Q', '%cs')))/float(check_output(('mocp', '-Q', '%ts')))
			self.prog.set_fraction(new_value)
		except:
			pass
		# set title, artist and time
		try:

			self.song.set_text(check_output(('mocp', '-Q', '%song'))[:-1])
			self.ct.set_text( check_output(('mocp', '-Q', '%ct'))[:-1] )
			self.tt.set_text( check_output(('mocp', '-Q', '%tt'))[:-1] )
			self.artist.set_text( check_output(('mocp', '-Q', '%artist'))[:-1] )

		# Life is too short to catch exceptions
		except:
			pass

		return True
	


win=MainWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()

