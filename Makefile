default: run

ui_mainwindow.py: ohm_gui/mainwindow.ui
	pyuic5 -x ohm_gui/mainwindow.ui -o ui_mainwindow.py

Tango_rc.py: ohm_gui/ui/tango/Tango.qrc
	pyrcc5 ohm_gui/ui/tango/Tango.qrc -o Tango_rc.py

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
	rm -rf build-ohm_gui-*

designer:
	open ohm_gui/ohm_gui.pro

.PHONY: run ui rc clean designer
