import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class MainWindow(QMainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()
		self.browser = QWebEngineView()
		self.browser.setUrl(QUrl('https://www.bing.com'))
		self.setCentralWidget(self.browser)
		self.showMaximized()

		# navbar 
		navbar = QToolBar()
		self.addToolBar(navbar)

		BackBtn = QAction('◀', self)
		BackBtn.triggered.connect(self.browser.back)
		navbar.addAction(BackBtn)

		ForwardBtn = QAction('▶', self)
		ForwardBtn.triggered.connect(self.browser.forward)
		navbar.addAction(ForwardBtn)

		ReloadBtn = QAction('🕑', self)
		ReloadBtn.triggered.connect(self.browser.reload)
		navbar.addAction(ReloadBtn)

		HomeBtn = QAction('🏠', self)
		HomeBtn.triggered.connect(self.NavigateHome)
		navbar.addAction(HomeBtn)

		self.UrlBar = QLineEdit()
		self.UrlBar.returnPressed.connect(self.NavigateUrl)
		navbar.addWidget(self.UrlBar)

		self.browser.urlChanged.connect(self.UpdateUrl)

		p4r = QAction('Pray4Refugees', self)
		p4r.triggered.connect(self.Navigatep4r)
		navbar.addAction(p4r)

		WasiLab= QAction('WasiLab', self)
		WasiLab.triggered.connect(self.NavigateWasiLab)
		navbar.addAction(WasiLab)

	def Navigatep4r(self):
		self.browser.setUrl(QUrl('https://www.pray4refugees.org'))

	def NavigateWasiLab(self):
		self.browser.setUrl(QUrl('https://rifatmuhtasim.github.io/TabLab'))

	def NavigateHome(self):
		self.browser.setUrl(QUrl('https://www.bing.com'))

	def NavigateUrl(self):
		url = self.UrlBar.text()
		self.browser.setUrl(QUrl(url))

	def UpdateUrl(self, x):
		self.UrlBar.setText(x.toString())

app = QApplication(sys.argv)
QApplication.setApplicationName('WasiZ')
window = MainWindow() 
app.exec_()