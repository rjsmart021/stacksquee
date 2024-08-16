class StackPage:
    def __init__(Stack, NewPage, BrowsingHistory, PagesViewed):
        Stack.NewPage = NewPage
        Stack.BrowsingHistory = BrowsingHistory
        Stack.PagesViewed = PagesViewed
       

    def __str__(self):
        Stack = f"NewPage": {Stack.NewPage}\nStack:"
        for i in range(len(Stack.BrowsingHistory)):
            Stack += f"\n    {Stack.BrowsingHistory[i]}"
        Stack += f"\nStack Total: ${Stack.PagesViewed}"
        return Stack
    
    def notify_customer(self):
        print(f"{self.Page}, your Stack is ready!\n")

    self.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
    self.add_new_tab(QUrl('http://www.google.com'), 'Homepage')
    self.tabs.currentWidget().page().profile().downloadRequested.connect(self.on_downloadRequested)
    self.tabs.currentWidget().page().fullScreenRequested.connect(lambda request: request.accept())

    self.setCentralWidget(self.tabs)
    self.showMaximized()

Add_page = StackQueue()

def navigate_to_url(self):

        if self.searchEntry.text().startswith('www.') and self.searchEntry.text().endswith('.com'):
            url = 'https://' + self.searchEntry.text()
            self.tabs.currentWidget().setUrl(QUrl(url))

        elif self.searchEntry.text().endswith('.com') and (not self.searchEntry.text().startswith('https://')
                                                           or self.searchEntry.text().startswith('http://')):
            url = 'https://www.' + self.searchEntry.text()
            self.tabs.currentWidget().setUrl(QUrl(url))

        elif self.searchEntry.text().startswith('http'):
            url = self.searchEntry.text()
            self.tabs.currentWidget().setUrl(QUrl(url))

        # if user don't write right link, then search in google
        elif not self.searchEntry.text().startswith('www.') and not self.searchEntry.text().endswith('.com'):
            url = 'https://www.google.com/search?q=' + self.searchEntry.text()
            self.tabs.currentWidget().setUrl(QUrl(url))
        else:
            url = self.searchEntry.text()
            self.tabs.currentWidget().setUrl(QUrl(url))

 def add_new_tab(self, qurl: str, label="Blank"):
        # if url is blank
        if qurl == '':
            # creating a google url
            qurl = QUrl('http://www.google.com')

        # if new tab request
        if qurl == False:
            qurl = QUrl('http://www.google.com')

        # creating a QWebEngineView object
        browser = QWebEngineView()

        # setting url to browser
        browser.setUrl(qurl)
        browser.setZoomFactor(1.2)
        # setting tab index
        i = self.tabs.addTab(browser, label)
        self.tabs.setCurrentIndex(i)

        # adding action to the browser when url is changed
        # update the url
        browser.urlChanged.connect(lambda qurl, browser=browser:
                                   self.update_urlbar(qurl, browser))

        # adding action to the browser when loading is finished
        # set the tab title
        browser.loadFinished.connect(lambda _, i=i, browser=browser:
                                     self.tabs.setTabText(i, browser.page().title()))

        # when tab is changed

    def current_tab_changed(self, i):
        try:
            # get the curl
            qurl = self.tabs.currentWidget().url()

            # update the url
            self.update_urlbar(qurl, self.tabs.currentWidget())

            # update the title
            self.update_title(self.tabs.currentWidget())
        except:
            return

    # when tab is closed
    def close_current_tab(self, i):
        self.tabs.removeTab(i)

    # method for updating the title
    def update_title(self, browser):

        # if signal is not from the current tab
        if browser != self.tabs.currentWidget():
            # do nothing
            return

        # get the page title
        title = self.tabs.currentWidget().page().title()

    # action to go to home page
    def navigate_home(self):
        if self.tabs.count() > 0:


 # method to update the url
    def update_urlbar(self, q, browser=None):

        # If this signal is not from the current tab, ignore
        if browser != self.tabs.currentWidget():
            return

        # set text to the url bar
        self.searchEntry.setText(q.toString())

        # set cursor position
        self.searchEntry.setCursorPosition(0)

  def foo(self):
        print("finished")

class StackQueue:
    def __init__(Stack):
        Stack.NewPage = []

    def is_empty(self):
        return len(self.Stacks) == 0

    def add_new_Stack(self, Stack):
        self.Stacks.append(Stack)

    def complete_next_Stack(self):
        if not self.is_empty():
            print("Stack up!")
            Stack = self.Stacks.pop(0)
            print(f"{Stack}")
            Stack.notify_customer()
        else:
            print("All Stack websites have been removed!")

Browser = QApplication(sys.argv)
QApplication.setApplicationName("GKHN Browser")
QApplication.setWindowIcon(QIcon('icns/sendmessage.png'))
screen = MainPage()
screen.show()
Browser.exec()

Add_page.complete_next_Stack()
Add_page.complete_next_Stack()
Add_page.complete_next_Stack()
