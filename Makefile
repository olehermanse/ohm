default: run

ui_mainwindow.py: ui_mainwindow.ui
	pyuic5 -x ui_mainwindow.ui -o ui_mainwindow.py

Tango_rc.py: ui/tango/Tango.qrc
	pyrcc5 ui/tango/Tango.qrc -o Tango_rc.py

ui: ui_mainwindow.py
rc: Tango_rc.py

run: ui rc
	python3 ohm.py

clean:
	rm -f ui_mainwindow.py
	rm -f Tango_rc.py
	rm -rf qt_creator
	rm -rf __pycache__
	rm -rf debug

designer:
	open ohm_gui.pro

.PHONY: run ui rc clean designer
