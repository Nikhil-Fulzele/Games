import sys
import tty
import termios


class _Getch:
	def __call__(self):
		fd = sys.stdin.fileno()
		old_settings = termios.tcgetattr(fd)
		try:
			tty.setraw(sys.stdin.fileno())
			ch = sys.stdin.read(3)
		finally:
			termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
		return ch


def get_key():
	inkey = _Getch()
	while(1):
		k=inkey()
		if k!='':break
	if k=='\x1b[A':
		print("up")
		return("up")
	elif k=='\x1b[B':
		print("down")
		return("down")
	elif k=='\x1b[C':
		print("right")
		return("right")
	elif k=='\x1b[D':
		print("left")
		return("left")
	else:
		return None
